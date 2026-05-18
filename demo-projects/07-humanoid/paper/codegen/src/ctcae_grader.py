"""CTCAE v5.0 grader.

Grades an AE per robot using a vital-sign decision table. Supports swarm
consensus: 3 robots grade independently, the median wins. If 2 robots
disagree by 2 or more grade levels, the grading is escalated to the
on-call physician immediately.
"""

from __future__ import annotations

import csv
import pathlib
import statistics
import uuid
from typing import Optional


class CTCAEGrader:
    def __init__(self, decision_table_path: pathlib.Path) -> None:
        self.decision_table = self._load_table(decision_table_path)

    def _load_table(self, path: pathlib.Path) -> list[dict]:
        rows: list[dict] = []
        if not path.exists():
            return rows
        with path.open() as f:
            for row in csv.DictReader(f):
                rows.append(
                    {
                        "ae_type": row["ae_type"],
                        "vital_threshold": row["vital_threshold"],
                        "grade": int(row["grade"]),
                        "term": row["term"],
                    }
                )
        return rows

    def grade_per_robot(self, ae_event: dict, vitals: dict) -> dict:
        ae_type = ae_event.get("ae_type", "other")
        grade, term = self._lookup(ae_type, vitals)
        return {
            "grading_id": f"grd-{uuid.uuid4().hex[:16]}",
            "ae_id": ae_event.get("ae_id", "ae-0000000000000000"),
            "graded_at_iso": "2026-05-17T12:01:30Z",
            "grader": "llm_per_site",
            "ctcae_version": "5.0",
            "ctcae_grade": grade,
            "ctcae_term": term,
            "confidence": 0.85,
            "superseded_by": None,
        }

    def grade_swarm_consensus(self, per_robot_gradings: list[dict]) -> dict:
        if not per_robot_gradings:
            raise ValueError("at least 1 per-robot grading is required")
        grades = [g["ctcae_grade"] for g in per_robot_gradings]
        majority = int(statistics.median(grades))
        confidences = [g.get("confidence", 0.5) for g in per_robot_gradings]
        consensus = {
            "grading_id": f"grd-{uuid.uuid4().hex[:16]}",
            "ae_id": per_robot_gradings[0].get("ae_id", "ae-0000000000000000"),
            "graded_at_iso": "2026-05-17T12:01:35Z",
            "grader": "swarm_consensus",
            "ctcae_version": "5.0",
            "ctcae_grade": majority,
            "ctcae_term": per_robot_gradings[0].get("ctcae_term", ""),
            "confidence": statistics.mean(confidences),
            "rationale": f"swarm consensus: {grades}",
            "superseded_by": None,
        }
        if max(grades) - min(grades) >= 2:
            consensus["escalated_to_physician"] = True
        return consensus

    def grade_by_physician(
        self,
        ae_event: dict,
        physician_id: str,
        grade: int,
        term: str,
        rationale: str,
    ) -> dict:
        return {
            "grading_id": f"grd-{uuid.uuid4().hex[:16]}",
            "ae_id": ae_event.get("ae_id", "ae-0000000000000000"),
            "graded_at_iso": "2026-05-17T12:05:00Z",
            "grader": "on_call_physician",
            "ctcae_version": "5.0",
            "ctcae_grade": grade,
            "ctcae_term": term,
            "confidence": 1.0,
            "rationale": rationale,
            "superseded_by": None,
        }

    def _lookup(self, ae_type: str, vitals: dict) -> tuple[int, str]:
        spo2 = vitals.get("spo2", 100)
        sbp = vitals.get("sbp", 120)
        loss = vitals.get("loss_of_consciousness_seconds", 0)
        rash = bool(vitals.get("rash"))
        wheezing = bool(vitals.get("wheezing"))
        fever = bool(vitals.get("fever"))
        hypotension = sbp < 90
        hypoxia = spo2 < 92
        if ae_type == "anaphylaxis":
            if spo2 < 85:
                return 4, "Anaphylaxis Grade 4 life threatening"
            if spo2 < 92:
                return 3, "Anaphylaxis Grade 3 severe"
            if wheezing and rash:
                return 2, "Anaphylaxis Grade 2 moderate"
            if rash:
                return 1, "Anaphylaxis Grade 1 mild"
        if ae_type == "hypotension":
            if sbp < 60:
                return 4, "Hypotension Grade 4 life threatening"
            if sbp < 70:
                return 3, "Hypotension Grade 3 severe"
            if sbp < 90:
                return 2, "Hypotension Grade 2 moderate"
        if ae_type == "hypoxia":
            if spo2 < 85:
                return 4, "Hypoxia Grade 4 life threatening"
            if spo2 < 88:
                return 3, "Hypoxia Grade 3 severe"
            if spo2 < 92:
                return 2, "Hypoxia Grade 2 moderate"
        if ae_type == "syncope":
            if loss > 180:
                return 4, "Syncope Grade 4 life threatening"
            if loss > 60:
                return 3, "Syncope Grade 3 severe"
            if loss > 10:
                return 2, "Syncope Grade 2 moderate"
        if ae_type == "cytokine_release_syndrome":
            if fever and hypotension and hypoxia:
                return 4, "CRS Grade 4 life threatening"
            if fever and hypotension:
                return 3, "CRS Grade 3 severe"
            if fever:
                return 2, "CRS Grade 2 moderate"
        if ae_type == "cardiac_arrest":
            return 5, "Cardiac Arrest Grade 5 death"
        return 1, f"{ae_type} Grade 1 mild"
