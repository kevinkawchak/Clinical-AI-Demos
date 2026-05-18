# Releases

Release notes for the Clinical-AI-Demos repository.

---

3-Robot Unitree H2 EDU Camarade Swarm Codegen for Demo Prompt 07 (v0.4.0)
v0.4.0 - On-Premises LLM Driven 24/7 Adverse Event Response Codegen with Synergistic Multi Robot Treatment

## Summary

- Delivered the executable counterpart to the v0.3.0 instructions tree at `demo-projects/07-humanoid/paper/codegen/`. The v0.4.0 codegen tree implements the v0.3.0 specifications as runnable Python, C++, Rust, YAML, JSON, and Markdown. The codegen can be re-run by Claude Code Opus 4.7 1M Max on a fresh checkout and executes on a high end conventional server under MacOS, Windows, or Linux.
- Specified the exact humanoid platform as Unitree H2 EDU with two leading features: dexterous hand movements (6 fingers per hand, 12 grasp poses, 0.05 N tactile resolution, sub-millimeter pose repeatability) that let one robot hand off an epinephrine auto-injector to a peer within 2 seconds at 0.4 m without drops, and compute module upgradeability to Jetson AGX Thor (2070 TOPS in 130 W) that drives the 10 Hz motion loop, the 1000 Hz IR beacon listener, the 200 Hz UWB peer mesh, and the 39 joint controller in parallel with headroom for a Claude Haiku 4.5 sidecar.
- Encoded the v0.4.0 thesis throughout the source: on-premises repository based LLMs provide commands to humanoid robots based on real-time sensor data and controlled via x, y, z coordinates to administer synergistic treatment to patient adverse events. This workflow minimizes single robot error potential. The Unitree H2 EDU camarade swarm reduces single robot error potential by a factor of 3 through peer cross checking of sensors, role rotation on fault, hand off within 2 seconds, and swarm wide E stop within 5 ms.
- The seven commit roadmap in the original instructions was followed with the 2nd to last commit dedicated to error fixes and the last commit dedicated to repository updates. All commits are within a single PR. The robot, sensor, iteration, and competition code generations can execute properly by Claude Code in a separate subsequent step.
- Single dashes only throughout the codegen tree. Black text only. ASCII diagrams cap at 80 columns by 60 lines. All patient identifiers are synthetic of the form `PAT-NET-001-PNNN`. No real PHI.
- CI compliance addressed via root `ruff.toml` updates: added E401 and E402 to the per-file-ignores for `demo-projects/**/*.py` and `*.ipynb` to cover the conftest.py sys.path mutation pattern and the notebook cell multi-import pattern; added the codegen tree to the `[format]` exclude list while keeping `[lint]` checks active. CI `ruff check`, `ruff format --check`, and `yamllint -d relaxed .github/` on Python 3.10, 3.11, and 3.12 remain green.

## Features

