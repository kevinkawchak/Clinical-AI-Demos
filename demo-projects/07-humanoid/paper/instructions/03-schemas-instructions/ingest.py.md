# Authoring Instructions for `src/ingest.py`

The future session writes this Python at `demo-projects/07-humanoid/paper/instructions/src/ingest.py` during Commit 2 of 7.

## Purpose

Reads `data/samples.jsonl` and validates each record against the corresponding JSON Schema in `schemas/`. Exits 0 on success, non-zero on failure.

## Required Behavior

- Use the `jsonschema` package (Draft 2020-12 validator).
- Load each schema once from `schemas/<name>.schema.json`.
- Stream `data/samples.jsonl` line by line.
- For each line, parse the JSON, look up the `schema` field, validate the `record` against the schema.
- Accumulate failures and report them at the end with line number and JSON Pointer path.
- Print a summary: total records, passed, failed.

## Suggested Skeleton

```
import json
import pathlib
import sys

import jsonschema

SCHEMAS = {
    "humanoid_command": "schemas/humanoid_command.schema.json",
    "swarm_message": "schemas/swarm_message.schema.json",
    "ae_event": "schemas/ae_event.schema.json",
    "ctcae_grading": "schemas/ctcae_grading.schema.json",
    "sponsor_acknowledgment": "schemas/sponsor_acknowledgment.schema.json",
    "fda_rtct_submission": "schemas/fda_rtct_submission.schema.json",
    "physician_escalation": "schemas/physician_escalation.schema.json",
    "llm_decision": "schemas/llm_decision.schema.json",
    "robot_camarade_state": "schemas/robot_camarade_state.schema.json",
    "peer_handoff": "schemas/peer_handoff.schema.json",
}


def load_schemas(base: pathlib.Path) -> dict:
    out = {}
    for name, path in SCHEMAS.items():
        out[name] = json.loads((base / path).read_text())
    return out


def main() -> int:
    base = pathlib.Path(__file__).resolve().parent.parent
    schemas = load_schemas(base)
    samples = (base / "data/samples.jsonl").read_text().splitlines()
    passed = 0
    failed = 0
    errors = []
    for line_no, raw in enumerate(samples, start=1):
        if not raw.strip():
            continue
        envelope = json.loads(raw)
        schema_name = envelope["schema"]
        record = envelope["record"]
        validator = jsonschema.Draft202012Validator(schemas[schema_name])
        line_errors = list(validator.iter_errors(record))
        if line_errors:
            failed += 1
            for err in line_errors:
                errors.append(f"line {line_no} schema {schema_name}: {err.message} at {list(err.absolute_path)}")
        else:
            passed += 1
    print(f"Records passed: {passed}")
    print(f"Records failed: {failed}")
    for err in errors:
        print(err)
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
```

## Validation Rules

- Exit code 0 on success, 1 on failure.
- Print 1 line per failure with line number and schema name.
- No PHI in error messages (patient IDs are synthetic anyway).

## Notes

- `ruff` lint will flag unused imports. None are present in the skeleton.
- This is a CLI; running it locally before committing is recommended.
- Add to commit 6 a pytest version (`tests/test_schemas.py`) that exercises the same code path.
