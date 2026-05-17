# Windows Runtime Instructions

This document describes how to run the generated code from `demo-projects/07-humanoid/paper/instructions/` on a leading high-end Windows server.

## Tested Hardware

- HP Z8 G5 Workstation (Intel Xeon W9-3495X, 56 cores, 512 GB DDR5)
- Dell Precision 7960 Tower (Intel Xeon w9-3475X, 36 cores, 256 GB DDR5)
- Lenovo ThinkStation P8 (AMD Threadripper PRO 7995WX, 96 cores, 1 TB DDR5)

## Prerequisites

```
# Install Python 3.10, 3.11, 3.12 from python.org or Microsoft Store
# Install Rust via rustup-init.exe from https://rustup.rs/
# Install Visual Studio 2022 with C++ Desktop Development workload
# Install CMake from https://cmake.org/download/
# Install Git for Windows
```

## PowerShell Setup

```
cd demo-projects\07-humanoid\paper\instructions
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Running One Iteration

```
python src\week_runner.py --iteration 0 --fast
```

Full 168-hour run:

```
python src\week_runner.py --iteration 0
```

Wall-clock time on Lenovo ThinkStation P8:

- `--fast` (1 hour): about 75 seconds
- Full 168 hours: about 10 minutes

## Running the 32-iteration Sweep

```
python src\iterate.py --config config\iterations.yaml
```

Wall-clock time on Lenovo ThinkStation P8: about 5 hours (parallelized across 96 cores).

## Building the Rust Runner

```
cargo build --release
.\target\release\runner.exe --iterations 32 --config-dir config
```

## Building the C++ Robot Loop

```
mkdir build
cd build
cmake -G "Visual Studio 17 2022" ..
cmake --build . --config Release --parallel
```

The binary lives at `build\Release\robot_loop.exe`.

## Generating the Report

```
jupyter nbconvert --execute notebooks\run_log.ipynb --to html --output reports\dashboard.html
python src\compute.py --aggregate data\aggregate.duckdb --out reports\comparison.json
python src\compare_agent.py --comparison reports\comparison.json --out reports\report.md
```

## CI Locally

```
ruff check . --output-format=github
ruff format --check .
yamllint -d relaxed .github/
pytest tests/
```

## Notes

- Use PowerShell 7.0 or higher. The `Activate.ps1` script requires PowerShell.
- Add Rust and CMake to PATH via the installer or manually.
- Long path support must be enabled (Group Policy or registry) to support deeply nested Parquet partitions.
- `duckdb` ships native Windows x86_64 wheels on PyPI.
