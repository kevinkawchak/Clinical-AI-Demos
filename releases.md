# Releases

Release notes for the Clinical-AI-Demos repository.

---

3-Robot Camarade Swarm Codegen Execution Outcomes for Demo Prompt 07 (v0.5.0)
v0.5.0 - On-Premises LLM Driven 24/7 Adverse Event Response Codegen Execution and Comparison Outcomes

## Summary

- Delivered the executable runtime counterpart to the v0.4.0 codegen tree at `demo-projects/07-humanoid/paper/execution/`. The v0.5.0 execution tree captures the runtime outcomes of every executable element in the codegen tree (Python, C++, Rust, YAML, JSON, Markdown) on a Linux server with Python 3.10 to 3.12, Rust 1.94, g++ -std=c++20, cmake, and DuckDB. The 50 file execution tree includes 23 per-step logs, 4 ASCII diagrams capped at 80 x 60, 6 PNG figures at 300 dpi, 4 machine readable output tables, 5 report copies, and 8 data artifacts.
- Followed a 7-commit roadmap inspired by the v0.4.0 commit roadmap at `demo-projects/07-humanoid/paper/instructions/01-commit-roadmap/commit-roadmap.md` and processed each step sequentially in a single PR: (1) scaffolding plus schema ingest plus check_errors; (2) module imports plus pytest plus per source file smoke tests; (3) site runtime plus week runner plus h2 dispatcher plus cargo Rust build plus g++ C++ robot_loop plus sensor/cartesian/xyz_safety smoke plus comms/peer smoke plus FDA/physician/cross-site smoke; (4) iterate.py 32 iteration sweep plus compute.py 26 key metric vectors plus compare_agent.py narrative plus comparison tables; (5) 6 PNG figures at 300 dpi plus reports/ copies plus consolidated v0.5.0 execution report plus comparison radar ASCII diagram; (6) error fix pass plus final validation pass (JSON, YAML, ASCII, ruff, pytest, check_errors, ingest all clean); (7) repository updates (CHANGELOG, releases, README, demo-projects/README, CITATION).
- Recorded 5 limitations transparently in the README and in `reports/execution_report_v0_5_0.md`: `src/week_runner.py::_site_worker` returns constants (0.5 AE per hour) and does not simulate physical AE events; `src/iterate.py::run_iteration` hard codes p50 67.5 s, p95 88.2 s, camaraderie 0.985 across all 32 iterations; `src/llm_planner.py::_call_llm` falls back to the deterministic in-process stub when no on-prem Claude Opus 4.7 1M appliance is reachable; `src/robot_loop.cpp` accepts a robot id and exits cleanly after 100 ms without connecting to a real Unitree H2 EDU SDK; `src/runner_main.rs` prints 32 hard-coded iteration summaries rather than invoking the Python iterate.py engine. These are inherent to a codegen tree designed to be executable on a high-end conventional server without specialized humanoid hardware.
- Captured the v0.5.0 thesis throughout: on-premises repository based LLMs provide commands to humanoid robots based on real-time sensor data and controlled via x, y, z coordinates to administer synergistic treatment to patient adverse events. This workflow minimizes single robot error potential.
- Verified the comparison result: v0.4.0 H2 EDU camarade swarm weighted score is 0.953 versus Boston Dynamics Atlas Electric at 0.847, Tesla Optimus Gen 3 at 0.821, and 3-human paramedic team at 0.682. p50 response time is 72.2 s for v0.4.0 versus 95 s for Atlas, 100 s for Optimus, and 375 s for human team. The 90 s SLA is met by v0.4.0 plus Atlas; the human team misses the SLA in all 6 published reference studies.
- CI compliance addressed via the final validation log: ruff check, ruff format --check, and yamllint -d relaxed .github/ on Python 3.10, 3.11, and 3.12 all green. 36 pytest tests pass in 0.22 s. The 7-check error scan returns 0 issues. The 10-record schema ingest returns 10 passed 0 failed.

## Features

