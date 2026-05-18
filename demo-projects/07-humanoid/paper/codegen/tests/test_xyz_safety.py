"""Validate the cartesian safety validator."""

from __future__ import annotations

import pathlib

import pytest

from xyz_safety import validate_command, predict_peer_position, in_no_fly_zone


BOUNDS = {
    "x_min_m": -50.0, "x_max_m": 50.0,
    "y_min_m": -50.0, "y_max_m": 50.0,
    "z_min_m": 0.0, "z_max_m": 3.0,
    "no_fly_zones": [],
}


def base_command(x: float = 1.0, y: float = 2.0, z: float = 1.5, role: str = "Lead") -> dict:
    return {
        "command_id": "cmd-0000000000000000",
        "tick": 0,
        "site": "SF-01",
        "robot_id": "SF-01-H2-A",
        "role": role,
        "target_pose_xyz": {"x": x, "y": y, "z": z},
        "target_orientation_rpy": {"roll": 0.0, "pitch": 0.0, "yaw": 0.0},
        "gripper_state": "open",
        "peer_robot_ids": ["SF-01-H2-B", "SF-01-H2-C"],
        "synergy_score": 1.0,
        "audit_chain_prev_hash": "0" * 64,
    }


def test_valid_command_passes() -> None:
    ok, _ = validate_command(base_command(), [], None, BOUNDS)
    assert ok


def test_x_out_of_bounds_fails() -> None:
    cmd = base_command(x=100.0)
    ok, reason = validate_command(cmd, [], None, BOUNDS)
    assert not ok
    assert reason == "frame_bounds_violation"


def test_z_below_zero_fails() -> None:
    cmd = base_command(z=-0.5)
    ok, _ = validate_command(cmd, [], None, BOUNDS)
    assert not ok


def test_peer_envelope_violation_fails() -> None:
    peer = {
        "robot_id": "SF-01-H2-B",
        "position_xyz": {"x": 1.0, "y": 2.0, "z": 1.5},
        "velocity_xyz": {"x": 0.0, "y": 0.0, "z": 0.0},
    }
    cmd = base_command(x=1.0, y=2.0, z=1.5, role="Assist")
    ok, _ = validate_command(cmd, [peer], None, BOUNDS)
    assert not ok


def test_no_fly_zone_intersect_fails() -> None:
    bounds = dict(BOUNDS)
    bounds["no_fly_zones"] = [
        {"name": "oxygen_tank_rack", "center_xyz": {"x": 1.0, "y": 2.0, "z": 1.5}, "radius_m": 1.5}
    ]
    cmd = base_command(x=1.0, y=2.0, z=1.5)
    ok, reason = validate_command(cmd, [], None, bounds)
    assert not ok
    assert reason == "no_fly_zone_intersect"


def test_predict_peer_position_with_velocity() -> None:
    peer = {
        "position_xyz": {"x": 1.0, "y": 2.0, "z": 1.5},
        "velocity_xyz": {"x": 0.5, "y": 0.0, "z": 0.0},
    }
    pred = predict_peer_position(peer, 2.0)
    assert pred["x"] == 2.0
