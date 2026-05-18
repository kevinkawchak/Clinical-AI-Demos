# Authoring Instructions for `src/comms_intellectual.py`

The future session writes this Python module during Commit 3 of 7.

## Purpose

Handles intellectual peer-to-peer communication through the on-prem Claude Code compute fabric. This is a publish-subscribe bus exposed by the per-site Claude Opus 4.7 1M deployment. Each robot publishes its self-state and reads peer state at 1 Hz.

## Key Behavior

- Publishes `robot_camarade_state` records at 1 Hz per robot.
- Subscribes to `site/{site_id}/world_model/robots` topic for peer state.
- Buffers the most recent state per peer for read-access by the local policy.
- Reads sensor digests, task progress tokens, and self-confidence values.

## Required Interfaces

```
class IntellectualComms:
    def __init__(self, robot_id: str, site_id: str, peer_ids: list[str]) -> None: ...
    def publish_self_state(self, state: dict) -> None: ...
    def read_peer_state(self, peer_id: str) -> dict: ...
    def read_all_peer_states(self) -> dict: ...
    def publish_task_progress(self, progress: dict) -> None: ...
    def publish_self_confidence(self, confidence: float) -> None: ...
```

## Cadence and Backoff

- Default publish cadence: 1 Hz.
- If LLM is unreachable, cadence increases to 2 Hz to keep peers informed.
- If a peer has not published for 1100 ms, the local view treats its state as stale.

## Suggested Skeleton

```
import time
import threading


class IntellectualComms:
    def __init__(self, robot_id, site_id, peer_ids):
        self.robot_id = robot_id
        self.site_id = site_id
        self.peer_ids = peer_ids
        self.peer_cache = {pid: None for pid in peer_ids}
        self.peer_cache_ts = {pid: 0.0 for pid in peer_ids}
        self.lock = threading.Lock()

    def publish_self_state(self, state):
        topic = f"site/{self.site_id}/world_model/robots/{self.robot_id}"
        self._publish(topic, state)

    def read_peer_state(self, peer_id):
        with self.lock:
            ts = self.peer_cache_ts.get(peer_id, 0.0)
            if time.time() - ts > 1.1:
                return None
            return self.peer_cache.get(peer_id)

    def read_all_peer_states(self):
        return {pid: self.read_peer_state(pid) for pid in self.peer_ids}

    def publish_task_progress(self, progress):
        topic = f"site/{self.site_id}/world_model/task_progress/{self.robot_id}"
        self._publish(topic, progress)

    def publish_self_confidence(self, confidence):
        topic = f"site/{self.site_id}/world_model/confidence/{self.robot_id}"
        self._publish(topic, {"confidence": float(confidence)})

    def _publish(self, topic, payload):
        pass  # broker integration (zmq, redis pubsub, or in-process bus)

    def _on_peer_update(self, peer_id, payload):
        with self.lock:
            self.peer_cache[peer_id] = payload
            self.peer_cache_ts[peer_id] = time.time()
```

## Validation Rules

- Self-publish cadence at most 1100 ms apart.
- Peer reads return None if stale.
- Topic names follow the `site/{site_id}/world_model/...` convention.

## Notes

- The intellectual channel runs at 1 Hz (slow). It is the high-level loop. The physical channel is the low-level loop. They do not block each other.
- In simulation, broker is in-process. Production uses Redis Pub/Sub or NATS hosted in the on-prem Claude Code appliance.
