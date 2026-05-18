"""Schema ingest validator for the 10 v0.4.0 codegen schemas.

Reads data/samples.jsonl and validates each record against the corresponding
JSON Schema in schemas/. Exits 0 on success, 1 on failure.
"""

from __future__ import annotations

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
    samples_path = base / "data" / "samples.jsonl"
    if not samples_path.exists():
        print(f"Samples file not found: {samples_path}")
        return 1
    samples = samples_path.read_text().splitlines()
    passed = 0
    failed = 0
    errors = []
    for line_no, raw in enumerate(samples, start=1):
        if not raw.strip():
            continue
        envelope = json.loads(raw)
        schema_name = envelope["schema"]
        record = envelope["record"]
        if schema_name not in schemas:
            errors.append(f"line {line_no}: unknown schema {schema_name}")
            failed += 1
            continue
        validator = jsonschema.Draft202012Validator(schemas[schema_name])
        line_errors = list(validator.iter_errors(record))
        if line_errors:
            failed += 1
            for err in line_errors:
                errors.append(
                    f"line {line_no} schema {schema_name}: {err.message} at {list(err.absolute_path)}"
                )
        else:
            passed += 1
    print(f"Records passed: {passed}")
    print(f"Records failed: {failed}")
    for err in errors:
        print(err)
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
