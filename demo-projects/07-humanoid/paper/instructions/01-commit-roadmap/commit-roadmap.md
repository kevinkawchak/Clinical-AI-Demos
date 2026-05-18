# Seven Commit Roadmap (Future Code Generation PR)

The future Claude Code Opus 4.7 1M Max session executes these instructions in one Pull Request comprised of 7 sequential commits. Each commit must run autonomously without user interaction.

## Commit 1 of 7: Project Overview and Configuration

Files authored at `demo-projects/07-humanoid/paper/instructions/`:

- `README.md` (top-level project README for the generated code tree, separate from this instruction README)
- `architecture.md` (4-site Mermaid)
- `pyproject.toml` (Python 3.10/3.11/3.12 support, ruff configuration cascading)
- `docker-compose.yml` (4 per-site llm services, 1 ingest, 1 simulator, 1 db, 1 cross-site bus)
- `config/network.yaml`
- `config/h2_humanoid.yaml` (12 robots)
- `config/site_coordination.yaml`
- `config/swarm_coordination.yaml` (new)
- `config/llm_loop.yaml`
- `config/escalation_rules.yaml`
- `LICENSE.txt`
- `diagrams/network_layout.txt`

Approximately 12 files, less than 50 KB. Detailed authoring instructions in `02-config-instructions/`.

## Commit 2 of 7: Schemas and Sample Data

Files authored at `demo-projects/07-humanoid/paper/instructions/`:

- `schemas/humanoid_command.schema.json`
- `schemas/swarm_message.schema.json` (new)
- `schemas/ae_event.schema.json`
- `schemas/ctcae_grading.schema.json`
- `schemas/sponsor_acknowledgment.schema.json`
- `schemas/fda_rtct_submission.schema.json`
- `schemas/physician_escalation.schema.json`
- `schemas/llm_decision.schema.json` (3-sub-command broadcast)
- `schemas/robot_camarade_state.schema.json` (new)
- `schemas/peer_handoff.schema.json` (new)
- `data/samples.jsonl` (representative records covering all 10 schemas)
- `src/ingest.py` (validates records against the 10 schemas)

Approximately 12 files, less than 60 KB. Detailed authoring instructions in `03-schemas-instructions/`.

## Commit 3 of 7: Robotic, Cartesian, Iteration Source Files

Files authored at `demo-projects/07-humanoid/paper/instructions/`:

- `src/h2_dispatcher.py` (3-robot atomic broadcast dispatch)
- `src/swarm_coordinator.py` (camaraderie logic, role rotation, invariants checker)
- `src/peer_state_tracker.py` (3-entry peer state model)
- `src/comms_physical.py` (60 GHz UWB plus IR beacon)
- `src/comms_intellectual.py` (on-prem Claude Code compute fabric pub-sub)
- `src/sensor_to_xyz.py` (sensor reading to cartesian frame projection)
- `src/kinematics.yaml` (H2 kinematics chain shared across all 3 robots)
- `src/cartesian_planner.py` (cartesian command authoring helper)
- `src/robot_loop.cpp` (10 Hz motion loop, 5 ms E-stop, joint-level)
- `data/sample_sensor.csv` (60 seconds of sample sensor stream for 1 robot)
- `data/sample_xyz.csv` (60 seconds of sample xyz commands)
- `diagrams/ae_response_flow.txt` (3 lane swimlane)
- `diagrams/swarm_dance.txt` (camarade synchronization pattern)
- `Cargo.toml` (Rust runner.rs lives in commit 4 but Cargo manifest declared here)

Approximately 14 files, less than 70 KB. Detailed authoring instructions in `04-robotic-instructions/`, `05-cartesian-instructions/`, and `06-iteration-instructions/`.

## Commit 4 of 7: Week Runner, Iterations, LLM Planner

Files authored at `demo-projects/07-humanoid/paper/instructions/`:

- `src/llm_planner.py` (broadcast 3-sub-command per tick)
- `src/broadcaster.py` (publish to site bus)
- `src/ctcae_grader.py` (CTCAE v5.0 grading)
- `src/fda_rtct_submitter.py` (1-hour sponsor acknowledgment)
- `src/physician_escalation.py` (CTCAE 3+ escalation)
- `src/week_runner.py` (168-hour orchestrator, 4 sites parallel)
- `src/iterate.py` (concurrent.futures sweep)
- `src/runner.rs` (Rust crossbeam runner)
- `config/iterations.yaml` (5-dim sweep)
- `data/week_humanoid_commands_sample.parquet` (sampled to 5 MB)
- `data/week_ae_events.parquet`
- `data/week_llm_decisions_sample.jsonl` (sampled to 2 MB)
- `data/iterations/index.jsonl`
- `data/aggregate.duckdb`
- `notebooks/run_log.ipynb`

Approximately 15 files, less than 80 KB plus 5 MB Parquet. Detailed authoring instructions in `06-iteration-instructions/` and `07-llm-planner-instructions/`.

