# Authoring Instructions for `tests/test_kinematics.py`

The future session writes this pytest module during Commit 6 of 7.

## Purpose

Validates the H2 kinematics chain in `src/kinematics.yaml`. Confirms 39 DOF, all joint ranges are physically reasonable, IK solver settings are consistent.

## Suggested Content

```
import pathlib
import yaml


def test_kinematics_has_39_dof():
    k = yaml.safe_load(pathlib.Path("src/kinematics.yaml").read_text())
    total = sum(len(chain) for chain in k["chains"].values())
    assert total == 39


def test_joint_ranges_reasonable():
    k = yaml.safe_load(pathlib.Path("src/kinematics.yaml").read_text())
    for chain_name, chain in k["chains"].items():
        for joint in chain:
            low, high = joint["range_rad"]
            assert low < high, f"{chain_name}.{joint['name']} has empty range"
            assert -3.5 <= low <= high <= 3.5


def test_ik_solver_settings():
    k = yaml.safe_load(pathlib.Path("src/kinematics.yaml").read_text())
    assert k["ik_solver"]["algorithm"] == "damped_least_squares"
    assert k["ik_solver"]["position_tolerance_m"] <= 0.01
    assert k["ik_solver"]["orientation_tolerance_rad"] <= 0.05
```

## Validation Rules

- 39 joints total.
- All ranges reasonable.
- IK solver settings present.

## Notes

- The kinematics tests are fast (under 1 second).
- The right_arm and right_leg sections in `kinematics.yaml` are filled in commit 6 if commit 3 left them abbreviated.
