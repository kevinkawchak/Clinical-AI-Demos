"""Cartesian safety validator.

Validates each humanoid_command against frame bounds, peer 2-second envelope,
patient envelope, and no-fly zones. Returns (ok, reason). Failures cause the
dispatcher to issue a hold-in-place command for the current tick.
"""

from __future__ import annotations

import math


def validate_command(
    command: dict,
    peer_states: list[dict],
    patient_state: dict | None,
    site_bounds: dict,
) -> tuple[bool, str]:
    pose = command["target_pose_xyz"]
    if not _within_bounds(pose, site_bounds):
        return False, "frame_bounds_violation"
    for peer in peer_states:
        predicted = predict_peer_position(peer, 2.0)
        d = _dist(pose, predicted)
        role = command.get("role", "Lead")
        if role in {"Assist", "Reserve"} and d < 0.4:
            return False, "peer_envelope_violation"
    if patient_state is not None:
        pp = patient_state.get(
            "position_xyz", {"x": 0.0, "y": 0.0, "z": 0.0}
        )
        d = _dist(pose, pp)
        role = command.get("role", "Lead")
        if role == "Reserve" and d < 1.0:
            return False, "reserve_inside_patient_radius"
        if role == "Assist" and d < 0.4:
            return False, "assist_too_close_without_handoff"
    if in_no_fly_zone(pose, site_bounds.get("no_fly_zones", [])):
        return False, "no_fly_zone_intersect"
    return True, "ok"


def predict_peer_position(peer_state: dict, seconds_ahead: float) -> dict:
    pos = peer_state.get(
        "position_xyz", {"x": 0.0, "y": 0.0, "z": 0.0}
    )
    vel = peer_state.get("velocity_xyz", {"x": 0.0, "y": 0.0, "z": 0.0})
    return {
        "x": pos["x"] + vel.get("x", 0.0) * seconds_ahead,
        "y": pos["y"] + vel.get("y", 0.0) * seconds_ahead,
        "z": pos["z"] + vel.get("z", 0.0) * seconds_ahead,
    }


def in_no_fly_zone(pose: dict, no_fly_zones: list[dict]) -> bool:
    for zone in no_fly_zones:
        c = zone.get("center_xyz", {"x": 0.0, "y": 0.0, "z": 0.0})
        r = float(zone.get("radius_m", 0.0))
        if _dist(pose, c) < r:
            return True
    return False


def _within_bounds(pose: dict, bounds: dict) -> bool:
    return (
        bounds.get("x_min_m", bounds.get("x_min", -50.0)) <= pose["x"] <= bounds.get("x_max_m", bounds.get("x_max", 50.0))
        and bounds.get("y_min_m", bounds.get("y_min", -50.0)) <= pose["y"] <= bounds.get("y_max_m", bounds.get("y_max", 50.0))
        and bounds.get("z_min_m", bounds.get("z_min", 0.0)) <= pose["z"] <= bounds.get("z_max_m", bounds.get("z_max", 3.0))
    )


def _dist(a: dict, b: dict) -> float:
    return math.sqrt(
        (a["x"] - b["x"]) ** 2 + (a["y"] - b["y"]) ** 2 + (a["z"] - b["z"]) ** 2
    )
