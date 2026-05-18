# Changelog

All notable changes to this repository are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

## [0.3.0] - 2026-05-17

### Added
- demo-projects/07-humanoid/paper/instructions/README.md - Comprehensive README for the v0.3.0 instruction tree. 9 badges, the v0.3.0 thesis statement, an inventory table with 14 properties, the directory structure, an ASCII diagram of the 4-site continental network with the central on-prem Claude Code compute bus, a Mermaid diagram for the single-site swarm, the future output footprint, and a BibTeX block citing the author's prior FAERS LLM work at DOI 10.5281/zenodo.18029100.
- demo-projects/07-humanoid/paper/instructions/00-project-overview/ - 6 foundation documents: architecture.md (6-layer system design from site to cross-site bus, decision cadence summary, failure modes, companion repo inputs minus the extra-hours dataset), swarm-overview.md (the 3 H2 camarade pattern with 3 named roles Lead Assist Reserve, 5-component priority score, physical and intellectual communication, 7 camaraderie invariants), thesis.md (8-section justification of on-prem repository-based LLMs commanding humanoid robots via x, y, z coordinates for synergistic treatment), working-memory-notes.md (168-hour window math, three-layer chunking strategy, commit processing rules, late commit memory pressure mitigations), camaraderie.md (concrete camaraderie expression across config, schemas, source code, iteration, comparison, diagrams, figures, reports, plus the one-sentence test), network-layout.txt (ASCII visualization of all 12 H2 humanoids across 4 swarms with their starting roles and 60 GHz UWB plus IR beacon physical channels).
- demo-projects/07-humanoid/paper/instructions/01-commit-roadmap/ - 12 documents: commit-roadmap.md (7-commit roadmap with file lists per commit), commit-6-error-scan.md (the 7-check error scan with schema field coverage, YAML config validation, cartesian frame bounds, robot ID coverage, ASCII diagram 80x60 cap, dash style, PHI absence), test_schemas.md plus test_swarm_invariants.md plus test_kinematics.md plus test_xyz_safety.md plus test_ctcae_grader.md (5 pytest module authoring instructions), conftest.md (pytest fixtures), site_frame_bounds.md (per-site cartesian bounds plus no-fly zones), check_errors_script.md (the standalone error scan script), ci_compliance_note.md (the 3-failing-checks fix pattern documented), ctcae_decision_table.md (CTCAE v5.0 vital threshold to grade mapping).
- demo-projects/07-humanoid/paper/instructions/02-config-instructions/ - 8 documents authoring 6 YAML config files plus pyproject.toml plus docker-compose.yml: network.yaml (PAT-NET-001 4-site definition with synthetic addresses, 200 enrolled patients, 12 H2 inventory, cross-site bus with phi_egress forbidden), h2_humanoid.yaml (12 robots tagged by camarade_group plus shared specs plus response kit plus starting roles), site_coordination.yaml (1 Hz broadcast with 3 fan-out and 3 ack targets, degraded modes for LLM/UWB/IR beacon down, cross-site summary with 9 de-identified fields, ed25519 signing per site), swarm_coordination.yaml (4 named camarade groups, 3 named roles, 5-component priority weights, Hungarian bipartite match, comms physical and intellectual, 7 invariants, camarade aggressiveness sweep, 1/2/3 robot down fallback), llm_loop.yaml (Claude Opus 4.7 1M on-prem at 1 Hz with 200 ms budget, 3 sub-command broadcast, world model fields, cross-site observation read-only at 1 hour cadence), escalation_rules.yaml (CTCAE grade 3+ escalation, FDA RTCT and sponsor 1 hour SLA, swarm fault for 1/2/3 robots down, perimeter breach, battery low at 25 percent), pyproject_toml.md (Python 3.10-3.12 with ruff cascade plus 11 runtime dependencies plus dev dependencies), docker_compose.md (4 per-site LLM services plus ingest plus simulator plus db plus cross-site-bus with phi_egress forbidden).
- demo-projects/07-humanoid/paper/instructions/03-schemas-instructions/ - 12 documents authoring the 10 JSON Schemas plus samples.jsonl plus ingest.py: humanoid_command (with peer_robot_ids array of exactly 2 entries plus audit chain plus synergy score), swarm_message (NEW, with 10 payload kinds for the camarade peer-to-peer channel), ae_event (with responding_swarm array of exactly 3 robot IDs), ctcae_grading (with grader enum including swarm_consensus), sponsor_acknowledgment (HR 9505 1 hour SLA), fda_rtct_submission (1 hour SLA plus hash chain plus ed25519 signature), physician_escalation (grade 3+ pager plus phone with 60 second ack), llm_decision (per-tick broadcast with exactly 3 sub_commands per record), robot_camarade_state (NEW, self plus 2 peers at 1 Hz), peer_handoff (NEW, 2 second SLA per hand-off).
- demo-projects/07-humanoid/paper/instructions/04-robotic-instructions/ - 8 documents: h2_dispatcher.md (3 sub-command atomic broadcast fan-out), swarm_coordinator.md (camaraderie logic, Hungarian bipartite match, 7 invariants check), robot_loop_cpp.md (10 Hz motion loop with 5 ms E-stop, cross-OS clang++ g++ MSVC build), comms_physical.md (60 GHz UWB at 200 Hz plus IR beacon at 1000 Hz with realistic latency and drop rate simulation), comms_intellectual.md (1 Hz pub-sub over the on-prem Claude Code compute fabric), peer_state_tracker.md (self plus 2 peer state with dead reckoning), ae_response_flow.txt.md (3-lane swimlane), swarm_dance.txt.md (NEW ASCII top-down view of 3 robots orbiting the patient bed), cargo_toml.md (Rust crate manifest).
- demo-projects/07-humanoid/paper/instructions/05-cartesian-instructions/ - 5 documents: kinematics.yaml.md (Unitree H2 39 DOF chain with DLS solver), sensor_to_xyz.md (RGB-D plus IR beacon plus UWB sensor projection into the shared site cartesian frame), cartesian_planner.md (quintic polynomial blending with 0.4 m hand-off plus 1.2 m rest distance envelope), xyz_safety.md (frame bounds plus patient envelope plus no-fly zone validation), sample_csvs.md (60-second illustrative sensor and xyz streams).
- demo-projects/07-humanoid/paper/instructions/06-iteration-instructions/ - 8 documents: iterations.yaml.md (32 iterations across 5 axes with Latin Hypercube Sampling, partitioned by site and day, L0/L1/L2/L3 layering), week_runner.md (concurrent.futures ProcessPoolExecutor with 4 site workers for the 168-hour window), iterate.md (32-iteration sweep with DuckDB aggregate), runner_rs.md (Rust crossbeam alternative), per_day_parquet.md (zstd level 3 compression with site plus day partitioning), aggregate_duckdb.md (7 aggregate tables for iterations and per_site and per_swarm and per_day and per_ae_type and camaraderie_invariants and handoffs), run_log_notebook.md (8-cell Jupyter notebook), run_log_record_layout.md (index.jsonl schema with 14 fields per iteration).
- demo-projects/07-humanoid/paper/instructions/07-llm-planner-instructions/ - 7 documents: llm_planner.md (per-tick Claude Opus 4.7 1M call returning the 3-sub-command llm_decision), broadcaster.md (atomic publish with 3 ack tracking and audit chain), shared_compute.md (the central on-prem Claude Code compute server as passive observer that never writes to robots), ctcae_grader.md (decision-table grading per robot plus swarm consensus majority with physician escalation on grade disagreement), fda_rtct_submitter.md (1 hour SLA enforcement with ed25519 signing), physician_escalation.md (CTCAE grade 3+ pager plus phone with 60 second ack and IV access block), architecture_summary.md (single-page module role table at multiple cadences).
- demo-projects/07-humanoid/paper/instructions/08-comparison-instructions/ - 10 documents: comparison_methodology.md (3 baseline categories plus 7 dimension weights including the new Camaraderie dimension), metrics_schema.md (26 keys with 4 new camaraderie keys), human_team_baseline.md (30-row 3-human-paramedic reference table), compute.md (per-iteration plus per-configuration plus ranking), compare_agent.md (LLM agent authoring the report narrative), prompt_frozen.md (locked system prompts for planner and comparison agent), report_markdown.md (Markdown report skeleton with Camaraderie section), dashboard_html.md (static HTML with 7 tabs), figures.md (6 PNG figures at 300 dpi including the new camaraderie_heatmap), comparison_json.md (machine-readable comparison output), h2_swarm_outcomes_parquet.md (per-AE outcome record across all 32 iterations).
- demo-projects/07-humanoid/paper/instructions/09-runtime-instructions/ - 3 documents: macos.md (Mac Studio M2 Ultra at 12 minute full run and 6.5 hour sweep), windows.md (Lenovo ThinkStation P8 at 5 hour sweep across 96 cores under PowerShell plus Visual Studio 2022), linux.md (Supermicro AS-2025HS-TNR at 4 hour sweep across 192 cores under Ubuntu 22.04/24.04).

