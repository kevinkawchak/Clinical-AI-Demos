# Demo Prompt 10: Humanoid Decentralized Home Care for DCT

[![Demo](https://img.shields.io/badge/Demo-10%20of%2010-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![Companion](https://img.shields.io/badge/Companion-physical--ai--oncology--trials-purple.svg)](https://github.com/kevinkawchak/physical-ai-oncology-trials)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18445179-blue)](https://doi.org/10.5281/zenodo.18445179)
[![Resolution](https://img.shields.io/badge/Resolution-1s%20visit%20%2B%2010s%20ambient-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![Humanoid](https://img.shields.io/badge/Humanoid-Figure%2003%20Field%20Edition-orange.svg)](https://www.figure.ai)
[![LLM](https://img.shields.io/badge/LLM-Claude%20Haiku%204.5%20Edge-blueviolet.svg)](https://www.anthropic.com)
[![Python](https://img.shields.io/badge/Python-3.10%20|%203.11%20|%203.12-blue.svg)](https://www.python.org/)

Released on 16 May 2026
CEO Kevin Kawchak, ChemicalQDevice

## Perspective

A Figure 03 humanoid in a Field Edition lightweight configuration (28 kg, weather-rated jacket, foldable for van transport) is delivered to the home of a Stage IV metastatic castration-resistant prostate cancer (mCRPC) patient (PAT-DCT-0001, 72 male, enrolled in a decentralized clinical trial of an oral PARP inhibitor + radioligand therapy combination). The humanoid performs a 4-hour active home visit (administers the per-cycle oral medication observed dosing, performs the per-cycle vitals check, draws a venous blood sample for PSA and CBC, ships the sample via overnight cold-chain courier, conducts the patient-reported outcome (PRO) survey by voice), then transitions to 20-hour ambient monitoring mode (idle in the corner of the living room, monitoring patient gait, sleep, and adherence to oral medication with vision-based pill-detection at 1 frame per 10 seconds). The Figure 03 runs an edge-deployed Claude Haiku 4.5 model (no cloud, no on-prem server, all inference happens on the humanoid's onboard NVIDIA Orin compute) with PHI never leaving the home. A sponsor-side Claude Opus 4.7 1M instance receives only de-identified summary reports through a federated learning aggregator.

## Thesis

Decentralized clinical trials (DCT) for oncology are bottlenecked by two competing requirements: continuous patient monitoring (which favors centralized sites) and patient-centric flexibility (which favors home visits). A Figure 03 Field Edition humanoid plus an edge-deployed Claude Haiku 4.5 resolves the tension: the humanoid provides continuous monitoring at home, the on-device LLM ensures PHI never leaves the home, and the federated learning aggregator delivers de-identified trial-level analytics to the sponsor. The 24-hour cycle (4-hour active + 20-hour ambient) demonstrates that one humanoid per enrolled DCT patient is operationally feasible at sponsor cost levels comparable to a weekly in-person trial site visit.

## Scope

- One simulated patient: PAT-DCT-0001 (72 male, Stage IV mCRPC, ECOG 2, BMI 28, living alone in a 90 m^2 single-floor home in rural Iowa, enrolled in DCT of olaparib + Lu-177 PSMA-617).
- One simulated humanoid: Figure 03 Field Edition (32 DOF, 1.68 m height, 28 kg, 4 kg payload per arm, IP65-rated, foldable for van transport, NVIDIA Orin onboard compute, 18 hour battery with overnight charging dock).
- One simulated LLM: Claude Haiku 4.5 edge (runs locally on NVIDIA Orin, no cloud, no PHI egress; 50 ms median latency on Orin AGX 64GB).
- One cycle duration: 24 hours (86,400 s); 4 hours active visit at 1 Hz LLM cadence (14,400 ticks), 20 hours ambient monitoring at 0.1 Hz LLM cadence (7,200 ticks).
- Per-cycle deliverables: 1 PSA + CBC blood sample (cold-chain shipped), 1 PRO survey result, 1 oral medication observed dose, 1 vitals snapshot (BP, pulse oximetry, weight, temperature).
- Iteration count: 16 deterministic iterations covering seed, edge LLM temperature, humanoid gait noise sigma, ambient activity classification noise, and cold-chain shipping delay distribution.

## Why a Future Pass

A 24-hour cycle produces 144,000 ticks of humanoid telemetry during the 4-hour active visit plus 72,000 ambient monitoring frames over the 20-hour ambient phase. The federated learning aggregator needs to ingest 1 de-identified summary per patient per cycle from ~50 DCT-enrolled patients; the simulation models the aggregator behavior for 1 patient over 1 cycle.

## Inputs from physical-ai-oncology-trials

| Path | Purpose |
|------|---------|
| `patients/paper/full-paper/sections/hr_9501_patient_self_selection.tex` | HR 9501 Patient Self-Selection Act |
| `patients/paper/full-paper/sections/hr_9502_robot_humanoid_choice.tex` | HR 9502 Humanoid Choice Act |
| `patients/paper/full-paper/sections/hr_9507_data_self_custody.tex` | HR 9507 Data Self-Custody Act (key reference) |
| `patient-journey/stage_09_surveillance.py` | Stage 9 long-term surveillance (verbatim) |
| `patient-journey/stage_07_immunotherapy.py` | Stage 7 immunotherapy (for oral medication observed dosing) |
| `patient-journey/patient_state.py` | Central data model |
| `federation/README.md` | Federated learning platform |
| `federation/federated_coordinator.py` | Federated coordinator (verbatim) |
| `federation/differential_privacy.py` | Differential privacy (verbatim) |
| `federation/secure_aggregation.py` | Secure aggregation (verbatim) |
| `federation/site_enrollment.py` | Site enrollment (adapt for home enrollment) |
| `federation/data_harmonization.py` | Data harmonization |
| `federation/consortium_reporting.py` | Consortium reporting |
| `federation/privacy_analytics.py` | Privacy analytics |
| `federation/examples-federation/06_full_consortium.py` | Full consortium reference |
| `privacy/de-identification/deidentification_pipeline.py` | Safe Harbor pipeline (verbatim) |
| `privacy/phi-pii-management/phi_detector.py` | PHI detection |
| `privacy/access-control/access_control_manager.py` | Patient access control |
| `privacy/breach-response/breach_response_protocol.py` | Breach response (home-based incident) |
| `privacy/dua-templates/dua_generator.py` | DUA for home-based data |
| `unification/usl/humanoids/usl_humanoid_scoring.py` | Humanoid USL scoring |
| `regulatory/Adaption-21-CFR-Part-50/source/Physical_AI_21_CFR_Part_50_chunk/` | Informed consent chunks |
| `regulatory/Adaption-21-CFR-Part-312/source/Physical_AI_21_CFR_Part_312_chunk/` | IND chunks |
| `agentic-ai/examples-agentic-ai/03_realtime_adaptive_treatment_agent.py` | Real-time adaptive agent |
| `competitions/instructions/chunking_strategy.md` | Three-layer chunking |
| `competitions/instructions/file_format_conventions.md` | File format defaults |

## Downstream LLM Processing Instructions

The future Claude Code Opus 4.7 1M Max session must:

1. Read all 7 files under `federation/` plus `federation/examples-federation/06_full_consortium.py` end to end. The federated coordinator, differential privacy module, and secure aggregation module in those files are the authoritative source for the sponsor-side federated learning aggregator behavior.
2. Read `patient-journey/stage_09_surveillance.py` for the long-term surveillance dataclasses and state transitions.
3. Implement the edge-deployed Claude Haiku 4.5 on NVIDIA Orin pattern. The model runs entirely on the humanoid; no PHI leaves the home. The federated learning aggregator receives a single de-identified summary per cycle (PSA value, CBC summary, PRO scores, vitals, medication adherence, gait classification, sleep summary).
4. The Safe Harbor 45 CFR 164.514(b) gate from `privacy/de-identification/deidentification_pipeline.py` is applied before the per-cycle summary is sent to the federated aggregator. The aggregator never sees raw patient name, DOB, MRN, or home address.
5. HR 9507 (Data Self-Custody Act) is the binding patient right: the patient retains the right to revoke aggregator submission for any cycle, and the humanoid emits a `data_self_custody_invoked` event when invoked.
6. Apply the three-layer chunking strategy. The 4-hour active visit produces approximately 5 MB of L1/L2 Parquet; the 20-hour ambient phase produces 200 KB of L3 aggregate plus a Zenodo-archived 800 MB raw vision stream (the simulation references the stream by pointer JSON; the real raw stream is never committed and never sent to the aggregator).
7. Run pre-commit checklist on every commit.
8. Commit and push seven sequential commits in a single PR on branch `claude/demo-10-home-care-shortid`.

## Future Output Tree

```
demo-projects/10-humanoid-decentralized-home-care-output/
  README.md
  config/
    home.yaml                        # 90 m^2 home layout
    figure_field_humanoid.yaml       # Figure 03 Field Edition specs
    edge_llm.yaml                    # Claude Haiku 4.5 on Orin config
    federated_aggregator.yaml        # Sponsor-side aggregator config
    patient_profile.yaml             # PAT-DCT-0001 baseline
  schemas/
    humanoid_command.schema.json
    home_visit_event.schema.json
    ambient_monitoring_frame.schema.json
    medication_adherence.schema.json
    blood_sample_handoff.schema.json
    pro_survey_response.schema.json
    federated_summary.schema.json
    data_self_custody.schema.json
    llm_decision.schema.json
  src/
    home_state.py
    figure_dispatcher.py
    edge_llm_planner.py              # Claude Haiku 4.5 on Orin
    phi_redactor.py                  # Safe Harbor before aggregator submission
    cold_chain_courier.py            # FedEx/UPS overnight cold-chain
    pill_detector.py                 # Vision-based pill detection
    gait_classifier.py
    sleep_classifier.py
    federated_submitter.py           # Submits de-identified summary to aggregator
    cycle_runner.py
  data/
    cycle_humanoid_commands.parquet  # 144,000 + 7,200 ticks
    cycle_llm_decisions.jsonl
    cycle_home_visit_events.jsonl
    cycle_ambient_frames.parquet     # 72,000 ambient frames at 0.1 Hz
    cycle_medication_adherence.jsonl
    cycle_blood_handoffs.jsonl
    cycle_pro_surveys.jsonl
    cycle_federated_summary.json     # 1 summary per cycle, de-identified
    iterations/
      run_NNNNN.parquet              # 16 iterations
      index.jsonl
      aggregate.duckdb
  diagrams/
    home_layout.txt                  # 80x60 ASCII home floor plan
    cycle_timeline.txt               # 24-hour timeline (active + ambient)
    federated_data_flow.txt          # PHI gating diagram
    medication_observed_dosing.txt
```

## Per-Commit Roadmap

| Commit | Files | Authored Content |
|--------|-------|------------------|
| 1 | 7 | README, architecture.md with home + federated Mermaid, pyproject.toml, docker-compose.yml (orin-edge, aggregator-proxy, simulator, db services), config/home.yaml, LICENSE.txt, home_layout.txt |
| 2 | 11 | 9 schemas + JSONL sample + ingest.py with HR 9507 self-custody validation |
| 3 | 12 | figure_dispatcher.py, edge_llm_planner.py for Claude Haiku 4.5 on Orin, phi_redactor.py, cold_chain_courier.py, pill_detector.py, gait_classifier.py, sleep_classifier.py, federated_submitter.py, kinematics.yaml for Figure 03 Field Edition, robot_loop.cpp with 100 ms E-stop (home-grade), sample CSVs, home flow ASCII |
| 4 | 11 | cycle_runner.py, iterations.yaml (5-dim sweep), iterate.py, runner.rs, Cargo.toml, per-iteration Parquet, index.jsonl, aggregate.duckdb with 8 tables, notebook, run log, Zenodo pointer for L0 raw ambient stream |
| 5 | 13 | comparison_methodology.md, metrics.schema.json with 24 keys (adds patient-self-custody-invocations, cold-chain-time-h, medication-observed-rate, ambient-detection-precision, PHI-egress-count), home_health_baseline.csv (30 rows from 6 published DCT case studies), figure_outcomes.parquet, compute.py, compare_agent.py, prompt frozen, comparison.json, report.md/.pdf, dashboard.html, summary.png, per-cycle adherence chart |
| 6 | 7-check error scan |
| 7 | 3 | Parent README, releases.md entry, CHANGELOG.md v1.1.0 block |

## CI Compliance

Add per-file-ignores to `ruff.toml`:

```toml
"demo-projects/10-humanoid-decentralized-home-care-output/**/*.py" = ["F401", "F402", "F821"]
```

Required pre-commit: `ruff check`, `ruff format --check`, `yamllint -d relaxed .github/`.

## Comparison Framework

Three categories:
1. Prior versions (snapshot at `releases/v1.0.0/`).
2. Competitor configurations: human home health nurse (1 visit per week), Optimus Gen 3 (heavier, less portable), Apollo (no edge LLM), Digit V5 (less dexterous for pill dispensing).
3. Hybrid: Figure 03 Field + weekly human home health nurse visit (non-zero `human_intervention_seconds`).

Weights: Patient Adherence 0.25, Patient Privacy (PHI Egress) 0.20, Time 0.10, Cost 0.15, Safety 0.10, Patient Experience 0.10, Federated Aggregator Latency 0.10.

## Notes

- Edge LLM: Claude Haiku 4.5 runs on NVIDIA Orin AGX 64GB onboard the Figure 03. No PHI ever leaves the home. The federated learning aggregator receives only de-identified summary statistics.
- HR 9507 patient self-custody: the patient may revoke aggregator submission for any cycle. The humanoid logs the revocation and continues normal in-home care without aggregator submission.
- Cold-chain courier: blood sample is shipped via FedEx Priority Overnight in a 2 degree C to 8 degree C insulated container with embedded temperature logger; humanoid hands the package to the FedEx driver at the front door.
- Observed dosing: humanoid watches the patient swallow the olaparib tablet via onboard vision at 30 fps, then prompts the patient to open their mouth for 2-second verification. Score: 0 (not observed), 0.5 (observed but not verified), 1.0 (observed and verified).
- Ambient gait monitoring: vision-based 2D pose estimation at 0.1 Hz, captured every 10 seconds; flags falls, prolonged immobility (over 4 hours during waking hours), and gait asymmetry trends.
- E-stop latency: 100 ms (home-grade, non-surgical).
- Cumulative cross-arm force limit: 12 N during medication observed dosing handoff to patient hand (the humanoid hands the tablet to the patient, not the reverse).
- Single dashes only. Black text only. ASCII diagrams cap at 80 by 60.