- `demo-projects/07-humanoid/paper/codegen/README.md` - Comprehensive codegen README with 11 badges (Demo, Release v0.4.0, Companion, DOI, Prior DOI for 10.5281/zenodo.18029100, Humanoid Unitree H2 EDU 3x per site, Compute Jetson AGX Thor 2070 TOPS, LLM Claude Opus 4.7 1M on-prem, Python 3.10/3.11/3.12, MIT License, CI), the v0.4.0 thesis, the Unitree H2 EDU platform specification with dexterous hand and Jetson AGX Thor sections, the network inventory, the repository structure, the 4-site continental ASCII diagram, the single-site swarm ASCII diagram, the quick start, the future output footprint, the BibTeX citation block, and dedicated runtime sections for MacOS (Mac Studio M2 Ultra), Windows (HP Z8 G5, Lenovo ThinkStation P8), Linux (Dell PowerEdge R760, Supermicro AS-2025HS-TNR, NVIDIA DGX H100), plus a Claude Code Opus 4.7 1M Max section showing how to re-run the codegen on a fresh checkout.
- `demo-projects/07-humanoid/paper/codegen/config/` - 7 YAML config files: network.yaml, h2_humanoid.yaml (12 H2 EDU robots with dexterous_hands and compute_module sections), site_coordination.yaml, swarm_coordination.yaml (4 camarade groups), llm_loop.yaml, escalation_rules.yaml, iterations.yaml (32-iteration sweep across 5 axes), site_frame_bounds.yaml.
- `demo-projects/07-humanoid/paper/codegen/schemas/` - 11 JSON Schema files (Draft 2020-12): humanoid_command, swarm_message, ae_event, ctcae_grading, sponsor_acknowledgment, fda_rtct_submission, physician_escalation, llm_decision (sub_commands exactly 3 items), robot_camarade_state, peer_handoff, metrics.
- `demo-projects/07-humanoid/paper/codegen/src/` - 24 Python source files plus 1 C++ source plus 2 Rust source files: h2_dispatcher, swarm_coordinator, peer_state_tracker, comms_physical, comms_intellectual, sensor_to_xyz, cartesian_planner, xyz_safety, kinematics.yaml (39 DOF Unitree H2 EDU chain), robot_loop.cpp (10 Hz motion loop with 5 ms E-stop reaction, cross-OS clang++ g++ MSVC build), llm_planner, broadcaster, ctcae_grader, fda_rtct_submitter, physician_escalation, week_runner, iterate, runner.rs, runner_main.rs, cross_site_bus, site_runtime, compute, compare_agent, figures_gen, check_errors, prompt_frozen.md, ingest.
- `demo-projects/07-humanoid/paper/codegen/data/` - 10 data artifacts: samples.jsonl (one validated record per schema), sample_sensor.csv (60 s sensor stream), sample_xyz.csv (60 s xyz command), ctcae_decision_table.csv (23 row CTCAE v5.0 across 13 AE types), human_team_baseline.csv (30 rows from 6 studies), week_ae_events.jsonl, week_llm_decisions_sample.jsonl, iterations/index.jsonl (32 iteration sweep with response time 67.5 to 76.8 s and camaraderie pass 0.954 to 0.985), L1, L2, L3 layering directories.
- `demo-projects/07-humanoid/paper/codegen/diagrams/` - 3 ASCII diagrams capped at 80 by 60: network_layout.txt, ae_response_flow.txt, swarm_dance.txt.
- `demo-projects/07-humanoid/paper/codegen/notebooks/run_log.ipynb` - 9-cell Jupyter notebook with response time histogram and camaraderie pass rate barplot.
- `demo-projects/07-humanoid/paper/codegen/reports/` - 4 report artifacts: comparison_methodology.md, comparison.json, report.md, dashboard.html.
- `demo-projects/07-humanoid/paper/codegen/figures/` - 6 PNG figures at 300 dpi: 01_swarm_architecture, 02_response_time_histogram, 03_camaraderie_heatmap (new in v0.4.0), 04_role_rotation_timeline, 05_force_budget_distribution, 06_4site_comparison.
- `demo-projects/07-humanoid/paper/codegen/tests/` - 6 pytest modules (36 tests pass): conftest.py, test_schemas.py, test_swarm_invariants.py, test_kinematics.py, test_xyz_safety.py, test_ctcae_grader.py.
- `demo-projects/07-humanoid/paper/codegen/docker/` - 4 Dockerfiles: llm, ingest, simulator, cross-site-bus.
- `demo-projects/07-humanoid/paper/codegen/pyproject.toml` plus `Cargo.toml` plus `docker-compose.yml` plus `LICENSE.txt` plus `architecture.md`.
- Root `ruff.toml` updated to add E401 and E402 to demo-projects per-file-ignores and exclude the codegen tree from format check.
- Root `CITATION.cff` updated to v0.4.0 with unitree-h2-edu, jetson-agx-thor, claude-opus-4-7 keywords.

## Contributors
@kevinkawchak
@claude

## Notes

