# Demo Prompt 03: Humanoid Pharmacy and IMP Compounding

[![Demo](https://img.shields.io/badge/Demo-03%20of%2010-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![Companion](https://img.shields.io/badge/Companion-physical--ai--oncology--trials-purple.svg)](https://github.com/kevinkawchak/physical-ai-oncology-trials)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18445179-blue)](https://doi.org/10.5281/zenodo.18445179)
[![Resolution](https://img.shields.io/badge/Resolution-100ms-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![Humanoid](https://img.shields.io/badge/Humanoid-Figure%2003-orange.svg)](https://www.figure.ai)
[![LLM](https://img.shields.io/badge/LLM-GPT--5.5%20Thinking%20on--prem-blueviolet.svg)](https://openai.com)
[![Python](https://img.shields.io/badge/Python-3.10%20|%203.11%20|%203.12-blue.svg)](https://www.python.org/)

Released on 16 May 2026
CEO Kevin Kawchak, ChemicalQDevice

## Perspective

A Figure 03 humanoid stands inside an ISO Class 5 clean room compounding CAR-T cell therapy for a single Stage IV diffuse large B-cell lymphoma patient (PAT-IMP-0001, 47 male, autologous CD19 CAR-T product). The compounding session lasts 4 hours (14,400 seconds) at 100 ms resolution (144,000 ticks) and follows USP 800 hazardous drug handling, USP 797 sterile compounding, and 21 CFR Part 211 cGMP. A locally-hosted GPT-5.5 Thinking model (on-prem on a workstation outside the clean room, talking to the humanoid over an air-gapped optical link) plans every pipette stroke, every centrifuge timing, and every cryopreservation step. The Figure 03 humanoid never touches the keyboard or the laptop. The pharmacist supervises from a viewing window through a Class II Type A2 biological safety cabinet glove port that the humanoid does not use.

## Thesis

Compounding investigational medicinal products (IMPs) by humanoid plus on-prem LLM eliminates the three highest-error human compounding failure modes documented in FDA 2024 inspection reports: ergonomic fatigue at hour 3, wrong-vial selection under time pressure, and missed cross-contamination cleanups. The Figure 03 hand precision (1 mm RMS, 5 N grip force, 24-finger-joint articulation) handles 0.5 mL serological pipettes, T-flask shaking patterns at 70 RPM, and OneSpinner cryo-controlled rate freezing handoffs without operator drift. The on-prem GPT-5.5 plans each 100 ms tick and emits a justification string that downstream regulators can audit. The simulation produces an unmodifiable hash-chained log per USP 800 and USP 797.

## Scope

- One simulated patient IMP order: PAT-IMP-0001 (CAR-T autologous, 2 x 10^7 cells per kg, 80 kg patient, total 1.6 x 10^9 cells, 50 mL final volume).
- One simulated humanoid: Figure 03 (32 DOF, 1.68 m height, 60 kg, 4 kg payload per arm, 24-finger-joint hand with 1 mm RMS, IP67-rated, EM-shielded for clean room electronics).
- One simulated LLM: GPT-5.5 Thinking on-prem (Ollama-style local inference, 100 ms median round-trip per planning tick).
- One compounding session duration: 4 hours (14,400 s, 144,000 ticks at 100 ms LLM cadence, 1,440,000 ticks at 10 Hz humanoid motion cadence).
- ISO Class 5 clean room with HEPA filtration at 0.3 micron 99.97 percent efficiency, 20-air-changes-per-hour, positive pressure of 12 Pa relative to ISO Class 7 ante-room.
- Iteration count: 16 deterministic iterations covering seed, LLM temperature, humanoid hand gripper noise sigma, and cryopreservation ramp rate variance.

## Why a Future Pass

A 4-hour compounding session at 10 Hz humanoid telemetry produces 1,440,000 ticks per humanoid plus 144,000 LLM decisions. The chain-of-custody log alone runs 50K records. Authoring inline is infeasible; the future session writes generators plus stratified human-review samples.

## Inputs from physical-ai-oncology-trials

| Path | Purpose |
|------|---------|
| `regulatory/Adaption-21-CFR-Part-312/source/Physical_AI_21_CFR_Part_312.tex` | 21 CFR Part 312 IND application adaptation (94 pages) |
| `regulatory/Adaption-21-CFR-Part-312/source/Physical_AI_21_CFR_Part_312_chunk/` | Chunked into 5 files for downstream LLM ingestion |
| `regulatory/Adaption-21-CFR-Part-50/source/Physical_AI_21_CFR_Part_50.tex` | 21 CFR Part 50 informed consent adaptation (37 pages) |
| `regulatory/adaption-ich-e6r3/source/main.tex` | ICH E6(R3) Physical AI Unification Guidance |
| `regulatory/adaption-ich-e6r3/source/main_chunk/` | Chunked into 4 files for downstream LLM ingestion |
| `regulatory/fda-compliance/fda_submission_tracker.py` | FDA submission tracking (cGMP scope inputs) |
| `regulatory-submit/iec62304_generator.py` | IEC 62304 software lifecycle documentation |
| `regulatory-submit/clinical_evidence.py` | Clinical evidence report generator |
| `regulatory-submit/audit_trail.py` | 21 CFR Part 11 audit trails |
| `privacy/phi-pii-management/phi_detector.py` | PHI detection (patient IMP order ingestion) |
| `privacy/access-control/access_control_manager.py` | Role-based access for compounding session |
| `unification/usl/humanoids/usl_humanoid_scoring.py` | Humanoid USL scoring framework |
| `examples-new/06_robotic_sample_handling.py` | Sample handling reference patterns |
| `digital-twins/clinical-integration/clinical_dt_interface.py` | FHIR/DICOM integration |
| `competitions/instructions/chunking_strategy.md` | Three-layer chunking (verbatim) |
| `competitions/instructions/file_format_conventions.md` | Repository-wide file formats |
| `competitions/instructions/ascii_diagram_guide.md` | ASCII drawing rules |
| `competitions/instructions/ci_compliance_checklist.md` | Pre-commit ruff and yamllint checklist |

## Downstream LLM Processing Instructions

The future Claude Code Opus 4.7 1M Max session must:

1. Read the 5 chunks under `regulatory/Adaption-21-CFR-Part-312/source/Physical_AI_21_CFR_Part_312_chunk/` plus the chunk README to assemble the IND-relevant compounding requirements. Do not re-chunk in this demo.
2. Read the 4 chunks under `regulatory/adaption-ich-e6r3/source/main_chunk/` for IMP custody and chain-of-custody requirements.
3. Pre-load USP 800 and USP 797 references from the public USP convention website (NOT included in physical-ai-oncology-trials) and write a `references/usp_extract.md` file inside the output tree.
4. Apply the three-layer chunking strategy from `competitions/instructions/chunking_strategy.md` and the file format defaults from `competitions/instructions/file_format_conventions.md`.
5. Replace any high-density SVG (e.g., 144,000-tick LLM plan series) with ASCII or Mermaid blocks.
6. Run pre-commit checklist before each commit.
7. Commit and push seven sequential commits in a single PR on branch `claude/demo-03-pharmacy-compounding-shortid`.

## Future Output Tree

```
demo-projects/03-humanoid-pharmacy-imp-compounding-output/
  README.md
  config/
    clean_room.yaml                  # ISO Class 5 clean room spec
    figure_humanoid.yaml             # Figure 03 specs
    llm_loop.yaml                    # GPT-5.5 Thinking on-prem config
    imp_order.yaml                   # PAT-IMP-0001 CAR-T order
  schemas/
    humanoid_command.schema.json     # Per-tick humanoid command
    pipette_stroke.schema.json       # Per-pipette-stroke record
    centrifuge_run.schema.json
    chain_of_custody.schema.json     # USP 800 chain-of-custody record
    llm_decision.schema.json
    deviation_log.schema.json        # USP 797 deviation log
  src/
    clean_room_state.py
    figure_dispatcher.py
    llm_planner.py
    usp800_enforcer.py
    usp797_enforcer.py
    cgmp_enforcer.py
    session_runner.py
  data/
    session_humanoid_commands.parquet # 1,440,000 ticks at 10 Hz
    session_llm_decisions.jsonl       # 144,000 LLM decisions
    session_chain_of_custody.parquet  # 50K records
    session_deviations.jsonl
    iterations/
      run_NNNNN.parquet               # 16 iterations
      index.jsonl
      aggregate.duckdb
  references/
    usp_extract.md                    # Authored from public USP 800 + USP 797
  diagrams/
    clean_room_layout.txt             # 80x60 ASCII
    pipette_path.txt
    humanoid_state_timeline.txt
```

## Per-Commit Roadmap

| Commit | Files | Authored Content |
|--------|-------|------------------|
| 1 | 7 | README, architecture.md with clean room Mermaid, pyproject.toml, docker-compose.yml (llm, ingest, simulator, db services), config/clean_room.yaml, LICENSE.txt, clean_room_layout.txt |
| 2 | 9 | 6 schemas + 2 sample JSONL files + ingest.py with chain-of-custody validation |
| 3 | 10 | figure_dispatcher.py, llm_planner.py, usp800_enforcer.py, usp797_enforcer.py, kinematics.yaml, robot_loop.cpp with 5 ms E-stop for compounding-grade safety, sensor_to_xyz.py with hand finger detail, sample CSVs, pipette path ASCII, Cargo.toml |
| 4 | 10 | session_runner.py, iterations.yaml (4-dim sweep), iterate.py, runner.rs, per-iteration Parquet, index.jsonl, aggregate.duckdb with 4 tables, notebook, run log |
| 5 | 12 | comparison_methodology.md, metrics.schema.json, human_compounder_baseline.csv (30 rows from 6 published cGMP CAR-T centers), figure_outcomes.parquet, compute.py, compare_agent.py, prompt frozen, comparison.json, report.md/.pdf, dashboard.html, summary.png |
| 6 | 7-check error scan |
| 7 | 3 | Parent README, releases.md entry, CHANGELOG.md v0.4.0 block |

## CI Compliance

Add per-file-ignores to `ruff.toml`:

```toml
"demo-projects/03-humanoid-pharmacy-imp-compounding-output/**/*.py" = ["F401", "F402", "F821"]
```

Required pre-commit: `ruff check`, `ruff format --check`, `yamllint -d relaxed .github/`. ASCII diagrams cap at 80 cols by 60 lines.

## Comparison Framework

Three categories:
1. Prior versions (snapshot at `releases/v0.3.0/`).
2. Competitor humanoid configurations: Sanctuary Phoenix Gen 8 (clean-room-rated), Apptronik Apollo (clean-room-rated), human pharmacist with manual compounding.
3. Hybrid: Figure 03 + human pharmacist override.

Weights: Sterility 0.30, Accuracy 0.30, Time 0.15, Cost 0.10, Safety 0.10, Patient Experience 0.05. The "Sterility" dimension is unique to this demo and weights particulate-count audit results from a Lighthouse Worldwide Solutions HandiLaz Mini II under the BSC.

## Notes

- Cumulative cross-hand tip-force limit: 8 N (CAR-T cells are sensitive to shear above 0.1 Pa shear stress; the humanoid grip force budget reflects this).
- E-stop latency: 5 ms (compounding-grade, matches the v3.9.1 surgical pattern for critical lab procedures).
- Pipette tip ejection at 10 mm above waste container to prevent aerosolization.
- T-flask shaking pattern at 70 RPM with 25 mm orbital diameter; the humanoid wrist replicates this without an external shaker.
- Cryopreservation ramp rate: 1 degree C per minute from 4 to -80 degree C using OneSpinner controlled-rate freezer; humanoid handoff timing within 1 second tolerance.
- Single dashes only. Black text only. No em dashes, no double dashes.
