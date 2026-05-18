"""Validate the 7 camaraderie invariants and the role assignment logic."""

from __future__ import annotations

import pathlib

import pytest

from swarm_coordinator import SwarmCoordinator

CONFIG = pathlib.Path(__file__).resolve().parent.parent / "config" / "swarm_coordination.yaml"


@pytest.fixture
def coord() -> SwarmCoordinator:
    return SwarmCoordinator("SF-01-swarm", CONFIG)


def build_robot(robot_id: str, role: str = "Reserve", soc: float = 0.95, x: float = 0.0, y: float = 0.0, z: float = 1.5) -> dict:
    return {
        "robot_id": robot_id,
        "position_xyz": {"x": x, "y": y, "z": z},
        "battery_soc": soc,
        "gripper_state": "open",
        "current_role": role,
        "task_token": "idle",
        "self_confidence": 0.9,
    }


def build_patient(x: float = 1.0, y: float = 2.0, z: float = 1.0) -> dict:
    return {"patient_id": "PAT-NET-001-P001", "position_xyz": {"x": x, "y": y, "z": z}}


def test_assignment_3_unique_roles(coord: SwarmCoordinator) -> None:
    robots = [
        build_robot("SF-01-H2-A", x=1.0, y=2.0),
        build_robot("SF-01-H2-B", x=2.0, y=2.0),
        build_robot("SF-01-H2-C", x=3.0, y=2.0),
    ]
    patient = build_patient()
    assignment = coord.assign_roles(robots, patient)
    assert sorted(assignment.values()) == ["Assist", "Lead", "Reserve"]


def test_priority_proximity_favors_close_robot(coord: SwarmCoordinator) -> None:
    near = build_robot("SF-01-H2-A", x=1.0, y=2.0)
    far = build_robot("SF-01-H2-B", x=20.0, y=20.0)
    patient = build_patient(x=1.0, y=2.0)
    near_score = coord.compute_priority(near, "Lead", patient, [far])
    far_score = coord.compute_priority(far, "Lead", patient, [near])
    assert near_score > far_score


def test_synergy_score_full_swarm(coord: SwarmCoordinator) -> None:
    robots = [build_robot(f"SF-01-H2-{c}", soc=0.95) for c in "ABC"]
    patient = build_patient()
    s = coord.synergy_score(robots, patient)
    assert s >= 0.9


def test_synergy_score_two_active(coord: SwarmCoordinator) -> None:
    robots = [
        build_robot("SF-01-H2-A", soc=0.95),
        build_robot("SF-01-H2-B", soc=0.95),
        build_robot("SF-01-H2-C", soc=0.05),
    ]
    patient = build_patient()
    s = coord.synergy_score(robots, patient)
    assert 0.6 <= s <= 0.8


def test_invariants_dict_has_7_keys(coord: SwarmCoordinator) -> None:
    robots = [build_robot(f"SF-01-H2-{c}") for c in "ABC"]
    invariants = coord.check_invariants(0, robots, [])
    assert set(invariants.keys()) == {
        "no_envelope_violation",
        "handoff_within_2s",
        "peer_sensor_in_model_within_1_tick",
        "swarm_estop_within_5ms",
        "self_state_publish_1hz",
        "defer_to_lead_during_ae",
        "willing_to_lead",
    }


def test_envelope_violation_caught(coord: SwarmCoordinator) -> None:
    robots = [
        build_robot("SF-01-H2-A", x=1.0, y=2.0, z=1.5),
        build_robot("SF-01-H2-B", x=1.1, y=2.0, z=1.5),
        build_robot("SF-01-H2-C", x=2.0, y=2.0, z=1.5),
    ]
    invariants = coord.check_invariants(0, robots, [])
    assert not invariants["no_envelope_violation"]
