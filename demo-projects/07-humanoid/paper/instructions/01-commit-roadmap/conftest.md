# Authoring Instructions for `tests/conftest.py`

The future session writes this pytest configuration during Commit 6 of 7.

## Purpose

Shared fixtures across the pytest suite. Sets `sys.path` so `src/` modules are importable.

## Suggested Content

```
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

import pytest


@pytest.fixture(scope="session")
def instructions_root():
    return ROOT


@pytest.fixture(scope="session")
def site_ids():
    return ["SF-01", "SD-01", "BO-01", "AT-01"]


@pytest.fixture(scope="session")
def robot_ids():
    return [
        "SF-01-H2-A", "SF-01-H2-B", "SF-01-H2-C",
        "SD-01-H2-D", "SD-01-H2-E", "SD-01-H2-F",
        "BO-01-H2-G", "BO-01-H2-H", "BO-01-H2-I",
        "AT-01-H2-J", "AT-01-H2-K", "AT-01-H2-L",
    ]
```

## Validation Rules

- `sys.path` inserts the `src/` directory at the head.
- Session-scoped fixtures for site and robot IDs.

## Notes

- Pytest auto-discovers `conftest.py` and applies its fixtures to all tests in the package.
- This file is intentionally small.