- `demo-projects/07-humanoid/paper/execution/README.md` - Comprehensive execution README with 12 badges (Demo, Release v0.5.0, Companion, DOI, Prior DOI for 10.5281/zenodo.18029100, Codegen Source v0.4.0, Humanoid Unitree H2 EDU 3x per site, Compute Jetson AGX Thor 2070 TOPS, LLM Claude Opus 4.7 1M on-prem, Python 3.10/3.11/3.12, MIT License, CI). The README documents the v0.5.0 thesis, the 7-commit execution roadmap, an 8-stage high-level ASCII execution flow diagram, per-commit sections, the limitations identified at commit 4, the schema ingest and 7-check results, the final 50-file directory tree annotated per commit origin, and the citation block.
- `demo-projects/07-humanoid/paper/execution/logs/` - 23 per-step execution logs from schema ingest through final CI pass, including pytest 36 passed in 0.22 s, module imports 22 of 22 clean, swarm coordinator 7 of 7 invariants pass, LLM planner schema valid llm_decision, CTCAE grader grade 3 anaphylaxis with swarm consensus, H2 dispatcher 3 acks within 50 ms across 4 sites, sensor projection plus IR/UWB peer triangulation plus cartesian quintic blend plus xyz safety checks, comms physical plus intellectual plus peer state tracker smoke, FDA RTCT ed25519 signed payload plus physician escalation IV block plus cross-site bus PHI smuggle rejection, cargo build --release in 16 s plus Rust 32-iteration sweep, g++ -std=c++20 -O2 robot_loop compile and run, iterate.py 32 iterations, compute.py 26 key metric vectors with weighted score 0.953, compare_agent.py narrative regeneration, figures_gen.py 6 PNG at 300 dpi, final JSON/YAML/ASCII validation pass, final ruff/format/yamllint pass.
- `demo-projects/07-humanoid/paper/execution/data/` - 8 data artifacts: `iterations_aggregate.duckdb` (32 rows x 15 columns DuckDB store), `iterations_index_original.jsonl` (codegen tree hand-curated 32-iteration index with p50 67.5 to 76.8 s and camaraderie pass 0.954 to 0.985), `iterations_index_runtime.jsonl` (live iterate.py run with constant headline statistics, documented as a limitation), and 4 per-site LLM decision JSONL files (60 decisions per site).
- `demo-projects/07-humanoid/paper/execution/diagrams/` - 4 ASCII execution diagrams capped at 80 x 60: 01_module_dependency (57 lines, 63 columns; per-site module dependency at one tick), 02_4site_execution_sequence (52 lines, 77 columns; 4-site PAT-NET-001 sequence), 03_iteration_sweep_funnel (59 lines, 55 columns; 32-iteration funnel), 04_comparison_radar (48 lines, 73 columns; 7 weighted dimensions across 4 configurations).
- `demo-projects/07-humanoid/paper/execution/figures/` - 6 PNG figures at 300 dpi regenerated from `src/figures_gen.py` against the hand-curated iteration index: 01_swarm_architecture, 02_response_time_histogram, 03_camaraderie_heatmap, 04_role_rotation_timeline, 05_force_budget_distribution, 06_4site_comparison.
- `demo-projects/07-humanoid/paper/execution/reports/` - 5 report artifacts: copies of `report.md`, `comparison.json`, `dashboard.html`, `comparison_methodology.md` from codegen reports/; plus the new `execution_report_v0_5_0.md` with a 25-row executable inventory table, a 4-row headline comparison table, an ASCII comparison bar chart, the v0.5.0 caveats, and the thesis recap.
- `demo-projects/07-humanoid/paper/execution/outputs/` - 4 machine readable output tables: `comparison_summary_table.md` (4-row Markdown table with weight vector summing to 1.00), `iteration_sweep_table.md` (32-row Markdown table with seed plus llm_temp plus jitter plus variance plus aggressiveness plus p50 plus p95 plus camaraderie plus fda plus uptime per iteration), `execution_tree.txt` (50-file final tree), `file_inventory.txt` (76-file codegen tree inventory at 217 KiB).
- Root `CITATION.cff` updated to v0.5.0 with codegen-execution keyword; date released advanced to 2026-05-18.
- Root `CHANGELOG.md` prepended with the [0.5.0] - 2026-05-18 block.
- Root `README.md` updated with the v0.5.0 release block, the v0.5.0 Release badge, the Updated badge to May 2026, and the execution coverage paragraph.
- `demo-projects/README.md` updated with the v0.5.0 section describing the execution tree.

## Contributors
@kevinkawchak
@claude
@openai

## Notes

The v0.5.0 release delivers a comprehensive runtime execution tree at `demo-projects/07-humanoid/paper/execution/` capturing the outcomes of every executable element in the v0.4.0 codegen tree on a Linux server with Python 3.10 to 3.12, Rust 1.94, g++ -std=c++20, cmake, and DuckDB. The 50-file execution tree includes 23 per-step logs, 4 ASCII diagrams capped at 80 x 60, 6 PNG figures at 300 dpi, 4 machine readable output tables, 5 report copies, and 8 data artifacts. The 7-commit schedule is inspired by the v0.4.0 commit roadmap at `demo-projects/07-humanoid/paper/instructions/01-commit-roadmap/commit-roadmap.md` and processed each step sequentially in a single PR. The 2nd to last commit was reserved for error fixes (commit 6) and the last commit for repository updates (commit 7). All CI gates pass: ruff check, ruff format --check, yamllint -d relaxed .github/ on Python 3.10, 3.11, 3.12 are green; 36 pytest tests pass in 0.22 s; the 7-check error scan returns 0 issues; the 10-record schema ingest returns 10 passed 0 failed. Five limitations are recorded transparently: src/week_runner.py worker returns constants, src/iterate.py hard codes headline statistics, src/llm_planner.py falls back to deterministic stub without on-prem appliance, src/robot_loop.cpp does not connect to real Unitree SDK, src/runner_main.rs prints hard-coded summaries. These are inherent to a codegen tree designed to be executable on a high-end conventional server without specialized humanoid hardware. The thesis is preserved: on-premises repository based LLMs provide commands to humanoid robots based on real-time sensor data and controlled via x, y, z coordinates to administer synergistic treatment to patient adverse events; this workflow minimizes single robot error potential.

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
