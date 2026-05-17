# Authoring Instructions for `reports/comparison.json`

The future session writes this JSON during Commit 5 of 7.

## Purpose

The machine-readable comparison output. Used by the dashboard and report generators.

## Schema

```
{
  "v0_3_0": { ... 26 metric keys ... },
  "v0_1_0": { ... 26 metric keys ... },
  "competitor_atlas": { ... 26 metric keys ... },
  "competitor_optimus": { ... 26 metric keys ... },
  "competitor_human_team": { ... 26 metric keys ... },
  "hybrid_2h2_1human": { ... 26 metric keys ... },
  "hybrid_1h2_2humans": { ... 26 metric keys ... },
  "weights": { ... 7 dimensions ... },
  "ranking": [ ... configuration_id ordered by weighted score, best first ... ],
  "statistical_significance": { ... per-pair Mann-Whitney U p-values ... },
  "timestamp_iso": "2026-05-17T12:00:00Z",
  "iteration_count": 32,
  "window_hours": 168
}
```

## Validation Rules

- All 7 configurations present.
- Each configuration has 26 metric keys.
- Weights sum to 1.0.
- Ranking has 7 entries.

## Notes

- The file is written by `src/compute.py`.
- It is the source of truth for the dashboard and the report.
