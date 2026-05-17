# Authoring Instructions for `src/iterate.py`

The future session writes this Python module during Commit 4 of 7.

## Purpose

Runs the 32-iteration sweep. Each iteration is a full `WeekRunner` run with one combination of (seed, LLM temperature, AE arrival jitter, response time variance, camarade aggressiveness).

## Key Behavior

- Reads `config/iterations.yaml`.
- Generates 32 parameter combinations via Latin Hypercube Sampling.
- Submits each combination to `WeekRunner`.
- Writes per-iteration Parquet plus a global index.
- Computes aggregate metrics in DuckDB at the end.

## Required Interfaces

```
def generate_lhs(axes: dict, n: int) -> list[dict]: ...
def run_iteration(iteration_id: int, params: dict) -> dict: ...
def build_index(results: list[dict], output_path: pathlib.Path) -> None: ...
def build_aggregate(results: list[dict], duckdb_path: pathlib.Path) -> None: ...
```

## Suggested Skeleton

```
import pathlib
import random


def generate_lhs(axes, n):
    # simple LHS: shuffle each axis values and zip
    combos = []
    shuffled = {}
    for axis_name, values in axes.items():
        repeated = (values * ((n + len(values) - 1) // len(values)))[:n]
        random.Random(42).shuffle(repeated)
        shuffled[axis_name] = repeated
    for i in range(n):
        combos.append({k: v[i] for k, v in shuffled.items()})
    return combos


def run_iteration(iteration_id, params):
    from week_runner import WeekRunner
    runner = WeekRunner(pathlib.Path("config"), iteration_id)
    return runner.run()


def build_index(results, output_path):
    import json
    with output_path.open("w") as f:
        for r in results:
            f.write(json.dumps(r) + "\n")


def build_aggregate(results, duckdb_path):
    import duckdb
    conn = duckdb.connect(str(duckdb_path))
    conn.execute("CREATE TABLE IF NOT EXISTS iterations (id INTEGER, ticks INTEGER, ae_count INTEGER, escalation_count INTEGER)")
    for r in results:
        conn.execute("INSERT INTO iterations VALUES (?, ?, ?, ?)", [r["iteration_id"], 604800, 0, 0])
```

## Validation Rules

- 32 iterations.
- Index file has 32 lines.
- DuckDB aggregate has 32 rows in the `iterations` table.

## Notes

- `duckdb` is the chosen in-process analytical store. It is lightweight and supports SQL on Parquet directly.
- The LHS generator is intentionally simple; production would use `scipy.stats.qmc.LatinHypercube`.
