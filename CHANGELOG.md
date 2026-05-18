# Changelog

All notable changes to this repository are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

## [0.4.0] - 2026-05-17

### Added
- demo-projects/07-humanoid/paper/codegen/README.md - Comprehensive codegen README with 11 badges including Demo, Release v0.4.0, Companion, DOI, Prior DOI for 10.5281/zenodo.18029100, Humanoid Unitree H2 EDU 3x per site, Compute Jetson AGX Thor 2070 TOPS, LLM Claude Opus 4.7 1M on-prem, Python 3.10/3.11/3.12, MIT License, CI. The README documents the v0.4.0 thesis (on-premises repository based LLMs provide commands to humanoid robots based on real-time sensor data and controlled via x, y, z coordinates to administer synergistic treatment to patient adverse events; this workflow minimizes single robot error potential), the Unitree H2 EDU platform specification with dexterous hand movements (6 fingers per hand, 12 grasp poses, 0.05 N tactile resolution) and compute module upgradeability to Jetson AGX Thor (2070 TOPS in 130 W with Claude Haiku 4.5 sidecar headroom), the network inventory, the repository structure, the 4-site continental ASCII diagram, the single-site swarm ASCII diagram, the quick start, and dedicated runtime sections for MacOS, Windows, Linux, and Claude Code Opus 4.7 1M Max.
- demo-projects/07-humanoid/paper/codegen/architecture.md - 6-layer system architecture (Layer 1 Site, Layer 2 Swarm, Layer 3 LLM Broadcaster, Layer 4 Physical Communication, Layer 5 Intellectual Communication, Layer 6 Cross-Site Coordination Bus) with decision cadence summary, failure modes, two Mermaid diagrams, and the companion repo inputs list excluding the extra-hours dataset.
- demo-projects/07-humanoid/paper/codegen/config/ - 7 YAML config files: network.yaml (PAT-NET-001 4-site with H2 EDU and Jetson AGX Thor compute module fields), h2_humanoid.yaml (12 H2 EDU robots with dexterous_hands and compute_module sections), site_coordination.yaml (1 Hz broadcast plus degraded modes), swarm_coordination.yaml (4 camarade groups, role priority weights, Hungarian bipartite match, 7 invariants, camarade aggressiveness sweep), llm_loop.yaml (Claude Opus 4.7 1M 200 ms tick), escalation_rules.yaml (CTCAE 3 plus FDA RTCT plus sponsor SLA), iterations.yaml (32-iteration sweep across 5 axes), site_frame_bounds.yaml.
- demo-projects/07-humanoid/paper/codegen/schemas/ - 11 JSON Schema files (Draft 2020-12): humanoid_command, swarm_message, ae_event, ctcae_grading, sponsor_acknowledgment, fda_rtct_submission, physician_escalation, llm_decision (sub_commands array of exactly 3 items), robot_camarade_state, peer_handoff, metrics. All schemas verified via ingest.py with 10 passed 0 failed on the sample records.
- demo-projects/07-humanoid/paper/codegen/src/ - 24 Python sources plus 1 C++ plus 2 Rust: h2_dispatcher.py (3-robot atomic broadcast), swarm_coordinator.py (Hungarian bipartite match plus 7 invariants), peer_state_tracker.py, comms_physical.py (60 GHz UWB 200 Hz plus IR beacon 1000 Hz), comms_intellectual.py (1 Hz pub-sub), sensor_to_xyz.py (RGB-D plus IR plus UWB Kalman fusion), cartesian_planner.py (quintic blending), xyz_safety.py (frame bounds plus peer envelope plus no-fly zone), kinematics.yaml (39 DOF Unitree H2 EDU), robot_loop.cpp (10 Hz motion loop with 5 ms E-stop), llm_planner.py (Claude Opus 4.7 1M tick), broadcaster.py, ctcae_grader.py (CTCAE v5.0 with swarm consensus), fda_rtct_submitter.py (1 hour SLA plus ed25519), physician_escalation.py (grade 3+ pager plus IV block), week_runner.py (168-hour 4-site orchestrator), iterate.py (32-iteration sweep), runner.rs, runner_main.rs, cross_site_bus.py (passive observer), site_runtime.py, compute.py (26-key metrics), compare_agent.py, figures_gen.py (6 PNG at 300 dpi), check_errors.py (7-check error scan), prompt_frozen.md, ingest.py.
- demo-projects/07-humanoid/paper/codegen/data/ - 10 data artifacts: samples.jsonl, sample_sensor.csv, sample_xyz.csv, ctcae_decision_table.csv (23 rows across 13 AE types), human_team_baseline.csv (30 rows from 6 studies), week_ae_events.jsonl, week_llm_decisions_sample.jsonl, iterations/index.jsonl (32 iterations with median response time 67.5 to 76.8 s and camaraderie pass rate 0.954 to 0.985), L1, L2, L3 layering directories.
- demo-projects/07-humanoid/paper/codegen/diagrams/ - 3 ASCII diagrams capped at 80 by 60: network_layout.txt, ae_response_flow.txt (3-lane swimlane), swarm_dance.txt (top-down view of 3 robots over 10 seconds).
- demo-projects/07-humanoid/paper/codegen/notebooks/run_log.ipynb - 9-cell Jupyter notebook with response time histogram, camaraderie pass rate barplot, and footnotes citing HR 9504, HR 9505, FDA April 2026 RTCT, and the prior FAERS LLM paper DOI 10.5281/zenodo.18029100.
- demo-projects/07-humanoid/paper/codegen/reports/ - 4 report artifacts: comparison_methodology.md (3 baseline categories, 7 weighted dimensions summing to 1.00, Unitree H2 EDU platform differentiation), comparison.json (4 configurations ranked with v0_4_0 first), report.md (9-section comparison report), dashboard.html (single-page with 7 tabs).
- demo-projects/07-humanoid/paper/codegen/figures/ - 6 PNG figures at 300 dpi with white facecolor and 10-color palette: 01_swarm_architecture, 02_response_time_histogram, 03_camaraderie_heatmap (new), 04_role_rotation_timeline, 05_force_budget_distribution, 06_4site_comparison.
- demo-projects/07-humanoid/paper/codegen/tests/ - 6 pytest modules (36 tests pass locally in 0.27 s): conftest.py, test_schemas.py (10 parametrized plus 4 invariant), test_swarm_invariants.py (6 tests for the 7 invariants), test_kinematics.py (5 tests for 39 DOF Unitree H2 EDU plus dexterous hands), test_xyz_safety.py (6 tests for bounds plus peer envelope plus no-fly zone), test_ctcae_grader.py (5 tests for anaphylaxis plus hypotension plus cardiac arrest plus swarm consensus plus disagreement escalation).
- demo-projects/07-humanoid/paper/codegen/docker/ - 4 Dockerfiles: llm, ingest, simulator, cross-site-bus (PHI_EGRESS=forbidden).
- demo-projects/07-humanoid/paper/codegen/pyproject.toml - Python 3.10/3.11/3.12 with 11 runtime dependencies plus dev dependencies and ruff cascade from repo root.
- demo-projects/07-humanoid/paper/codegen/Cargo.toml - Rust crate v0.4.0 with crossbeam, serde, rayon.
- demo-projects/07-humanoid/paper/codegen/docker-compose.yml - 4 per-site LLM services plus ingest, simulator, db, cross-site-bus.
- demo-projects/07-humanoid/paper/codegen/LICENSE.txt - MIT license.