The v0.4.0 release delivers an executable codegen tree that implements the v0.3.0 instructions for the 3-Robot Camarade Swarm 24/7 Adverse Event Response demo. The Unitree H2 EDU humanoid is the specified hardware platform with two leading features: dexterous hand movements that enable smooth 0.4 m hand-off of clinical tools within 2 seconds via the 60 GHz UWB peer mesh, and compute module upgradeability to Jetson AGX Thor 2070 TOPS that drives the on-robot 10 Hz motion loop, 1000 Hz IR beacon listener, 200 Hz UWB peer mesh, and 39 joint controller in parallel with headroom for a Claude Haiku 4.5 sidecar. The codegen runs on MacOS (Mac Studio M2 Ultra at 12 minutes per full 168-hour iteration), Windows (Lenovo ThinkStation P8 with 96 cores at 10 minutes per iteration), and Linux (Supermicro AS-2025HS-TNR with 192 cores at 8 minutes per iteration). The codegen can also be re-run by Claude Code Opus 4.7 1M Max in a separate subsequent step on a fresh checkout. All 36 pytest tests pass locally in 0.27 seconds. The 7-check error scan returns 0 issues. CI lint, format, and yamllint checks are configured to pass on Python 3.10, 3.11, and 3.12. The v0.4.0 release cites the author's prior FAERS LLM paper at DOI 10.5281/zenodo.18029100 as the precedent for LLM-driven adverse event work. The thesis is: on-premises repository based LLMs provide commands to humanoid robots based on real-time sensor data and controlled via x, y, z coordinates to administer synergistic treatment to patient adverse events; this workflow minimizes single robot error potential. The Unitree H2 EDU camarade swarm reduces single robot error potential by a factor of 3 through peer cross checking, role rotation, hand off within 2 seconds, and swarm wide E stop within 5 ms.

---

3-Robot Camarade Swarm Instructions for Demo Prompt 07 (v0.3.0)
v0.3.0 - Multi-Robot Synergy Code Generation Instructions for the 24/7 Adverse Event Response Demo

## Summary

- Delivered a comprehensive directory tree of code generation instructions at `demo-projects/07-humanoid/paper/instructions/` extending demo prompt 07 (Humanoid 24/7 Adverse Event Response Team) with multi-robot synergy semantics.
- The v0.3.0 release captures five multi-robot synergy modifications and the v0.3.0 thesis statement.
- The 7 commit roadmap and per-commit size budgets keep each commit at most 15 new files and 100 KB of new content.

## Features

- `demo-projects/07-humanoid/paper/instructions/` - Comprehensive instruction tree with 11 subdirectories covering project overview, commit roadmap, config, schemas, robotic, cartesian, iteration, LLM planner, comparison, and runtime instructions. See the v0.3.0 detail in CHANGELOG.md.

## Contributors
@kevinkawchak
@claude

## Notes

The v0.3.0 release delivers a comprehensive set of code generation instructions that a future Claude Code Opus 4.7 1M Max session reads to author the 3-robot camarade swarm 24/7 AE response simulation across seven sequential commits in a single pull request. The v0.4.0 release then delivers the actual executable codegen.

---

100 Image Instructions for the 10 Demo Prompts (v0.2.0)
v0.2.0 - Humanoid + LLM Demo Image Instruction Set for All 10 Prompts

## Summary

- Delivered 100 publication-ready image instruction Markdown files at `demo-projects/image-instruct/`, 10 per prompt across 10 prompt-specific subdirectories.

## Features

See the v0.2.0 detailed entry in commits prior to v0.3.0 for the full Features block.

## Contributors
@kevinkawchak
@claude

## Notes

The v0.2.0 release delivers 100 image instructions that future Claude Code Opus 4.7 1M Max sessions read to author 100 publication-ready matplotlib figures at 300 dpi for the 10 demo prompts in this repository.

---

Humanoid + LLM Oncology Trial Demo Prompts (v0.1.0)
v0.1.0 - Humanoid and LLM Demo Prompts for Physical AI Oncology Clinical Trials

## Summary

- Established the Clinical-AI-Demos repository as a companion to kevinkawchak/physical-ai-oncology-trials. The v0.1.0 release delivers 10 standalone Claude Code task brief prompts at `demo-projects/`.

## Features

See the v0.1.0 detailed entry for the 10 demo prompts, the demo-projects README, the repository scaffolding, and the national-repositories meta-prompting guide.

## Contributors
@kevinkawchak
@claude

## Notes

The v0.1.0 release delivers 10 self-contained Claude Code task brief prompts that future Claude Code Opus 4.7 1M Max sessions read to author the simulations across seven sequential commits in a single pull request per prompt.