### Changed
- README.md - Added the v0.3.0 release block above the v0.2.0 release block at the top of the README. Updated the Release badge from v0.2.0 to v0.3.0. Added the Prior DOI badge for 10.5281/zenodo.18029100. Added the `demo-projects/07-humanoid/paper/instructions/` subtree (with 11 named subdirectories) to the repository structure tree. Added the v0.3.0 box to the demo flow ASCII diagram. Updated the Mermaid repository topology diagram with the SW node and an excludes-extra-hours edge to the companion repo. Updated the Mermaid demo prompt execution loop with the SW input box. Updated the humanoid coverage section to clarify 3 H2 per site for prompt 07 in v0.3.0 (12 H2 total). Updated the documentation files index to include the v0.3.0 instructions README row. Updated the Citation section to include the prior FAERS LLM BibTeX entry at DOI 10.5281/zenodo.18029100. Updated the BibTeX software version from 0.2.0 to 0.3.0.
- demo-projects/README.md - Updated the Release badge from v0.2.0 to v0.3.0. Added a Swarm Instructions for Prompt 07 (v0.3.0) section that lists the directory tree and the 7-commit roadmap. Updated the file listing block to include the `07-humanoid/paper/instructions/` subdirectory.
- releases.md - Prepended the v0.3.0 release entry at the top of the file in the Summary / Features / Contributors / Notes format. The v0.2.0 and v0.1.0 entries remain immediately below in chronological order.
- CITATION.cff - Updated the version field from 0.2.0 to 0.3.0 and the date-released field to 2026-05-17.

