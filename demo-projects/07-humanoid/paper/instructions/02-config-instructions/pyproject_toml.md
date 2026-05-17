# Authoring Instructions for `pyproject.toml`

The future session writes this file at the root of the instruction tree during Commit 1 of 7.

## Purpose

Declares Python project metadata, dependencies, and Ruff configuration that cascades from the repository root `ruff.toml`.

## Content

```
[project]
name = "pat-net-001-ae-swarm"
version = "0.3.0"
requires-python = ">=3.10,<3.13"
authors = [
  { name = "Kevin Kawchak", email = "kevin@chemicalqdevice.com" },
]
description = "PAT-NET-001 24/7 Camarade Swarm Adverse Event Response (Demo Prompt 07 v0.3.0)"
readme = "README.md"
license = { text = "MIT" }

dependencies = [
  "numpy>=1.26",
  "pandas>=2.2",
  "pyarrow>=15",
  "duckdb>=1.0",
  "jsonschema>=4.21",
  "pyyaml>=6",
  "matplotlib>=3.8",
  "jupyter>=1.0",
  "scipy>=1.12",
  "anthropic>=0.30",
  "cryptography>=42",
]

[project.optional-dependencies]
dev = [
  "ruff>=0.5",
  "yamllint>=1.35",
  "pytest>=8",
  "pytest-cov>=5",
]

[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[tool.ruff]
line-length = 120
target-version = "py310"
extend = "../../../../../ruff.toml"

[tool.pytest.ini_options]
testpaths = ["tests"]
minversion = "8.0"
addopts = "-q --strict-markers"
```

## Validation Rules

- `requires-python` covers 3.10, 3.11, 3.12.
- Ruff config cascades from the repo root.
- All dependencies pin minimum versions only (forward compatible).

## Notes

- The `extend = "../../../../../ruff.toml"` path goes up 5 levels from `demo-projects/07-humanoid/paper/instructions/` to the repo root where `ruff.toml` lives.
- `cryptography` is used for the ed25519 signing of FDA RTCT submissions.
- `anthropic` is the on-prem appliance API client.
