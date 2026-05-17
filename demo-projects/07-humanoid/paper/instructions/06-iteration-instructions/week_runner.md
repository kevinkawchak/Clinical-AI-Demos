# Authoring Instructions for `src/week_runner.py`

The future session writes this Python module during Commit 4 of 7.

## Purpose

Orchestrates one 168-hour run of the 4-site network. Spawns 4 site processes in parallel, runs each for 604,800 LLM ticks, collects results, writes Parquet output.

## Key Behavior

- Uses `concurrent.futures.ProcessPoolExecutor` with `max_workers=4`.
- Each worker simulates one site for the full 168-hour window.
- Each worker holds 3 robot loops in-process, 1 LLM planner, 1 broadcaster, 1 dispatcher, 1 ingest of AE events.
- Output: 7 daily Parquet files (one per day) plus a hourly JSONL plus a per-iteration summary.

## Required Interfaces

```
class WeekRunner:
    def __init__(self, config_dir: pathlib.Path, iteration_id: int) -> None: ...
    def run(self) -> dict: ...
    def site_worker(self, site_id: str) -> dict: ...
```

## Suggested Skeleton

```
import concurrent.futures
import pathlib


class WeekRunner:
    def __init__(self, config_dir, iteration_id):
        self.config_dir = config_dir
        self.iteration_id = iteration_id

    def run(self):
        sites = ["SF-01", "SD-01", "BO-01", "AT-01"]
        results = {}
        with concurrent.futures.ProcessPoolExecutor(max_workers=4) as pool:
            futures = {pool.submit(self.site_worker, s): s for s in sites}
            for fut in concurrent.futures.as_completed(futures):
                site = futures[fut]
                results[site] = fut.result()
        return self._aggregate(results)

    def site_worker(self, site_id):
        # build site components: 3 robot loops, 1 LLM planner, 1 dispatcher, 1 broadcaster, ingest
        # tick 604,800 times at 1 Hz simulated
        # write per-day Parquet at end of each simulated day
        return {"site_id": site_id, "ticks": 604800}

    def _aggregate(self, results):
        return {"iteration_id": self.iteration_id, "sites": results}
```

## Validation Rules

- 4 sites simulated in parallel.
- 604,800 ticks per site.
- 7 daily Parquet files per site, partitioned by site and day.

## Notes

- The simulation uses simulated clock advancement; wall-clock time per run is around 15 minutes on a high-end server with 16 cores.
- For local testing, a `--fast` flag samples 1 hour instead of 168 hours.
