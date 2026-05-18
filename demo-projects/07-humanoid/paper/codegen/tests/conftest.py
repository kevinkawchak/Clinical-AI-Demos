"""Shared pytest fixtures for the v0.4.0 codegen test suite."""

from __future__ import annotations

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

import pytest


@pytest.fixture(scope="session")
def instructions_root() -> pathlib.Path:
    return ROOT


@pytest.fixture(scope="session")
def site_ids() -> list[str]:
    return ["SF-01", "SD-01", "BO-01", "AT-01"]


@pytest.fixture(scope="session")
def robot_ids() -> list[str]:
    return [
        "SF-01-H2-A", "SF-01-H2-B", "SF-01-H2-C",
        "SD-01-H2-D", "SD-01-H2-E", "SD-01-H2-F",
        "BO-01-H2-G", "BO-01-H2-H", "BO-01-H2-I",
        "AT-01-H2-J", "AT-01-H2-K", "AT-01-H2-L",
    ]
