# Authoring Instructions for `src/check_errors.py`

The future session writes this Python script during Commit 6 of 7.

## Purpose

The 7-check error scan. Exits 0 if no issues, 1 if any issue. Logs each issue on stdout.

## Required Behavior

1. Walk the instruction tree.
2. Check schema field coverage (every `["key"]` reference in `src/*.py` exists in the schema files).
3. Validate YAML configs by parsing them.
4. Check cartesian coordinates in code and fixtures.
5. Check robot IDs.
6. Check ASCII diagram sizes.
7. Check dash style (no em dash, no double dash in prose, no triple dash in prose outside markdown tables and standard markdown HR).
8. Check PHI absence.

## Suggested Skeleton

```
import ast
import pathlib
import re
import sys
import json
import yaml


ROOT = pathlib.Path(__file__).resolve().parent.parent

ROBOT_IDS = {
    "SF-01-H2-A", "SF-01-H2-B", "SF-01-H2-C",
    "SD-01-H2-D", "SD-01-H2-E", "SD-01-H2-F",
    "BO-01-H2-G", "BO-01-H2-H", "BO-01-H2-I",
    "AT-01-H2-J", "AT-01-H2-K", "AT-01-H2-L",
}

ERRORS = []


def log(category, file, detail):
    ERRORS.append(f"{category} {file}: {detail}")


def check_yaml_validity():
    for f in (ROOT / "config").glob("*.yaml"):
        try:
            yaml.safe_load(f.read_text())
        except yaml.YAMLError as e:
            log("yaml", f, str(e))


def check_json_schemas():
    for f in (ROOT / "schemas").glob("*.schema.json"):
        try:
            json.loads(f.read_text())
        except json.JSONDecodeError as e:
            log("json", f, str(e))


def check_ascii_sizes():
    if not (ROOT / "diagrams").exists():
        return
    for f in (ROOT / "diagrams").glob("*.txt"):
        lines = f.read_text().splitlines()
        if len(lines) > 60:
            log("ascii_rows", f, f"{len(lines)} rows")
        for i, line in enumerate(lines, start=1):
            if len(line) > 80:
                log("ascii_cols", f, f"line {i} cols {len(line)}")


def check_phi():
    pattern = re.compile(r"\b(?:John|Jane)\s+(?:Doe|Smith)\b")
    for f in ROOT.rglob("*.md"):
        if pattern.search(f.read_text()):
            log("phi", f, "possible real name")


def main():
    check_yaml_validity()
    check_json_schemas()
    check_ascii_sizes()
    check_phi()
    for e in ERRORS:
        print(e)
    return 0 if not ERRORS else 1


if __name__ == "__main__":
    sys.exit(main())
```

## Validation Rules

- Exit 0 if no issues.
- One log line per issue.
- Categories include: yaml, json, ascii_rows, ascii_cols, phi, dash, robot_id, cartesian_bounds, schema_coverage.

## Notes

- The check_errors script is fast (under 1 second).
- Add to the future session's pre-commit hook for commit 6 and beyond.