### Notes
- All v0.3.0 additions are Markdown only at the time of this PR. No Python, no YAML source files, no JSON files outside Markdown code blocks. The CI lint-and-format workflow (ruff check, ruff format --check, yamllint -d relaxed .github/) on the Python 3.10 / 3.11 / 3.12 matrix remains green.
- The existing `ruff.toml` per-file-ignores entry `"demo-projects/**/*.py" = ["F401", "F402", "F821"]` covers the future generator source that the downstream Claude Code Opus 4.7 1M Max session will author under `demo-projects/07-humanoid/paper/instructions/src/`. The 3-failing-checks pattern (Cl / lint-and-format on Python 3.10, 3.11, 3.12) called out in the project brief is prevented by the markdown-only scope of this PR.
- The v0.3.0 release is built on a single PR with 7 sequential commits, authored autonomously without user interaction. Each commit is processed by Claude Code with the documented working-memory-notes pattern (three-layer chunking, per-commit size budget, no late-commit re-read of prior commits) to avoid context window truncation.
- The v0.3.0 release cites the author's prior FAERS LLM paper at DOI 10.5281/zenodo.18029100 as the precedent for LLM-driven adverse event work. The BibTeX entry is included in the top-level README.md Citation section, in the v0.3.0 instructions README.md, and referenced in the thesis and CTCAE grader instructions.
- The v0.3.0 release excludes the `extra-hours/` dataset (hour-56 through hour-83) from `kevinkawchak/physical-ai-oncology-trials/new-trial/national-24-7-trial/extra-hours/` from the future code generation inputs. Only `hour-00/` through `hour-55/` are read by the future session.
- The v0.3.0 release defines 3 Unitree H2 humanoids per site (not 3 rotating across 4 sites; 12 H2 humanoids total across the 4 PAT-NET-001 sites in San Francisco SF-01, San Diego SD-01, Boston BO-01, Atlanta AT-01).
- The thesis is the binding design property: On-premises repository based LLMs provide commands to humanoid robots based on real-time sensor data and controlled via x, y, z coordinates to administer synergistic treatment to patients adverse events. This workflow minimizes single robot error potential.
- Single dashes only throughout the instruction tree. Black text only. ASCII diagrams cap at 80 columns by 60 lines. All patient identifiers are synthetic of the form `PAT-NET-001-PNNN`. No real PHI.

