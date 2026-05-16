# Demo Prompt 06: Humanoid Tele-Surgical Assistant

[![Demo](https://img.shields.io/badge/Demo-06%20of%2010-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![Companion](https://img.shields.io/badge/Companion-physical--ai--oncology--trials-purple.svg)](https://github.com/kevinkawchak/physical-ai-oncology-trials)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18445179-blue)](https://doi.org/10.5281/zenodo.18445179)
[![Resolution](https://img.shields.io/badge/Resolution-1ms-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![Humanoid](https://img.shields.io/badge/Humanoid-Apptronik%20Apollo-orange.svg)](https://apptronik.com)
[![LLM](https://img.shields.io/badge/LLM-Claude%20Opus%204.7%20%2B%20Operator-blueviolet.svg)](https://www.anthropic.com)
[![Python](https://img.shields.io/badge/Python-3.10%20|%203.11%20|%203.12-blue.svg)](https://www.python.org/)

Released on 16 May 2026
CEO Kevin Kawchak, ChemicalQDevice

## Perspective

An Apptronik Apollo humanoid stands at the patient-side bed of a rural critical-access oncology clinic in Big Timber, Montana (population 1,700, nearest tertiary oncology center 220 miles away) during a 90-minute robot-assisted Whipple procedure (pancreaticoduodenectomy) on a Stage IIA pancreatic adenocarcinoma patient (PAT-TELE-0001, 64 male). A board-certified pancreaticobiliary surgeon at the University of Minnesota Masonic Cancer Center teleoperates the Intuitive da Vinci SP from 1,100 miles away. The Apollo humanoid is the patient-side surgical assistant: passes laparoscopic instruments between the da Vinci docking station and the back-table tray, reloads endoscopic staplers, refills the irrigation pump, monitors fascia tension via non-contact vision, assists with manual closure if the da Vinci goes down, and is the only entity in the OR capable of converting to open emergency surgery within 5 minutes if the LLM and remote surgeon both lose connectivity. An on-prem Claude Opus 4.7 1M context model runs the Apollo planning loop with a mandatory operator-in-the-loop confirmation for any instrument exchange.

## Thesis

Tele-surgery for rural and critical-access oncology trial sites is currently blocked by the lack of a patient-side surgical assistant. Apollo plus an on-prem Claude Opus 4.7 reasoning loop fills that role: Apollo handles every physical step that the remote surgeon cannot perform via the da Vinci SP, and the on-prem LLM ensures every Apollo action is double-checked against the live surgical state. The mandatory operator-in-the-loop confirmation ensures no Apollo instrument exchange happens without explicit remote surgeon consent, recorded with hash-chained provenance for the FDA RTCT submission.

## Scope

- One simulated patient: PAT-TELE-0001 (64 male, Stage IIA pancreatic adenocarcinoma, BMI 23, ECOG 1, undergoing pancreaticoduodenectomy).
- One simulated humanoid: Apptronik Apollo (40 DOF, 1.73 m height, 73 kg, 25 kg payload per arm, 0.5 mm RMS positioning, IP54-rated, dual-camera head with 4K).
- One simulated da Vinci SP (single-port robot, 4 arms, 8 mm instruments, 1,100 miles teleoperation link via DOD-grade encrypted link with 50 ms round-trip latency).
- One simulated LLM: Claude Opus 4.7 1M context on-prem (200 ms median latency budget for planning, 1 second budget for instrument exchange confirmation roundtrip with remote surgeon).
- One procedure duration: 90 minutes (5,400 s, 5,400,000 ticks at 1 ms LLM cadence for instrument-exchange planning, 54,000,000 ticks at 10 kHz humanoid motion cadence for fine motor work).
- Iteration count: 32 deterministic iterations covering seed, LLM temperature, humanoid hand gripper noise sigma, tele-link latency jitter (10-100 ms), and IK solver tolerance.

## Why a Future Pass

A 90-minute tele-surgical session at 10 kHz humanoid motion plus 1 ms LLM planning produces 54,000,000 humanoid records plus 5,400,000 LLM decisions plus a continuous remote-surgeon telemetry stream. The data volume is comparable to the v3.9.0 glioblastoma 1-hour simulation; the future session inherits the chunking pattern.

## Inputs from physical-ai-oncology-trials

| Path | Purpose |
|------|---------|
| `competitions/instructions/glioblastoma_context.md` | Patient context pattern (verbatim format) |
| `competitions/instructions/robot_specification.md` | Robot specification pattern (verbatim format) |
| `competitions/instructions/chunking_strategy.md` | Three-layer chunking (verbatim) |
| `competitions/instructions/file_format_conventions.md` | File format defaults |
| `competitions/instructions/ascii_diagram_guide.md` | ASCII drawing rules |
| `competitions/instructions/runtime_environments.md` | Linux, Mac, Windows recipes |
| `competitions/instructions/competition_protocol.md` | Three-category competitor model |
| `competitions/instructions/ci_compliance_checklist.md` | Pre-commit checklist (verbatim) |
| `competitions/instructions/pr_workflow.md` | Seven-commit single-PR pattern (verbatim) |
| `competitions/instructions/commit_01_project_overview.md` through `commit_07_repository_updates.md` | 7-commit reference structure |
| `unification/surgical_robotics/challenges.md` | Surgical robotics challenges |
| `unification/surgical_robotics/opportunities.md` | Surgical robotics opportunities |
| `unification/usl/surgical/intuitive_davinci/` | da Vinci USL scoring data |
| `unification/usl/humanoids/usl_humanoid_scoring.py` | Humanoid USL scoring |
| `patient-journey/stage_05_surgery.py` | Stage 5 surgery (provides per-tick patient state) |
| `examples-new/03_ros2_surgical_deployment.py` | ROS 2 surgical deployment patterns |
| `examples-new/04_hand_eye_calibration_registration.py` | Hand-eye calibration |
| `examples-new/05_shared_autonomy_teleoperation.py` | Shared autonomy teleoperation (key reference) |
| `agentic-ai/examples-agentic-ai/05_safety_constrained_agent_executor.py` | Safety-constrained agent executor |
| `frameworks/nvidia-isaac/INTEGRATION.md` | Isaac Sim integration |
| `regulatory/Adaption-21-CFR-Part-50/source/Physical_AI_21_CFR_Part_50_chunk/` | Informed consent chunks |

## Downstream LLM Processing Instructions

The future Claude Code Opus 4.7 1M Max session must:

1. Read all 17 v3.9.0 instruction files under `competitions/instructions/` and apply the pattern to this tele-surgical demo. The glioblastoma 1-hour simulation is the closest analog; inherit the seven-commit pattern, the three-layer chunking strategy, the SVG-to-ASCII replacement rule, and the CI compliance checklist verbatim.
2. The Apollo humanoid command stream is sampled at 10 kHz (10x the v3.9.0 1 kHz pattern) because instrument exchanges require sub-millisecond force feedback. The LLM planning loop runs at 1 kHz with a 200 ms reasoning budget per tick.
3. The mandatory operator-in-the-loop confirmation: every instrument exchange triggers a 1 second roundtrip to the remote surgeon. If the remote surgeon does not confirm within 1 second, the LLM falls back to a conservative "hold instrument" action and queues the exchange for re-confirmation.
4. The 1,100-mile DOD-grade encrypted link has a 50 ms baseline round-trip latency with jitter up to 100 ms per iteration. The simulation samples 5 latency profiles across the 32 iterations.
5. Apply the three-layer chunking strategy. Per-iteration L1 50 ms aggregate Parquet (~500 KB), L2 1 second aggregate (~25 KB), L3 per-phase aggregate (~5 KB), events (~10 KB). Per-iteration L0 raw of approximately 32 MB archived to Zenodo (32 iter * 32 MB = 1.0 GB, free 50 GB tier).
6. Run pre-commit checklist on every commit.
7. Commit and push seven sequential commits in a single PR on branch `claude/demo-06-tele-surgery-shortid`.

## Future Output Tree

```
demo-projects/06-humanoid-tele-surgical-assistant-output/
  README.md
  config/
    or_layout.yaml                   # Big Timber OR layout
    apollo_humanoid.yaml             # Apollo specs
    davinci_sp.yaml                  # da Vinci SP specs (simulated)
    tele_link.yaml                   # 1,100-mile encrypted link specs
    llm_loop.yaml                    # Claude Opus 4.7 1M config
  schemas/
    humanoid_command.schema.json
    instrument_exchange.schema.json
    surgeon_confirmation.schema.json
    davinci_telemetry.schema.json
    llm_decision.schema.json
    tele_link_event.schema.json
    safety_zone_breach.schema.json
  src/
    or_state.py
    apollo_dispatcher.py
    llm_planner.py                   # Claude Opus 4.7 1 kHz loop
    operator_in_loop.py              # Remote surgeon confirmation
    safety_arbiter.py                # IEC 80601-2-77 + ISO 10218
    open_conversion_planner.py       # 5-minute emergency open conversion
    procedure_runner.py
  data/
    procedure_humanoid_commands.parquet # 54,000,000 ticks at 10 kHz
    procedure_llm_decisions.jsonl       # 5,400,000 decisions
    procedure_davinci_telemetry.parquet
    procedure_instrument_exchanges.jsonl
    procedure_tele_link.parquet
    iterations/
      run_NNNNN.parquet              # 32 iterations
      index.jsonl                    # SHA-256 manifest
      aggregate.duckdb               # 6 required tables
  diagrams/
    or_layout.txt                    # 80x60 ASCII
    apollo_state_timeline.txt
    instrument_exchange_flow.txt
    tele_link_latency_distribution.txt
```

## Per-Commit Roadmap

| Commit | Files | Authored Content |
|--------|-------|------------------|
| 1 | 7 | README, architecture.md with tele-surgical Mermaid topology, pyproject.toml, docker-compose.yml (llm, ingest, simulator, db, davinci-proxy services), config/or_layout.yaml, LICENSE.txt, or_layout.txt |
| 2 | 9 | 7 schemas + JSONL sample + ingest.py with surgeon-confirmation validation |
| 3 | 10 | apollo_dispatcher.py, llm_planner.py, operator_in_loop.py, safety_arbiter.py, kinematics.yaml for Apollo 40 DOF, robot_loop.cpp with 5 ms E-stop (surgical-grade), sensor_to_xyz.py, sample CSVs, instrument exchange ASCII, Cargo.toml |
| 4 | 11 | procedure_runner.py, iterations.yaml (5-dim sweep with tele-link latency), iterate.py, runner.rs, per-iteration L1 to L3 Parquet, index.jsonl with SHA-256, aggregate.duckdb with 6 tables, notebook, run log, Zenodo pointer JSON for L0 raw |
| 5 | 13 | comparison_methodology.md, metrics.schema.json with 21 keys (adds tele-link-loss-count, manual-conversion-trigger-count), surgeon_only_baseline.csv (30 rows from 6 published tele-surgical case series), apollo_outcomes.parquet, compute.py, compare_agent.py, prompt frozen, comparison.json, report.md/.pdf, dashboard.html, summary.png, per-iteration tele-link latency chart |
| 6 | 7-check error scan |
| 7 | 3 | Parent README, releases.md entry, CHANGELOG.md v0.7.0 block |

## CI Compliance

Add per-file-ignores to `ruff.toml`:

```toml
"demo-projects/06-humanoid-tele-surgical-assistant-output/**/*.py" = ["F401", "F402", "F821"]
```

Required pre-commit: `ruff check`, `ruff format --check`, `yamllint -d relaxed .github/`.

## Comparison Framework

Three categories:
1. Prior versions of this demo (snapshot at `releases/v0.6.0/`).
2. Competitor humanoid configurations: Boston Dynamics Atlas Electric, Tesla Optimus Gen 3, Figure 03, human patient-side assistant.
3. Hybrid: Apollo + human OR nurse with non-zero `human_intervention_seconds`.

Weights: Quality 0.30, Time 0.15, Cost 0.10, Safety 0.20, Patient Experience 0.05, Tele-Link Resilience 0.20.

## Notes

- E-stop latency: 5 ms (surgical-grade, matches the v3.9.0 glioblastoma pattern).
- Apollo grip force: never exceeds 5 N when handling laparoscopic instruments; force-share clamps at 4.5 N.
- Tele-link loss for more than 3 seconds triggers the open-conversion planner which reads `open_conversion_planner.py`. The Apollo humanoid is the only entity that can perform the manual open conversion; the remote surgeon cannot.
- The IRB and IND for the procedure are inherited from `regulatory/Adaption-21-CFR-Part-312/` patterns.
- The FDA Breakthrough Device Designation pathway is inherited from `regulatory-submit/classification_advisor.py` patterns.
- Single dashes only. Black text only. ASCII diagrams cap at 80 by 60.