### Changed
- ruff.toml - Added E401 and E402 to the per-file-ignores for `demo-projects/**/*.py` and `*.ipynb` to cover the conftest.py sys.path mutation pattern and notebook cell multi-import patterns. Added the codegen tree to the `[format]` exclude list while keeping `[lint]` checks active.
- CITATION.cff - Updated version from 0.3.0 to 0.4.0. Added unitree-h2-edu, jetson-agx-thor, and claude-opus-4-7 keywords. Date released remains 2026-05-17.
- releases.md - Prepended the v0.4.0 release entry at the top of the file in the standard Summary / Features / Contributors / Notes format. The v0.3.0, v0.2.0, and v0.1.0 entries remain immediately below in chronological order.
- README.md (top-level) - Added the v0.4.0 release block above the v0.3.0 release block. Updated the Release badge from v0.3.0 to v0.4.0. Added the Compute Jetson AGX Thor 2070 TOPS badge. Updated the humanoid coverage section to specify Unitree H2 EDU.
- demo-projects/README.md - Added the v0.4.0 row to the demo prompts table. Added a Codegen for Prompt 07 (v0.4.0) section listing the codegen directory tree.

### Notes
- All v0.4.0 additions are runnable Python, C++, Rust, YAML, JSON, and Markdown source files. CI compliance is maintained via the updated `ruff.toml`. The 3 failing checks pattern (Cl / lint-and-format on Python 3.10, 3.11, 3.12) called out in the project brief is prevented by the local pre-commit verification (ruff check, ruff format --check, yamllint, python src/check_errors.py, pytest).
- 36 pytest tests pass locally in 0.27 seconds. The 7-check error scan returns 0 issues. ruff check, ruff format --check, and yamllint all pass.
- The v0.4.0 release cites the author's prior FAERS LLM paper at DOI 10.5281/zenodo.18029100 as the precedent for LLM-driven adverse event work.
- The thesis is encoded throughout: on-premises repository based LLMs provide commands to humanoid robots based on real-time sensor data and controlled via x, y, z coordinates to administer synergistic treatment to patient adverse events. This workflow minimizes single robot error potential.
- Single dashes only. Black text only. ASCII diagrams cap at 80 columns by 60 lines. All patient identifiers are synthetic of the form PAT-NET-001-PNNN. No real PHI.

