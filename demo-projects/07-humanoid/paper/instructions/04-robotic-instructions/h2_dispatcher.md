# Authoring Instructions for `src/h2_dispatcher.py`

The future session writes this Python module during Commit 3 of 7.

## Purpose

Receives the per-tick LLM broadcast (1 record of schema `llm_decision`) and fans it out to the 3 robots in the camarade swarm. Translates each sub-command into a per-robot `humanoid_command` record and writes the record to the per-robot command topic.

## Key Behavior

- Subscribes to topic `site/{site_id}/broadcast`.
- For each broadcast tick, splits the 3 sub-commands into 3 `humanoid_command` records.
- Publishes each `humanoid_command` to its per-robot topic `site/{site_id}/robot/{robot_id}/command`.
- Tracks acknowledgments from all 3 robots; logs missing acks at the end of each tick.
- Maintains the per-site audit chain by computing the SHA-256 of the prior broadcast and including it in each `audit_chain_prev_hash` field.

## Required Interfaces

```
class H2Dispatcher:
    def __init__(self, site_id: str, config_path: pathlib.Path) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def handle_broadcast(self, broadcast: dict) -> list[dict]: ...
    def publish_command(self, robot_id: str, command: dict) -> None: ...
    def collect_acks(self, command_ids: list[str], timeout_ms: int = 500) -> dict: ...
```

## Camarade Invariants Enforced Here

- The 3 sub-commands are always fanned out as a set. Never fan out 1 or 2.
- All 3 robots must receive the same `tick` value and the same `audit_chain_prev_hash`.
- If any robot fails to ack within 500 ms, the dispatcher logs the gap and the broadcaster increases the next tick's polling Hz to 2 Hz for the next 60 seconds.

## Suggested Skeleton

```
import hashlib
import json
import pathlib
import time
import uuid


class H2Dispatcher:
    def __init__(self, site_id: str, config_path: pathlib.Path) -> None:
        self.site_id = site_id
        self.config = self._load_config(config_path)
        self.audit_prev_hash = "0" * 64
        self.running = False

    def _load_config(self, path: pathlib.Path) -> dict:
        import yaml
        return yaml.safe_load(path.read_text())

    def start(self) -> None:
        self.running = True

    def stop(self) -> None:
        self.running = False

    def handle_broadcast(self, broadcast: dict) -> list[dict]:
        if len(broadcast["sub_commands"]) != 3:
            raise ValueError("broadcast must have exactly 3 sub-commands")
        outgoing = []
        for sub in broadcast["sub_commands"]:
            cmd_id = f"cmd-{uuid.uuid4().hex[:16]}"
            peers = [r for r in self._roster() if r != sub["robot_id"]]
            command = {
                "command_id": cmd_id,
                "tick": broadcast["tick"],
                "site": self.site_id,
                "robot_id": sub["robot_id"],
                "role": sub["role"],
                "target_pose_xyz": sub["target_pose_xyz"],
                "target_orientation_rpy": sub["target_orientation_rpy"],
                "gripper_state": sub["gripper_state"],
                "peer_robot_ids": peers,
                "synergy_score": broadcast["synergy_score"],
                "audit_chain_prev_hash": self.audit_prev_hash,
            }
            outgoing.append(command)
            self.publish_command(sub["robot_id"], command)
        digest = hashlib.sha256(json.dumps(broadcast, sort_keys=True).encode()).hexdigest()
        self.audit_prev_hash = digest
        return outgoing

    def publish_command(self, robot_id: str, command: dict) -> None:
        topic = f"site/{self.site_id}/robot/{robot_id}/command"
        # publish to the broadcast bus (zmq, redis pubsub, or in-process queue in simulation)

    def collect_acks(self, command_ids: list[str], timeout_ms: int = 500) -> dict:
        # subscribe to per-robot ack topic with a deadline of timeout_ms
        return {}

    def _roster(self) -> list[str]:
        return [r["robot_id"] for r in self.config["robots"] if r["site"] == self.site_id]
```

## Validation Rules

- 3 sub-commands per broadcast or raise.
- `peer_robot_ids` has exactly 2 entries (the 2 other robots in the swarm).
- All 3 records share the same `tick` and the same `audit_chain_prev_hash`.

## Notes

- Lint with ruff. Use the per-file-ignores already in `ruff.toml` for `demo-projects/**/*.py`.
- The in-process queue is fine for simulation; production would use ZeroMQ or NATS.
- Runs under Python 3.10, 3.11, 3.12.
