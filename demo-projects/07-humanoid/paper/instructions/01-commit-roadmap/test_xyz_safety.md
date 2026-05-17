# Authoring Instructions for `tests/test_xyz_safety.py`

The future session writes this pytest module during Commit 6 of 7.

## Purpose

Validates the cartesian safety validator in `src/xyz_safety.py`.

## Suggested Content

```
import pathlib
import pytest

from xyz_safety import validate_command, predict_peer_position, in_no_fly_zone


BOUNDS = {"x_min": -50.0, "x_max": 50.0, "y_min": -50.0, "y_max": 50.0, "z_min": 0.0, "z_max": 3.0, "no_fly_zones": []}


def base_command(x=1.0, y=2.0, z=1.5):
    return {
        "command_id": "cmd-0000000000000000",
        "tick": 0,
        "site": "SF-01",
        "robot_id": "SF-01-H2-A",
        "role": "Lead",
        "target_pose_xyz": {"x": x, "y": y, "z": z},
        "target_orientation_rpy": {"roll": 0.0, "pitch": 0.0, "yaw": 0.0},
        "gripper_state": "open",
        "peer_robot_ids": ["SF-01-H2-B", "SF-01-H2-C"],
        "synergy_score": 1.0,
        "audit_chain_prev_hash": "0" * 64,
    }


def test_valid_command_passes():
    ok, reason = validate_command(base_command(), [], None, BOUNDS)
    assert ok


def test_x_out_of_bounds_fails():
    cmd = base_command(x=100.0)
    ok, reason = validate_command(cmd, [], None, BOUNDS)
    assert not ok


def test_z_below_zero_fails():
    cmd = base_command(z=-0.5)
    ok, reason = validate_command(cmd, [], None, BOUNDS)
    assert not ok


def test_peer_envelope_violation_fails():
    peer = {"robot_id": "SF-01-H2-B", "position_xyz": {"x": 1.0, "y": 2.0, "z": 1.5}, "velocity_mps": 0.0}
    cmd = base_command(x=1.0, y=2.0, z=1.5)
    cmd["role"] = "Assist"
    ok, reason = validate_command(cmd, [peer], None, BOUNDS)
    assert not ok
```

## Validation Rules

- 4 tests covering bounds and peer envelope.
- All tests pass deterministically.

## Notes

- The future session may need to add a fifth test for no-fly zones; commit 6 includes the test fixture.
