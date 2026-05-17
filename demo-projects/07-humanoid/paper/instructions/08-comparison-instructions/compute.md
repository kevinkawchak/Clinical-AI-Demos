# Authoring Instructions for `src/compute.py`

The future session writes this Python module during Commit 5 of 7.

## Purpose

Computes the 26-key metric vector for each iteration and each configuration. Reads `data/aggregate.duckdb` and `data/human_team_baseline.csv`. Writes `reports/comparison.json`.

## Required Interfaces

```
def compute_iteration_metrics(iteration_id: int, duckdb_path: pathlib.Path) -> dict: ...
def compute_configuration_metrics(configuration_id: str, iteration_metrics: list[dict]) -> dict: ...
def compute_weighted_score(metrics: dict, weights: dict) -> float: ...
def rank_configurations(configurations: dict) -> list[dict]: ...
```

## Suggested Skeleton

```
import json
import pathlib

import duckdb


WEIGHTS = {
    "response_time": 0.25,
    "patient_safety": 0.20,
    "fda_rtct_compliance": 0.15,
    "camaraderie": 0.10,
    "cost": 0.10,
    "safety": 0.10,
    "patient_experience": 0.10,
}


def compute_iteration_metrics(iteration_id, duckdb_path):
    conn = duckdb.connect(str(duckdb_path), read_only=True)
    row = conn.execute("SELECT * FROM iterations WHERE iteration_id = ?", [iteration_id]).fetchone()
    cols = [c[0] for c in conn.description]
    return dict(zip(cols, row))


def compute_configuration_metrics(configuration_id, iteration_metrics):
    import statistics
    out = {"configuration_id": configuration_id}
    keys = set().union(*(m.keys() for m in iteration_metrics))
    for k in keys:
        values = [m[k] for m in iteration_metrics if isinstance(m.get(k), (int, float))]
        if values:
            out[k] = statistics.median(values)
    return out


def compute_weighted_score(metrics, weights):
    rt = 1.0 / max(metrics.get("response_time_p50_seconds", 1.0), 1.0)
    ps = metrics.get("patient_safety_estop_reliability", 0.0)
    fda = metrics.get("fda_rtct_1hr_compliance_rate", 0.0)
    cam = metrics.get("camaraderie_invariants_pass_rate", 0.0)
    cost = 1.0 / max(metrics.get("cost_amortized_per_ae_usd", 1.0), 1.0)
    safe = 1.0 - min(metrics.get("patient_safety_envelope_violations", 0), 100) / 100
    pe = metrics.get("patient_survey_score", 0.0)
    return (
        weights["response_time"] * rt
        + weights["patient_safety"] * ps
        + weights["fda_rtct_compliance"] * fda
        + weights["camaraderie"] * cam
        + weights["cost"] * cost
        + weights["safety"] * safe
        + weights["patient_experience"] * pe
    )


def rank_configurations(configurations):
    scored = [(cid, compute_weighted_score(m, WEIGHTS)) for cid, m in configurations.items()]
    return sorted(scored, key=lambda kv: kv[1], reverse=True)
```

## Validation Rules

- 26 keys per metric record.
- All numeric values in expected ranges.
- Weighted score is a real number; higher is better.

## Notes

- DuckDB read-only mode prevents accidental writes.
- The score is a simple weighted sum; production would calibrate the response time and cost components via z-score normalization first.