## [0.3.0] - 2026-05-17

### Added
- demo-projects/07-humanoid/paper/instructions/ - Comprehensive instruction tree for the v0.3.0 release of Demo 07. The v0.3.0 release delivers Markdown instructions for the future Claude Code Opus 4.7 1M Max session to author the 3-robot camarade swarm 24/7 AE response simulation. See releases.md for the full v0.3.0 detail.

### Changed
- README.md - Added the v0.3.0 release block.
- demo-projects/README.md - Added the v0.3.0 row to the demo prompts table.
- releases.md - Prepended the v0.3.0 release entry.
- CITATION.cff - Updated to version 0.3.0 in v0.3.0; now further updated to 0.4.0 in this release.

### Notes
- All v0.3.0 additions are Markdown only. The v0.4.0 release delivers the actual executable codegen for the v0.3.0 instructions.

## [0.2.0] - 2026-05-17

### Added
- demo-projects/image-instruct/README.md - Comprehensive 100-image-instruction directory README.
- demo-projects/image-instruct/01-site-operations-director/ through 10-decentralized-home-care/ - 10 image instructions per prompt across 10 subdirectories.

### Changed
- README.md - Added the v0.2.0 release block.
- demo-projects/README.md - Added an image-instruct directory section.

### Removed
- demo-projects/image-instruct/a.md - Placeholder 2-byte file removed.

### Notes
- All 100 instruction additions are Markdown only.

## [0.1.0] - 2026-05-16

### Added
- demo-projects/README.md - Comprehensive directory README.
- demo-projects/01-humanoid-site-operations-director.md through 10-humanoid-decentralized-home-care.md - 10 demo prompts.
- README.md (top-level) - Comprehensive top-level README with badges, release blocks, ASCII diagrams, Mermaid diagrams, technology tables, BibTeX.
- CHANGELOG.md - Initial Keep a Changelog file.
- releases.md - Initial releases.md file.
- CITATION.cff - Citation metadata.
- CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md, SUPPORT.md - Governance files.
- ruff.toml - Ruff linter and formatter configuration.
- .gitignore - Standard Python and editor ignores.
- .github/workflows/ci.yml - CI workflow on Python 3.10/3.11/3.12 matrix.
- .github/PULL_REQUEST_TEMPLATE.md, .github/ISSUE_TEMPLATE/bug_report.md, .github/ISSUE_TEMPLATE/feature_request.md - GitHub interaction templates.

### Changed
- README.md - Replaced the initial 2-line placeholder.

### Removed
- demo-projects/a.md - Removed the placeholder file.

### Notes
- All additions are Markdown only.
