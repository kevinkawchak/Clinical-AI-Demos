# Authoring Instructions for `data/h2_swarm_outcomes.parquet`

The future session writes this Parquet during Commit 5 of 7.

## Purpose

Per-AE outcome record across all 32 iterations. One row per (iteration, AE).

## Columns

```
iteration_id            INTEGER
ae_id                   VARCHAR
site                    VARCHAR
ae_type                 VARCHAR
ctcae_grade             INTEGER
responding_swarm        VARCHAR  # JSON array of 3 robot IDs
response_seconds        DOUBLE
resolution_seconds      DOUBLE
physician_paged         BOOLEAN
physician_ack_seconds   DOUBLE
fda_rtct_sla_met        BOOLEAN
sponsor_ack_sla_met     BOOLEAN
peer_handoff_count      INTEGER
peer_handoff_p95_s      DOUBLE
role_rotation_count     INTEGER
camaraderie_pass_rate   DOUBLE
lead_robot_at_start     VARCHAR
lead_robot_at_end       VARCHAR
estop_triggered         BOOLEAN
force_budget_violations INTEGER
envelope_violations     INTEGER
```

## Validation Rules

- Row count is approximately 84 AEs x 32 iterations = 2,688 rows.
- All booleans are explicit (no nulls).
- Synthetic AE IDs follow the pattern `ae-[0-9a-f]{16}`.

## Notes

- Partition by `iteration_id` for fast scans.
- Use zstd compression level 3.
- Read by `compute.py` to aggregate per-AE-type and per-site metrics.
