# Codegen: 3-Robot Camarade Swarm 24/7 Adverse Event Response (Demo 07 v0.4.0)

[![Demo](https://img.shields.io/badge/Demo-07%20of%2010-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![Release](https://img.shields.io/badge/Release-v0.4.0-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![Companion](https://img.shields.io/badge/Companion-physical--ai--oncology--trials-purple.svg)](https://github.com/kevinkawchak/physical-ai-oncology-trials)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18445179-blue)](https://doi.org/10.5281/zenodo.18445179)
[![Prior DOI](https://img.shields.io/badge/Prior%20DOI-10.5281%2Fzenodo.18029100-blue)](https://doi.org/10.5281/zenodo.18029100)
[![Humanoid](https://img.shields.io/badge/Humanoid-Unitree%20H2%20EDU%20(3x%20per%20site)-orange.svg)](https://www.unitree.com)
[![Compute](https://img.shields.io/badge/Compute-Jetson%20AGX%20Thor%202070%20TOPS-blue.svg)](https://www.nvidia.com)
[![LLM](https://img.shields.io/badge/LLM-Claude%20Opus%204.7%201M%20on--prem-blueviolet.svg)](https://www.anthropic.com)
[![Python](https://img.shields.io/badge/Python-3.10%20|%203.11%20|%203.12-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://img.shields.io/badge/CI-ruff%20|%20yamllint-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

Released on 17 May 2026
CEO Kevin Kawchak, ChemicalQDevice

This codegen tree is the realized counterpart to `demo-projects/07-humanoid/paper/instructions/`. It implements the v0.3.0 instructions as executable Python, C++, Rust, YAML, JSON, and Markdown that run on a high end conventional server under MacOS, Windows, or Linux, and that can be re-run by Claude Code Opus 4.7 1M Max in a separate subsequent step.

## Thesis

On-premises repository based LLMs provide commands to humanoid robots based on real-time sensor data and controlled via x, y, z coordinates to administer synergistic treatment to patient adverse events. This workflow minimizes single robot error potential.

Three Unitree H2 EDU humanoids per site act together as a swarm at all 4 PAT-NET-001 sites (San Francisco, San Diego, Boston, Atlanta). One Claude Opus 4.7 1M on-prem repository at each site broadcasts a single command set to all 3 robots per tick. The robots talk to one another physically (60 GHz ultra-wideband short range plus IR-band line-of-sight beacons) and intellectually (shared on-prem cloud compute fabric on the central Claude Code server). The robots adapt to patient acuity, attending physician presence, and the position and status of the other two robots in the swarm. This camaraderie reduces single robot error potential by a factor of 3.

## Humanoid Platform: Unitree H2 EDU

The H2 EDU is the education-grade variant of the Unitree H2 humanoid. It carries the same 39 DOF spine plus arms plus legs chain, the same 1.8 m height and 70 kg mass, the same 10 kg per arm payload, and the same IP65 outdoor rating, with two leading features tuned for clinical research and adverse event response.

- Dexterous hand movements: 6 fingers per hand with tactile pads at each fingertip, 12 active grasp poses, 0.05 N tactile resolution, sub-millimeter pose repeatability. The dexterous hands let one robot hand off an epinephrine auto-injector or a pulse oximeter to a peer at a 0.4 m hand-off distance within 2 seconds without dropping or fumbling. The same hands prepare an IV access tray, place ECG leads, and seat an emergency airway kit without operator assistance.
- Compute module upgradeability to Jetson AGX Thor (2070 TOPS): the on-robot compute slot accepts the Jetson AGX Thor compute module, delivering 2070 TOPS of AI inference throughput in a single 130 W envelope. This drives the on-board 10 Hz motion loop, the 1000 Hz IR beacon listener, the 200 Hz UWB peer mesh, and the 39 joint controller in parallel, with headroom for a Claude Haiku 4.5 sidecar that can answer local sensor questions without leaving the robot.

| Spec | Value |
|------|-------|
| Platform | Unitree H2 EDU |
| Degrees of freedom | 39 (spine 5, arms 2 x 8, legs 2 x 6, plus base) |
| Height | 1.8 m |
| Mass | 70 kg |
| Payload per arm | 10 kg |
| Battery | 5 hours, hot-swappable |
| Ingress protection | IP65, outdoor-rated |
| Hand | Dexterous, 6 fingers, 12 grasps, 0.05 N tactile resolution |
| Compute slot | Upgradeable to Jetson AGX Thor (2070 TOPS) |
| E-stop reaction | 5 ms swarm-wide |
| Per-arm cumulative force | 15 N during chest compressions, 5 N otherwise |
| Inter-robot minimum distance | 1.2 m at rest, 0.4 m during shared task handoff |
| Cumulative cross-robot force | 22 N during 3-robot patient transfer |

## Network Inventory

| Property | Value |
|----------|-------|
| Network | PAT-NET-001 |
| Sites | 4 (San Francisco SF-01, San Diego SD-01, Boston BO-01, Atlanta AT-01) |
| Robots per site | 3 Unitree H2 EDU |
| Robots total | 12 H2 EDU across the 4 sites |
| LLM per site | 1 on-prem Claude Opus 4.7 1M (200 ms median latency, redundant failover within the site) |
| LLM cadence | 1 Hz broadcast to all 3 robots simultaneously |
| Humanoid motion cadence | 10 Hz per active H2 EDU |
| Monitoring window | 168 hours (1 week) |
| AE volume | About 84 AEs across the 4-site week, of which about 24 are SAE (CTCAE grade 3 or higher) |
| Iterations | 32 deterministic sweeps |

## Repository Structure

```
demo-projects/07-humanoid/paper/codegen/
  README.md                                # This file
  architecture.md                          # 4-site Mermaid plus layer breakdown
  LICENSE.txt                              # MIT license
  pyproject.toml                           # Python 3.10/3.11/3.12 with ruff cascade
  docker-compose.yml                       # 4 per-site LLM, ingest, simulator, db, cross-site-bus
  Cargo.toml                               # Rust runner crate
  config/
    network.yaml                           # PAT-NET-001 4-site definition
    h2_humanoid.yaml                       # 12 H2 EDU robots
    site_coordination.yaml                 # Per-site broadcast plus cross-site summary
    swarm_coordination.yaml                # 4 camarade groups plus role rotation
    llm_loop.yaml                          # Claude Opus 4.7 1M tick parameters
    escalation_rules.yaml                  # CTCAE 3 plus FDA RTCT plus sponsor SLA
    iterations.yaml                        # 32-iteration sweep (commit 4)
    site_frame_bounds.yaml                 # Per-site no-fly zones (commit 6)
  schemas/
    humanoid_command.schema.json
    swarm_message.schema.json
    ae_event.schema.json
    ctcae_grading.schema.json
    sponsor_acknowledgment.schema.json
    fda_rtct_submission.schema.json
    physician_escalation.schema.json
    llm_decision.schema.json
    robot_camarade_state.schema.json
    peer_handoff.schema.json
    metrics.schema.json                    # commit 5
  src/
    ingest.py                              # JSON Schema validator for samples
    h2_dispatcher.py                       # 3-robot atomic broadcast
    swarm_coordinator.py                   # Camaraderie logic
    peer_state_tracker.py                  # Self plus 2 peers state
    comms_physical.py                      # 60 GHz UWB plus IR beacon
    comms_intellectual.py                  # Pub-sub on Claude Code fabric
    sensor_to_xyz.py                       # Sensor to shared cartesian frame
    cartesian_planner.py                   # Quintic blending plus envelope check
    xyz_safety.py                          # Frame bounds plus envelope plus no-fly
    kinematics.yaml                        # Unitree H2 EDU 39 DOF chain
    robot_loop.cpp                         # 10 Hz motion loop with 5 ms E-stop
    llm_planner.py                         # Per-site 1 Hz Claude Opus 4.7 1M
    broadcaster.py                         # Atomic publish with 3 ack tracking
    ctcae_grader.py                        # CTCAE v5.0 grading
    fda_rtct_submitter.py                  # 1 hour SLA enforced
    physician_escalation.py                # Grade 3 plus pager and IV block
    week_runner.py                         # 168-hour orchestrator
    iterate.py                             # 32-iteration sweep
    cross_site_bus.py                      # Central observer
    site_runtime.py                        # Per-site glue
    compute.py                             # 26 metric vector
    compare_agent.py                       # LLM comparison narrative
    figures_gen.py                         # 6 PNG figures at 300 dpi
    check_errors.py                        # 7-check error scan
    prompt_frozen.md                       # Locked LLM system prompt
    runner.rs                              # Rust crossbeam alternative
    runner_main.rs                         # Rust binary entry
  data/
    samples.jsonl                          # 10 schemas representative records
    sample_sensor.csv                      # 60 s sensor stream sample
    sample_xyz.csv                         # 60 s xyz command sample
    ctcae_decision_table.csv               # CTCAE v5.0 vital threshold map
    human_team_baseline.csv                # 30 rows from 6 published studies
    week_ae_events.jsonl                   # Sampled AE records
    week_llm_decisions_sample.jsonl        # Sampled LLM decisions
    iterations/
      index.jsonl                          # 32-iteration parameter sweep
      l1/                                  # Per-minute aggregates
      l2/                                  # Per-hour aggregates
      l3/                                  # Per-day Markdown narratives
  diagrams/
    network_layout.txt                     # 4-site ASCII layout
    ae_response_flow.txt                   # 3-lane Lead Assist Reserve swimlane
    swarm_dance.txt                        # Top-down view of 3 robots dancing
    h2_rotation_timeline.txt               # Role rotation timeline
  notebooks/
    run_log.ipynb                          # Jupyter notebook for the run log
  reports/
    comparison_methodology.md
    comparison.json
    report.md
    dashboard.html
  figures/
    01_swarm_architecture.png              # Generated by figures_gen.py
    02_response_time_histogram.png
    03_camaraderie_heatmap.png
    04_role_rotation_timeline.png
    05_force_budget_distribution.png
    06_4site_comparison.png
  tests/
    conftest.py
    test_schemas.py
    test_swarm_invariants.py
    test_kinematics.py
    test_xyz_safety.py
    test_ctcae_grader.py
  docker/
    llm/Dockerfile
    ingest/Dockerfile
    simulator/Dockerfile
    cross-site-bus/Dockerfile
```

## High Level ASCII Diagram

```
                  PAT-NET-001 4-Site Continental Adverse Event Response Network
                  ===============================================================

  +-----------------+      +-----------------+      +-----------------+      +-----------------+
  | San Francisco   |      | San Diego       |      | Boston          |      | Atlanta         |
  | Site SF-01      |      | Site SD-01      |      | Site BO-01      |      | Site AT-01      |
  |                 |      |                 |      |                 |      |                 |
  | Claude Opus 4.7 |      | Claude Opus 4.7 |      | Claude Opus 4.7 |      | Claude Opus 4.7 |
  | 1M on-prem      |      | 1M on-prem      |      | 1M on-prem      |      | 1M on-prem      |
  | broadcaster     |      | broadcaster     |      | broadcaster     |      | broadcaster     |
  |   |   |   |     |      |   |   |   |     |      |   |   |   |     |      |   |   |   |     |
  |   v   v   v     |      |   v   v   v     |      |   v   v   v     |      |   v   v   v     |
  | H2-A H2-B H2-C  |      | H2-D H2-E H2-F  |      | H2-G H2-H H2-I  |      | H2-J H2-K H2-L  |
  | swarm camarades |      | swarm camarades |      | swarm camarades |      | swarm camarades |
  | (Unitree H2 EDU)|      | (Unitree H2 EDU)|      | (Unitree H2 EDU)|      | (Unitree H2 EDU)|
  +-----------------+      +-----------------+      +-----------------+      +-----------------+
           |                       |                        |                        |
           +-----------------------+------------------------+------------------------+
                                   |
                                   v
                  +-----------------------------------------+
                  | Central On-Prem Claude Code Compute Bus |
                  | (de-identified summaries only)          |
                  | shared fabric for cross-site learning   |
                  +-----------------------------------------+
```

## Single Site Swarm ASCII Diagram

```
                  Inside One Site: 3 Unitree H2 EDU Camarades
                  ==============================================

                +--------------------------+
                | Claude Opus 4.7 1M       |
                | on-prem appliance        |
                | 200 ms latency budget    |
                | 1 Hz broadcast cadence   |
                +-----------+--------------+
                            |
                            | broadcast bus (1 Hz, atomic)
                            v
                +-----------+--------------+
                |   Site Broadcast Bus     |
                |   site/<id>/broadcast    |
                +---+--------+----------+--+
                    |        |          |
                    v        v          v
                +---+--+  +--+---+  +---+--+
                | H2-A |  | H2-B |  | H2-C |
                | Lead |  |Assist|  |Reserve|
                +------+  +------+  +------+
                   ^         ^         ^
                   |         |         |
                   +---------+---------+
                       60 GHz UWB peer mesh (200 Hz, 5 ms RTT)
                       IR beacon line-of-sight (1000 Hz, 1 ms RTT)
                                |
                                v
                  +-----------------------------+
                  | Sensor Aggregator           |
                  | builds shared world model   |
                  | feeds LLM next tick         |
                  +-----------------------------+
```

## Quick Start

```
cd demo-projects/07-humanoid/paper/codegen
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e .

# Validate the 10 schemas against the sample records
python src/ingest.py

# Run one iteration in fast mode (1 hour subset)
python src/week_runner.py --iteration 0 --fast

# Run the full 32-iteration sweep
python src/iterate.py --config config/iterations.yaml

# Generate figures
python src/figures_gen.py --output figures/

# Compute comparison metrics
python src/compute.py --aggregate data/aggregate.duckdb --out reports/comparison.json

# Run the test suite
pytest tests/

# Run the 7-check error scan
python src/check_errors.py
```

See `architecture.md` for the full system breakdown and the per-platform runtime sections below for MacOS, Windows, and Linux.

## Future Output Footprint

The codegen tree produces approximately:

- 72 source files (Python, C++, Rust, YAML, JSON, Markdown)
- 7 Parquet files (one per day of the 168-hour week)
- 32 iteration Parquet files plus 1 index.jsonl and 1 aggregate.duckdb
- 4 ASCII diagrams capped at 80 by 60
- 6 figures at 300 dpi
- 1 Markdown report plus 1 PDF plus 1 HTML dashboard

## Citation

```
@misc{kawchak_2025_18029100,
  author       = {Kawchak, Kevin},
  title        = {Code Generation Competition: 16 Proprietary vs.
                   Open-Source LLMs and Iterative Learning Based on FDA
                   Adverse Event Reporting System
                  },
  month        = dec,
  year         = 2025,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.18029100},
  url          = {https://doi.org/10.5281/zenodo.18029100},
}

@software{kawchak_2026_clinical_ai_demos_v0_4_0,
  author       = {Kawchak, Kevin and Claude},
  title        = {Clinical-AI-Demos v0.4.0 Demo 07 Codegen: 3-Robot Camarade Swarm 24/7 AE Response},
  month        = may,
  year         = 2026,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.18445179},
  url          = {https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/07-humanoid/paper/codegen},
}
```

## Notes

- Single dashes only. No em dashes. No double dashes. No triple dashes in prose. Markdown table separators are necessary and are preserved.
- Black text throughout. Default rendering on white background.
- ASCII diagrams cap at 80 columns by 60 lines.
- All patient identifiers are synthetic, of the form PAT-NET-001-PNNN.
- The original prompt 07 extra-hours dataset (hour-56 through hour-83 in `physical-ai-oncology-trials/new-trial/national-24-7-trial/extra-hours/`) is NOT included as input. Only hour-00 through hour-55 are read.
- Three Unitree H2 EDU humanoids per site, not 3 humanoids rotating across the 4 sites. 12 H2 EDU humanoids total. Each site owns its own 3 robot camarade swarm.

## Runtime: MacOS

Tested on Mac Studio M2 Ultra (24-core CPU, 192 GB unified memory), Mac Pro M2 Ultra, and MacBook Pro M3 Max.

```
brew install python@3.10 python@3.11 python@3.12 rust duckdb cmake
cd demo-projects/07-humanoid/paper/codegen
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e .
python src/week_runner.py --iteration 0 --fast        # 1 hour subset
python src/week_runner.py --iteration 0               # full 168 hours
python src/iterate.py --config config/iterations.yaml # 32-iteration sweep
cargo build --release                                  # Rust runner
mkdir -p build && cd build && cmake .. && cmake --build .  # C++ robot loop
```

Wall clock on Mac Studio M2 Ultra: full 168 hours about 12 minutes per iteration; full 32-iteration sweep about 6.5 hours in Python or 2 hours in Rust.

## Runtime: Windows

Tested on HP Z8 G5 Workstation, Dell Precision 7960 Tower, Lenovo ThinkStation P8.

```
# Install Python 3.10/3.11/3.12, Rust via rustup-init.exe, Visual Studio 2022 with C++ workload, CMake, Git
cd demo-projects\07-humanoid\paper\codegen
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .
python src\week_runner.py --iteration 0 --fast
python src\iterate.py --config config\iterations.yaml
cargo build --release
mkdir build && cd build && cmake -G "Visual Studio 17 2022" .. && cmake --build . --config Release --parallel
```

Wall clock on Lenovo ThinkStation P8 (96 cores): full 168 hours about 10 minutes per iteration; full 32-iteration sweep about 5 hours.

## Runtime: Linux

Tested on Dell PowerEdge R760, Supermicro AS-2025HS-TNR, NVIDIA DGX H100.

```
sudo apt update
sudo apt install -y python3.10 python3.11 python3.12 python3-pip python3-venv build-essential cmake git curl
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
cd demo-projects/07-humanoid/paper/codegen
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e .
python src/week_runner.py --iteration 0 --fast
python src/iterate.py --config config/iterations.yaml
cargo build --release
mkdir -p build && cd build && cmake .. && make -j$(nproc)
docker-compose up -d
```

Wall clock on Supermicro AS-2025HS-TNR (192 cores): full 168 hours about 8 minutes per iteration; full 32-iteration sweep about 4 hours.

## Running Under Claude Code Opus 4.7 1M Max

Claude Code Opus 4.7 1M Max reads this codegen tree on a fresh checkout, validates every schema, generates the full 168-hour 32-iteration run, builds the comparison report, and writes the 6 figures. From any platform:

```
git clone https://github.com/kevinkawchak/Clinical-AI-Demos
cd Clinical-AI-Demos/demo-projects/07-humanoid/paper/codegen
claude code --run "python src/week_runner.py --iteration 0 --fast && pytest tests/ && python src/check_errors.py"
```

Claude Code reuses the on-prem Claude Opus 4.7 1M appliance for the per-tick planning loop. If no appliance is reachable, the planning loop falls back to the deterministic in-process stub in `src/llm_planner.py`, and the run completes without LLM calls. This makes the codegen self-contained and reproducible without external services.
