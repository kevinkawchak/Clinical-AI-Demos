# Demo Prompt 08: Humanoid Clinical Research Coordinator

[![Demo](https://img.shields.io/badge/Demo-08%20of%2010-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![Companion](https://img.shields.io/badge/Companion-physical--ai--oncology--trials-purple.svg)](https://github.com/kevinkawchak/physical-ai-oncology-trials)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18445179-blue)](https://doi.org/10.5281/zenodo.18445179)
[![Resolution](https://img.shields.io/badge/Resolution-1s-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![Humanoid](https://img.shields.io/badge/Humanoid-1X%20Neo%20Beta-orange.svg)](https://www.1x.tech)
[![LLM](https://img.shields.io/badge/LLM-Multi--Model%20Ensemble-blueviolet.svg)](https://www.anthropic.com)
[![Python](https://img.shields.io/badge/Python-3.10%20|%203.11%20|%203.12-blue.svg)](https://www.python.org/)

Released on 16 May 2026
CEO Kevin Kawchak, ChemicalQDevice

## Perspective

A 1X Neo Beta humanoid serves as the primary clinical research coordinator (CRC) for a Stage IIIB NSCLC enrollment cohort across an 8-hour business-day shift (08:00 to 16:00 PDT). The CRC humanoid greets patients in the trial site waiting room, escorts them to the consent room, administers the IRB-approved informed consent script (in patient's chosen language: English, Spanish, Mandarin, Tagalog, Vietnamese), runs the eligibility checklist (ECOG performance status, blood work, imaging review), prepares the case report form (CRF) entries, schedules follow-up visits via the site EHR, processes the per-patient stipend payment per the trial protocol, and answers patient questions via a multi-model LLM ensemble (Claude Opus 4.7 for medical reasoning, Gemini 3 Pro for multi-language, GPT-5.5 for stipend payment guidance). The Neo Beta's soft-skin compliant body and 35 kg light frame make it well-suited for in-person patient interaction.

## Thesis

A dedicated CRC humanoid for one enrollment cohort across an 8-hour shift compresses the per-patient consent-to-enrollment timeline from the current 7-day median (per published Phase II/III NSCLC enrollment data) to the same-day median. The Neo Beta humanoid handles every physical CRC task (greeting, escorting, blood draw assistance under nurse supervision, CRF data entry, stipend dispensing) while the multi-model LLM ensemble ensures the medical reasoning, multi-language communication, and payment guidance are each handled by the model best suited for that domain. Inheriting HR 9501 (Patient Self-Selection of Physical AI Oncology Trials Act) ensures the patient retains the right to refuse humanoid CRC support and request a human CRC at any time.

## Scope

- One simulated trial: TRIAL-NSCLC-3A (Stage IIIB NSCLC, target enrollment 200, current enrollment 87/200, sponsor SPO-2026-001).
- One simulated humanoid: 1X Neo Beta (28 DOF, 1.65 m height, 35 kg, 5 kg payload per arm, soft tendon-driven joints with compliant skin, indoor-rated, 6 hour battery).
- One simulated LLM ensemble: Claude Opus 4.7 (medical reasoning), Gemini 3 Pro (multi-language), GPT-5.5 Thinking (stipend guidance), all on-prem with cloud failover gated by Safe Harbor.
- One shift duration: 8 hours (28,800 s, 28,800 ticks at 1 Hz LLM cadence, 288,000 ticks at 10 Hz humanoid motion cadence).
- Patient cohort: 12 prospective patients (8 new consults, 4 follow-up visits) covering 4 language preferences.
- Iteration count: 16 deterministic iterations covering seed, LLM ensemble routing weights, humanoid task-priority weights, and patient-language distribution.

## Why a Future Pass

A 12-patient 8-hour CRC shift produces 288,000 humanoid records, 28,800 LLM decisions, ~36 informed consent documents, ~12 CRF entries, ~12 stipend payment records, and ~24 follow-up visit schedules.

## Inputs from physical-ai-oncology-trials

| Path | Purpose |
|------|---------|
| `patient-journey/stage_01_prescreening.py` | Stage 1 pre-screening and referral intake (verbatim) |
| `patient-journey/stage_02_enrollment.py` | Stage 2 enrollment and informed consent (verbatim) |
| `patient-journey/patient_state.py` | Central data model |
| `patient-journey/master_journey.py` | Master journey orchestrator |
| `patient-journey/diagrams/stage_01/` | Pre-screening ASCII diagrams (3 perspectives) |
| `patient-journey/diagrams/stage_02/` | Enrollment ASCII diagrams (3 perspectives) |
| `patients/paper/full-paper/sections/hr_9501_patient_self_selection.tex` | HR 9501 Patient Self-Selection Act |
| `patients/paper/full-paper/sections/hr_9502_robot_humanoid_choice.tex` | HR 9502 Robot-and-Humanoid Choice Act |
| `patients/paper/full-paper/sections/hr_9503_procedural_modification.tex` | HR 9503 Procedural Modification Act |
| `patients/paper/full-paper/sections/hr_9507_data_self_custody.tex` | HR 9507 Data Self-Custody Act |
| `regulatory/Adaption-21-CFR-Part-50/source/Physical_AI_21_CFR_Part_50.tex` | 21 CFR Part 50 informed consent (verbatim) |
| `regulatory/Adaption-21-CFR-Part-50/source/Physical_AI_21_CFR_Part_50_chunk/` | Chunked into 3 files |
| `regulatory/irb-management/irb_protocol_manager.py` | IRB protocol management |
| `regulatory/ich-gcp/gcp_compliance_checker.py` | GCP compliance |
| `privacy/access-control/access_control_manager.py` | Patient role-based access |
| `privacy/dua-templates/dua_generator.py` | Data Use Agreement generation |
| `privacy/de-identification/deidentification_pipeline.py` | Safe Harbor before cloud LLM |
| `unification/usl/humanoids/` | Humanoid USL scoring (Neo Beta not listed; humanoid_scoring.py provides framework) |
| `agentic-ai/examples-agentic-ai/02_react_procedure_planner.py` | ReAct procedure planner |
| `agentic-ai/examples-agentic-ai/06_protocol_rag_compliance_agent.py` | Protocol RAG agent |
| `competitions/instructions/chunking_strategy.md` | Three-layer chunking |
| `competitions/instructions/file_format_conventions.md` | File format defaults |

## Downstream LLM Processing Instructions

The future Claude Code Opus 4.7 1M Max session must:

1. Read `patient-journey/stage_01_prescreening.py` and `patient-journey/stage_02_enrollment.py` end to end. The dataclasses, state transitions, and method signatures in these files are the authoritative source for what counts as a CRC tick.
2. Read `patients/paper/full-paper/sections/hr_9501_*` through `hr_9503_*` and `hr_9507_*` to extract the four patient rights that the CRC humanoid must respect: self-selection (HR 9501), humanoid choice (HR 9502), procedural modification (HR 9503), data self-custody (HR 9507). The CRC humanoid emits a `patient_right_invoked` event whenever a patient invokes any of these rights, and the LLM ensemble routes the appropriate response.
3. Implement the multi-model LLM ensemble routing: Claude Opus 4.7 for any medical-reasoning prompt (eligibility check, AE history, family history), Gemini 3 Pro for any prompt in a non-English target language, GPT-5.5 Thinking for any stipend-payment or per-visit cost prompt. The routing decision is logged in `llm_decision.schema.json`.
4. Apply Safe Harbor 45 CFR 164.514(b) gate from `privacy/de-identification/deidentification_pipeline.py` before any cloud LLM call (the on-prem stack handles PHI; cloud failover requires de-id).
5. Apply the three-layer chunking strategy.
6. Run pre-commit checklist on every commit.
7. Commit and push seven sequential commits in a single PR on branch `claude/demo-08-research-coordinator-shortid`.

## Future Output Tree

```
demo-projects/08-humanoid-clinical-research-coordinator-output/
  README.md
  config/
    trial_site.yaml                  # TRIAL-NSCLC-3A site config
    neo_humanoid.yaml                # Neo Beta specs
    llm_ensemble.yaml                # Claude/Gemini/GPT routing rules
    patient_languages.yaml           # English, Spanish, Mandarin, Tagalog, Vietnamese
  schemas/
    humanoid_command.schema.json
    consent_event.schema.json
    eligibility_check.schema.json
    crf_entry.schema.json
    stipend_payment.schema.json
    followup_visit.schema.json
    patient_right_invoked.schema.json
    llm_decision.schema.json
  src/
    site_state.py
    neo_dispatcher.py
    llm_ensemble_router.py           # Claude/Gemini/GPT routing
    consent_scribe.py                # IRB-approved consent script in 5 languages
    eligibility_checker.py
    crf_writer.py
    stipend_dispenser.py
    followup_scheduler.py
    shift_runner.py
  data/
    shift_humanoid_commands.parquet  # 288,000 ticks
    shift_llm_decisions.jsonl        # 28,800 decisions
    shift_consents.parquet           # ~36 consent records
    shift_eligibilities.parquet
    shift_crf_entries.parquet
    shift_stipends.parquet
    shift_followups.parquet
    shift_patient_rights.jsonl
    iterations/
      run_NNNNN.parquet              # 16 iterations
      index.jsonl
      aggregate.duckdb
  diagrams/
    site_layout.txt                  # 80x60 ASCII waiting + consent + exam rooms
    patient_flow.txt
    neo_state_timeline.txt
    consent_workflow.txt
```

## Per-Commit Roadmap

| Commit | Files | Authored Content |
|--------|-------|------------------|
| 1 | 7 | README, architecture.md with ensemble Mermaid, pyproject.toml, docker-compose.yml (claude-proxy, gemini-proxy, gpt-proxy, ingest, simulator, db services), config/trial_site.yaml, LICENSE.txt, site_layout.txt |
| 2 | 10 | 8 schemas + JSONL sample + ingest.py with consent validation |
| 3 | 11 | neo_dispatcher.py, llm_ensemble_router.py, consent_scribe.py with 5-language script, eligibility_checker.py, crf_writer.py, stipend_dispenser.py, followup_scheduler.py, kinematics.yaml for Neo Beta, robot_loop.cpp with 100 ms E-stop (consent-room grade), sample CSVs, patient flow ASCII |
| 4 | 10 | shift_runner.py, iterations.yaml (4-dim sweep with language distribution), iterate.py, runner.rs, Cargo.toml, per-iteration Parquet, index.jsonl, aggregate.duckdb with 8 tables, notebook, run log |
| 5 | 12 | comparison_methodology.md, metrics.schema.json with 20 keys (adds language-coverage, patient-right-invocations, consent-comprehension-score), human_crc_baseline.csv (30 rows from 6 published NSCLC enrollment studies), neo_outcomes.parquet, compute.py, compare_agent.py, prompt frozen, comparison.json, report.md/.pdf, dashboard.html, summary.png |
| 6 | 7-check error scan |
| 7 | 3 | Parent README, releases.md entry, CHANGELOG.md v0.9.0 block |

## CI Compliance

Add per-file-ignores to `ruff.toml`:

```toml
"demo-projects/08-humanoid-clinical-research-coordinator-output/**/*.py" = ["F401", "F402", "F821"]
```

Required pre-commit: `ruff check`, `ruff format --check`, `yamllint -d relaxed .github/`.

## Comparison Framework

Three categories:
1. Prior versions (snapshot at `releases/v0.8.0/`).
2. Competitor humanoid configurations: Tesla Optimus Gen 3, Figure 03, Atlas Electric, human CRC.
3. Hybrid: Neo Beta + human CRC override with non-zero `human_intervention_seconds`.

Weights: Patient Experience 0.30, Enrollment Velocity 0.20, Consent Comprehension 0.15, Cost 0.10, Safety 0.10, Time 0.10, Multi-language Coverage 0.05.

## Notes

- The Neo Beta humanoid must invoke a human CRC override whenever the patient explicitly requests a human, per HR 9501 right to humanoid refusal.
- The consent comprehension score is computed by re-reading the consent back to the patient and asking 3 standardized comprehension questions. Score is logged per consent event.
- Stipend payment: the humanoid never handles physical cash. Payments are dispatched via the trial site's electronic payment gateway with a hash-chained receipt.
- The Neo Beta soft-tendon joints provide compliant patient contact (max 20 N contact force during escort handoff); rigid humanoids (Atlas, Optimus) require higher safety margins for the same task.
- E-stop latency: 100 ms (non-surgical, patient-interaction grade).
- All 12 patients in the simulated cohort have synthetic IDs only (TRIAL-NSCLC-3A-PNNN).
- Single dashes only. Black text only. ASCII diagrams cap at 80 by 60.
