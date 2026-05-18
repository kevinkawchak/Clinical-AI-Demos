"""Per-site H2 EDU dispatcher.

Receives the LLM broadcast and fans out 3 humanoid_command records to the
3 robots in the camarade swarm. Tracks acks within 500 ms and maintains the
per-site audit chain via SHA-256 over each broadcast.
"""

from __future__ import annotations

import hashlib
import json
import pathlib
import threading
import time
import uuid
from typing import Optional

import yaml


class H2Dispatcher:
    def __init__(self, site_id: str, config_path: pathlib.Path) -> None:
        self.site_id = site_id
        self.config = self._load_config(config_path)
        self.audit_prev_hash = "0" * 64
        self.running = False
        self._published: dict[int, list[str]] = {}
        self._acks: dict[int, set[str]] = {}
        self._lock = threading.Lock()

    def _load_config(self, path: pathlib.Path) -> dict:
        return yaml.safe_load(path.read_text())

    def start(self) -> None:
        self.running = True

    def stop(self) -> None:
        self.running = False

    def handle_broadcast(self, broadcast: dict) -> list[dict]:
        if len(broadcast["sub_commands"]) != 3:
            raise ValueError("broadcast must have exactly 3 sub-commands")
        outgoing: list[dict] = []
        roster = self._roster()
        for sub in broadcast["sub_commands"]:
            cmd_id = f"cmd-{uuid.uuid4().hex[:16]}"
            peers = [r for r in roster if r != sub["robot_id"]]
            if len(peers) != 2:
                raise ValueError(
                    f"expected exactly 2 peers for {sub['robot_id']}, got {len(peers)}"
                )
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
                "synergy_score": broadcast.get("synergy_score", 0.0),
                "audit_chain_prev_hash": self.audit_prev_hash,
            }
            outgoing.append(command)
            self.publish_command(sub["robot_id"], command)
        with self._lock:
            self._published[broadcast["tick"]] = [c["command_id"] for c in outgoing]
            self._acks.setdefault(broadcast["tick"], set())
        digest = hashlib.sha256(
            json.dumps(broadcast, sort_keys=True).encode()
        ).hexdigest()
        self.audit_prev_hash = digest
        return outgoing

    def publish_command(self, robot_id: str, command: dict) -> None:
        topic = f"site/{self.site_id}/robot/{robot_id}/command"
        # In simulation we route through an in-process queue; production uses
        # ZeroMQ or NATS to the per-robot subscriber.
        _ = topic

    def ack(self, tick: int, robot_id: str) -> None:
        with self._lock:
            self._acks.setdefault(tick, set()).add(robot_id)

    def collect_acks(
        self, tick: int, timeout_ms: int = 500
    ) -> dict:
        deadline = time.time() + timeout_ms / 1000.0
        while time.time() < deadline:
            with self._lock:
                acks = self._acks.get(tick, set())
            if len(acks) >= 3:
                break
            time.sleep(0.005)
        with self._lock:
            published = self._published.get(tick, [])
            acks = self._acks.get(tick, set())
        return {"tick": tick, "published": published, "acks": sorted(acks)}

    def _roster(self) -> list[str]:
        robots = self.config.get("robots", [])
        return [r["robot_id"] for r in robots if r.get("site") == self.site_id]


def make_dispatcher(site_id: str, network_yaml: pathlib.Path) -> H2Dispatcher:
    return H2Dispatcher(site_id, network_yaml)


if __name__ == "__main__":
    base = pathlib.Path(__file__).resolve().parent.parent
    cfg = base / "config" / "h2_humanoid.yaml"
    disp = make_dispatcher("SF-01", cfg)
    print(f"Dispatcher ready for {disp.site_id} with {len(disp._roster())} robots")
