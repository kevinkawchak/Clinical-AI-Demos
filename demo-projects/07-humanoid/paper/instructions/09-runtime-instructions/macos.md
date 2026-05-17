# MacOS Runtime Instructions

This document describes how to run the generated code from `demo-projects/07-humanoid/paper/instructions/` on a leading high-end MacOS server.

## Tested Hardware

- Mac Studio M2 Ultra (24-core CPU, 60-core GPU, 192 GB unified memory)
- Mac Pro M2 Ultra (24-core CPU, 76-core GPU, 192 GB unified memory)
- MacBook Pro M3 Max (16-core CPU, 40-core GPU, 128 GB unified memory)

## Prerequisites

```
# Install Homebrew if not present
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python 3.10, 3.11, 3.12 and tools
brew install python@3.10 python@3.11 python@3.12 rust duckdb cmake

# Install uv for dependency management (optional but recommended)
brew install uv
```

## Setup

```
cd demo-projects/07-humanoid/paper/instructions
uv venv .venv --python 3.12
source .venv/bin/activate
uv pip install -r requirements.txt  # generated from pyproject.toml
```

The `requirements.txt` file is regenerated from `pyproject.toml` by the future session via `uv pip compile pyproject.toml -o requirements.txt`.

## Running One Iteration

```
python src/week_runner.py --iteration 0 --fast
```

The `--fast` flag runs a 1-hour subset instead of the full 168-hour window for smoke testing. Full run:

```
python src/week_runner.py --iteration 0
```

Wall-clock time on Mac Studio M2 Ultra:

- `--fast` (1 hour): about 90 seconds
- Full 168 hours: about 12 minutes

## Running the 32-iteration Sweep

```
python src/iterate.py --config config/iterations.yaml
```

Wall-clock time on Mac Studio M2 Ultra: about 6.5 hours.

## Building the Rust Runner

```
cargo build --release
./target/release/runner --iterations 32 --config-dir config
```

Wall-clock time: about 2 hours.

## Building the C++ Robot Loop

```
mkdir -p build && cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
cmake --build . --parallel
```

The binary lives at `build/robot_loop`. Run with `./build/robot_loop --robot-id SF-01-H2-A`.

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

## Notes

- The Apple Silicon Python build is recommended over Rosetta x86_64 for the iteration sweep; about 2.5x speed difference observed.
- `duckdb` ships native ARM64 wheels on PyPI.
- For C++ compile, install Xcode Command Line Tools (`xcode-select --install`).
