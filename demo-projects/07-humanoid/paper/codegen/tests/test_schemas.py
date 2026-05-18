"""Validate each schema in schemas/ against its sample record in data/samples.jsonl."""

from __future__ import annotations

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
def samples() -> dict:
    out: dict = {}
    for line in (ROOT / "data" / "samples.jsonl").read_text().splitlines():
        if not line.strip():
            continue
        envelope = json.loads(line)
        out[envelope["schema"]] = envelope["record"]
    return out


@pytest.mark.parametrize("name", SCHEMAS)
def test_sample_validates(name: str, samples: dict) -> None:
    schema = json.loads((ROOT / "schemas" / f"{name}.schema.json").read_text())
    record = samples[name]
    validator = jsonschema.Draft202012Validator(schema)
    errors = list(validator.iter_errors(record))
    assert not errors, f"{name}: {[e.message for e in errors]}"


def test_llm_decision_has_3_subcommands(samples: dict) -> None:
    decision = samples["llm_decision"]
    assert len(decision["sub_commands"]) == 3
    roles = [sc["role"] for sc in decision["sub_commands"]]
    assert sorted(roles) == ["Assist", "Lead", "Reserve"]


def test_humanoid_command_has_2_peers(samples: dict) -> None:
    command = samples["humanoid_command"]
    assert len(command["peer_robot_ids"]) == 2


def test_swarm_message_receivers_at_most_2(samples: dict) -> None:
    msg = samples["swarm_message"]
    assert 1 <= len(msg["receiver_robot_ids"]) <= 2


def test_ae_event_responding_swarm_has_3(samples: dict) -> None:
    ae = samples["ae_event"]
    assert len(ae["responding_swarm"]) == 3
