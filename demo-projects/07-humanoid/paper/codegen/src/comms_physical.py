"""Physical comms: 60 GHz UWB peer mesh and IR beacon line-of-sight.

In simulation we use in-process queues with realistic latency budgets. UWB has
a 5 ms round-trip with 0.1 percent drop. IR beacon has a 1 ms round-trip with
no drop (line-of-sight). Production replaces the queues with Unitree SDK
transceivers.
"""

from __future__ import annotations

import queue
import random
import time
import uuid


class PhysicalComms:
    def __init__(self, robot_id: str, peer_ids: list[str], seed: int = 42) -> None:
        self.robot_id = robot_id
        self.peer_ids = list(peer_ids)
        self.uwb_in: queue.Queue = queue.Queue()
        self.ir_in: queue.Queue = queue.Queue()
        self._rng = random.Random(seed)

    def send_uwb(
        self,
        payload_kind: str,
        payload: dict,
        receiver_ids: list[str],
        priority: str = "normal",
    ) -> str:
        if self._rng.random() < 0.001:
            return ""  # simulated drop at 0.1 percent
        msg_id = f"msg-{uuid.uuid4().hex[:16]}"
        latency_ms = 5 + (self._rng.random() - 0.5) * 4
        ts_ms = int(time.time() * 1000)
        msg = {
            "message_id": msg_id,
            "sender_robot_id": self.robot_id,
            "receiver_robot_ids": list(receiver_ids),
            "channel": "uwb_60ghz",
            "payload_kind": payload_kind,
            "timestamp_ms": ts_ms,
            "payload": payload,
            "priority": priority,
        }
        self._deliver_uwb(msg, max(1, int(latency_ms)))
        return msg_id

    def send_ir(
        self,
        payload_kind: str,
        payload: dict,
        receiver_ids: list[str],
        priority: str = "critical",
    ) -> str:
        msg_id = f"msg-{uuid.uuid4().hex[:16]}"
        latency_ms = 1 + (self._rng.random() - 0.5)
        ts_ms = int(time.time() * 1000)
        msg = {
            "message_id": msg_id,
            "sender_robot_id": self.robot_id,
            "receiver_robot_ids": list(receiver_ids),
            "channel": "ir_beacon",
            "payload_kind": payload_kind,
            "timestamp_ms": ts_ms,
            "payload": payload,
            "priority": priority,
        }
        self._deliver_ir(msg, max(1, int(latency_ms)))
        return msg_id

    def recv_uwb(self, timeout_ms: int = 5) -> list[dict]:
        return self._drain(self.uwb_in, timeout_ms)

    def recv_ir(self, timeout_ms: int = 1) -> list[dict]:
        return self._drain(self.ir_in, timeout_ms)

    def propagate_estop(self) -> None:
        for peer in self.peer_ids:
            self.send_ir(
                "e_stop_propagation",
                {"reason": "local_safety_trip"},
                [peer],
                priority="critical",
            )

    def _drain(self, q: queue.Queue, timeout_ms: int) -> list[dict]:
        out: list[dict] = []
        deadline = time.time() + timeout_ms / 1000.0
        while time.time() < deadline:
            try:
                out.append(q.get_nowait())
            except queue.Empty:
                break
        return out

    def _deliver_uwb(self, msg: dict, delay_ms: int) -> None:
        self.uwb_in.put(msg)

    def _deliver_ir(self, msg: dict, delay_ms: int) -> None:
        self.ir_in.put(msg)
