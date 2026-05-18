"""Intellectual comms: 1 Hz pub-sub via the on-prem Claude Code compute fabric.

Each robot publishes its self-state and reads peer state at 1 Hz. Topics
follow the convention site/<site_id>/world_model/robots/<robot_id>. In
simulation we use an in-process registry; production uses Redis Pub/Sub or
NATS hosted in the on-prem Claude Code appliance.
"""

from __future__ import annotations

import threading
import time
from typing import Optional


_REGISTRY: dict[str, dict] = {}
_REGISTRY_TS: dict[str, float] = {}
_LOCK = threading.Lock()


class IntellectualComms:
    def __init__(self, robot_id: str, site_id: str, peer_ids: list[str]) -> None:
        self.robot_id = robot_id
        self.site_id = site_id
        self.peer_ids = list(peer_ids)

    def publish_self_state(self, state: dict) -> None:
        topic = f"site/{self.site_id}/world_model/robots/{self.robot_id}"
        self._publish(topic, state)

    def read_peer_state(self, peer_id: str) -> Optional[dict]:
        topic = f"site/{self.site_id}/world_model/robots/{peer_id}"
        with _LOCK:
            ts = _REGISTRY_TS.get(topic, 0.0)
            if time.time() - ts > 1.1:
                return None
            return dict(_REGISTRY.get(topic, {}))

    def read_all_peer_states(self) -> dict:
        return {pid: self.read_peer_state(pid) for pid in self.peer_ids}

    def publish_task_progress(self, progress: dict) -> None:
        topic = f"site/{self.site_id}/world_model/task_progress/{self.robot_id}"
        self._publish(topic, progress)

    def publish_self_confidence(self, confidence: float) -> None:
        topic = f"site/{self.site_id}/world_model/confidence/{self.robot_id}"
        self._publish(topic, {"confidence": float(confidence)})

    def _publish(self, topic: str, payload: dict) -> None:
        with _LOCK:
            _REGISTRY[topic] = dict(payload)
            _REGISTRY_TS[topic] = time.time()
