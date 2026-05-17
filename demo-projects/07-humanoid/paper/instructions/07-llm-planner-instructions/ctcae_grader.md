# Authoring Instructions for `src/ctcae_grader.py`

The future session writes this Python module during Commit 4 of 7.

## Purpose

Grades adverse events on the CTCAE v5.0 scale (1 mild to 5 fatal). One grading per AE per re-grade event. The HR 9505 SLA requires a grading within 1 hour of AE detection.

## Key Behavior

- Reads the AE event record plus the patient vitals at AE time.
- Maps the vital signs to a CTCAE term and grade using a rule-based decision table.
- Records the grading via the `schemas/ctcae_grading.schema.json` record format.
- Allows the on-call physician to override the grading; the LLM-generated grading is then marked superseded.
- Supports swarm consensus: all 3 robots in the camarade swarm independently grade; the majority wins.

## Required Interfaces

```
class CTCAEGrader:
    def __init__(self, decision_table_path: pathlib.Path) -> None: ...
    def grade_per_robot(self, ae_event: dict, vitals: dict) -> dict: ...
    def grade_swarm_consensus(self, per_robot_gradings: list[dict]) -> dict: ...
    def grade_by_physician(self, ae_event: dict, physician_id: str, grade: int, term: str, rationale: str) -> dict: ...
```

## Decision Table Excerpt

```
# data/ctcae_decision_table.csv (authored in commit 4)
ae_type,vital_threshold,grade,term
anaphylaxis,spo2<85,4,Anaphylaxis Grade 4 life threatening
anaphylaxis,spo2<92,3,Anaphylaxis Grade 3 severe
anaphylaxis,wheezing+rash,2,Anaphylaxis Grade 2 moderate
hypotension,sbp<70,4,Hypotension Grade 4 life threatening
hypotension,sbp<90,3,Hypotension Grade 3 severe
hypoxia,spo2<88,3,Hypoxia Grade 3 severe
hypoxia,spo2<92,2,Hypoxia Grade 2 moderate
syncope,loss_of_consciousness_seconds>60,3,Syncope Grade 3 severe
cytokine_release_syndrome,fever+hypotension+hypoxia,4,CRS Grade 4 life threatening
cardiac_arrest,asystole,5,Cardiac Arrest Grade 5 death
```

## Swarm Consensus Algorithm

- All 3 robots run `grade_per_robot` independently.
- The grade is set to the median grade across the 3.
- If 2 robots disagree by 2 or more grade levels, the grading is escalated to the on-call physician immediately.
- The grader returns a consensus record with `grader: swarm_consensus` and the 3 individual gradings in the rationale.

## Validation Rules

- Grade in [1, 5].
- CTCAE version is exactly `5.0`.
- Confidence is the proportion of robots agreeing with the consensus.

## Notes

- The decision table is intentionally simple. Production would use a learned classifier trained on FAERS data per the BibTeX reference 10.5281/zenodo.18029100.
- The author's prior FAERS work (DOI 10.5281/zenodo.18029100) provides the precedent for LLM-driven adverse event grading.
