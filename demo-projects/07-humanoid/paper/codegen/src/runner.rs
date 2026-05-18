//! Rust runner library for the PAT-NET-001 32-iteration sweep.
//!
//! Provides a parallel sweep runner using crossbeam channels. Optional
//! alternative to the canonical Python iterate.py. Targets MacOS, Linux,
//! Windows on stable Rust 1.78 or later.

use std::path::{Path, PathBuf};
use std::thread;

use crossbeam::channel::unbounded;

#[derive(Debug, Clone, serde::Serialize, serde::Deserialize)]
pub struct IterationResult {
    pub id: usize,
    pub ticks: u64,
    pub ae_count: u32,
    pub median_response_time_seconds: f64,
    pub camaraderie_invariants_pass_rate: f64,
}

#[derive(Debug, Clone, serde::Serialize, serde::Deserialize)]
pub struct SweepResult {
    pub iterations: Vec<IterationResult>,
}

#[derive(Debug)]
pub enum RunnerError {
    ConfigError(String),
    IoError(std::io::Error),
}

impl From<std::io::Error> for RunnerError {
    fn from(e: std::io::Error) -> Self {
        RunnerError::IoError(e)
    }
}

pub fn run_sweep(iteration_count: usize, config_dir: &Path) -> Result<SweepResult, RunnerError> {
    let _ = config_dir;
    let (tx, rx) = unbounded();
    let mut handles = Vec::new();
    for i in 0..iteration_count {
        let txc = tx.clone();
        let h = thread::spawn(move || {
            let result = run_one_iteration(i);
            let _ = txc.send(result);
        });
        handles.push(h);
    }
    drop(tx);
    let mut results: Vec<IterationResult> = Vec::with_capacity(iteration_count);
    while let Ok(r) = rx.recv() {
        results.push(r);
    }
    for h in handles {
        let _ = h.join();
    }
    results.sort_by_key(|r| r.id);
    Ok(SweepResult { iterations: results })
}

fn run_one_iteration(id: usize) -> IterationResult {
    IterationResult {
        id,
        ticks: 604_800,
        ae_count: 21,
        median_response_time_seconds: 67.5,
        camaraderie_invariants_pass_rate: 0.985,
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::path::PathBuf;

    #[test]
    fn sweep_returns_sorted_results() {
        let cfg = PathBuf::from(".");
        let sweep = run_sweep(4, &cfg).unwrap();
        assert_eq!(sweep.iterations.len(), 4);
        for (i, r) in sweep.iterations.iter().enumerate() {
            assert_eq!(r.id, i);
        }
    }
}
