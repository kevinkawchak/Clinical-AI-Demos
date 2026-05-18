# Authoring Instructions for `data/samples.jsonl`

The future session writes this JSONL file during Commit 2 of 7.

## Purpose

A representative sample for each of the 10 schemas authored in commit 2. One record per schema, encoded as one JSON object per line. The file is read by `src/ingest.py` to validate the schemas round trip.

## Layout

One line per schema:

```
{"schema": "humanoid_command", "record": { ... see schema ... }}
{"schema": "swarm_message", "record": { ... see schema ... }}
{"schema": "ae_event", "record": { ... see schema ... }}
{"schema": "ctcae_grading", "record": { ... see schema ... }}
{"schema": "sponsor_acknowledgment", "record": { ... see schema ... }}
{"schema": "fda_rtct_submission", "record": { ... see schema ... }}
{"schema": "physician_escalation", "record": { ... see schema ... }}
{"schema": "llm_decision", "record": { ... see schema ... }}
{"schema": "robot_camarade_state", "record": { ... see schema ... }}
{"schema": "peer_handoff", "record": { ... see schema ... }}
```

## Authoring Rules

- Each line is a self-contained JSON object.
- The `record` field validates against the schema referenced by the `schema` field.
- Use synthetic identifiers (PAT-NET-001-P001 for patient, SF-01-H2-A through L for robots).
- ISO timestamps use `2026-05-17T12:00:00Z` baseline; offsets between records reflect realistic AE response timing.
- Hash fields use a placeholder like `"0000000000000000000000000000000000000000000000000000000000000000"`.

## Validation

`src/ingest.py` opens this file, parses each line, looks up the schema, and validates the record against the schema. A non-zero exit code indicates a schema mismatch and must be fixed in commit 6.

## Notes

- Total file size around 20 KB.
- This file is the documentation-by-example for the 10 schemas.
