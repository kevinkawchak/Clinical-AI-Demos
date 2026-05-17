# Authoring Instructions for Per-Day Parquet Outputs

The future session generates these Parquet files during Commit 4 of 7. They live under `data/`.

## Files

```
data/week_humanoid_commands.parquet           # Per-tick humanoid_command records, all 12 robots, 168 hours
data/week_humanoid_commands_sample.parquet    # 5 MB sample for commit, full file archived to Zenodo
data/week_ae_events.parquet                   # About 84 AE records, one row per AE
data/week_ctcae_gradings.parquet              # CTCAE grading records
data/week_fda_rtct_submissions.parquet        # FDA RTCT submission records
data/week_physician_escalations.parquet       # Physician escalation records
data/week_llm_decisions.jsonl                 # Per-tick LLM broadcast decisions, all sites
data/week_llm_decisions_sample.jsonl          # 2 MB sample for commit
data/week_swarm_messages.parquet              # UWB plus IR plus pubsub messages, sampled to 5 MB
data/week_peer_handoffs.parquet               # Hand-off records
data/week_robot_camarade_states.parquet       # 1 Hz state records per robot, sampled to 5 MB
```

## Schema Cross-References

Each Parquet file's column names and types come from the corresponding JSON Schema in `schemas/`. The future session converts the JSON Schema to a `pyarrow.Schema` programmatically at write time.

## Partitioning

All Parquet files are partitioned by `site` (4 values) and `day` (7 values). Total of 28 partitions per file. Each partition is a separate Parquet write that DuckDB and pandas can read efficiently.

## Compression

Use zstd level 3 compression. Trade-off: compresses 168-hour command stream from about 200 MB raw to about 30 MB.

## Sampling Strategy

Files flagged with `_sample` are sampled by:

- Stratified random sampling: pick the same percentage from each (site, day) partition.
- Target file size: 5 MB for command and state Parquet, 2 MB for JSONL.
- Sampling seed: 42 for reproducibility.

## Validation Rules

- All files have a header row matching the schema.
- All timestamps are ISO 8601 with UTC offset.
- All patient IDs are PAT-NET-001-PNNN format.

## Notes

- The full week file (`data/week_humanoid_commands.parquet`) is archived to Zenodo via the L0 archive flow. Only the sample is committed.
- Use `pyarrow.parquet.write_table` with `compression="zstd"`, `compression_level=3`, `use_dictionary=True`.
