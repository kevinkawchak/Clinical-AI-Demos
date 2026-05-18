# Authoring Instructions for `src/runner.rs`

The future session writes this Rust source during Commit 4 of 7.

## Purpose

A fast Rust-based parallel runner that can replace the Python `iterate.py` for production-scale iteration sweeps. Uses `crossbeam` for thread management and `parquet` for output. Optional; the Python version is the default.

## Build

- Cargo manifest at `Cargo.toml` (authored in commit 3).
- `cargo build --release`.
- Cross-platform: MacOS, Linux, Windows via stable Rust 1.78+.

## Required Interfaces

```
pub fn run_sweep(iteration_count: usize, config_dir: &Path) -> Result<SweepResult, RunnerError>;
pub struct SweepResult { ... }
pub enum RunnerError { ConfigError, IOError(std::io::Error), ParquetError }
```

## Suggested Skeleton

```
use std::path::Path;
use std::thread;
use crossbeam::channel::unbounded;

pub fn run_sweep(iteration_count: usize, config_dir: &Path) -> Result<SweepResult, RunnerError> {
    let (tx, rx) = unbounded();
    let mut handles = vec![];
    for i in 0..iteration_count {
        let txc = tx.clone();
        let h = thread::spawn(move || {
            let result = run_iteration(i);
            txc.send(result).ok();
        });
        handles.push(h);
    }
    drop(tx);
    let mut results = vec![];
    while let Ok(r) = rx.recv() {
        results.push(r);
    }
    for h in handles {
        h.join().ok();
    }
    Ok(SweepResult { iterations: results })
}

fn run_iteration(id: usize) -> IterationResult {
    IterationResult { id, ticks: 604_800 }
}
```

## Validation Rules

- Compiles under stable Rust on all 3 OS.
- `cargo clippy` passes with no warnings.
- `cargo fmt --check` passes.

## Notes

- Rust runner is optional for v0.3.0. The Python iterate.py is the canonical path.
- The 168-hour 32-iteration sweep takes about 8 hours in Python, around 2 hours in Rust on the same hardware.
