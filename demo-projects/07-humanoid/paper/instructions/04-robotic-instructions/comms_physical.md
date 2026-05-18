# Authoring Instructions for `src/comms_physical.py`

The future session writes this Python module during Commit 3 of 7.

## Purpose

Handles the physical inter-robot channels: 60 GHz ultra-wideband peer mesh and IR-band beacon line-of-sight. Both channels are simulated as in-process queues with realistic latency budgets.

## Key Behavior

- Two channels: UWB (60 GHz, 200 Hz, 5 ms round-trip), IR beacon (1000 Hz, 1 ms round-trip).
- UWB is used for: handoff_request, handoff_ack, sensor_share, proximity_alert, shared_world_model_update.
- IR beacon is used for: e_stop_propagation, cartesian_frame_align.
- Messages are typed via the `swarm_message` schema.
- Each message logs a send timestamp and a receive timestamp for SLA measurement.

## Required Interfaces

```
class PhysicalComms:
    def __init__(self, robot_id: str, peer_ids: list[str]) -> None: ...
    def send_uwb(self, payload_kind: str, payload: dict, receiver_ids: list[str], priority: str = "normal") -> str: ...
    def send_ir(self, payload_kind: str, payload: dict, receiver_ids: list[str], priority: str = "critical") -> str: ...
    def recv_uwb(self, timeout_ms: int = 5) -> list[dict]: ...
    def recv_ir(self, timeout_ms: int = 1) -> list[dict]: ...
    def propagate_estop(self) -> None: ...
```

## Latency Simulation

- UWB: 5 ms round-trip, jittered by 2 ms uniform.
- IR beacon: 1 ms round-trip, jittered by 0.5 ms uniform.
- Both channels drop messages with 0.1 percent probability to simulate radio interference.

## Suggested Skeleton

```
import queue
import random
import time
import uuid


class PhysicalComms:
    def __init__(self, robot_id, peer_ids):
        self.robot_id = robot_id
        self.peer_ids = peer_ids
        self.uwb_in = queue.Queue()
        self.ir_in = queue.Queue()

    def send_uwb(self, payload_kind, payload, receiver_ids, priority="normal"):
        if random.random() < 0.001:
            return ""  # dropped
        msg_id = f"msg-{uuid.uuid4().hex[:16]}"
        latency_ms = 5 + (random.random() - 0.5) * 4
        ts_ms = int(time.time() * 1000)
        msg = {
            "message_id": msg_id,
            "sender_robot_id": self.robot_id,
            "receiver_robot_ids": receiver_ids,
            "channel": "uwb_60ghz",
            "payload_kind": payload_kind,
            "timestamp_ms": ts_ms,
            "payload": payload,
            "priority": priority,
        }
        # simulate via in-process queues registered by site bus
        deliver_after_ms = int(latency_ms)
        self._deliver_uwb(msg, deliver_after_ms)
        return msg_id

    def send_ir(self, payload_kind, payload, receiver_ids, priority="critical"):
        msg_id = f"msg-{uuid.uuid4().hex[:16]}"
        latency_ms = 1 + (random.random() - 0.5)
        ts_ms = int(time.time() * 1000)
        msg = {
            "message_id": msg_id,
            "sender_robot_id": self.robot_id,
            "receiver_robot_ids": receiver_ids,
            "channel": "ir_beacon",
            "payload_kind": payload_kind,
            "timestamp_ms": ts_ms,
            "payload": payload,
            "priority": priority,
        }
        deliver_after_ms = max(1, int(latency_ms))
        self._deliver_ir(msg, deliver_after_ms)
        return msg_id

    def recv_uwb(self, timeout_ms=5):
        out = []
        deadline = time.time() + timeout_ms / 1000.0
        while time.time() < deadline:
            try:
                out.append(self.uwb_in.get_nowait())
            except queue.Empty:
                break
        return out

    def recv_ir(self, timeout_ms=1):
        out = []
        deadline = time.time() + timeout_ms / 1000.0
        while time.time() < deadline:
            try:
                out.append(self.ir_in.get_nowait())
            except queue.Empty:
                break
        return out

    def propagate_estop(self):
        for peer in self.peer_ids:
            self.send_ir("e_stop_propagation", {"reason": "local_safety_trip"}, [peer], priority="critical")

    def _deliver_uwb(self, msg, delay_ms):
        # in simulation, schedule via site bus; in production, push to UWB transceiver
        self.uwb_in.put(msg)

    def _deliver_ir(self, msg, delay_ms):
        self.ir_in.put(msg)
```

## Camarade Invariants Enforced Here

- E-stop within 5 ms: `propagate_estop` uses the IR channel, which has a 1 ms round-trip ceiling.
- Drop rate observability: every dropped UWB message is logged for later forensics.

## Validation Rules

- UWB messages have `channel: uwb_60ghz`.
- IR messages have `channel: ir_beacon`.
- Receiver count at most 2.

## Notes

- In simulation, the queue stand-in for radio hardware is fine. Production replaces the queues with Unitree SDK transceivers.
- The 0.1 percent UWB drop rate is consistent with industry benchmarks for 60 GHz at 30 m range.
