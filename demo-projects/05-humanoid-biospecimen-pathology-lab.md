# Demo Prompt 05: Humanoid Biospecimen and Pathology Lab Assistant

[![Demo](https://img.shields.io/badge/Demo-05%20of%2010-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![Companion](https://img.shields.io/badge/Companion-physical--ai--oncology--trials-purple.svg)](https://github.com/kevinkawchak/physical-ai-oncology-trials)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18445179-blue)](https://doi.org/10.5281/zenodo.18445179)
[![Resolution](https://img.shields.io/badge/Resolution-100ms-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![Humanoid](https://img.shields.io/badge/Humanoid-Sanctuary%20Phoenix%20Gen%208-orange.svg)](https://www.sanctuary.ai)
[![LLM](https://img.shields.io/badge/LLM-Gemini%203%20Pro%20%2B%20Ollama-blueviolet.svg)](https://gemini.google)
[![Python](https://img.shields.io/badge/Python-3.10%20|%203.11%20|%203.12-blue.svg)](https://www.python.org/)

Released on 16 May 2026
CEO Kevin Kawchak, ChemicalQDevice

## Perspective

A Sanctuary AI Phoenix Gen 8 humanoid processes 8 fresh biopsy specimens through a CAP-accredited oncology pathology lab during a 12-hour day shift. The specimens arrive at irregular intervals from 4 surgical suites across the hospital between 07:00 and 19:00 local time. Each specimen requires: gross examination, fixation in 10 percent neutral buffered formalin (NBF), processing, paraffin embedding, microtome sectioning at 4 micron, H&E staining, immunohistochemistry panels (PD-L1 22C3, MSI-H, HER2, ER/PR for breast, EGFR for NSCLC), and digital slide scanning at 40x for pathologist review. The Phoenix Gen 8 humanoid is rated for benchtop laboratory work with its 24-finger dexterous hand and its 0.5 mm RMS positioning. The LLM stack is Gemini 3 Pro (cloud) plus Ollama Qwen3 72B (on-prem) coordinated through a Model Context Protocol (MCP) server. Pathologist sign-off remains human, but every physical handling step is humanoid.

## Thesis

Pathology specimen handling has the highest cumulative human-error rate of any clinical trial laboratory workflow: 2 to 5 percent of specimens experience at least one preanalytical error per 2024 College of American Pathologists Q-Probes data. The Phoenix Gen 8 humanoid plus an MCP-coordinated LLM stack eliminates the four highest-error preanalytical steps (mislabeling, cold ischemia time excursions, formalin fixation duration drift, and embedding orientation rotation). The 12-hour simulation produces a hash-chained chain-of-custody log per specimen that supports CAP, CLIA, and 21 CFR Part 58 (GLP) audit requirements.

## Scope

- One simulated lab: PATH-LAB-001 (CAP-accredited, 4 grossing stations, 1 tissue processor, 1 embedding center, 1 microtome, 1 stainer, 1 digital scanner).
- One simulated humanoid: Sanctuary Phoenix Gen 8 (24 DOF per hand, 1.7 m height, 70 kg, 5 kg payload per arm, 0.5 mm RMS positioning, EM-shielded for stainer electronics).
- One simulated LLM stack: Gemini 3 Pro cloud + Ollama Qwen3 72B on-prem, coordinated via MCP (Model Context Protocol) server.
- One shift duration: 12 hours (43,200 s, 432,000 ticks at 100 ms LLM cadence, 4,320,000 ticks at 10 Hz humanoid motion cadence).
- Specimen cohort: 8 specimens (2 NSCLC core needle, 2 breast core needle, 2 colorectal punch, 1 melanoma excisional, 1 lymphoma excisional).
- Iteration count: 16 deterministic iterations covering seed, LLM temperature, humanoid hand gripper noise sigma, and specimen arrival jitter.

## Why a Future Pass

A 12-hour shift at 10 Hz humanoid telemetry plus 100 ms LLM inference for 8 specimens produces 4,320,000 humanoid records plus 432,000 LLM decisions plus a 1,200-record chain-of-custody log. Authoring inline is infeasible.

## Inputs from physical-ai-oncology-trials

| Path | Purpose |
|------|---------|
| `digital-twins/patient-modeling/tumor_twin_pipeline.py` | Tumor digital twin pipeline (for downstream specimen-to-twin linkage) |
| `digital-twins/clinical-integration/clinical_dt_interface.py` | FHIR/DICOM clinical integration |
| `digital-twins/examples-twins/04_tumor_microenvironment_immunotherapy_dt.py` | Tumor microenvironment twin (PD-L1 / TME staining linkage) |
| `examples-new/06_robotic_sample_handling.py` | Robotic sample handling reference |
| `examples-new/01_realtime_safety_monitoring.py` | Real-time safety monitoring |
| `agentic-ai/examples-agentic-ai/01_mcp_clinical_robotics_server.py` | MCP clinical robotics server (verbatim reference) |
| `agentic-ai/examples-agentic-ai/04_autonomous_simulation_orchestrator.py` | Autonomous orchestration |
| `unification/usl/humanoids/usl_humanoid_scoring.py` | Humanoid USL scoring |
| `tools/dicom-inspector/dicom_inspector.py` | DICOM inspection (for digital slide files) |
| `regulatory/ich-gcp/gcp_compliance_checker.py` | GCP compliance |
| `regulatory/Adaption-21-CFR-Part-312/source/Physical_AI_21_CFR_Part_312_chunk/` | IND application chunks |
| `privacy/de-identification/deidentification_pipeline.py` | Safe Harbor before cloud LLM call |
| `privacy/phi-pii-management/phi_detector.py` | PHI detection |
| `competitions/instructions/chunking_strategy.md` | Three-layer chunking |
| `competitions/instructions/file_format_conventions.md` | File format defaults |
| `competitions/instructions/ascii_diagram_guide.md` | ASCII drawing rules |
| `frameworks/nvidia-isaac/INTEGRATION.md` | Isaac Sim integration (for humanoid-hand simulation) |

## Downstream LLM Processing Instructions

The future Claude Code Opus 4.7 1M Max session must:

1. Read `agentic-ai/examples-agentic-ai/01_mcp_clinical_robotics_server.py` end to end. The MCP server pattern in that file is the authoritative source for the on-prem-plus-cloud LLM coordination. Implement an MCP server in this demo that exposes 7 tools to both Gemini 3 Pro and Ollama Qwen3 72B: `gross_examine`, `formalin_fix`, `process_tissue`, `embed_paraffin`, `microtome_section`, `stain_he`, `stain_ihc`. Each tool emits a humanoid command stream and a chain-of-custody event.
2. The cloud Gemini 3 Pro path is invoked only after `privacy/de-identification/deidentification_pipeline.py` Safe Harbor gate has redacted PHI from the specimen accession metadata. The on-prem Qwen3 72B path handles all PHI-bearing inference.
3. The CAP, CLIA, and 21 CFR Part 58 (GLP) requirements are downstream regulatory references. Read the IND adaptation chunks under `regulatory/Adaption-21-CFR-Part-312/source/Physical_AI_21_CFR_Part_312_chunk/` to inherit the IND-relevant specimen handling requirements.
4. Apply the three-layer chunking strategy.
5. Run pre-commit checklist on every commit.
6. Commit and push seven sequential commits in a single PR on branch `claude/demo-05-pathology-lab-shortid`.

## Future Output Tree

```
demo-projects/05-humanoid-biospecimen-pathology-lab-output/
  README.md
  config/
    pathology_lab.yaml               # PATH-LAB-001 layout
    phoenix_humanoid.yaml            # Phoenix Gen 8 specs
    llm_mcp.yaml                     # MCP server config, tool registry
    specimen_arrivals.yaml           # 8 specimen arrival schedule
  schemas/
    humanoid_command.schema.json
    specimen_record.schema.json
    chain_of_custody.schema.json
    grossing_event.schema.json
    fixation_event.schema.json
    embedding_event.schema.json
    sectioning_event.schema.json
    staining_event.schema.json
    digital_slide_record.schema.json
    llm_decision.schema.json
  src/
    lab_state.py
    phoenix_dispatcher.py
    mcp_server.py                    # 7 tools exposed via MCP
    llm_router.py                    # Gemini 3 Pro + Ollama Qwen3 72B
    phi_redactor.py
    cap_compliance.py                # CAP Q-Probes thresholds
    glp_compliance.py                # 21 CFR Part 58 compliance
    shift_runner.py
  data/
    shift_humanoid_commands.parquet  # 4,320,000 ticks
    shift_llm_decisions.jsonl        # 432,000 decisions
    shift_chain_of_custody.parquet   # 1,200 events
    shift_specimens.parquet          # 8 specimen records
    digital_slides/                  # 8 DICOM-pathology slides (placeholder JSON)
    iterations/
      run_NNNNN.parquet              # 16 iterations
      index.jsonl
      aggregate.duckdb
  diagrams/
    pathology_lab_layout.txt         # 80x60 ASCII
    specimen_flow.txt
    humanoid_state_timeline.txt
    chain_of_custody_diagram.txt
```

## Per-Commit Roadmap

| Commit | Files | Authored Content |
|--------|-------|------------------|
| 1 | 7 | README, architecture.md with MCP server Mermaid topology, pyproject.toml, docker-compose.yml (gemini-proxy, ollama, mcp-server, ingest, simulator services), config/pathology_lab.yaml, LICENSE.txt, pathology_lab_layout.txt |
| 2 | 10 | 9 schemas (humanoid_command, specimen_record, chain_of_custody, grossing, fixation, embedding, sectioning, staining, digital_slide) + ingest.py with CAP rule validation |
| 3 | 11 | phoenix_dispatcher.py, mcp_server.py with 7 tools, llm_router.py, phi_redactor.py, cap_compliance.py, glp_compliance.py, kinematics.yaml for 24-DOF hand, robot_loop.cpp with 10 ms E-stop for benchtop work, sample CSVs, hand-trace ASCII, Cargo.toml |
| 4 | 10 | shift_runner.py, iterations.yaml (4-dim sweep), iterate.py, runner.rs, per-iteration Parquet, index.jsonl, aggregate.duckdb with 5 tables, notebook, run log |
| 5 | 12 | comparison_methodology.md, metrics.schema.json with 19 keys, human_pathologist_baseline.csv (30 rows from 6 published CAP Q-Probes datasets), phoenix_outcomes.parquet, compute.py, compare_agent.py with Gemini 3 Pro and Ollama backends, prompt frozen, comparison.json, report.md/.pdf, dashboard.html, summary.png |
| 6 | 7-check error scan |
| 7 | 3 | Parent README, releases.md entry, CHANGELOG.md v0.6.0 block |

## CI Compliance

Add per-file-ignores to `ruff.toml`:

```toml
"demo-projects/05-humanoid-biospecimen-pathology-lab-output/**/*.py" = ["F401", "F402", "F821"]
```

Required pre-commit: `ruff check`, `ruff format --check`, `yamllint -d relaxed .github/`. The MCP server config YAML must yamllint clean with `relaxed` profile.

## Comparison Framework

Three categories:
1. Prior versions (snapshot at `releases/v0.5.0/`).
2. Competitor humanoid configurations: Figure 03, Tesla Optimus Gen 3 (less dexterous), human histotechnician.
3. Hybrid: Phoenix Gen 8 + human pathologist sign-off only.

Weights: Accuracy 0.30, Chain-of-Custody Integrity 0.25, Turn-Around-Time 0.20, Cost 0.10, Safety 0.10, Patient Experience 0.05.

## Notes

- Cold ischemia time (CIT): the humanoid must place each specimen in 10 percent NBF within 30 minutes of surgical removal. CIT excursions are flagged with priority 0.95.
- Formalin fixation duration: 6 to 24 hours per CAP guideline; deviations are flagged.
- Microtome sectioning at 4 micron with 1 micron tolerance; humanoid wrist torque feedback ensures consistent ribbon advancement.
- IHC stainer (Ventana BenchMark Ultra simulated) handoff: humanoid loads slides into the stainer carousel without touching the bar-coded labels.
- Digital slide scanner output: 40x magnification, .svs format placeholder JSON in the output tree (real .svs files would be 1 to 4 GB each and exceed the GitHub 10 MB cap; the future session writes Zenodo pointer JSON files for the real .svs scans).
- The Phoenix Gen 8 hand has 24 DOF; the demo exercises 18 of those DOF (the remaining 6 are tertiary opposable thumb joints reserved for surgical instrument handling demos).
- All Markdown files use single dashes only. Black text only. ASCII diagrams cap at 80 by 60.
