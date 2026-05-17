# Authoring Instructions for `tests/test_schemas.py`

The future session writes this pytest module during Commit 6 of 7.

## Purpose

Validates each schema in `schemas/` against a sample record from `data/samples.jsonl`. Acts as the regression bench for schemas; any schema breakage shows up as a test failure.

## Suggested Content

```
import json
import pathlib

import jsonschema
import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent

SCHEMAS = [
    "humanoid_command",
    "swarm_message",
    "ae_event",
    "ctcae_grading",
    "sponsor_acknowledgment",
    "fda_rtct_submission",
    "physician_escalation",
    "llm_decision",
    "robot_camarade_state",
    "peer_handoff",
]


@pytest.fixture(scope="module")
def samples():
    out = {}
    for line in (ROOT / "data/samples.jsonl").read_text().splitlines():
        if not line.strip():
            continue
        envelope = json.loads(line)
        out[envelope["schema"]] = envelope["record"]
    return out


@pytest.mark.parametrize("name", SCHEMAS)
def test_sample_validates(name, samples):
    schema = json.loads((ROOT / f"schemas/{name}.schema.json").read_text())
    record = samples[name]
    validator = jsonschema.Draft202012Validator(schema)
    errors = list(validator.iter_errors(record))
    assert not errors, f"{name}: {[e.message for e in errors]}"


def test_llm_decision_has_3_subcommands(samples):
    decision = samples["llm_decision"]
    assert len(decision["sub_commands"]) == 3
    roles = [sc["role"] for sc in decision["sub_commands"]]
    assert sorted(roles) == ["Assist", "Lead", "Reserve"]


def test_humanoid_command_has_2_peers(samples):
    command = samples["humanoid_command"]
    assert len(command["peer_robot_ids"]) == 2


def test_swarm_message_receivers_at_most_2(samples):
    msg = samples["swarm_message"]
    assert 1 <= len(msg["receiver_robot_ids"]) <= 2
```

## Validation Rules

- 10 parametrized tests for the 10 schemas.
- 3 additional invariant tests.
- Exit 0 on success.

## Notes

- `pytest -q` runs the suite in under 5 seconds.
- This test is the regression bench against schema drift.
