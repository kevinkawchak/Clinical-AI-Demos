# Demo Prompt 01: Humanoid Trial Site Operations Director

[![Demo](https://img.shields.io/badge/Demo-01%20of%2010-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![Companion](https://img.shields.io/badge/Companion-physical--ai--oncology--trials-purple.svg)](https://github.com/kevinkawchak/physical-ai-oncology-trials)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18445179-blue)](https://doi.org/10.5281/zenodo.18445179)
[![Resolution](https://img.shields.io/badge/Resolution-1s-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![Humanoid](https://img.shields.io/badge/Humanoid-Atlas%20Electric-orange.svg)](https://www.bostondynamics.com/atlas)
[![LLM](https://img.shields.io/badge/LLM-Claude%20Opus%204.7%201M-blueviolet.svg)](https://www.anthropic.com)
[![Python](https://img.shields.io/badge/Python-3.10%20|%203.11%20|%203.12-blue.svg)](https://www.python.org/)

Released on 16 May 2026
CEO Kevin Kawchak, ChemicalQDevice

## Perspective

A single Boston Dynamics Atlas Electric humanoid stands at the central operations console of a Physical AI oncology clinical trial site. Across an 8-hour day shift (08:00 to 16:00 PDT) the humanoid coordinates 12 robotic surgical bays, 24 patient recovery rooms, 8 imaging suites, and 1 pharmacy clean room. The humanoid is the on-the-ground director of all site operations and is the single accountable agent for the shift. An on-prem Claude Opus 4.7 1M context LLM serves as the planner and arbiter for cross-bay scheduling, regulatory compliance gating, and adverse event escalation. The shift director humanoid never sits down and never asks the LLM to repeat itself.

## Thesis

On-prem Claude Opus 4.7 reads the live state of every bay, every patient, and every robot at 1 Hz; emits site-level commands at the same cadence; and dispatches the Atlas humanoid to perform the highest-priority physical task in the next 60 seconds. The humanoid arbitrates between three competing physical actions per minute on average across the 28,800 second shift (480 actions per hour). The simulation produces a continuous timeline of humanoid commands, bay-level status, patient vitals, and LLM decision rationale that downstream regulators can audit at second resolution.

## Scope

- One simulated trial site: PAT-SITE-001 (San Francisco, 4 floors, 12 surgical bays, 24 recovery rooms, 8 imaging suites, 1 pharmacy clean room).
- One simulated humanoid: Atlas Electric (28 DOF, 1.5 m height, 89 kg, 11 kg payload per arm, IP67-rated for clean room entry).
- One simulated LLM: Claude Opus 4.7 1M context (on-prem via Anthropic batch API mirror, 200 ms median round-trip latency budget).
- One shift duration: 8 hours (28,800 s, 28,800 ticks at 1 Hz LLM inference cadence, 287,520 ticks at 10 Hz humanoid motion control cadence).
- Patient cohort: 10 active patients across 3 oncology indications (4 NSCLC, 3 breast cancer Stage IIIA, 3 colorectal Stage IIIB).
- Iteration count: 32 deterministic iterations covering seed, LLM temperature, humanoid task-priority weights, and patient acuity distribution.

## Why a Future Pass

An 8-hour shift at 10 Hz humanoid motion control generates 287,520 ticks of structured telemetry plus a 28,800-tick LLM decision log. Authoring that volume inline as Markdown would exceed working memory. The downstream Claude Code Opus 4.7 1M Max session will author generator scripts that produce the full data files at runtime, plus stratified human-review samples.

## Inputs from physical-ai-oncology-trials

The future session must read the following input files from the companion repository:

| Path | Purpose |
|------|---------|
| `new-trial/README.md` | 24-hour on-demand trial simulation overview |
| `new-trial/site_specification.md` | Facility and staffing specifications for the trial site |
| `new-trial/psl_framework.md` | PSL scoring framework for robot evaluation |
| `new-trial/hour-00/hour_00_simulation.md` through `new-trial/hour-23/hour_23_simulation.md` | 24 hourly master simulation logs (pattern reference) |
| `new-trial/hour-00/hour_00_diagram_facility.txt` | Facility layout ASCII diagram (template) |
| `new-trial/hour-00/hour_00_diagram_patient_flow.txt` | Patient flow ASCII diagram (template) |
| `new-trial/hour-00/hour_00_diagram_robot_status.txt` | Robot status timeline ASCII diagram (template) |
| `new-trial/site/01-legislation-authorization/` | SB 1042 authorization act (regulatory ground) |
| `new-trial/site/04-city-regulations/` | SF municipal code update (zoning and access) |
| `new-trial/site/07-building-code/` | Facility construction standards |
| `new-trial/site/10-site-operations/` | Activation and SOPs (verbatim source) |
| `new-trial/site/11-emergency-preparedness/` | Emergency response plan (verbatim source) |
| `unification/usl/humanoids/boston_dynamics_atlas/` | Atlas USL scoring data |
| `unification/usl/humanoids/usl_humanoid_scoring.py` | Humanoid USL scoring framework |
| `patient-journey/patient_state.py` | Central data model (10 enums, 14 dataclasses) |
| `patient-journey/master_journey.py` | 10-stage patient orchestration logic |
| `regulatory/ich-gcp/gcp_compliance_checker.py` | GCP compliance verification |
| `competitions/instructions/ci_compliance_checklist.md` | Pre-commit ruff and yamllint checklist (verbatim) |
| `competitions/instructions/pr_workflow.md` | Seven-commit single-PR workflow (verbatim) |
| `competitions/instructions/ascii_diagram_guide.md` | ASCII drawing rules (80 col by 60 line cap) |

## Downstream LLM Processing Instructions

The future Claude Code Opus 4.7 1M Max session must:

1. Clone or update `kevinkawchak/physical-ai-oncology-trials` to read the input files listed above. Do not modify or commit anything to that repository.
2. Pre-chunk any input file over 20K tokens. The `new-trial/site/all-documents/all_documents_chunk/` pattern shows how to chunk 11-document legislative sources.
3. Apply the three-layer chunking strategy from `competitions/instructions/chunking_strategy.md`: Layer 1 generators not data, Layer 2 per-commit file budgets covering 7 to 12 files per commit, Layer 3 within-file caps at 1,000 records JSONL, 1,000 rows CSV, 500 lines Markdown, 80 columns by 60 lines ASCII.
4. Replace any SVG diagrams with ASCII (`.txt`) or Mermaid (in `.md`) when the data exceeds 100,000 points or 100 KB.
5. Author the output tree under `demo-projects/01-humanoid-site-operations-director-output/` (Clinical-AI-Demos) without writing to the companion repository.
6. Run the CI compliance checklist before each commit: `ruff check .`, `ruff format --check .`, `yamllint -d relaxed .github/`.
7. Commit and push to a branch named `claude/demo-01-site-director-shortid` with seven sequential commits in a single PR.

## Future Output Tree

```
demo-projects/01-humanoid-site-operations-director-output/
  README.md                          # Site director overview with v0.1.0 DOI badge
  config/
    site.yaml                        # PAT-SITE-001 facility and bay map
    atlas_humanoid.yaml              # Atlas Electric kinematic and force limits
    llm_loop.yaml                    # Claude Opus 4.7 inference budget, temperature, retry
    shift_schedule.yaml              # 08:00 to 16:00 PDT shift definition
  schemas/
    humanoid_command.schema.json     # Per-tick humanoid command record
    bay_status.schema.json           # Per-bay status record
    patient_vitals.schema.json       # Per-patient vitals record
    llm_decision.schema.json         # Per-tick LLM decision rationale
  src/
    site_state.py                    # Site state model (12 bays + 24 rooms + 8 imaging + 1 pharmacy)
    atlas_dispatcher.py              # Atlas humanoid command emission
    llm_planner.py                   # Claude Opus 4.7 1 Hz planner loop
    safety_arbiter.py                # IEC 80601-2-77 and ISO 10218 enforcement
    shift_runner.py                  # 8-hour shift orchestrator
  data/
    shift_humanoid_commands.parquet  # 287,520 ticks at 10 Hz
    shift_bay_status.parquet         # 28,800 ticks at 1 Hz across 12 bays
    shift_patient_vitals.parquet     # 28,800 ticks at 1 Hz across 10 patients
    shift_llm_decisions.jsonl        # 28,800 LLM decisions with rationale
    iterations/
      run_NNNNN.parquet              # 32 iteration outputs
      index.jsonl                    # SHA-256 manifest
      aggregate.duckdb               # 4 required tables
  results/
    shift_summary.md                 # 8-hour shift summary with KPIs
    psl_humanoid_score.json          # Atlas PSL score for the shift
    comparison.json                  # Atlas vs. Optimus vs. human director
  diagrams/
    facility_layout.txt              # 80x60 ASCII facility map
    patient_flow.txt                 # 80x60 ASCII patient flow
    humanoid_state_timeline.txt      # 80x60 ASCII state timeline
```

## Per-Commit Roadmap

| Commit | Files | Authored Content |
|--------|-------|------------------|
| 1 | 7 | Project README, architecture.md with Mermaid, pyproject.toml, docker-compose.yml, config/site.yaml, LICENSE.txt, architecture_overview.txt |
| 2 | 8 | Bay status schema, humanoid command schema, patient vitals schema, LLM decision schema, site_state.py with 12 bays, JSONL sample, CSV sample, ingest.py |
| 3 | 9 | atlas_dispatcher.py, llm_planner.py, safety_arbiter.py, kinematics.yaml, shift coordinate frame doc, robot_loop.cpp with 50 ms E-stop, sample CSVs, xyz path ASCII |
| 4 | 10 | shift_runner.py, iterations.yaml (4-dim sweep), iterate.py with ProcessPoolExecutor, runner.rs, Cargo.toml, run_NNNNN.parquet for 32 iterations, index.jsonl, aggregate.duckdb, analysis notebook with cleared outputs, run log |
| 5 | 12 | comparison_methodology.md, metrics.schema.json, human_director_baseline.csv (30 rows from 6 published trial site case studies), atlas_outcomes.parquet, compute.py, compare_agent.py (Anthropic API and Ollama backends), comparison_prompt.md frozen at v0.1.0, comparison.json, comparison_report.md, comparison_report.pdf, plotly dashboard, summary PNG |
| 6 | 7-check error scan | ruff format, ruff check, yamllint, schema cross-validate, path cross-reference for leftover SVG, generator determinism via SHA-256, markdown lint |
| 7 | 3 | Parent README update, releases.md entry, CHANGELOG.md v0.2.0 block |

## CI Compliance

The future session must keep `lint-and-format` green on Python 3.10, 3.11, and 3.12. Required pre-commit commands:

```bash
ruff check .
ruff format --check .
yamllint -d relaxed .github/
```

Add a per-file-ignores entry to `ruff.toml` for `demo-projects/01-humanoid-site-operations-director-output/**/*.py` covering `F401`, `F402`, `F821` to match the existing patterns for `patient-journey/`, `regulatory/`, and `unification/` in the companion repository.

## Comparison Framework

The future session must rank the Atlas-led shift against three baselines:

1. **Prior demo versions of this project** (snapshot at `demo-projects/01-humanoid-site-operations-director-output/releases/v0.2.0/`).
2. **Competitor humanoids**: Tesla Optimus Gen 3, Figure 03, Agility Digit V5, Apptronik Apollo, manual human operations director.
3. **Hybrid teams**: Atlas + human director with non-zero `human_intervention_seconds` field.

Use the five comparison dimensions from `competitions/instructions/competition_protocol.md` with v0.1.0-frozen weights (Quality 0.40, Time 0.25, Cost 0.20, Safety 0.10, Patient Experience 0.05) and the Gaussian N(mu, sigma squared) skill rating with mu_0 = 600 and sigma_0 = 200 inherited from the Orbit Wars Kaggle competition pattern.

## Notes

- All Markdown files in the output must use single dashes only, no em dashes, no double dashes, no triple dashes outside valid Markdown table separators.
- Black text only throughout. No color overrides.
- ASCII diagrams cap at 80 columns by 60 lines.
- The downstream simulation must not produce or read PHI. All patient identifiers are synthetic (PAT-SITE-001-P01 through PAT-SITE-001-P10).
- The Atlas humanoid kinematic limits and the Claude Opus 4.7 inference budget are inputs to the simulation, not outputs. Do not modify them in derived work.