## [0.2.0] - 2026-05-17

### Added
- demo-projects/image-instruct/README.md - Comprehensive 100-image-instruction directory README. Documents the fixed set of 10 chart types per prompt (3 landscape full-page: system architecture, operational timeline gantt, regulatory compliance heatmap; 7 portrait: value proposition canvas, financial waterfall, capability radar, sankey flow, process funnel, strategic quadrant, decision tree).
- demo-projects/image-instruct/01-site-operations-director/ through 10-decentralized-home-care/ - 10 image instructions per prompt across 10 subdirectories. See releases.md for the full v0.2.0 detail.

### Changed
- README.md - Added the v0.2.0 release block above the v0.1.0 release block.
- demo-projects/README.md - Added an image-instruct directory section.
- @kevinkawchak fixed README.md file ASCII diagrams in main/ on 2026-17-2026.

### Removed
- demo-projects/image-instruct/a.md - Placeholder 2-byte file removed in commit 101 of this PR before the v0.2.0 release.

### Notes
- All 100 instruction additions are Markdown only. No Python, YAML, or other CI-checked files are introduced. The lint-and-format CI workflow remains green.

## [0.1.0] - 2026-05-16

### Added
- demo-projects/README.md - Comprehensive directory README that ties the 10 standalone Claude Code task brief prompts together.
- demo-projects/01-humanoid-site-operations-director.md through 10-humanoid-decentralized-home-care.md - 10 demo prompts.
- README.md (top-level) - Comprehensive top-level README with badges, release blocks, ASCII diagrams, Mermaid diagrams, technology tables, BibTeX.
- CHANGELOG.md - Initial Keep a Changelog file with the [0.1.0] entry.
- releases.md - Initial releases.md file with the v0.1.0 release entry.
- CITATION.cff - Citation metadata in Citation File Format 1.2.0.
- CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md, SUPPORT.md - Governance files.
- ruff.toml - Ruff linter and formatter configuration.
- .gitignore - Standard Python and editor ignores.
- .github/workflows/ci.yml - CI workflow on Python 3.10/3.11/3.12 matrix.
- .github/PULL_REQUEST_TEMPLATE.md, .github/ISSUE_TEMPLATE/bug_report.md, .github/ISSUE_TEMPLATE/feature_request.md - GitHub interaction templates.

### Changed
- README.md - Replaced the initial 2-line placeholder with the full v0.1.0 comprehensive README.

### Removed
- demo-projects/a.md - Removed the placeholder file.

### Notes
- All additions are Markdown only. The lint-and-format CI workflow remains green.
