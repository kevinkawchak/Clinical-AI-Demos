# Authoring Instructions for `data/aggregate.duckdb`

The future session generates this DuckDB database during Commit 4 of 7.

## Purpose

A single DuckDB file containing the aggregate tables across all 32 iterations. Backed by Parquet files for the heavy data; the DuckDB file itself is small (under 5 MB).

## Tables

```
CREATE TABLE iterations (
  iteration_id INTEGER,
  seed INTEGER,
  llm_temperature DOUBLE,
  ae_arrival_jitter_seconds INTEGER,
  response_time_variance DOUBLE,
  camarade_aggressiveness DOUBLE,
  ticks INTEGER,
  ae_count INTEGER,
  escalation_count INTEGER,
  fda_rtct_count INTEGER,
  median_response_time_seconds DOUBLE,
  p95_response_time_seconds DOUBLE,
  camaraderie_invariants_pass_rate DOUBLE,
  peer_handoff_p95_seconds DOUBLE,
  role_rotation_count INTEGER
);

CREATE TABLE per_site (
  iteration_id INTEGER,
  site VARCHAR,
  ae_count INTEGER,
  median_response_time_seconds DOUBLE,
  swarm_uptime_percent DOUBLE
);

CREATE TABLE per_swarm (
  iteration_id INTEGER,
  swarm_id VARCHAR,
  lead_role_changes INTEGER,
  assist_role_changes INTEGER,
  reserve_role_changes INTEGER,
  camaraderie_invariants_pass_rate DOUBLE
);

CREATE TABLE per_day (
  iteration_id INTEGER,
  site VARCHAR,
  day_of_week INTEGER,
  ae_count INTEGER,
  median_response_time_seconds DOUBLE,
  battery_swaps_count INTEGER
);

CREATE TABLE per_ae_type (
  iteration_id INTEGER,
  ae_type VARCHAR,
  count INTEGER,
  median_response_time_seconds DOUBLE,
  ctcae_grade_distribution VARCHAR
);

CREATE TABLE camaraderie_invariants (
  iteration_id INTEGER,
  invariant_name VARCHAR,
  pass_count INTEGER,
  fail_count INTEGER,
  pass_rate DOUBLE
);

CREATE TABLE handoffs (
  iteration_id INTEGER,
  requester_role VARCHAR,
  responder_role VARCHAR,
  tool VARCHAR,
  count INTEGER,
  median_seconds DOUBLE,
  p95_seconds DOUBLE,
  decline_count INTEGER
);
```

## Build Step

- After all 32 iterations finish, `src/iterate.py` reads each iteration's per-day Parquet outputs and inserts aggregated rows.
- The DuckDB file is committed to the repository (under 5 MB).

## Validation Rules

- 32 rows in `iterations` table.
- 128 rows in `per_site` (32 iterations x 4 sites).
- 128 rows in `per_swarm` (32 iterations x 4 swarms).

## Notes

- DuckDB SQL queries against this file power the dashboard in `reports/dashboard.html`.
- All metrics are also exposed via the `metrics.schema.json` in commit 5.
