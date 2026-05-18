"""Validate the CTCAE v5.0 grader."""

from __future__ import annotations

import pathlib

import pytest

from ctcae_grader import CTCAEGrader

ROOT = pathlib.Path(__file__).resolve().parent.parent


@pytest.fixture
def grader() -> CTCAEGrader:
    return CTCAEGrader(ROOT / "data" / "ctcae_decision_table.csv")


def test_anaphylaxis_grade_4_on_low_spo2(grader: CTCAEGrader) -> None:
    ae = {"ae_id": "ae-0000000000000000", "ae_type": "anaphylaxis"}
    vitals = {"spo2": 80, "rash": True, "wheezing": True}
    result = grader.grade_per_robot(ae, vitals)
    assert result["ctcae_grade"] == 4


def test_hypotension_grade_3(grader: CTCAEGrader) -> None:
    ae = {"ae_id": "ae-0000000000000000", "ae_type": "hypotension"}
    vitals = {"sbp": 65}
    result = grader.grade_per_robot(ae, vitals)
    assert result["ctcae_grade"] == 3


def test_cardiac_arrest_grade_5(grader: CTCAEGrader) -> None:
    ae = {"ae_id": "ae-0000000000000000", "ae_type": "cardiac_arrest"}
    vitals = {}
    result = grader.grade_per_robot(ae, vitals)
    assert result["ctcae_grade"] == 5


def test_swarm_consensus_majority(grader: CTCAEGrader) -> None:
    gradings = [
        {"ae_id": "ae-0000000000000000", "ctcae_grade": 3, "confidence": 0.9},
        {"ae_id": "ae-0000000000000000", "ctcae_grade": 3, "confidence": 0.8},
        {"ae_id": "ae-0000000000000000", "ctcae_grade": 4, "confidence": 0.7},
    ]
    result = grader.grade_swarm_consensus(gradings)
    assert result["ctcae_grade"] == 3
    assert result["grader"] == "swarm_consensus"


def test_swarm_consensus_escalates_on_disagreement(grader: CTCAEGrader) -> None:
    gradings = [
        {"ae_id": "ae-0000000000000000", "ctcae_grade": 1, "confidence": 0.9},
        {"ae_id": "ae-0000000000000000", "ctcae_grade": 4, "confidence": 0.8},
        {"ae_id": "ae-0000000000000000", "ctcae_grade": 2, "confidence": 0.7},
    ]
    result = grader.grade_swarm_consensus(gradings)
    assert result.get("escalated_to_physician", False)
