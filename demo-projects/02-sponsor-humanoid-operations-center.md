# Demo Prompt 02: Pharmaceutical Sponsor Humanoid Operations Center

[![Demo](https://img.shields.io/badge/Demo-02%20of%2010-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![Companion](https://img.shields.io/badge/Companion-physical--ai--oncology--trials-purple.svg)](https://github.com/kevinkawchak/physical-ai-oncology-trials)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18445179-blue)](https://doi.org/10.5281/zenodo.18445179)
[![Resolution](https://img.shields.io/badge/Resolution-1s-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![Humanoid](https://img.shields.io/badge/Humanoid-Tesla%20Optimus%20Gen%203-orange.svg)](https://www.tesla.com/AI)
[![LLM](https://img.shields.io/badge/LLM-Claude%20Sonnet%204.6%20%2B%20Cloud%20Failover-blueviolet.svg)](https://www.anthropic.com)
[![Python](https://img.shields.io/badge/Python-3.10%20|%203.11%20|%203.12-blue.svg)](https://www.python.org/)

Released on 16 May 2026
CEO Kevin Kawchak, ChemicalQDevice

## Perspective

A pharmaceutical company sponsor (SPO-2026-001, mid-cap oncology specialist running 5 active Phase II and Phase III oncology trials) operates a Humanoid Operations Center on the 40th floor of its global HQ. Five Tesla Optimus Gen 3 humanoids work alongside 12 human staff across three shifts. The Optimus humanoids perform physical sponsor tasks (paper-document handling, regulatory filing physical-packet preparation, vial chain-of-custody scanning, sample courier handoff to overnight carriers, dispensary kit assembly) while a Claude Sonnet 4.6 on-prem deployment handles document drafting, FDA RTCT submission preparation, and per-site CRA call summaries. Cloud failover to Claude Opus 4.7 1M activates for any task exceeding 200K input tokens or requiring 1M-context reasoning across all 5 trials simultaneously.

## Thesis

A sponsor Humanoid Operations Center compresses the calendar time between trial events (adverse event reports arriving at sponsor receipt, regulatory submission packets exiting sponsor offices, IMP kits leaving sponsor depot) from 24 hours to 1 hour by running 24/7 with 5 humanoids and a continuously-on LLM. The 168-hour weekly simulation produces an auditable record of every humanoid pick, every LLM document draft, every FDA RTCT submission, and every CRA call summary. The on-prem LLM never reveals trial-specific patient data to a cloud failover without applying the Safe Harbor 45 CFR 164.514(b) de-identification gate first.

## Scope

- One simulated sponsor: SPO-2026-001 (mid-cap oncology, 250 employees, 5 active oncology trials, headquartered in Boston).
- Five simulated humanoids: 5 Tesla Optimus Gen 3 units (43 DOF, 1.73 m height, 57 kg, 9 kg payload per arm, 5 actuator-shared fingers per hand for vial gripping).
- One simulated LLM: Claude Sonnet 4.6 on-prem (default) with cloud failover to Claude Opus 4.7 1M (Anthropic API, gated by PHI redaction).
- One week duration: 168 hours (604,800 s, 604,800 ticks at 1 Hz LLM cadence, 6,048,000 ticks at 10 Hz humanoid motion cadence).
- Active trial portfolio: TRIAL-NSCLC-3A, TRIAL-CRC-2B, TRIAL-BREAST-2C, TRIAL-PROSTATE-3A, TRIAL-PANC-2A.
- Document types: FDA RTCT submission, IRB amendment, CRA call summary, IMP kit manifest, adverse event report, SAE narrative, DSMB monthly summary, sponsor SOP update.
- Iteration count: 16 deterministic iterations covering seed, LLM failover threshold, humanoid task-priority weight matrix, and per-trial enrollment velocity.

## Why a Future Pass

A 168-hour sponsor center simulation with 5 humanoids at 10 Hz produces 30,240,000 humanoid-tick records plus 604,800 LLM decision records. Authoring inline would exceed working memory. The future session writes generator scripts and stratified human-review samples.

## Inputs from physical-ai-oncology-trials

| Path | Purpose |
|------|---------|
| `sponsor/input_files/` | 16 sponsor playbook and organization chunks (verbatim source) |
| `sponsor/paper/main.tex` | Autonomous sponsor paper (18 sections + 6 appendices) |
| `sponsor/final_paper/scripts/run_sponsor_simulation.py` | Master 24-hour sponsor simulation runner |
| `sponsor/final_paper/scripts/sponsor_server/` | FastAPI sponsor control server (15 files) |
| `sponsor/final_paper/scripts/hourly/` | 24 hourly sponsor generators + JSON output |
| `sponsor/final_paper/scripts/core_agents/` | 53 core sponsor agent implementations |
| `sponsor/final_paper/scripts/coordination/` | Agent event bus, escalation, gates |
| `sponsor/final_paper/scripts/safety/` | Robotic safety workflows |
| `sponsor/final_paper/scripts/dashboard/` | Terminal dashboard and reports |
| `sponsor/final_paper/168_hours/` | 168-hour simulation reference (verbatim pattern) |
| `sponsor/final_paper/168_hours/run_168h_simulation.py` | 168-hour master runner |
| `sponsor/final_paper/168_hours/day_01/` through `day_07/` | 7-day reference structure |
| `unification/usl/humanoids/tesla_optimus/` | Optimus USL scoring data |
| `regulatory/regulatory-intelligence/regulatory_tracker.py` | Multi-jurisdiction monitoring |
| `regulatory/fda-compliance/fda_submission_tracker.py` | 510(k) / De Novo / PMA tracking |
| `regulatory-submit/presub_generator.py` | Pre-Submission (Q-Sub) package generation |
| `regulatory-submit/pccp_engine.py` | PCCP document authoring |
| `regulatory-submit/audit_trail.py` | 21 CFR Part 11 audit trails |
| `privacy/de-identification/deidentification_pipeline.py` | Safe Harbor 45 CFR 164.514(b) gate |
| `competitions/instructions/chunking_strategy.md` | Three-layer chunking (verbatim) |
| `competitions/instructions/file_format_conventions.md` | Repository-wide file formats |

## Downstream LLM Processing Instructions

The future Claude Code Opus 4.7 1M Max session must:

1. Read all 16 chunks under `sponsor/input_files/` (`sponsor_01-08_*.md` plus `org_01-07_*.md`) plus the cross-document alignment README before authoring any output. These define the End-to-End Sponsor Playbook and the Sponsor Organization layout that the simulation must respect.
2. Mirror the 168-hour structure from `sponsor/final_paper/168_hours/` (7 day directories with hourly subdirectories) but replace single-humanoid agent emissions with 5-humanoid Optimus emissions and add an explicit Humanoid Operations Center physical-task track.
3. Use the FastAPI sponsor control server pattern from `sponsor/final_paper/scripts/sponsor_server/` for the on-prem LLM endpoint. The 15-file pattern includes auth, rate limit, audit log, document draft, document review, document signoff endpoints.
4. Apply the Safe Harbor 45 CFR 164.514(b) gate from `privacy/de-identification/deidentification_pipeline.py` before any cloud failover call. Cloud failover is permitted only after de-identification.
5. Follow the 168-hour file budget: per-day under 1.5 MB committed, total per-week under 10 MB committed. L0 raw of 1.2 GB across all humanoid 10 Hz motion telemetry archived to Zenodo (free 50 GB tier).
6. Run pre-commit checklist: `ruff check .`, `ruff format --check .`, `yamllint -d relaxed .github/`.
7. Commit and push seven sequential commits in a single PR on branch `claude/demo-02-sponsor-center-shortid`.

## Future Output Tree

```
demo-projects/02-sponsor-humanoid-operations-center-output/
  README.md
  config/
    sponsor.yaml                     # SPO-2026-001 portfolio definition
    optimus_humanoid.yaml            # 5x Optimus Gen 3 specs
    llm_loop.yaml                    # Sonnet 4.6 on-prem + Opus 4.7 cloud failover
    portfolio_trials.yaml            # 5 active oncology trials
  schemas/
    humanoid_command.schema.json
    document_draft.schema.json
    cra_call_summary.schema.json
    imp_kit_manifest.schema.json
    ae_report.schema.json
    llm_decision.schema.json
    audit_trail.schema.json
  src/
    sponsor_state.py
    optimus_dispatcher.py            # 5-humanoid arbiter with inter-humanoid coordination
    llm_drafter.py                   # Sonnet 4.6 default + Opus 4.7 cloud failover
    phi_redactor.py                  # Safe Harbor gate before cloud egress
    fda_rtct_submitter.py            # FDA RTCT pilot integration
    week_runner.py                   # 168-hour orchestrator
  data/
    week_humanoid_commands.parquet   # 6,048,000 ticks across 5 humanoids
    week_llm_decisions.jsonl         # 604,800 LLM decisions
    week_documents/                  # 200+ authored documents (drafts, finals)
    week_imp_manifests.parquet
    week_ae_reports.parquet
    iterations/
      run_NNNNN.parquet              # 16 iteration outputs
      index.jsonl
      aggregate.duckdb
  diagrams/
    sponsor_center_layout.txt        # 40th floor ASCII map
    humanoid_state_timeline.txt
    document_flow.txt
```

## Per-Commit Roadmap

| Commit | Files | Authored Content |
|--------|-------|------------------|
| 1 | 7 | Project README, architecture.md with 5-humanoid Mermaid topology, pyproject.toml, docker-compose.yml with sponsor_server service, config/sponsor.yaml, LICENSE.txt, sponsor_center_layout.txt |
| 2 | 9 | 7 schemas (humanoid_command, document_draft, cra_call_summary, imp_kit_manifest, ae_report, llm_decision, audit_trail), JSONL samples, ingest.py |
| 3 | 10 | optimus_dispatcher.py with 5-humanoid coordination, llm_drafter.py with failover, phi_redactor.py, kinematics.yaml for 5 Optimus units, sensor_to_xyz.py, robot_loop.cpp with inter-humanoid heartbeat, per-humanoid CSV samples, xyz path ASCII, 8 mm inter-humanoid minimum distance check |
| 4 | 11 | week_runner.py, iterations.yaml (4-dim sweep), iterate.py, runner.rs, Cargo.toml, per-day Parquet outputs for 7 days, index.jsonl, aggregate.duckdb with 6 tables, analysis notebook, run log |
| 5 | 13 | comparison_methodology.md, metrics.schema.json with 19 required keys, sponsor_baseline.csv (human-only sponsor operations from 6 published Phase II/III sponsor case studies), optimus_outcomes.parquet, compute.py, compare_agent.py, comparison_prompt.md frozen, comparison.json, report.md, report.pdf, dashboard.html, summary.png, per-humanoid contribution chart |
| 6 | 7-check error scan |
| 7 | 3 | Parent README, releases.md entry, CHANGELOG.md v0.3.0 block |

## CI Compliance

Add per-file-ignores to `ruff.toml`:

```toml
"demo-projects/02-sponsor-humanoid-operations-center-output/**/*.py" = ["F401", "F402", "F821", "E402"]
```

Run `ruff check`, `ruff format --check`, `yamllint -d relaxed .github/` on every commit. The companion `sponsor/` directory uses `E402` because of sys.path manipulation; this demo inherits that allowance.

## Comparison Framework

Three categories:
1. Prior versions of this demo (snapshot at `releases/v0.2.0/`).
2. Competitor sponsor humanoid configurations: Figure 03 (3 units), Atlas Electric (3 units), human-only sponsor operations.
3. Hybrid teams with non-zero `human_intervention_seconds`.

Weights: Quality 0.35, Time 0.25, Cost 0.20, Safety 0.10, FDA RTCT Latency 0.10. Gaussian skill rating mu_0 = 600, sigma_0 = 200.

## Notes

- Single dashes only. No em dashes, no double dashes.
- The 5-humanoid coordination protocol must respect a cumulative 25 N tip-force limit across all humanoid arms operating in the same 2 m by 2 m workspace zone, with proportional throttling above 22 N.
- Cloud failover is logged in the audit trail with the cloud model name, the redaction hash, and the calling humanoid ID. No PHI ever crosses the cloud boundary.
- FDA RTCT submissions follow the v3.4.2 National 24/7 Continuous RTCT pattern from `new-trial/national-24-7-trial/` with sponsor-side hash-chained provenance.
