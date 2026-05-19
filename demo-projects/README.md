# Demo Projects: Humanoid + LLM Oncology Clinical Trial Prompts

[![Release](https://img.shields.io/badge/Release-v0.6.0-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![Companion](https://img.shields.io/badge/Companion-physical--ai--oncology--trials-purple.svg)](https://github.com/kevinkawchak/physical-ai-oncology-trials)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18445179-blue)](https://doi.org/10.5281/zenodo.18445179)
[![Prior DOI](https://img.shields.io/badge/Prior%20DOI-10.5281%2Fzenodo.18029100-blue)](https://doi.org/10.5281/zenodo.18029100)
[![Prompts](https://img.shields.io/badge/Prompts-10-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects)
[![Image Instructions](https://img.shields.io/badge/Image%20Instructions-100-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct)
[![Swarm Instructions](https://img.shields.io/badge/Swarm%20Instructions-Demo%2007%20v0.3.0-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/07-humanoid/paper/instructions)
[![Codegen](https://img.shields.io/badge/Codegen-Demo%2007%20v0.4.0-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/07-humanoid/paper/codegen)
[![Execution](https://img.shields.io/badge/Execution-Demo%2007%20v0.5.0-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/07-humanoid/paper/execution)
[![Draft Paper](https://img.shields.io/badge/Draft%20Paper-Demo%2007%20v0.6.0-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/07-humanoid/paper/draft-paper)
[![Humanoid](https://img.shields.io/badge/Humanoid-Unitree%20H2%20EDU-orange.svg)](https://www.unitree.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10%20|%203.11%20|%203.12-blue.svg)](https://www.python.org/)

Released on 20 May 2026
CEO Kevin Kawchak, ChemicalQDevice

This directory contains 10 standalone Claude Code task brief prompts for downstream Claude Code Opus 4.7 1M Max sessions to author Physical AI oncology clinical trial demonstrations. Every demo features a distinct humanoid platform, an explicit large language model control loop, and a unique perspective spanning surgical, patient care, sponsor operations, pharmacy, pathology, telesurgery, adverse event, research coordination, radiation oncology, and decentralized home care scenarios. As of v0.2.0 the directory also contains 100 image instructions at `image-instruct/` (10 per prompt). As of v0.3.0 the directory also contains the multi-robot synergy code generation instructions for demo prompt 07 at `07-humanoid/paper/instructions/`. As of v0.4.0 the directory also contains the executable codegen for demo prompt 07 at `07-humanoid/paper/codegen/`. As of v0.5.0 the directory also contains the codegen execution outcomes at `07-humanoid/paper/execution/`. As of v0.6.0 the directory also contains the draft paper LaTeX scaffold at `07-humanoid/paper/draft-paper/` for the upcoming 70 plus page paper "Triple Humanoid 24/7 Adverse Event Oncology Trial Response Team: 4-Site Rotation."

## Why This Directory Exists

The companion repository kevinkawchak/physical-ai-oncology-trials covers end-to-end infrastructure for Physical AI oncology clinical trials. Clinical-AI-Demos covers the next layer: the wide-scope demonstrations that humanoid agents perform inside that infrastructure. Each prompt in this directory is a self-contained task brief that a future Claude Code Opus 4.7 1M Max session reads to author a complete simulation across seven sequential commits in a single pull request.

## Thesis

A new oncology clinical trial industry is forming around humanoid agents and large language models. Surgical robots are evolving toward general-purpose humanoid bodies with 30 to 50 degrees of freedom and 5 to 25 kg per-arm payload. Frontier large language models (Claude Opus 4.7, GPT-5.5, Gemini 3) provide the planning and reasoning loop. On-prem and edge LLM deployments keep PHI off the public cloud.

As of v0.3.0, demo prompt 07 extends the perspective with explicit multi-robot synergy: 3 H2 humanoids per site act as a camarade swarm with a single broadcast tick from the on-prem Claude Opus 4.7 1M.

As of v0.4.0, the executable codegen at `07-humanoid/paper/codegen/` implements the v0.3.0 instructions. The robot platform is specified as Unitree H2 EDU with two leading features: dexterous hand movements (6 fingers per hand, 12 grasp poses, 0.05 N tactile resolution) that enable 0.4 m hand-off of clinical tools to peers within 2 seconds, and compute module upgradeability to Jetson AGX Thor (2070 TOPS in 130 W) that drives the on-robot 10 Hz motion loop, 1000 Hz IR beacon listener, 200 Hz UWB peer mesh, and 39 joint controller in parallel with headroom for a Claude Haiku 4.5 sidecar.

The v0.4.0 thesis: on-premises repository based LLMs provide commands to humanoid robots based on real-time sensor data and controlled via x, y, z coordinates to administer synergistic treatment to patient adverse events. This workflow minimizes single robot error potential.

## The 10 Demo Prompts

| # | Demo | Humanoid | LLM | Duration | Resolution |
|---|------|----------|-----|----------|------------|
| 01 | [Humanoid Trial Site Operations Director](01-humanoid-site-operations-director.md) | Boston Dynamics Atlas Electric | Claude Opus 4.7 1M on-prem | 8 hours | 1 s |
| 02 | [Pharmaceutical Sponsor Humanoid Operations Center](02-sponsor-humanoid-operations-center.md) | 5x Tesla Optimus Gen 3 | Claude Sonnet 4.6 + Opus 4.7 cloud failover | 168 hours (1 week) | 1 s |
| 03 | [Humanoid Pharmacy and IMP Compounding](03-humanoid-pharmacy-imp-compounding.md) | Figure 03 | GPT-5.5 Thinking on-prem | 4 hours | 100 ms |
| 04 | [Humanoid Post-Operative Recovery Nurse](04-humanoid-post-op-recovery-nurse.md) | Agility Digit V5 | Claude Haiku/Sonnet + Ollama Llama 4 70B | 24 hours | 1 s |
| 05 | [Humanoid Biospecimen and Pathology Lab Assistant](05-humanoid-biospecimen-pathology-lab.md) | Sanctuary Phoenix Gen 8 | Gemini 3 Pro + Ollama Qwen3 72B via MCP | 12 hours | 100 ms |
| 06 | [Humanoid Tele-Surgical Assistant](06-humanoid-tele-surgical-assistant.md) | Apptronik Apollo | Claude Opus 4.7 1M + operator-in-the-loop | 90 minutes | 1 ms |
| 07 | [Humanoid 24/7 Adverse Event Response Team (v0.3.0 instructions, v0.4.0 codegen, v0.5.0 execution, v0.6.0 draft paper at 07-humanoid/paper/)](07-humanoid-24-7-adverse-event-response.md) | 3x Unitree H2 EDU per site (12 total) | Per-site Claude Opus 4.7 1M broadcast to 3 robots | 168 hours (1 week) | 1 s |
| 08 | [Humanoid Clinical Research Coordinator](08-humanoid-clinical-research-coordinator.md) | 1X Neo Beta | Claude + Gemini + GPT ensemble routing | 8 hours | 1 s |
| 09 | [Humanoid Radiation Oncology Technologist](09-humanoid-radiation-oncology-technologist.md) | Atlas + Optimus pair | NVIDIA GR00T N1.6 + Cosmos Reason 2 + Claude arbiter | 8 hours | 100 ms |
| 10 | [Humanoid Decentralized Home Care for DCT](10-humanoid-decentralized-home-care.md) | Figure 03 Field Edition | Claude Haiku 4.5 edge on NVIDIA Orin | 24 hours | 1 s active + 10 s ambient |

## Image Instructions (v0.2.0)

100 image instructions at `image-instruct/`, 10 per prompt across 10 subdirectories. 30 landscape + 70 portrait = 100 image instructions total.

## Swarm Instructions for Prompt 07 (v0.3.0)

Multi-robot synergy code generation instructions for demo prompt 07 are placed at `07-humanoid/paper/instructions/`. The instruction tree directs a future Claude Code Opus 4.7 1M Max session to author a complete 168-hour 4-site simulation with 3 H2 humanoids per site (12 total), broadcast publish-subscribe at 1 Hz, peer 60 GHz UWB plus IR beacon physical channels, shared on-prem Claude Code compute fabric intellectual channel, and the 7 camaraderie invariants.

## Codegen for Prompt 07 (v0.4.0)

The executable codegen for demo prompt 07 is at `07-humanoid/paper/codegen/`. The codegen implements the v0.3.0 instructions as runnable Python, C++, Rust, YAML, JSON, and Markdown. Robot platform: Unitree H2 EDU with dexterous hands (6 fingers per hand, 12 grasp poses, 0.05 N tactile resolution) and compute module upgradeable to Jetson AGX Thor (2070 TOPS).

Directory tree:

```
demo-projects/07-humanoid/paper/codegen/
  README.md                                # Comprehensive codegen README with 11 badges
  architecture.md                          # 6-layer architecture with Mermaid diagrams
  pyproject.toml                           # Python 3.10/3.11/3.12 with ruff cascade
  Cargo.toml                               # Rust runner crate
  docker-compose.yml                       # 4 per-site LLM, ingest, simulator, db, bus
  LICENSE.txt                              # MIT
  config/                                  # 7 YAML config files
  schemas/                                 # 11 JSON Schema files (Draft 2020-12)
  src/                                     # 24 Python, 1 C++, 2 Rust source files
  data/                                    # Samples, sensor csv, xyz csv, CTCAE, baseline
  diagrams/                                # 3 ASCII diagrams capped at 80 by 60
  notebooks/                               # run_log.ipynb
  reports/                                 # comparison_methodology, comparison.json, report.md, dashboard.html
  figures/                                 # 6 PNG figures at 300 dpi
  tests/                                   # 6 pytest modules (36 tests pass in 0.27 s)
  docker/                                  # 4 Dockerfiles (llm, ingest, simulator, bus)
```

Runtime support:

- MacOS: Mac Studio M2 Ultra at 12 minutes per 168-hour iteration
- Windows: Lenovo ThinkStation P8 at 10 minutes per iteration (96 cores)
- Linux: Supermicro AS-2025HS-TNR at 8 minutes per iteration (192 cores)
- Claude Code Opus 4.7 1M Max: re-run on fresh checkout

The v0.4.0 release cites the author's prior FAERS LLM paper at DOI 10.5281/zenodo.18029100 as the precedent for LLM-driven adverse event work.

## Execution for Prompt 07 (v0.5.0)

The codegen execution outcomes for demo prompt 07 are at `07-humanoid/paper/execution/`. The execution tree captures the runtime outcomes of every executable element in the v0.4.0 codegen tree on a Linux server with Python 3.10 to 3.12, Rust 1.94, g++ -std=c++20, cmake, and DuckDB. 50 file tree with 23 per-step logs, 4 ASCII diagrams capped at 80 by 60, 6 PNG figures at 300 dpi (regenerated from src/figures_gen.py against the hand-curated iteration index), 4 machine readable output tables, 5 report copies plus the consolidated execution_report_v0_5_0.md, and 8 data artifacts.

Directory tree:

```
demo-projects/07-humanoid/paper/execution/
  README.md                        # 12 badges, 7 commit roadmap, ASCII flow
  logs/                            # 23 per step execution logs
    01_schema_ingest.log           # 10 passed 0 failed
    02_check_errors.log            # 0 issues across 7 checks
    03_pytest.log                  # 36 passed in 0.22 s
    04_module_imports.log          # 22 of 22
    05_swarm_coordinator_smoke.log # 7 of 7 invariants pass
    06_llm_planner_smoke.log       # schema valid llm_decision
    07_ctcae_grader_smoke.log      # grade 3 anaphylaxis with swarm consensus
    08_h2_dispatcher_smoke.log     # 3 acks within 50 ms
    09_site_runtime_4site.log      # 4 sites x 60 ticks
    10_h2_dispatcher_init.log      # 12 robot roster across 4 sites
    11_week_runner_fast.log        # 3600 ticks per site
    12_sensor_xyz_safety_smoke.log # sensor projection plus xyz safety
    13_comms_peer_smoke.log        # uwb + ir + pubsub + peer state
    14_fda_phys_xsite_smoke.log    # ed25519 signed plus PHI smuggle reject
    15_cargo_build.log             # cargo build --release 16 s
    16_rust_runner.log             # Rust 32 iteration sweep
    17_cpp_robot_loop.log          # g++ -std=c++20 -O2 robot_loop
    18_iterate_sweep.log           # 32 iterations
    19_compute_metrics.log         # weighted score v0_4_0 = 0.953
    20_compare_agent_narrative.log # natural language report
    21_figures_generation.log      # 6 PNG at 300 dpi
    22_validation_pass.log         # JSON YAML ASCII OK
    23_final_ci_pass.log           # ruff format yamllint pytest all green
  data/                            # 8 data artifacts
  diagrams/                        # 4 ASCII execution diagrams
  figures/                         # 6 PNG figures at 300 dpi
  reports/                         # 4 codegen report copies plus execution report
  outputs/                         # comparison plus iteration plus tree plus inventory tables
```

Recorded limitations:
- src/week_runner.py worker returns constants
- src/iterate.py hard codes headline statistics
- src/llm_planner.py falls back to deterministic stub without on-prem appliance
- src/robot_loop.cpp does not connect to real Unitree H2 EDU SDK
- src/runner_main.rs prints hard-coded summaries

These limitations are inherent to a codegen tree designed to be executable on a high-end conventional server without specialized humanoid hardware.

## Draft Paper for Prompt 07 (v0.6.0)

The draft paper LaTeX scaffold for demo prompt 07 is at `07-humanoid/paper/draft-paper/` for the upcoming paper "Triple Humanoid 24/7 Adverse Event Oncology Trial Response Team: 4-Site Rotation" by Kevin Kawchak (ORCID 0009-0007-5457-8667, CEO ChemicalQDevice). The scaffold has 12 source files (main.tex, humanoid_paper_template.sty, references.bib, README.md, and 8 section files: abstract, introduction, methods, results, discussion, limitations_future, conclusions, back_matter) plus a `LaTeX-Source.zip` Overleaf bundle. Every section file carries bracketed instructions naming the exact RESEARCH files a future Claude Code Opus 4.7 1M Max session must read before authoring that section. The future session expands the 20 page scaffold to a 70 plus page final paper. Bibliography entries carry both the bare DOI in the doi field and the full https://doi.org/ resolver URL in the url field, plus a howpublished \url so the ieeetr style prints clickable links in the rendered PDF. The author's December 2025 FDA AERS paper at 10.5281/zenodo.18029100 (`kawchak_2025_18029100`) is cited as the prior evidence that LLMs are effective on FDA adverse event data. CI passes ruff, ruff format, and yamllint on Python 3.10/3.11/3.12.

Directory tree:

```
demo-projects/07-humanoid/paper/draft-paper/
  main.tex                          # Top level manuscript file
  humanoid_paper_template.sty       # Style file, shared 8 col table macro
  references.bib                    # 15 entries with clickable DOI + URL
  README.md                         # 8 badges, file inventory, ASCII pipeline
  LaTeX-Source.zip                  # Overleaf bundle of all source files
  sections/
    abstract.tex                    # ~300 word abstract scaffold
    introduction.tex                # 5 subsection introduction scaffold
    methods.tex                     # 9 subsection methods scaffold
    results.tex                     # 7 subsection results scaffold
    discussion.tex                  # 6 subsection discussion scaffold
    limitations_future.tex          # 5 subsection limits scaffold
    conclusions.tex                 # 4 subsection conclusions scaffold
    back_matter.tex                 # Acks, Ethics, Rights, Cite, Data
```

## Safety Constraints Across the 10 Demos

| Demo | E-Stop Latency | Cum. Force Limit | Inter-Humanoid Min Distance | PHI Egress |
|------|---------------|------------------|-----------------------------|------------|
| 01 | 50 ms | 15 N | n/a (1 humanoid) | none |
| 02 | 100 ms | 25 N | 8 mm | gated by Safe Harbor |
| 03 | 5 ms | 8 N | n/a (1 humanoid) | none |
| 04 | 100 ms | 12 N | n/a (1 humanoid) | none (Ollama PHI route) |
| 05 | 10 ms | 10 N | n/a (1 humanoid) | gated by Safe Harbor |
| 06 | 5 ms | 5 N | n/a (1 humanoid) | none |
| 07 (v0.3.0 plus v0.4.0) | 5 ms (swarm-wide) | 15 N per arm, 22 N cumulative cross-robot | 0.4 m handoff, 1.2 m rest | none |
| 08 | 100 ms | 20 N | n/a (1 humanoid) | gated by Safe Harbor |
| 09 | 5 ms | 22 N | 1.5 m | none |
| 10 | 100 ms | 12 N | n/a (1 humanoid) | none (edge LLM only) |

## Notes

- All prompts use single dashes only. No em dashes, no double dashes, no triple dashes in prose.
- ASCII diagrams cap at 80 columns by 60 lines.
- All patient identifiers are synthetic. No real PHI is referenced.
- The seven-commit single-PR pattern.
- CI compliance: `ruff check`, `ruff format --check`, `yamllint -d relaxed .github/` must pass on Python 3.10, 3.11, and 3.12 before any prompt's output PR is merged.
- The v0.3.0 swarm instructions and v0.4.0 codegen for prompt 07 cite the author's prior FAERS LLM paper at DOI 10.5281/zenodo.18029100.
- The v0.4.0 codegen specifies Unitree H2 EDU as the exact humanoid platform with dexterous hands (6 fingers, 12 grasp poses, 0.05 N tactile resolution) and compute module upgradeability to Jetson AGX Thor 2070 TOPS.
