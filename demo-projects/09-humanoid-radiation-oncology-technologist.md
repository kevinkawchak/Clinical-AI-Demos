# Demo Prompt 09: Humanoid Radiation Oncology Technologist

[![Demo](https://img.shields.io/badge/Demo-09%20of%2010-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![Companion](https://img.shields.io/badge/Companion-physical--ai--oncology--trials-purple.svg)](https://github.com/kevinkawchak/physical-ai-oncology-trials)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18445179-blue)](https://doi.org/10.5281/zenodo.18445179)
[![Resolution](https://img.shields.io/badge/Resolution-100ms-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![Humanoid](https://img.shields.io/badge/Humanoid-Atlas%20%2B%20Optimus%20Pair-orange.svg)](https://www.bostondynamics.com/atlas)
[![LLM](https://img.shields.io/badge/LLM-GR00T%20N1.6%20%2B%20Cosmos%20Reason%202-blueviolet.svg)](https://www.nvidia.com)
[![Python](https://img.shields.io/badge/Python-3.10%20|%203.11%20|%203.12-blue.svg)](https://www.python.org/)

Released on 16 May 2026
CEO Kevin Kawchak, ChemicalQDevice

## Perspective

A pair of humanoid robots, one Boston Dynamics Atlas Electric and one Tesla Optimus Gen 3, work cooperatively as radiation oncology technologists across an 8-hour day shift treating 10 glioblastoma stereotactic radiosurgery (SRS) patients on a Varian Edge linear accelerator. The Atlas humanoid is the primary patient handler (escort from waiting room, transfer to LINAC couch, immobilization mask placement, cone-beam CT (CBCT) alignment, post-treatment escort) while the Optimus humanoid is the LINAC-side operator (couch positioning, daily morning QA, weekly TG-142 QA, EPID dosimetry verification, machine cleaning between patients). The LLM stack uses NVIDIA GR00T N1.6 humanoid foundation model plus NVIDIA Cosmos Reason 2 vision-language model running on a local NVIDIA DGX SuperPOD with a privileged Anthropic Claude Opus 4.7 1M context arbiter for final treatment-delivery authorization. The medical physicist and radiation oncologist remain in the LINAC control room for treatment plan sign-off; the humanoids perform every physical task in the treatment vault.

## Thesis

Radiation oncology technologist (RTT) work is a high-volume, high-precision task where humanoid kinematic accuracy (Atlas 0.5 mm RMS, Optimus 1 mm RMS) exceeds the human-RTT median accuracy of 2 mm reported in 2024 ASTRO surveys. The dual-humanoid pair plus the GR00T + Cosmos Reason 2 + Claude Opus 4.7 stack delivers consistent 10-patient SRS throughput while preserving the AAPM TG-100 risk-informed quality management framework. The hand-off between physical task (humanoid) and decision authority (medical physicist + radiation oncologist) is recorded with hash-chained provenance for the medical event reporting required by NRC 10 CFR 35.

## Scope

- One simulated linear accelerator: Varian Edge with HyperArc, kV CBCT, 6D couch, ExacTrac surface guidance (simulated).
- Two simulated humanoids:
  - Atlas Electric (28 DOF, 1.5 m height, 89 kg, 11 kg payload per arm, IP67-rated, patient-contact compliant skin)
  - Tesla Optimus Gen 3 (43 DOF, 1.73 m height, 57 kg, 9 kg payload per arm, IP54-rated, machine-room rated)
- One simulated LLM stack: NVIDIA GR00T N1.6 (humanoid foundation model, runs on DGX SuperPOD), NVIDIA Cosmos Reason 2 (VLM, runs on DGX SuperPOD), Claude Opus 4.7 1M (Anthropic on-prem, arbiter for treatment delivery authorization).
- One shift duration: 8 hours (28,800 s, 288,000 ticks at 100 ms LLM cadence, 2,880,000 ticks at 10 Hz humanoid motion cadence per humanoid).
- Patient cohort: 10 glioblastoma SRS patients (single-fraction 16 Gy, mask-immobilized, CBCT guided).
- Iteration count: 16 deterministic iterations covering seed, GR00T temperature, Cosmos Reason 2 vision noise, Atlas-Optimus coordination lag, and CBCT alignment tolerance.

## Why a Future Pass

A dual-humanoid 8-hour shift with 10 patients at 100 ms LLM cadence and 10 Hz humanoid motion cadence produces 5,760,000 humanoid records (across 2 humanoids) plus 288,000 LLM decisions plus 10 treatment delivery records with full 6D couch alignment telemetry.

## Inputs from physical-ai-oncology-trials

| Path | Purpose |
|------|---------|
| `digital-twins/treatment-simulation/treatment_simulator.py` | Treatment simulation reference |
| `digital-twins/examples-twins/03_adaptive_radiation_therapy_dt.py` | Adaptive radiation therapy digital twin (key reference) |
| `digital-twins/patient-modeling/tumor_twin_pipeline.py` | Tumor twin for SRS target volume |
| `digital-twins/clinical-integration/clinical_dt_interface.py` | FHIR/DICOM (DICOM-RT) integration |
| `examples/02_digital_twin_surgical_planning.py` | Twin-based planning reference |
| `examples-new/01_realtime_safety_monitoring.py` | Real-time safety monitoring |
| `examples-new/04_hand_eye_calibration_registration.py` | Hand-eye calibration |
| `unification/usl/humanoids/boston_dynamics_atlas/` | Atlas USL scoring |
| `unification/usl/humanoids/tesla_optimus/` | Optimus USL scoring |
| `unification/usl/humanoids/usl_humanoid_scoring.py` | Humanoid USL scoring |
| `unification/simulation_physics/physics_parameter_mapping.yaml` | Physics parameter mapping |
| `frameworks/nvidia-isaac/INTEGRATION.md` | Isaac Sim integration (for humanoid + LINAC simulation) |
| `agentic-ai/examples-agentic-ai/01_mcp_clinical_robotics_server.py` | MCP server pattern |
| `agentic-ai/examples-agentic-ai/05_safety_constrained_agent_executor.py` | Safety-constrained executor |
| `tools/dicom-inspector/dicom_inspector.py` | DICOM (DICOM-RT plan) inspection |
| `tools/dose-calculator/dose_calculator.py` | Dose calculation |
| `regulatory/fda-compliance/fda_submission_tracker.py` | FDA compliance (LINAC is a 510(k) device) |
| `competitions/instructions/chunking_strategy.md` | Three-layer chunking |
| `competitions/instructions/ascii_diagram_guide.md` | ASCII drawing rules |

## Downstream LLM Processing Instructions

The future Claude Code Opus 4.7 1M Max session must:

1. Read `digital-twins/examples-twins/03_adaptive_radiation_therapy_dt.py` end to end. The adaptive radiation therapy digital twin in that file is the authoritative source for SRS treatment delivery semantics. Inherit the dataclasses and state transitions.
2. Implement the dual-humanoid coordination protocol with explicit role separation: Atlas is the patient handler (never touches the LINAC), Optimus is the machine operator (never touches the patient except during emergency E-stop assist). The coordination is logged at 1 kHz.
3. The NVIDIA GR00T N1.6 + Cosmos Reason 2 stack runs on a local DGX SuperPOD. The Claude Opus 4.7 1M arbiter runs on a separate on-prem Anthropic deployment and is consulted only at three decision gates: (a) treatment delivery authorization, (b) CBCT alignment tolerance escalation, (c) emergency E-stop.
4. Inherit the DICOM-RT plan ingestion pattern from `tools/dicom-inspector/dicom_inspector.py` and the dose calculation pattern from `tools/dose-calculator/dose_calculator.py`. The simulation does not perform real Monte Carlo dose calculation; it reads pre-computed dose maps from a Zenodo-archived reference dataset.
5. Apply the three-layer chunking strategy. Per-shift L1 / L2 / L3 Parquet totals approximately 8 MB committed; L0 raw of 400 MB archived to Zenodo.
6. Run pre-commit checklist on every commit.
7. Commit and push seven sequential commits in a single PR on branch `claude/demo-09-radiation-oncology-shortid`.

## Future Output Tree

```
demo-projects/09-humanoid-radiation-oncology-technologist-output/
  README.md
  config/
    linac_vault.yaml                 # Varian Edge vault layout
    atlas_humanoid.yaml              # Atlas Electric specs (patient handler)
    optimus_humanoid.yaml            # Optimus Gen 3 specs (machine operator)
    llm_stack.yaml                   # GR00T + Cosmos + Claude arbiter config
    patient_cohort.yaml              # 10 glioblastoma SRS patients
  schemas/
    humanoid_command.schema.json
    patient_setup.schema.json
    cbct_alignment.schema.json
    treatment_delivery.schema.json
    qa_check.schema.json
    medical_event.schema.json        # NRC 10 CFR 35 medical event
    llm_decision.schema.json
    dicom_rt_record.schema.json
  src/
    vault_state.py
    atlas_dispatcher.py              # Patient handler
    optimus_dispatcher.py            # Machine operator
    dual_humanoid_coordinator.py     # Atlas-Optimus 1 kHz coordination
    groot_planner.py                 # GR00T N1.6 humanoid foundation model
    cosmos_vision.py                 # Cosmos Reason 2 VLM
    claude_arbiter.py                # Claude Opus 4.7 1M authorization
    dicom_rt_reader.py               # DICOM-RT plan ingestion
    qa_runner.py                     # TG-142 morning QA + weekly QA
    shift_runner.py
  data/
    shift_humanoid_commands.parquet  # 5.76M ticks across 2 humanoids
    shift_llm_decisions.jsonl        # 288,000 decisions
    shift_patient_setups.parquet     # 10 patient setup records
    shift_cbct_alignments.parquet
    shift_treatments.parquet         # 10 treatment delivery records
    shift_qa_checks.parquet          # Morning + weekly QA
    shift_medical_events.jsonl       # Any NRC 10 CFR 35 medical events
    iterations/
      run_NNNNN.parquet              # 16 iterations
      index.jsonl
      aggregate.duckdb
  diagrams/
    vault_layout.txt                 # 80x60 ASCII LINAC vault
    patient_flow.txt
    atlas_optimus_coordination.txt
    dose_distribution_summary.txt
```

## Per-Commit Roadmap

| Commit | Files | Authored Content |
|--------|-------|------------------|
| 1 | 7 | README, architecture.md with dual-humanoid Mermaid, pyproject.toml, docker-compose.yml (groot, cosmos, claude-proxy, ingest, simulator, db services), config/linac_vault.yaml, LICENSE.txt, vault_layout.txt |
| 2 | 10 | 8 schemas + JSONL sample + ingest.py with DICOM-RT validation |
| 3 | 12 | atlas_dispatcher.py, optimus_dispatcher.py, dual_humanoid_coordinator.py with 1 kHz coordination, groot_planner.py, cosmos_vision.py, claude_arbiter.py, dicom_rt_reader.py, qa_runner.py, kinematics.yaml for both humanoids, robot_loop.cpp with 5 ms E-stop, sample CSVs, dual-humanoid choreography ASCII |
| 4 | 11 | shift_runner.py, iterations.yaml (5-dim sweep), iterate.py, runner.rs, Cargo.toml, per-patient Parquet for 10 patients, index.jsonl, aggregate.duckdb with 8 tables, notebook, run log, Zenodo pointer for L0 raw and reference dose maps |
| 5 | 13 | comparison_methodology.md, metrics.schema.json with 23 keys (adds cbct-alignment-mm, treatment-delivery-time-s, qa-pass-rate, medical-event-rate, dose-discrepancy-percent), human_rtt_pair_baseline.csv (30 rows from 6 published RTT pair workflow studies), humanoid_outcomes.parquet, compute.py, compare_agent.py, prompt frozen, comparison.json, report.md/.pdf, dashboard.html, summary.png, dual-humanoid timing histogram |
| 6 | 7-check error scan |
| 7 | 3 | Parent README, releases.md entry, CHANGELOG.md v1.0.0 block |

## CI Compliance

Add per-file-ignores to `ruff.toml`:

```toml
"demo-projects/09-humanoid-radiation-oncology-technologist-output/**/*.py" = ["F401", "F402", "F821"]
```

Required pre-commit: `ruff check`, `ruff format --check`, `yamllint -d relaxed .github/`.

## Comparison Framework

Three categories:
1. Prior versions (snapshot at `releases/v0.9.0/`).
2. Competitor configurations:
   - Single humanoid (Atlas only, Optimus only, Figure 03 only)
   - Different dual-humanoid pairings (Atlas + Phoenix, Atlas + Figure, Optimus + Apollo)
   - Human RTT pair
3. Hybrid: dual-humanoid + human RTT supervisor with non-zero `human_intervention_seconds`.

Weights: CBCT Alignment Accuracy 0.25, Treatment Delivery Time 0.15, QA Pass Rate 0.15, Safety 0.20, Cost 0.10, Patient Experience 0.05, Inter-Humanoid Coordination 0.10.

## Notes

- Atlas-Optimus inter-humanoid distance: minimum 1.5 m at all times in the vault (LINAC arc clearance plus humanoid arm reach).
- E-stop latency: 5 ms (radiation delivery grade; AAPM TG-100 risk class 5).
- Cumulative cross-humanoid force limit: 22 N when assisting patient transfer to LINAC couch; 5 N otherwise.
- Atlas patient-contact skin compliance: max 30 N contact force during patient escort handoff.
- Optimus machine-contact: max 50 N force when actuating the 6D couch control panel.
- The medical physicist and radiation oncologist sign off the treatment plan in the LINAC control room before any humanoid action; the Claude arbiter records the sign-off hash.
- NRC 10 CFR 35 medical event reporting: any dose discrepancy over 20 percent of prescribed dose, any treatment to wrong patient or wrong site, or any unintended dose to non-target tissue triggers a medical event log entry within 24 hours.
- All 10 patients in the simulated cohort have synthetic IDs only (PAT-SRS-GBM-PNNN).
- Single dashes only. Black text only. ASCII diagrams cap at 80 by 60.
