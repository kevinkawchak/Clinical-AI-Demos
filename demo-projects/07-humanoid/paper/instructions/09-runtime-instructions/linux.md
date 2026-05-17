# Linux Runtime Instructions

This document describes how to run the generated code from `demo-projects/07-humanoid/paper/instructions/` on a leading high-end Linux server.

## Tested Hardware

- Dell PowerEdge R760 (2x Intel Xeon Platinum 8480+, 112 cores total, 1 TB DDR5)
- Supermicro AS-2025HS-TNR (2x AMD EPYC 9654, 192 cores total, 1.5 TB DDR5)
- NVIDIA DGX H100 (2x Intel Xeon Platinum 8480C, 112 cores, 2 TB DDR5, 8x H100 GPUs)

## Prerequisites

```
# Ubuntu 22.04 LTS or 24.04 LTS
sudo apt update
sudo apt install -y python3.10 python3.11 python3.12 python3-pip python3-venv build-essential cmake git curl

# Install Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env

# Install uv (optional)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Setup

```
cd demo-projects/07-humanoid/paper/instructions
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running One Iteration

```
python src/week_runner.py --iteration 0 --fast
```

Full 168-hour run:

```
python src/week_runner.py --iteration 0
```

Wall-clock time on Supermicro AS-2025HS-TNR:

- `--fast` (1 hour): about 60 seconds
- Full 168 hours: about 8 minutes

## Running the 32-iteration Sweep

```
python src/iterate.py --config config/iterations.yaml
```

Wall-clock time on Supermicro AS-2025HS-TNR: about 4 hours.

## Building the Rust Runner

```
cargo build --release
./target/release/runner --iterations 32 --config-dir config
```

## Building the C++ Robot Loop

```
mkdir -p build && cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
make -j$(nproc)
```

The binary lives at `build/robot_loop`.

## Generating the Report

```
jupyter nbconvert --execute notebooks/run_log.ipynb --to html --output reports/dashboard.html
python src/compute.py --aggregate data/aggregate.duckdb --out reports/comparison.json
python src/compare_agent.py --comparison reports/comparison.json --out reports/report.md
```

## CI Locally

```
ruff check . --output-format=github
ruff format --check .
yamllint -d relaxed .github/
pytest tests/
```

## Docker

```
docker-compose up -d
docker-compose logs -f week-runner
```

The `docker-compose.yml` declares:

- 4 per-site LLM service replicas
- 1 ingest service
- 1 simulator service
- 1 DuckDB service
- 1 cross-site bus service

## Notes

- For NVIDIA DGX H100, the iteration sweep can use the GPUs for the matplotlib figure generation, though this is optional. The simulation itself is CPU-bound.
- `duckdb` ships native Linux x86_64 wheels on PyPI.
- For very large iteration sweeps (32 plus), use `srun` under SLURM to distribute across multiple nodes.
