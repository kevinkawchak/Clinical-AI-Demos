# Run Log Record Layout

For a single 168-hour 32-iteration run, the future session's output looks like:

```
data/
  iterations/
    run_00000.parquet
    run_00001.parquet
    ...
    run_00031.parquet
    index.jsonl                # 32 lines
    aggregate.duckdb           # 7 tables
    l1/                        # minute aggregates per site per day
      site=SF-01/day=0/...
      site=SF-01/day=1/...
      ...
    l2/                        # hour summaries per site per day
      site=SF-01/day=0.jsonl
      ...
    l3/                        # day narrative markdown
      site=SF-01/day=0.md
      ...
  week_humanoid_commands_sample.parquet
  week_ae_events.parquet
  week_ctcae_gradings.parquet
  week_fda_rtct_submissions.parquet
  week_physician_escalations.parquet
  week_llm_decisions_sample.jsonl
  week_swarm_messages.parquet
  week_peer_handoffs.parquet
  week_robot_camarade_states.parquet
  samples.jsonl
  human_team_baseline.csv
  ctcae_decision_table.csv
```

## index.jsonl Schema

Each line is a JSON object with:

```
{
  "iteration_id": 0,
  "seed": 1,
  "llm_temperature": 0.0,
  "ae_arrival_jitter_seconds": 0,
  "response_time_variance": 0.0,
  "camarade_aggressiveness": 1.0,
  "sites": ["SF-01", "SD-01", "BO-01", "AT-01"],
  "ticks_per_site": 604800,
  "ae_count_total": 84,
  "ctcae_grade_distribution": {"1": 22, "2": 38, "3": 18, "4": 5, "5": 1},
  "median_response_time_seconds": 67.5,
  "p95_response_time_seconds": 88.2,
  "camaraderie_invariants_pass_rate": 0.985,
  "fda_rtct_1hr_compliance_rate": 0.999,
  "swarm_uptime_percent": 99.7,
  "l0_raw_parquet_zenodo_doi": "10.5281/zenodo.placeholder"
}
```

## Notes

- L0 raw is archived to Zenodo. Only the DOI is in the index.
- L1, L2, L3 are committed for inspection. L0 is too large for git.
- The `samples.jsonl` from commit 2 is preserved across runs; the per-iteration index distinguishes the runs.
