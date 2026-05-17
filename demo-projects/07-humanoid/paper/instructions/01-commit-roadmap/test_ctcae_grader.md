# Authoring Instructions for `tests/test_ctcae_grader.py`

The future session writes this pytest module during Commit 6 of 7.

## Purpose

Validates the CTCAE grading logic in `src/ctcae_grader.py`.

## Suggested Content

```
import pathlib
import pytest

from ctcae_grader import CTCAEGrader


@pytest.fixture
def grader():
    return CTCAEGrader(pathlib.Path("data/ctcae_decision_table.csv"))


def test_anaphylaxis_grade_4_on_low_spo2(grader):
    ae = {"ae_id": "ae-0000000000000000", "ae_type": "anaphylaxis"}
    vitals = {"spo2": 80, "rash": True, "wheezing": True}
    result = grader.grade_per_robot(ae, vitals)
    assert result["ctcae_grade"] == 4


def test_hypotension_grade_3(grader):
    ae = {"ae_id": "ae-0000000000000000", "ae_type": "hypotension"}
    vitals = {"sbp": 85}
    result = grader.grade_per_robot(ae, vitals)
    assert result["ctcae_grade"] == 3


def test_swarm_consensus_majority(grader):
    gradings = [
        {"ctcae_grade": 3, "confidence": 0.9},
        {"ctcae_grade": 3, "confidence": 0.8},
        {"ctcae_grade": 4, "confidence": 0.7},
    ]
    result = grader.grade_swarm_consensus(gradings)
    assert result["ctcae_grade"] == 3
    assert result["grader"] == "swarm_consensus"


def test_swarm_consensus_escalates_on_disagreement(grader):
    gradings = [
        {"ctcae_grade": 1, "confidence": 0.9},
        {"ctcae_grade": 4, "confidence": 0.8},
        {"ctcae_grade": 2, "confidence": 0.7},
    ]
    result = grader.grade_swarm_consensus(gradings)
    assert result.get("escalated_to_physician", False)
```

## Validation Rules

- 4 tests covering individual grading and swarm consensus.
- Disagreement test confirms physician escalation.

## Notes

- The decision table is loaded once per test module via the fixture.
- The swarm consensus test confirms the camarade benefit: 3 independent gradings catch outliers.
