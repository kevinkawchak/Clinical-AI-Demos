# Working Memory Notes for Claude Code

The future Claude Code Opus 4.7 1M Max session must process a 168-hour window without LLM working memory truncation. This document captures the practical rules.

## The Window

```
One monitoring window: 168 hours
  604,800 s
  604,800 ticks at 1 Hz LLM cadence
  6,048,000 ticks at 10 Hz humanoid motion cadence per H2 when active
```

With 3 H2 per site and 4 sites, the upper bound on motion ticks per week is 3 * 4 * 6,048,000 equals 72,576,000 motion ticks across the network. The upper bound on LLM broadcast decisions per week is 4 sites * 604,800 ticks equals 2,419,200 broadcast decisions across the network.

No Claude Code working memory can hold 72 million motion records in a single context window. The data must be processed in chunks, persisted to disk, and only the chunk metadata kept in memory.

## Chunking Strategy

Use the three-layer chunking strategy from `kevinkawchak/physical-ai-oncology-trials/competitions/instructions/chunking_strategy.md`:

- L0 raw: per-tick sensor and motion records, archived to Zenodo, never loaded into the LLM context.
- L1 minute: per-minute aggregates (median, p95, count) per (robot, site, minute). Loaded only on demand for spot checks.
- L2 hour: per-hour aggregates (median, p95, count, AE count, escalation count). Loaded into the LLM context for run summaries.
- L3 day: per-day aggregates plus narrative AE descriptions. Always available in the LLM context for end-of-run reasoning.

Approximate sizes:

- L0 raw: about 3.2 GB across 4 sites (32 MB per iteration x 25 iter x 4 sites). Stored in Parquet partitioned by site and day. Archived to Zenodo.
- L1 minute: about 60 MB across 4 sites. Stored in Parquet partitioned by site and day.
- L2 hour: about 1 MB across 4 sites. Stored in JSONL.
- L3 day: about 100 KB across 4 sites. Stored in Markdown.

The LLM keeps L3 in working memory at all times, loads L2 for runs in scope, loads L1 only for spot checks, and never loads L0.

## Commit Processing Rules

The future session commits 7 sequential commits in one PR. Each commit must be authored without re-reading prior commits in full. Use these rules:

1. Author each commit's files in one push_files call.
2. Do not stream large data files into the LLM context. Instead, author a small Python script and run it locally to produce the data; commit the data file separately.
3. For Parquet generation, author the schema first (in commit 2 schemas/), then author the writer in commit 4 (week_runner.py), and only run the writer to generate Parquet at runtime.
4. For each commit, the LLM context need only hold:
   a. The 7 commit roadmap (constant)
   b. The current commit's instruction file from `01-commit-roadmap/` (about 5 KB)
   c. The schemas it depends on (about 20 KB total)
   d. The L3 day summaries for any prior data dependencies (about 1 KB)
5. After each commit, the LLM context can be safely truncated except for the 7 commit roadmap and the schemas.

## Late Commit Memory Pressure

The 6th and 7th commits are most prone to truncation because they reference all prior commits. Mitigations:

- Commit 6 (error scan) must run a local script to check all files; it should not re-read every file into the LLM context. Author the script in commit 4 and run it at commit 6.
- Commit 7 (repository updates) must use templates from `10-repository-update-instructions/` rather than re-reading the prior 6 commits.

## Tick Math Cheat Sheet

```
LLM cadence:    1 Hz   = 1 tick per second
Motion cadence: 10 Hz  = 10 ticks per second
UWB peer mesh:  200 Hz = 200 ticks per second
IR beacon:      1000 Hz = 1000 ticks per second

One minute:  60 LLM ticks,  600 motion ticks,  12,000 UWB,  60,000 IR
One hour:    3,600 LLM,     36,000 motion,     720,000 UWB,  3,600,000 IR
One day:    86,400 LLM,    864,000 motion,   17,280,000 UWB, 86,400,000 IR
One week:  604,800 LLM,  6,048,000 motion,  120,960,000 UWB, 604,800,000 IR
```

Only the LLM tick count needs to be tracked in the LLM context window. All other cadences are summarized at the L1 layer.

## Commit Size Budget

For LLM working memory safety, each commit should add no more than 15 new files and no more than 100 KB of new instructional content. The 7 commits in this present PR follow that budget:

| Commit | New Files | New KB | Memory Notes |
|--------|-----------|--------|--------------|
| 1 | 8 | 35 | Foundation, all reusable across later commits |
| 2 | 14 | 55 | Configs and schemas, structured data, low prose |
| 3 | 15 | 60 | Robotic, cartesian, iteration instructions |
| 4 | 9 | 45 | LLM planner, runtime |
| 5 | 9 | 40 | Comparison framework |
| 6 | 4 | 15 | Error fix notes only; runs local script |
| 7 | 4 | 20 | Templates only; runs local script |

Total: 63 files plus 270 KB across 7 commits, well within the 1M context budget for any single commit.

## Idempotency

Every instruction in this directory is idempotent. The future session may re-run any commit (for example commit 6 fixes after commit 5 errors are found) without breaking prior commits. This is enforced by:

- Schema-first design (commit 2 schemas are read by commit 3 and commit 4)
- File-level overwrite semantics (re-running an instruction overwrites the file at the same path)
- No mutable shared state between commits except for the audit log, which is append-only

## What Not To Do

- Do not paste the contents of an input companion repository file into the LLM context. Instead, summarize at L3 day granularity.
- Do not re-read the full 7 commit roadmap at every commit. Read it once, cache the relevant slice, move on.
- Do not commit Parquet larger than 5 MB. Larger Parquet is archived to Zenodo and only the pointer is committed.
- Do not commit JSONL larger than 2 MB. Sample down to a representative 2 MB.
- Do not commit any file with raw PHI. All patient IDs are synthetic.
