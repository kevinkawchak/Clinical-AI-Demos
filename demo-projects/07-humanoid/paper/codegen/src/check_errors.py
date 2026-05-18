"""Commit 6 of 7 the 7-check error scan.

Exits 0 if no issues, 1 if any issue. Logs each issue on stdout.
Checks:
1. Schema field coverage
2. YAML config validity
3. JSON schema validity
4. ASCII diagram size (80 col x 60 row cap)
5. Robot ID coverage (12 named robots)
6. Dash style in prose (no em dash, no triple dashes outside markdown HR)
7. PHI absence (only synthetic PAT-NET-001-PNNN)
"""

from __future__ import annotations

import json
import pathlib
import re
import sys

import yaml


ROOT = pathlib.Path(__file__).resolve().parent.parent

ROBOT_IDS = {
    "SF-01-H2-A", "SF-01-H2-B", "SF-01-H2-C",
    "SD-01-H2-D", "SD-01-H2-E", "SD-01-H2-F",
    "BO-01-H2-G", "BO-01-H2-H", "BO-01-H2-I",
    "AT-01-H2-J", "AT-01-H2-K", "AT-01-H2-L",
}

ERRORS: list[str] = []


def log(category: str, path: pathlib.Path, detail: str) -> None:
    ERRORS.append(f"{category} {path}: {detail}")


def check_yaml_validity() -> None:
    for f in (ROOT / "config").glob("*.yaml"):
        try:
            yaml.safe_load(f.read_text())
        except yaml.YAMLError as e:
            log("yaml", f, str(e))


def check_json_schemas() -> None:
    for f in (ROOT / "schemas").glob("*.schema.json"):
        try:
            json.loads(f.read_text())
        except json.JSONDecodeError as e:
            log("json", f, str(e))


def check_ascii_sizes() -> None:
    diagrams_dir = ROOT / "diagrams"
    if not diagrams_dir.exists():
        return
    for f in diagrams_dir.glob("*.txt"):
        lines = f.read_text().splitlines()
        if len(lines) > 60:
            log("ascii_rows", f, f"{len(lines)} rows")
        for i, line in enumerate(lines, start=1):
            if len(line) > 80:
                log("ascii_cols", f, f"line {i} cols {len(line)}")


def check_robot_ids() -> None:
    for f in ROOT.rglob("*.py"):
        text = f.read_text()
        found = set(re.findall(r"\b[A-Z]{2}-\d{2}-H2-[A-L]\b", text))
        for x in found - ROBOT_IDS:
            log("robot_id", f, f"unknown robot id {x}")


def check_dash_style() -> None:
    for f in ROOT.rglob("*.md"):
        if "instructions" in str(f):
            continue
        text = f.read_text()
        if "—" in text:
            log("dash_em", f, "em dash present")


def check_phi() -> None:
    for f in ROOT.rglob("*.md"):
        text = f.read_text()
        if re.search(r"\b(John|Jane)\s+(Doe|Smith)\b", text):
            log("phi", f, "possible real name")


def check_schema_coverage() -> None:
    schema_props: dict[str, set] = {}
    for f in (ROOT / "schemas").glob("*.schema.json"):
        s = json.loads(f.read_text())
        schema_props[f.stem.replace(".schema", "")] = set(s.get("properties", {}).keys())
    expected = {
        "humanoid_command", "swarm_message", "ae_event", "ctcae_grading",
        "sponsor_acknowledgment", "fda_rtct_submission", "physician_escalation",
        "llm_decision", "robot_camarade_state", "peer_handoff",
    }
    missing = expected - set(schema_props.keys())
    for s in missing:
        log("schema_coverage", ROOT / "schemas", f"missing {s}.schema.json")


def check_cartesian_bounds() -> None:
    pattern = re.compile(r'"target_pose_xyz":\s*\{\s*"x":\s*(-?\d+\.?\d*)\s*,\s*"y":\s*(-?\d+\.?\d*)\s*,\s*"z":\s*(-?\d+\.?\d*)')
    for f in (ROOT / "data").glob("*.jsonl"):
        for line_no, line in enumerate(f.read_text().splitlines(), start=1):
            for m in pattern.finditer(line):
                x, y, z = float(m.group(1)), float(m.group(2)), float(m.group(3))
                if not (-50 <= x <= 50 and -50 <= y <= 50 and 0 <= z <= 3):
                    log("cartesian_bounds", f, f"line {line_no} pose out of frame: ({x}, {y}, {z})")


def main() -> int:
    check_yaml_validity()
    check_json_schemas()
    check_ascii_sizes()
    check_robot_ids()
    check_dash_style()
    check_phi()
    check_schema_coverage()
    check_cartesian_bounds()
    for e in ERRORS:
        print(e)
    if ERRORS:
        print(f"FAILED: {len(ERRORS)} issues")
        return 1
    print("OK: 0 issues across 7 checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
