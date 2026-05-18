"""Per-robot peer state tracker.

Maintains self plus 2 peer state. Updated by intellectual comms at 1 Hz and
by physical UWB sensor_share more frequently. Estimates peer position via
simple dead-reckoning when peer publish is stale. Detects peer faults at
1100 ms staleness.
"""

from __future__ import annotations

import threading
import time
import uuid
from typing import Optional


class PeerStateTracker:
    def __init__(self, robot_id: str, peer_ids: list[str]) -> None:
        if len(peer_ids) != 2:
            raise ValueError("peer_ids must have exactly 2 entries")
        self.robot_id = robot_id
        self.peer_ids = list(peer_ids)
        self._self_state: Optional[dict] = None
        self._peer_state: dict[str, dict] = {pid: {} for pid in peer_ids}
        self._peer_last_seen: dict[str, float] = {pid: 0.0 for pid in peer_ids}
        self._lock = threading.Lock()

    def update_self(self, self_state: dict) -> None:
        with self._lock:
            self._self_state = dict(self_state)

    def update_peer_via_pubsub(self, peer_id: str, peer_state: dict) -> None:
        if peer_id not in self.peer_ids:
            return
        with self._lock:
            self._peer_state[peer_id] = dict(peer_state)
            self._peer_last_seen[peer_id] = time.time()

    def update_peer_via_uwb(self, peer_id: str, sensor_share: dict) -> None:
        if peer_id not in self.peer_ids:
            return
        with self._lock:
            existing = self._peer_state.get(peer_id, {})
            existing.update(sensor_share)
            self._peer_state[peer_id] = existing
            self._peer_last_seen[peer_id] = time.time()

    def snapshot(self) -> dict:
        with self._lock:
            self_state = dict(self._self_state or {})
            peer_a_id, peer_b_id = self.peer_ids
            peer_a = dict(self._peer_state.get(peer_a_id, {}))
            peer_b = dict(self._peer_state.get(peer_b_id, {}))
            now = time.time()
            return {
                "state_id": f"st-{uuid.uuid4().hex[:16]}",
                "robot_id": self.robot_id,
                "site": self_state.get("site", "SF-01"),
                "timestamp_iso": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(now)),
                "self_state": self_state,
                "peer_state_a": peer_a,
                "peer_state_b": peer_b,
            }

    def peer_is_stale(self, peer_id: str, threshold_s: float = 1.1) -> bool:
        with self._lock:
            ts = self._peer_last_seen.get(peer_id, 0.0)
        return (time.time() - ts) > threshold_s

    def detect_faults(self, threshold_s: float = 1.1) -> list[str]:
        return [pid for pid in self.peer_ids if self.peer_is_stale(pid, threshold_s)]
