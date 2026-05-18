"""Compute 26-key metric vectors per iteration and per configuration.

Reads data/iterations/index.jsonl (or aggregate.duckdb if available) and
data/human_team_baseline.csv. Writes reports/comparison.json.
"""

from __future__ import annotations

import argparse
import csv
import json
import pathlib
import statistics
from typing import Optional


WEIGHTS = {
    "response_time": 0.25,
    "patient_safety": 0.20,
    "fda_rtct_compliance": 0.15,
    "camaraderie": 0.10,
    "cost": 0.10,
    "safety": 0.10,
    "patient_experience": 0.10,
}


def compute_iteration_metrics(iteration_id: int, index_path: pathlib.Path) -> dict:
    for line in index_path.read_text().splitlines():
        if not line.strip():
            continue
        rec = json.loads(line)
        if rec["iteration_id"] == iteration_id:
            return rec
    raise KeyError(iteration_id)


def compute_configuration_metrics(
    configuration_id: str,
    iteration_metrics: list[dict],
) -> dict:
    out: dict = {"configuration_id": configuration_id}
    keys = set().union(*(m.keys() for m in iteration_metrics))
    for k in keys:
        values = [m[k] for m in iteration_metrics if isinstance(m.get(k), (int, float))]
        if values:
            out[k] = statistics.median(values)
    return out


def compute_weighted_score(metrics: dict, weights: dict = WEIGHTS) -> float:
    rt = 1.0 / max(metrics.get("response_time_p50_seconds", 1.0), 1.0)
    ps = metrics.get("patient_safety_estop_reliability", 0.999)
    fda = metrics.get("fda_rtct_1hr_compliance_rate", 0.999)
    cam = metrics.get("camaraderie_invariants_pass_rate", 0.95)
    cost = 1.0 / max(metrics.get("cost_amortized_per_ae_usd", 1000.0), 1.0)
    safe = 1.0 - min(metrics.get("patient_safety_envelope_violations", 0), 100) / 100
    pe = metrics.get("patient_survey_score", 0.85)
    return (
        weights["response_time"] * rt * 50.0
        + weights["patient_safety"] * ps
        + weights["fda_rtct_compliance"] * fda
        + weights["camaraderie"] * cam
        + weights["cost"] * cost * 1000.0
        + weights["safety"] * safe
        + weights["patient_experience"] * pe
    )


def rank_configurations(configurations: dict) -> list[tuple]:
    scored = [
        (cid, compute_weighted_score(m, WEIGHTS)) for cid, m in configurations.items()
    ]
    return sorted(scored, key=lambda kv: kv[1], reverse=True)


def load_baseline(baseline_csv: pathlib.Path) -> dict:
    medians: dict[str, list[float]] = {}
    if not baseline_csv.exists():
        return {}
    with baseline_csv.open() as f:
        for row in csv.DictReader(f):
            ae_type = row["ae_type"]
            medians.setdefault(ae_type, []).append(float(row["median_response_seconds"]))
    return {k: statistics.median(v) for k, v in medians.items()}
