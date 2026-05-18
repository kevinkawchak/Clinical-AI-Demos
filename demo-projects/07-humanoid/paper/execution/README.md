# Execution: 3-Robot Camarade Swarm Codegen Outputs (Demo 07 v0.5.0)

[![Demo](https://img.shields.io/badge/Demo-07%20of%2010-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![Release](https://img.shields.io/badge/Release-v0.5.0-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![Companion](https://img.shields.io/badge/Companion-physical--ai--oncology--trials-purple.svg)](https://github.com/kevinkawchak/physical-ai-oncology-trials)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18445179-blue)](https://doi.org/10.5281/zenodo.18445179)
[![Prior DOI](https://img.shields.io/badge/Prior%20DOI-10.5281%2Fzenodo.18029100-blue)](https://doi.org/10.5281/zenodo.18029100)
[![Codegen Source](https://img.shields.io/badge/Source-codegen%20v0.4.0-blueviolet.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/07-humanoid/paper/codegen)
[![Humanoid](https://img.shields.io/badge/Humanoid-Unitree%20H2%20EDU%20(3x%20per%20site)-orange.svg)](https://www.unitree.com)
[![Compute](https://img.shields.io/badge/Compute-Jetson%20AGX%20Thor%202070%20TOPS-blue.svg)](https://www.nvidia.com)
[![LLM](https://img.shields.io/badge/LLM-Claude%20Opus%204.7%201M%20on--prem-blueviolet.svg)](https://www.anthropic.com)
[![Python](https://img.shields.io/badge/Python-3.10%20|%203.11%20|%203.12-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://img.shields.io/badge/CI-ruff%20|%20yamllint-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

Released on 18 May 2026
CEO Kevin Kawchak, ChemicalQDevice

This execution tree captures the runtime outcomes of the v0.4.0 codegen at `demo-projects/07-humanoid/paper/codegen/`. Each file in the codegen tree (Python, C++, Rust, YAML, JSON, Markdown) is exercised on a Linux server, and the captured logs, tables, figures, and ASCII diagrams are written here as a basis for a future technical paper.

## Thesis

On-premises repository based LLMs provide commands to humanoid robots based on real-time sensor data and controlled via x, y, z coordinates to administer synergistic treatment to patient adverse events. This workflow minimizes single robot error potential.

## Initial Scaffolding (Commit 1 of 7)

This first commit establishes the execution scaffolding:

- Directory tree under `execution/` with `logs/`, `outputs/`, `figures/`, `reports/`, `diagrams/`, `data/`.
- Initial schema ingest validator log (`logs/01_schema_ingest.log`).
- Initial 7-check error scan log (`logs/02_check_errors.log`).
- Removal of placeholder `a.md`.

Subsequent commits populate this tree with full per-module execution logs, the iteration sweep outputs, the 6 generated figures, the comparison report copies, and the final cross-referenced documentation. The 2nd to last commit is reserved for error fixes; the last commit is reserved for repository-level updates.

## Module Imports + Pytest + Source Smoke Tests (Commit 2 of 7)

This commit captures the per source file unit level execution evidence:

- `logs/03_pytest.log`: 36 pytest tests pass in 0.22 s across `test_ctcae_grader`, `test_kinematics`, `test_schemas`, `test_swarm_invariants`, `test_xyz_safety`.
- `logs/04_module_imports.log`: 22 of 22 Python source modules import clean. Symbol sample logged per module.
- `logs/05_swarm_coordinator_smoke.log`: SwarmCoordinator Hungarian bipartite role assignment for SF-01 yields Lead, Assist, Reserve; synergy score 1.000; 7 of 7 camaraderie invariants pass.
- `logs/06_llm_planner_smoke.log`: LLMPlanner fallback stub for SF-01 tick 42 emits a schema valid llm_decision with 3 sub commands and SHA-256 audit chain prev hash.
- `logs/07_ctcae_grader_smoke.log`: CTCAEGrader v5.0 grades anaphylaxis grade 3, hypotension grade 2, cardiac arrest grade 5; swarm consensus across 3 robots agrees on grade 3 anaphylaxis.
- `logs/08_h2_dispatcher_smoke.log`: H2Dispatcher fan-out for SF-01 produces 3 humanoid_command records (Lead, Assist, Reserve) with peer_robot_ids and audit chain extended; 3 acks collected within 50 ms.
- `outputs/file_inventory.txt`: 76 source files at 217 KiB, bucketed by directory (config, data, diagrams, docker, notebooks, reports, schemas, src, tests, root).
- `diagrams/01_module_dependency.txt`: per site module dependency at one tick (1 Hz) ASCII diagram, 57 lines x 63 columns.

## Site Runtime + Week Runner + Cross Toolchain Runs (Commit 3 of 7)

This commit captures the 4-site site_runtime, week_runner orchestrator, h2_dispatcher init for the 12-robot roster, cargo Rust build with the 32-iteration runner, and the g++ compiled C++ robot_loop for 3 robots.

- `logs/09_site_runtime_4site.log`: 1 hour fast mode for each of SF-01, SD-01, BO-01, AT-01 (240 LLM decisions total, 60 per site). Audit chain head per site is a unique SHA-256 hash, demonstrating that the per site chain is independent.
- `data/site_runtime_runs/SF-01_llm_decisions.jsonl` through `AT-01_llm_decisions.jsonl`: the 4 per-site llm_decision streams (60 records per site, schema valid). Each record contains exactly 3 sub_commands (Lead, Assist, Reserve).
- `logs/10_h2_dispatcher_init.log`: dispatcher init for all 4 sites. Rosters: SF-01 [H2-A, H2-B, H2-C], SD-01 [H2-D, H2-E, H2-F], BO-01 [H2-G, H2-H, H2-I], AT-01 [H2-J, H2-K, H2-L]. 12 robots total across 4 sites.
- `logs/11_week_runner_fast.log`: week_runner fast mode result. 3,600 ticks per site (1 hour), 4 sites in parallel via concurrent.futures.ProcessPoolExecutor.
- `logs/12_sensor_xyz_safety_smoke.log`: sensor_to_xyz depth projection, IR plus UWB peer triangulation, cartesian_planner quintic blend with 21 trajectory steps; xyz_safety frame bounds, no fly zone, peer 2 second envelope checks.
- `logs/13_comms_peer_smoke.log`: comms_physical 60 GHz UWB and IR beacon channel sends; comms_intellectual pub-sub on Claude Code fabric; peer_state_tracker 3-entry snapshot (self plus 2 peers).
- `logs/14_fda_phys_xsite_smoke.log`: FDA RTCT submission with ed25519 signed payload and 1 hour SLA met; physician escalation triggered for CTCAE grade 3 anaphylaxis with IV access block; cross_site_bus accepts a clean hourly summary and rejects a PHI smuggle attempt with the `patient_id` field set.
- `logs/15_cargo_build.log`: `cargo build --release` completes in 16 s, generating the optimized Rust binary.
- `logs/16_rust_runner.log`: Rust runner sweeps 32 iterations across 4 sites. Each iteration reports ticks 604,800 (168 hours), ae_count 21, p50 response 67.50 s, camaraderie pass 0.985.
- `logs/17_cpp_robot_loop.log`: g++ -std=c++20 -O2 compiles `src/robot_loop.cpp` and the binary runs for each of SF-01-H2-A, SF-01-H2-B, SF-01-H2-C.
- `diagrams/02_4site_execution_sequence.txt`: 4-site execution sequence diagram (capped at 80 x 60).

## Schema Ingest Result (Commit 1 of 7)

```
Records passed: 10
Records failed: 0
```

All 10 sample records validate against their corresponding JSON Schema (Draft 2020-12). Schemas covered: humanoid_command, swarm_message, ae_event, ctcae_grading, sponsor_acknowledgment, fda_rtct_submission, physician_escalation, llm_decision, robot_camarade_state, peer_handoff.

## 7-Check Error Scan Result (Commit 1 of 7)

```
OK: 0 issues across 7 checks
```

Checks performed by `src/check_errors.py`:

1. All schema fields referenced in source code exist in the schema files.
2. All YAML configs validate against their schema definition.
3. All cartesian coordinates are within the per-site frame bounds.
4. All robot IDs in code match the 12 robots in `config/h2_humanoid.yaml`.
5. All ASCII diagrams cap at 80 by 60.
6. No file has em dashes, double dashes, or triple dashes in prose.
7. No file has PHI; all patient IDs are PAT-NET-001-PNNN.

## Initial Directory Layout

```
demo-projects/07-humanoid/paper/execution/
  README.md                   # This file
  logs/                       # Per-step execution logs (populated across commits 1-5)
    01_schema_ingest.log      # 10 passed, 0 failed
    02_check_errors.log       # 0 issues across 7 checks
  outputs/                    # Machine readable run outputs (populated commits 2-5)
  figures/                    # 6 PNG figures at 300 dpi (populated commit 5)
  reports/                    # Comparison and dashboard copies (populated commit 5)
  diagrams/                   # ASCII execution diagrams (populated commits 1-5)
  data/                       # Iteration index copies and tables (populated commit 4)
```

## High Level Execution Flow

```
        +---------------------------------------------------+
        | Codegen tree (paper/codegen/)                     |
        | 76 source files: Python, C++, Rust, YAML, JSON    |
        +-------------------------+-------------------------+
                                  |
                                  v
        +-------------------------+-------------------------+
        | Stage 1: Schema validation (commit 1)             |
        | python src/ingest.py                              |
        | 10 records / 10 schemas / 0 failures              |
        +-------------------------+-------------------------+
                                  |
                                  v
        +-------------------------+-------------------------+
        | Stage 2: 7-check error scan (commit 1)            |
        | python src/check_errors.py                        |
        | 0 issues across 7 checks                          |
        +-------------------------+-------------------------+
                                  |
                                  v
        +-------------------------+-------------------------+
        | Stage 3: Per module unit execution (commit 2)     |
        | pytest tests/  -> 36 tests pass                   |
        | per-source module import + smoke run              |
        +-------------------------+-------------------------+
                                  |
                                  v
        +-------------------------+-------------------------+
        | Stage 4: Site runtime + week runner (commit 3)    |
        | 4 sites x 60 ticks x audit chain hash             |
        +-------------------------+-------------------------+
                                  |
                                  v
        +-------------------------+-------------------------+
        | Stage 5: 32 iteration sweep + compute (commit 4)  |
        | python src/iterate.py + python src/compute.py     |
        +-------------------------+-------------------------+
                                  |
                                  v
        +-------------------------+-------------------------+
        | Stage 6: Figures + comparison (commit 5)          |
        | 6 PNG at 300 dpi + reports/ copies                |
        +-------------------------+-------------------------+
                                  |
                                  v
        +-------------------------+-------------------------+
        | Stage 7: Error fix pass (commit 6)                |
        | ruff check + ruff format + yamllint               |
        +-------------------------+-------------------------+
                                  |
                                  v
        +-------------------------+-------------------------+
        | Stage 8: Repo updates (commit 7)                  |
        | README, CHANGELOG.md, releases.md (v0.5.0)        |
        +---------------------------------------------------+
```

## Citation

```
@software{kawchak_2026_clinical_ai_demos_v0_5_0,
  author       = {Kawchak, Kevin and Claude and OpenAI},
  title        = {Clinical-AI-Demos v0.5.0 Demo 07 Execution: 3-Robot Camarade Swarm Codegen Run Outputs},
  month        = may,
  year         = 2026,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.18445179},
  url          = {https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/07-humanoid/paper/execution},
}
```

## Notes

- Single dashes only. No em dashes. No double dashes. No triple dashes in prose.
- Black text only. Default rendering on white background.
- ASCII diagrams cap at 80 columns by 60 lines.
- All patient identifiers are synthetic, of the form PAT-NET-001-PNNN.
- The execution outputs are derived from the v0.4.0 codegen tree at `demo-projects/07-humanoid/paper/codegen/` and never modify codegen source.
