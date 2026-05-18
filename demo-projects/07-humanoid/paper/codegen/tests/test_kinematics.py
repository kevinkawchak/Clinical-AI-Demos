"""Validate the H2 EDU kinematics chain."""

from __future__ import annotations

import pathlib

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent


def test_kinematics_has_39_dof() -> None:
    k = yaml.safe_load((ROOT / "src" / "kinematics.yaml").read_text())
    total = sum(len(chain) for chain in k["chains"].values())
    assert total == 39


def test_platform_is_h2_edu() -> None:
    k = yaml.safe_load((ROOT / "src" / "kinematics.yaml").read_text())
    assert k["platform"] == "Unitree H2 EDU"


def test_joint_ranges_reasonable() -> None:
    k = yaml.safe_load((ROOT / "src" / "kinematics.yaml").read_text())
    for chain_name, chain in k["chains"].items():
        for joint in chain:
            low, high = joint["range_rad"]
            assert low < high, f"{chain_name}.{joint['name']} has empty range"
            assert -3.5 <= low <= high <= 3.5, (
                f"{chain_name}.{joint['name']} range {low},{high} out of bounds"
            )


def test_ik_solver_settings() -> None:
    k = yaml.safe_load((ROOT / "src" / "kinematics.yaml").read_text())
    assert k["ik_solver"]["algorithm"] == "damped_least_squares"
    assert k["ik_solver"]["position_tolerance_m"] <= 0.01
    assert k["ik_solver"]["orientation_tolerance_rad"] <= 0.05


def test_dexterous_hands_present() -> None:
    k = yaml.safe_load((ROOT / "src" / "kinematics.yaml").read_text())
    assert "left_hand" in k["chains"]
    assert "right_hand" in k["chains"]
    assert len(k["chains"]["left_hand"]) >= 3
    assert len(k["chains"]["right_hand"]) >= 3
