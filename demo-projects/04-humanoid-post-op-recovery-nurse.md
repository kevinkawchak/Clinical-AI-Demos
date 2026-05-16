# Demo Prompt 04: Humanoid Post-Operative Recovery Nurse

[![Demo](https://img.shields.io/badge/Demo-04%20of%2010-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![Companion](https://img.shields.io/badge/Companion-physical--ai--oncology--trials-purple.svg)](https://github.com/kevinkawchak/physical-ai-oncology-trials)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18445179-blue)](https://doi.org/10.5281/zenodo.18445179)
[![Resolution](https://img.shields.io/badge/Resolution-1s-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![Humanoid](https://img.shields.io/badge/Humanoid-Agility%20Digit%20V5-orange.svg)](https://agilityrobotics.com)
[![LLM](https://img.shields.io/badge/LLM-Claude%20%2B%20Ollama%20Llama%204-blueviolet.svg)](https://www.anthropic.com)
[![Python](https://img.shields.io/badge/Python-3.10%20|%203.11%20|%203.12-blue.svg)](https://www.python.org/)

Released on 16 May 2026
CEO Kevin Kawchak, ChemicalQDevice

## Perspective

An Agility Digit V5 humanoid serves as the primary night-shift post-operative recovery nurse for a single Stage IIIB NSCLC patient (PAT-REC-0001, 58 female) following robot-assisted thoracoscopic lobectomy. The recovery monitoring window is 24 hours (08:00 to 08:00 next day) at 1 second resolution. The Digit V5 humanoid stays within 2 m of the patient at all times, observes pulse oximetry and respiratory rate via non-contact sensors, refills IV bags, repositions the patient every 2 hours per pressure-injury prevention protocol, summons the on-call human RN when any rule-based threshold trips, and reads the patient bedtime stories or answers questions via natural-language voice synthesis when the patient is awake. An on-prem Anthropic Claude (Haiku 4.5 default for latency, Sonnet 4.6 escalation for complex reasoning) plus an Ollama-hosted Llama 4 70B (PHI-handling local backup) drive the planning loop.

## Thesis

A dedicated humanoid bedside nurse for one post-operative oncology patient eliminates the leading causes of preventable post-op morbidity: late detection of hypoxia, missed reposition windows, IV bag dry-runs, and patient anxiety unattended. The Digit V5 platform is the right choice because its bipedal lower body provides 1.8 m height to read vitals from any bed angle and its 9 kg payload arm can lift a 500 mL saline bag from the IV pole hook without disturbing the patient. The on-prem LLM never sends PHI to the cloud; the Llama 4 70B Ollama backup handles all PHI-bearing inference.

## Scope

- One simulated patient: PAT-REC-0001 (58 female, Stage IIIB NSCLC, day 0 post-op robot-assisted thoracoscopic lobectomy, ECOG 1 baseline, BMI 27).
- One simulated humanoid: Agility Digit V5 (16 DOF, 1.8 m height, 80 kg, 9 kg payload per arm, IP54-rated for hospital wet areas, 12 hour battery with hot-swap).
- One simulated LLM stack: Claude Haiku 4.5 default (50 ms median latency for routine ticks), Claude Sonnet 4.6 escalation (500 ms for complex reasoning), Ollama Llama 4 70B local (PHI-bearing inference only).
- One monitoring window duration: 24 hours (86,400 s, 86,400 ticks at 1 Hz LLM cadence, 864,000 ticks at 10 Hz humanoid motion cadence).
- Recovery room: single-bed PACU-step-down unit, 32 m^2, with bed, IV pole, pulse oximeter, ECG, respiratory rate monitor, urinary catheter, NG tube, chest tube.
- Iteration count: 16 deterministic iterations covering seed, LLM temperature, humanoid task-priority weights, and patient acuity variance.

## Why a Future Pass

A 24-hour bedside monitoring session produces 864,000 humanoid telemetry ticks plus 86,400 LLM decisions plus a continuous patient vitals stream. The downstream session writes generators and stratified samples.

## Inputs from physical-ai-oncology-trials

| Path | Purpose |
|------|---------|
| `patient-journey/patient_state.py` | Central data model (10 enums, 14 dataclasses) |
| `patient-journey/stage_06_recovery.py` | Stage 6 post-operative recovery (verbatim algorithmic source) |
| `patient-journey/stage_05_surgery.py` | Stage 5 surgery (provides immediate post-op handoff state) |
| `patient-journey/master_journey.py` | Master orchestrator with stage transitions |
| `patient-journey/deliverables/charts/` | Recovery charts (visualization patterns) |
| `patient-journey/deliverables/tables/` | Recovery tables (data presentation patterns) |
| `patient-journey/diagrams/stage_06/` | Stage 6 ASCII progress diagrams (3 perspectives) |
| `examples-new/01_realtime_safety_monitoring.py` | Real-time safety monitoring patterns |
| `examples-new/02_sensor_fusion_intraoperative.py` | Sensor fusion (adapt for non-invasive vitals fusion) |
| `unification/usl/humanoids/agility_digit/` | Digit USL scoring data |
| `regulatory/ich-gcp/gcp_compliance_checker.py` | Good Clinical Practice |
| `regulatory/Adaption-21-CFR-Part-50/source/Physical_AI_21_CFR_Part_50_chunk/` | Informed consent chunks (verbatim) |
| `privacy/phi-pii-management/phi_detector.py` | PHI detection at LLM boundary |
| `privacy/access-control/access_control_manager.py` | RN access to humanoid override |
| `competitions/instructions/chunking_strategy.md` | Three-layer chunking |
| `competitions/instructions/ascii_diagram_guide.md` | ASCII diagram templates |
| `competitions/instructions/file_format_conventions.md` | File format defaults |

## Downstream LLM Processing Instructions

The future Claude Code Opus 4.7 1M Max session must:

1. Read `patient-journey/stage_06_recovery.py` end to end. The dataclasses, enums, and state transitions in that file are the authoritative source for what counts as a recovery tick. Do not re-derive.
2. Read `patient-journey/patient_state.py` to inherit the central data model. Add five new dataclasses specific to the humanoid bedside role: `HumanoidPosition`, `HumanoidArmAction`, `BedsideTaskPriority`, `LLMBackendRoute`, `PatientPreference`.
3. Apply the three-layer chunking strategy. Per-second vitals at 1 Hz over 24 hours produces 86,400 records per channel; keep this as Parquet, not Markdown.
4. The Llama 4 70B Ollama path is invoked when any prompt would contain PHI fields (patient name, date of birth, MRN). The Claude path is invoked for all non-PHI inference. Document this routing in `phi_redactor.py`.
5. Use the 5-stage diagrams under `patient-journey/diagrams/stage_06/` as exact ASCII templates. The future session must produce 24 hourly snapshot diagrams plus 3 cumulative diagrams (60 ASCII diagrams total).
6. Run pre-commit checklist on every commit.
7. Commit and push seven sequential commits in a single PR on branch `claude/demo-04-recovery-nurse-shortid`.

## Future Output Tree

```
demo-projects/04-humanoid-post-op-recovery-nurse-output/
  README.md
  config/
    recovery_room.yaml               # 32 m^2 room layout
    digit_humanoid.yaml              # Digit V5 specs
    llm_routing.yaml                 # Haiku/Sonnet/Llama 4 routing rules
    patient_profile.yaml             # PAT-REC-0001 baseline
  schemas/
    humanoid_command.schema.json
    bedside_task.schema.json
    patient_vitals.schema.json
    llm_decision.schema.json
    reposition_event.schema.json
    iv_refill_event.schema.json
    rn_escalation.schema.json
  src/
    recovery_state.py
    digit_dispatcher.py
    llm_router.py                    # Haiku/Sonnet/Llama 4 routing
    phi_redactor.py
    reposition_planner.py            # 2-hour pressure-injury prevention
    voice_synthesis.py               # Bedtime story / patient conversation
    night_shift_runner.py
  data/
    shift_humanoid_commands.parquet  # 864,000 ticks
    shift_patient_vitals.parquet     # 86,400 ticks across 8 channels
    shift_llm_decisions.jsonl        # 86,400 decisions
    shift_repositions.jsonl
    shift_iv_refills.jsonl
    shift_rn_escalations.jsonl
    iterations/
      run_NNNNN.parquet              # 16 iterations
      index.jsonl
      aggregate.duckdb
  diagrams/
    recovery_room_layout.txt         # 80x60 ASCII
    24_hour_state_timeline.txt
    patient_vitals_24h.txt
    hour_00.txt through hour_23.txt  # 24 hourly snapshots
    cumulative_position_trace.txt    # Digit trajectory aggregate
    cumulative_intervention.txt
    cumulative_voice.txt
```

## Per-Commit Roadmap

| Commit | Files | Authored Content |
|--------|-------|------------------|
| 1 | 7 | README, architecture.md with Mermaid topology, pyproject.toml, docker-compose.yml (haiku, sonnet, ollama, ingest, simulator services), config/recovery_room.yaml, LICENSE.txt, recovery_room_layout.txt |
| 2 | 9 | 7 schemas + 2 sample JSONL + ingest.py with vitals validation |
| 3 | 10 | digit_dispatcher.py, llm_router.py with 3-backend routing, phi_redactor.py, reposition_planner.py with 2-hour cadence, voice_synthesis.py, kinematics.yaml, robot_loop.cpp with 100 ms E-stop (bedside-grade), sample CSVs, position trace ASCII, Cargo.toml |
| 4 | 10 | night_shift_runner.py, iterations.yaml (4-dim sweep), iterate.py, runner.rs, per-iteration Parquet, index.jsonl, aggregate.duckdb with 4 tables, notebook, run log |
| 5 | 12 | comparison_methodology.md, metrics.schema.json, human_rn_baseline.csv (30 rows from 6 published PACU studies), digit_outcomes.parquet, compute.py, compare_agent.py, prompt frozen, comparison.json, report.md/.pdf, dashboard.html, summary.png |
| 6 | 7-check error scan |
| 7 | 3 | Parent README, releases.md entry, CHANGELOG.md v0.5.0 block |

## CI Compliance

Add per-file-ignores to `ruff.toml`:

```toml
"demo-projects/04-humanoid-post-op-recovery-nurse-output/**/*.py" = ["F401", "F402", "F821"]
```

Required pre-commit checks: `ruff check`, `ruff format --check`, `yamllint -d relaxed .github/`.

## Comparison Framework

Three categories:
1. Prior versions (snapshot at `releases/v0.4.0/`).
2. Competitor humanoid configurations: Tesla Optimus Gen 3 (smaller payload), 1X Neo Beta (smaller), human RN.
3. Hybrid: Digit V5 + human RN with non-zero `human_intervention_seconds`.

Weights: Patient Safety 0.35, Patient Experience 0.25, Response Latency 0.15, Cost 0.10, Sterility 0.10, Time 0.05.

## Notes

- The Digit V5 must stay within 2 m of the patient at all times during the shift. Any excursion beyond 2 m triggers an immediate return-to-bedside task with priority 1.0.
- IV bag refill: when the bag drops below 100 mL, the humanoid retrieves a fresh 500 mL bag from the wall-mounted dispenser within 60 seconds.
- Reposition every 2 hours per Braden Scale Q-shift protocol; humanoid arms lift the patient gently with two-arm contact at chest and pelvis, never pulling on the chest tube or NG tube.
- Bedside voice: the humanoid uses a Claude-generated voice with a low, warm timbre at 60 dBA average. Volume increases to 70 dBA only when the patient requests a louder volume.
- All PHI inference runs on the local Ollama Llama 4 70B. No PHI ever leaves the local network.
- Single dashes only. Black text only. No em dashes, no double dashes.
