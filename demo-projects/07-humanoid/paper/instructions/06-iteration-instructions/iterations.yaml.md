# Authoring Instructions for `config/iterations.yaml`

The future session writes this YAML during Commit 4 of 7.

## Purpose

Defines the 32-iteration deterministic sweep across 5 dimensions: seed, LLM temperature, AE arrival jitter, response time variance, camarade aggressiveness.

## Fields

```
iteration_count: 32
seed_base: 1717171717

axes:
  - name: seed
    values: [1, 2, 3, 4, 5, 6, 7, 8]
  - name: llm_temperature
    values: [0.0, 0.1, 0.2, 0.3]
  - name: ae_arrival_jitter_seconds
    values: [0, 30, 60, 120]
  - name: response_time_variance
    values: [0.0, 0.05, 0.10, 0.20]
  - name: camarade_aggressiveness
    values: [0.5, 0.75, 1.0, 1.25]

sweep_strategy: lhs_32
latin_hypercube_balanced_pairs: true

output_dir: data/iterations
parquet_partition_by:
  - site
  - day

l0_archive_target: zenodo
l0_archive_max_gb_per_site: 1.0
l1_minute_parquet: data/iterations/l1
l2_hour_jsonl: data/iterations/l2
l3_day_markdown: data/iterations/l3

run_index: data/iterations/index.jsonl
run_aggregate: data/iterations/aggregate.duckdb
```

## Validation Rules

- 32 iterations total.
- 5 axes.
- Latin hypercube sampling for balanced coverage.

## Notes

- `lhs_32` is a 32-point Latin Hypercube design. Each axis value appears in the same number of iterations.
- `l0_archive_max_gb_per_site` caps the per-site raw archive at 1 GB. Total across 4 sites is 4 GB, within the Zenodo free tier.
