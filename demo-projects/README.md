# Demo Projects: Humanoid + LLM Oncology Clinical Trial Prompts

[![Release](https://img.shields.io/badge/Release-v0.3.0-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![Companion](https://img.shields.io/badge/Companion-physical--ai--oncology--trials-purple.svg)](https://github.com/kevinkawchak/physical-ai-oncology-trials)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18445179-blue)](https://doi.org/10.5281/zenodo.18445179)
[![Prior DOI](https://img.shields.io/badge/Prior%20DOI-10.5281%2Fzenodo.18029100-blue)](https://doi.org/10.5281/zenodo.18029100)
[![Prompts](https://img.shields.io/badge/Prompts-10-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects)
[![Image Instructions](https://img.shields.io/badge/Image%20Instructions-100-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct)
[![Swarm Instructions](https://img.shields.io/badge/Swarm%20Instructions-Demo%2007%20v0.3.0-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/07-humanoid/paper/instructions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10%20|%203.11%20|%203.12-blue.svg)](https://www.python.org/)

Released on 17 May 2026
CEO Kevin Kawchak, ChemicalQDevice

This directory contains 10 standalone Claude Code task brief prompts for downstream Claude Code Opus 4.7 1M Max sessions to author Physical AI oncology clinical trial demonstrations. Every demo features a distinct humanoid platform, an explicit large language model control loop, and a unique perspective spanning surgical, patient care, sponsor operations, pharmacy, pathology, telesurgery, adverse event, research coordination, radiation oncology, and decentralized home care scenarios. As of v0.2.0 the directory also contains 100 image instructions at `image-instruct/` (10 per prompt). As of v0.3.0 the directory also contains the multi-robot synergy code generation instructions for demo prompt 07 at `07-humanoid/paper/instructions/`.

## Why This Directory Exists

The companion repository kevinkawchak/physical-ai-oncology-trials covers end-to-end infrastructure for Physical AI oncology clinical trials (sponsors, sites, regulatory adaptations, federated learning, digital twins, surgical simulations). Clinical-AI-Demos covers the next layer: the wide-scope demonstrations that humanoid agents perform inside that infrastructure. Each prompt in this directory is a self-contained task brief that a future Claude Code Opus 4.7 1M Max session reads to author a complete simulation across seven sequential commits in a single pull request.

## Thesis

A new oncology clinical trial industry is forming around humanoid agents and large language models. Surgical robots are evolving toward general-purpose humanoid bodies with 30 to 50 degrees of freedom and 5 to 25 kg per-arm payload. Frontier large language models (Claude Opus 4.7, GPT-5.5, Gemini 3) provide the planning and reasoning loop. On-prem and edge LLM deployments (Anthropic Cowork, Ollama Llama 4, NVIDIA GR00T) keep PHI off the public cloud. Every trial site, every pharmaceutical sponsor, every pharmacy clean room, every patient recovery room, every pathology lab, every LINAC vault, every adverse event call, every CRC visit, every home visit gains a humanoid plus an LLM. This directory delivers 10 perspectives on what those deployments look like.

As of v0.3.0, demo prompt 07 extends the perspective with explicit multi-robot synergy: 3 H2 humanoids per site act as a camarade swarm with a single broadcast tick to all 3 from the on-prem Claude Opus 4.7 1M, peer 60 GHz UWB plus IR beacon physical comms, shared on-prem Claude Code compute fabric intellectual comms, and adaptation to patients, doctors, and other robots. The v0.3.0 thesis: On-premises repository based LLMs provide commands to humanoid robots based on real-time sensor data and controlled via x, y, z coordinates to administer synergistic treatment to patients adverse events. This workflow minimizes single robot error potential.

## The 10 Demo Prompts

| # | Demo | Humanoid | LLM | Duration | Resolution |
|---|------|----------|-----|----------|------------|
| 01 | [Humanoid Trial Site Operations Director](01-humanoid-site-operations-director.md) | Boston Dynamics Atlas Electric | Claude Opus 4.7 1M on-prem | 8 hours | 1 s |
| 02 | [Pharmaceutical Sponsor Humanoid Operations Center](02-sponsor-humanoid-operations-center.md) | 5x Tesla Optimus Gen 3 | Claude Sonnet 4.6 + Opus 4.7 cloud failover | 168 hours (1 week) | 1 s |
| 03 | [Humanoid Pharmacy and IMP Compounding](03-humanoid-pharmacy-imp-compounding.md) | Figure 03 | GPT-5.5 Thinking on-prem | 4 hours | 100 ms |
| 04 | [Humanoid Post-Operative Recovery Nurse](04-humanoid-post-op-recovery-nurse.md) | Agility Digit V5 | Claude Haiku/Sonnet + Ollama Llama 4 70B | 24 hours | 1 s |
| 05 | [Humanoid Biospecimen and Pathology Lab Assistant](05-humanoid-biospecimen-pathology-lab.md) | Sanctuary Phoenix Gen 8 | Gemini 3 Pro + Ollama Qwen3 72B via MCP | 12 hours | 100 ms |
| 06 | [Humanoid Tele-Surgical Assistant](06-humanoid-tele-surgical-assistant.md) | Apptronik Apollo | Claude Opus 4.7 1M + operator-in-the-loop | 90 minutes | 1 ms |
| 07 | [Humanoid 24/7 Adverse Event Response Team (v0.3.0 swarm at 07-humanoid/paper/instructions)](07-humanoid-24-7-adverse-event-response.md) | 3x Unitree H2 per site (12 total) | Per-site Claude Opus 4.7 1M broadcast to 3 robots | 168 hours (1 week) | 1 s |
| 08 | [Humanoid Clinical Research Coordinator](08-humanoid-clinical-research-coordinator.md) | 1X Neo Beta | Claude + Gemini + GPT ensemble routing | 8 hours | 1 s |
| 09 | [Humanoid Radiation Oncology Technologist](09-humanoid-radiation-oncology-technologist.md) | Atlas + Optimus pair | NVIDIA GR00T N1.6 + Cosmos Reason 2 + Claude arbiter | 8 hours | 100 ms |
| 10 | [Humanoid Decentralized Home Care for DCT](10-humanoid-decentralized-home-care.md) | Figure 03 Field Edition | Claude Haiku 4.5 edge on NVIDIA Orin | 24 hours | 1 s active + 10 s ambient |

## Image Instructions (v0.2.0)

100 image instructions are placed at `image-instruct/`, 10 per prompt across 10 subdirectories. Each instruction specifies one publication-ready 300 dpi matplotlib PNG that a future Claude Code Opus 4.7 1M Max session will author. 30 landscape + 70 portrait = 100 image instructions total.

## Swarm Instructions for Prompt 07 (v0.3.0)

Multi-robot synergy code generation instructions for demo prompt 07 are placed at `07-humanoid/paper/instructions/`. The instruction tree directs a future Claude Code Opus 4.7 1M Max session to author a complete 168-hour 4-site simulation with 3 H2 humanoids per site (12 total), broadcast publish-subscribe at 1 Hz, peer 60 GHz UWB plus IR beacon physical channels, shared on-prem Claude Code compute fabric intellectual channel, and the 7 camaraderie invariants.

Directory tree:

```
demo-projects/07-humanoid/paper/instructions/
  README.md                                # Comprehensive overview with badges, ASCII, Mermaid, BibTeX
  00-project-overview/                     # Architecture, swarm, thesis, working memory, camaraderie, network layout
  01-commit-roadmap/                       # 7 commit roadmap, error scan, 5 pytest modules, conftest, site_frame_bounds, CI compliance
  02-config-instructions/                  # network, h2_humanoid, site_coordination, swarm_coordination, llm_loop, escalation_rules, pyproject.toml, docker-compose.yml
  03-schemas-instructions/                 # 10 JSON Schemas plus samples.jsonl plus ingest.py
  04-robotic-instructions/                 # h2_dispatcher, swarm_coordinator, robot_loop.cpp, comms_physical, comms_intellectual, peer_state_tracker, ASCII diagrams, Cargo.toml
  05-cartesian-instructions/               # kinematics.yaml, sensor_to_xyz, cartesian_planner, xyz_safety, sample CSVs
  06-iteration-instructions/               # iterations.yaml, week_runner, iterate, runner.rs, per-day Parquet, aggregate.duckdb, run log notebook
  07-llm-planner-instructions/             # llm_planner, broadcaster, shared_compute, ctcae_grader, fda_rtct_submitter, physician_escalation, architecture summary
  08-comparison-instructions/              # comparison methodology, metrics schema, human team baseline, compute, compare agent, prompt frozen, report, dashboard, figures, JSON, Parquet
  09-runtime-instructions/                 # MacOS, Windows, Linux runtime guides
  10-repository-update-instructions/       # README, releases, CHANGELOG update guides
```

The v0.3.0 release cites the author's prior FAERS LLM paper at DOI 10.5281/zenodo.18029100 as the precedent for LLM-driven adverse event work.

| # | Image Instructions Subdirectory | Humanoid + LLM Stack | Landscape | Portrait |
|---|---------------------------------|----------------------|-----------|----------|
| 01 | [image-instruct/01-site-operations-director/](image-instruct/01-site-operations-director) | Atlas Electric + Claude Opus 4.7 1M on-prem | 3 | 7 |
| 02 | [image-instruct/02-sponsor-operations-center/](image-instruct/02-sponsor-operations-center) | 5x Tesla Optimus Gen 3 + Sonnet/Opus failover | 3 | 7 |
| 03 | [image-instruct/03-pharmacy-imp-compounding/](image-instruct/03-pharmacy-imp-compounding) | Figure 03 + GPT-5.5 Thinking on-prem | 3 | 7 |
| 04 | [image-instruct/04-post-op-recovery-nurse/](image-instruct/04-post-op-recovery-nurse) | Digit V5 + Haiku/Sonnet + Llama 4 70B | 3 | 7 |
| 05 | [image-instruct/05-biospecimen-pathology-lab/](image-instruct/05-biospecimen-pathology-lab) | Phoenix Gen 8 + Gemini/Qwen via MCP | 3 | 7 |
| 06 | [image-instruct/06-tele-surgical-assistant/](image-instruct/06-tele-surgical-assistant) | Apollo + Claude Opus 4.7 1M + Operator | 3 | 7 |
| 07 | [image-instruct/07-adverse-event-response/](image-instruct/07-adverse-event-response) | 3x Unitree H2 per site + Per-Site Claude Opus (v0.3.0 swarm) | 3 | 7 |
| 08 | [image-instruct/08-clinical-research-coordinator/](image-instruct/08-clinical-research-coordinator) | Neo Beta + Claude+Gemini+GPT ensemble | 3 | 7 |
| 09 | [image-instruct/09-radiation-oncology-technologist/](image-instruct/09-radiation-oncology-technologist) | Atlas+Optimus + GR00T+Cosmos+Claude arbiter | 3 | 7 |
| 10 | [image-instruct/10-decentralized-home-care/](image-instruct/10-decentralized-home-care) | Figure 03 Field + Claude Haiku 4.5 on Orin | 3 | 7 |

## Coverage Matrix

```
                                          Setting Coverage
              Trial   Sponsor  Pharmacy  Recovery  Patho  Tele  AE   CRC  RadOnc  Home
              Site    HQ                  Room     Lab    Surg  Resp       Vault   DCT
01 Site Dir   X
02 Sponsor    .       X        .          .        .      .     .    .    .       .
03 Pharmacy   .       .        X          .        .      .     .    .    .       .
04 Recovery   .       .        .          X        .      .     .    .    .       .
05 Pathology  .       .        .          .        X      .     .    .    .       .
06 Tele-Surg  .       .        .          .        .      X     .    .    .       .
07 AE Resp    X       X        .          X        .      .     X    .    .       .
08 CRC        X       .        .          .        .      .     .    X    .       .
09 RadOnc     X       .        .          .        .      .     .    .    X       .
10 Home DCT   .       X        .          .        .      .     .    .    .       X
```

```
                                          Humanoid Coverage
              Atlas  Optimus  Figure  Digit  Phoenix  Apollo  Neo  H2  Field  Pair
01 Site Dir   X
02 Sponsor    .      X (5)    .       .      .        .       .    .   .      .
03 Pharmacy   .      .        X       .      .        .       .    .   .      .
04 Recovery   .      .        .       X      .        .       .    .   .      .
05 Pathology  .      .        .       .      X        .       .    .   .      .
06 Tele-Surg  .      .        .       .      .        X       .    .   .      .
07 AE Resp    .      .        .       .      .        .       .    X (3 per site x 4 sites = 12) .   .
08 CRC        .      .        .       .      .        .       X    .   .      .
09 RadOnc     .      .        .       .      .        .       .    .   .      X (Atlas+Optimus)
10 Home DCT   .      .        .       .      .        .       .    .   X      .
```

## Common Prompt Template

Every prompt in this directory follows the same template:

```
1. Title with v0.1.0 release badge, companion badge, DOI badge,
   resolution badge, humanoid badge, LLM badge, Python version badge.
2. Perspective: who is the humanoid, where, when, why, what does it do?
3. Thesis: the on-prem LLM + humanoid solution.
4. Scope: one specific scenario with patient, humanoid, LLM, duration,
   resolution, iteration count.
5. Why a Future Pass: chunking justification.
6. Inputs from physical-ai-oncology-trials: exact file paths with
   purpose statements.
7. Downstream LLM Processing Instructions: step-by-step procedure for
   the future Claude Code Opus 4.7 1M Max session.
8. Future Output Tree: ASCII tree of files the future session authors.
9. Per-Commit Roadmap: 7-commit single-PR breakdown.
10. CI Compliance: ruff + yamllint configuration.
11. Comparison Framework: three-category competitor model with weights.
12. Notes: safety constraints, force limits, E-stop latency budgets,
    PHI handling rules.
```

## How to Run a Prompt

A downstream Claude Code Opus 4.7 1M Max session executes each prompt as follows:

1. Read the prompt file in this directory (e.g., `01-humanoid-site-operations-director.md`).
2. Read the 10 image instruction files in `image-instruct/NN-<short-name>/` for the chart specifications.
3. For prompt 07 v0.3.0, read the multi-robot synergy code generation instructions in `07-humanoid/paper/instructions/`.
4. Clone or update `kevinkawchak/physical-ai-oncology-trials` to read the input files listed under "Inputs from physical-ai-oncology-trials".
5. Pre-chunk any input file over 20K tokens per the chunking strategy in `competitions/instructions/chunking_strategy.md` of the companion repository.
6. Author the output tree under `demo-projects/<NN-name>-output/` (or `demo-projects/07-humanoid/paper/instructions/` for v0.3.0 prompt 07) following the "Future Output Tree" section, including a `figures/` subdirectory populated from the 10 image instructions.
7. Apply the SVG-to-ASCII replacement rule from `competitions/instructions/ascii_diagram_guide.md` for any high-frequency time series.
8. Run the pre-commit checklist: `ruff check .`, `ruff format --check .`, `yamllint -d relaxed .github/`.
9. Commit seven sequential commits in a single PR on a branch named `claude/demo-NN-name-shortid`.
10. The seventh commit updates the main README, releases.md, and CHANGELOG.md.

## ASCII Architecture Diagram

```
                   Clinical-AI-Demos: Humanoid + LLM Demo Prompts
                   ===============================================

  +-------------------+      +-------------------+      +-------------------+
  |   Prompt File +   |      |   Future Claude   |      |   Output Tree     |
  |   Image           |----->|   Code Opus 4.7   |----->|   under demo-     |
  |   Instructions    |      |   1M Max Session  |      |   projects/NN-*-  |
  |   + Swarm Instr   |      +-------------------+      |   output/ or 07-  |
  |   (this dir)      |               |                 |   humanoid/paper/ |
  +-------------------+               |                 +-------------------+
                                      v                           |
                             +-------------------+                |
                             | physical-ai-      |                v
                             | oncology-trials   |      +-------------------+
                             | input files       |      |   7 Sequential    |
                             | (extra-hours      |      |   Commits in 1 PR |
                             | excluded in 07    |      |   on Clinical-AI- |
                             | v0.3.0)           |      |   Demos           |
                             +-------------------+      +-------------------+
                                       |
                  +--------------------+--------------------+
                  |                                         |
                  v                                         v
        +-------------------+                  +-------------------+
        | sponsor/, new-    |                  | competitions/     |
        | trial/, patient-  |                  | instructions/     |
        | journey/, etc.    |                  | chunking pattern  |
        +-------------------+                  +-------------------+
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
| 07 (v0.3.0) | 5 ms (swarm-wide) | 15 N per arm, 22 N cumulative cross-robot | 0.4 m handoff, 1.2 m rest | none |
| 08 | 100 ms | 20 N | n/a (1 humanoid) | gated by Safe Harbor |
| 09 | 5 ms | 22 N | 1.5 m | none |
| 10 | 100 ms | 12 N | n/a (1 humanoid) | none (edge LLM only) |

## Notes

- All prompts use single dashes only. No em dashes, no double dashes, no triple dashes in prose.
- ASCII diagrams cap at 80 columns by 60 lines per `competitions/instructions/ascii_diagram_guide.md`.
- All patient identifiers are synthetic. No real PHI is referenced.
- The seven-commit single-PR pattern is documented in `competitions/instructions/pr_workflow.md` of the companion repository.
- CI compliance: `ruff check`, `ruff format --check`, `yamllint -d relaxed .github/` must pass on Python 3.10, 3.11, and 3.12 before any prompt's output PR is merged.
- The 100 image instructions at `image-instruct/` use a shared color palette and DejaVu Sans typography. Single dashes only; section sign § for regulatory citations; no em dashes; no emoji; no dark mode; white facecolor for every PNG.
- The v0.3.0 swarm instructions at `07-humanoid/paper/instructions/` cite the author's prior FAERS LLM paper at DOI 10.5281/zenodo.18029100. The instruction tree excludes the `extra-hours/` dataset from the companion repository. 3 H2 humanoids per site (not 3 rotating across 4 sites; 12 H2 total). Camaraderie is the binding design property.
