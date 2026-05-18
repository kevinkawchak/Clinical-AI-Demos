# Authoring Instructions for `Cargo.toml`

The future session writes this Cargo manifest during Commit 3 of 7. Lives at the root of the instruction tree alongside `pyproject.toml`.

## Purpose

Declares the Rust crate for `src/runner.rs` (authored in commit 4).

## Content

```
[package]
name = "pat-net-001-runner"
version = "0.3.0"
edition = "2021"
license = "MIT"
authors = ["Kevin Kawchak <kevin@chemicalqdevice.com>"]
description = "Rust runner for PAT-NET-001 32-iteration sweep"

[dependencies]
crossbeam = "0.8"
parquet = "54"
arrow = "54"
serde = { version = "1", features = ["derive"] }
serde_json = "1"
rayon = "1.10"

[lib]
name = "pat_net_001_runner"
path = "src/runner.rs"
crate-type = ["rlib"]

[[bin]]
name = "runner"
path = "src/runner_main.rs"

[profile.release]
opt-level = 3
lto = true
codegen-units = 1
```

## Build Targets

- MacOS Intel: `cargo build --release --target x86_64-apple-darwin`
- MacOS Apple Silicon: `cargo build --release --target aarch64-apple-darwin`
- Linux x86_64: `cargo build --release --target x86_64-unknown-linux-gnu`
- Windows x86_64: `cargo build --release --target x86_64-pc-windows-msvc`

## Validation Rules

- `cargo check` passes with no warnings.
- `cargo clippy -- -D warnings` passes.
- `cargo fmt --check` passes.

## Notes

- Rust crate is optional. Pyhton iterate.py is canonical.
- The Cargo manifest is committed in commit 3 even though the source is committed in commit 4; this lets `cargo check` work after commit 3.
