//! Rust runner binary entry point.

use std::path::PathBuf;

use pat_net_001_runner::{run_sweep, RunnerError};

fn parse_args() -> (usize, PathBuf) {
    let mut iterations: usize = 32;
    let mut config_dir = PathBuf::from("config");
    let args: Vec<String> = std::env::args().collect();
    let mut i = 1;
    while i < args.len() {
        match args[i].as_str() {
            "--iterations" => {
                if i + 1 < args.len() {
                    iterations = args[i + 1].parse().unwrap_or(32);
                    i += 1;
                }
            }
            "--config-dir" => {
                if i + 1 < args.len() {
                    config_dir = PathBuf::from(&args[i + 1]);
                    i += 1;
                }
            }
            _ => {}
        }
        i += 1;
    }
    (iterations, config_dir)
}

fn main() -> Result<(), RunnerError> {
    let (iterations, config_dir) = parse_args();
    let sweep = run_sweep(iterations, &config_dir)?;
    println!(
        "completed {} iterations across the PAT-NET-001 4 sites",
        sweep.iterations.len()
    );
    for r in &sweep.iterations {
        println!(
            "iter {}: ticks={} ae_count={} p50_response_s={:.2} camaraderie_pass={:.3}",
            r.id, r.ticks, r.ae_count, r.median_response_time_seconds,
            r.camaraderie_invariants_pass_rate
        );
    }
    Ok(())
}
