# Authoring Instructions for `src/llm_planner.py`

The future session writes this Python module during Commit 4 of 7.

## Purpose

The per-site Claude Opus 4.7 1M planning loop. Reads the shared world model at 1 Hz, calls the LLM via the on-prem Anthropic appliance, and emits a single `llm_decision` record with 3 sub-commands per tick.

## Key Behavior

- Runs once per LLM tick at 1 Hz.
- Builds the prompt from: world model snapshot, patient state, doctor state, peer-robot state, recent AE events, and HR 9504 plus HR 9505 framing.
- Calls the on-prem Claude Opus 4.7 1M API with `model: claude-opus-4-7` and `temperature` from the iteration parameter.
- Parses the response as a JSON `llm_decision` record.
- Validates the record against `schemas/llm_decision.schema.json`.
- Hands the record to `broadcaster.py`.

## Required Interfaces

```
class LLMPlanner:
    def __init__(self, site_id: str, config_dir: pathlib.Path) -> None: ...
    def plan_tick(self, world_model: dict, tick: int) -> dict: ...
    def build_prompt(self, world_model: dict, tick: int) -> str: ...
    def parse_response(self, raw: str, tick: int) -> dict: ...
    def validate_decision(self, decision: dict) -> None: ...
```

## Prompt Conventions

- The system prompt is loaded from `src/prompt_frozen.md` (authored in commit 5).
- The system prompt frames the LLM as the planner for a 3-robot camarade swarm; emphasizes the 7 invariants.
- The user message contains the world model snapshot as JSON.
- The user message also lists the 3 robot IDs, their current roles, and their current battery state.

## Suggested Skeleton

```
import json
import pathlib
import time
import uuid

import jsonschema


class LLMPlanner:
    def __init__(self, site_id, config_dir):
        self.site_id = site_id
        self.config = self._load(config_dir)
        self.system_prompt = (pathlib.Path("src/prompt_frozen.md")).read_text()
        self.schema = json.loads(pathlib.Path("schemas/llm_decision.schema.json").read_text())
        self.audit_prev_hash = "0" * 64

    def _load(self, d):
        import yaml
        return yaml.safe_load((d / "llm_loop.yaml").read_text())

    def plan_tick(self, world_model, tick):
        prompt = self.build_prompt(world_model, tick)
        raw = self._call_llm(prompt)
        decision = self.parse_response(raw, tick)
        self.validate_decision(decision)
        return decision

    def build_prompt(self, world_model, tick):
        return json.dumps({"tick": tick, "site": self.site_id, "world": world_model}, sort_keys=True)

    def parse_response(self, raw, tick):
        decision = json.loads(raw)
        decision["decision_id"] = f"dec-{uuid.uuid4().hex[:16]}"
        decision["tick"] = tick
        decision["site"] = self.site_id
        decision["decided_at_iso"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        decision["audit_chain_prev_hash"] = self.audit_prev_hash
        return decision

    def validate_decision(self, decision):
        validator = jsonschema.Draft202012Validator(self.schema)
        errors = list(validator.iter_errors(decision))
        if errors:
            raise ValueError(f"llm_decision invalid: {errors[0].message}")

    def _call_llm(self, prompt):
        # in simulation: a deterministic stub that returns a 3-sub-command payload
        # in production: anthropic.Anthropic().messages.create(model="claude-opus-4-7", ...)
        return json.dumps({
            "synergy_score": 1.0,
            "sub_commands": [
                {"robot_id": f"{self.site_id}-H2-A", "role": "Lead",    "target_pose_xyz": {"x": 1.0, "y": 2.0, "z": 1.5}, "target_orientation_rpy": {"roll": 0.0, "pitch": 0.0, "yaw": 0.0}, "gripper_state": "open"},
                {"robot_id": f"{self.site_id}-H2-B", "role": "Assist",  "target_pose_xyz": {"x": 1.0, "y": 2.8, "z": 1.5}, "target_orientation_rpy": {"roll": 0.0, "pitch": 0.0, "yaw": 0.0}, "gripper_state": "holding_oximeter"},
                {"robot_id": f"{self.site_id}-H2-C", "role": "Reserve", "target_pose_xyz": {"x": 2.5, "y": 2.0, "z": 1.5}, "target_orientation_rpy": {"roll": 0.0, "pitch": 0.0, "yaw": 0.0}, "gripper_state": "open"},
            ],
            "peer_observability": {
                "all_3_robots_reporting_state": True,
                "all_3_robots_within_uwb_range": True,
                "all_3_robots_within_ir_beacon_line_of_sight": True,
            },
        })
```

## Validation Rules

- Exactly 3 sub-commands per decision.
- Roles are unique (Lead, Assist, Reserve).
- Synergy score in [0.0, 1.0].

## Notes

- The simulation stub is deterministic. The production version calls the on-prem Anthropic API with `claude-opus-4-7`.
- The shared cloud compute pattern: all 3 robots see the same broadcast in the same tick. The LLM never authors per-robot commands separately.