## Commit 5 of 7: Comparison Framework, Reports, Figures

Files authored at `demo-projects/07-humanoid/paper/instructions/`:

- `reports/comparison_methodology.md`
- `schemas/metrics.schema.json` (22 keys plus 4 camaraderie keys equals 26 keys)
- `data/human_team_baseline.csv` (30 rows from 6 published trial site AE response studies)
- `data/h2_swarm_outcomes.parquet`
- `src/compute.py`
- `src/compare_agent.py`
- `src/prompt_frozen.md`
- `reports/comparison.json`
- `reports/report.md`
- `reports/report.pdf`
- `reports/dashboard.html`
- `figures/01_swarm_architecture.png`
- `figures/02_response_time_histogram.png`
- `figures/03_camaraderie_heatmap.png`
- `figures/04_role_rotation_timeline.png`
- `figures/05_force_budget_distribution.png`
- `figures/06_4site_comparison.png`

Approximately 17 files, less than 60 KB Markdown plus about 10 MB PNG plus PDF. Detailed authoring instructions in `08-comparison-instructions/`.

## Commit 6 of 7: Error Fixes

This commit is designated for fixing all errors found in commits 1 through 5. The future session must run the following before committing:

- `ruff check . --output-format=github`
- `ruff format --check .`
- `yamllint -d relaxed .github/`
- `python -m json.tool` on every `.json` and `.schema.json`
- `python -c "import yaml; yaml.safe_load(open('config/X.yaml'))"` on every YAML
- 7-check error scan:
  1. All schema fields referenced in source code exist in the schema files
  2. All YAML configs validate against their schema definition
  3. All cartesian coordinates are within the per-site frame bounds
  4. All robot IDs in code match the 12 robots in `config/h2_humanoid.yaml`
  5. All ASCII diagrams cap at 80 by 60
  6. No file has em dashes, double dashes, or triple dashes in prose (markdown tables and standard markdown HR can use them)
  7. No file has PHI; all patient IDs are PAT-NET-001-PNNN

Files authored in commit 6:

- `src/check_errors.py` (the 7-check script)
- `tests/test_schemas.py` (pytest validating each schema against a sample record)
- `tests/test_swarm_invariants.py` (pytest validating the 7 camaraderie invariants)
- `tests/test_kinematics.py` (pytest validating H2 kinematics chain)

Approximately 4 files plus fixes to any prior commit file. Detailed authoring instructions in the parent README of `01-commit-roadmap/`.

## Commit 7 of 7: Repository Updates

The last commit updates the kevinkawchak/Clinical-AI-Demos repository-level files:

- Top-level `README.md`: add v0.3.0 release block, update repository structure tree to include `demo-projects/07-humanoid/paper/instructions/`, update Updated badge.
- `releases.md`: prepend a v0.3.0 release entry in the standard Summary / Features / Contributors / Notes format.
- `CHANGELOG.md`: prepend a `[0.3.0] - 2026-05-17` block above the `[0.2.0]` entry.
- `demo-projects/README.md`: add the v0.3.0 row to the demo prompts table, add a new section describing the instructions directory tree.

Approximately 4 files modified. Detailed authoring instructions in `10-repository-update-instructions/`.

## Commit Order and Idempotency

The 7 commits must be issued in the order above. Each commit must succeed and pass CI before the next is issued. If a commit fails CI, fix in commit 6 and skip ahead from there. Do not amend prior commits.

Every commit is idempotent within its scope. Re-running commit 1 re-authors the same 12 files. Re-running commit 6 re-runs the 7-check script and re-authors the test files.

## CI Compliance Per Commit

The CI workflow runs `ruff check`, `ruff format --check`, `yamllint -d relaxed .github/` on Python 3.10, 3.11, 3.12. All 7 commits must keep CI green. Specific patterns:

- Commit 1 to 3: mostly markdown, YAML, JSON. CI is naturally green.
- Commit 4 to 5: Python source. Must pass `ruff check` and `ruff format --check`. The repository-level `ruff.toml` per-file-ignores entry for `demo-projects/**/*.py` (F401, F402, F821) covers the demo source. If a new lint rule is triggered, add it to the per-file-ignores in commit 6.
- Commit 6: explicit lint and format pass. CI re-runs and stays green.
- Commit 7: documentation only. CI stays green.

## Branch and PR

Branch: `claude/demo-07-ae-swarm-shortid` (future code generation session). The present instructions PR is on branch `claude/adverse-event-instructions-Famwq`.

PR title: `Demo 07 v0.3.0: 3-Robot Camarade Swarm 24/7 AE Response`.

PR description: include the thesis, the 7 commit summary, the camaraderie invariants checklist, and the CI status. Reference the prior DOI 10.5281/zenodo.18029100 from the author's prior FDA AE LLM paper.
