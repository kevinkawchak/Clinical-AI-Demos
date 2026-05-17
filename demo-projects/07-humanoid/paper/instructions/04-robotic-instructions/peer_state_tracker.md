# Authoring Instructions for `src/peer_state_tracker.py`

The future session writes this Python module during Commit 3 of 7.

## Purpose

Maintains the per-robot peer-state model: self plus 2 peers. Reads from both intellectual and physical comms. Exposes a snapshot API used by `swarm_coordinator.py` and the local policy.

## Key Behavior

- Holds 3 entries: self_state, peer_state_a, peer_state_b.
- Updated by intellectual comms at 1 Hz.
- Updated by physical comms (UWB sensor_share) more frequently.
- Estimates peer position by dead-reckoning when peer publish is stale.
- Detects peer faults if state has not refreshed for more than 1100 ms.

## Required Interfaces

```
class PeerStateTracker:
    def __init__(self, robot_id: str, peer_ids: list[str]) -> None: ...
    def update_self(self, self_state: dict) -> None: ...
    def update_peer_via_pubsub(self, peer_id: str, peer_state: dict) -> None: ...
    def update_peer_via_uwb(self, peer_id: str, sensor_share: dict) -> None: ...
    def snapshot(self) -> dict: ...
    def peer_is_stale(self, peer_id: str) -> bool: ...
    def detect_faults(self) -> list[str]: ...
```

## Validation Rules

- Snapshot output validates against `robot_camarade_state.schema.json`.
- Fault detection list contains peer IDs whose state has been stale for more than 1.1 s.

## Notes

- This module is small, but it is the gateway through which the swarm sees itself. Test thoroughly in `tests/test_peer_state_tracker.py` in commit 6.
- The dead-reckoning step uses last known velocity and acceleration estimates from the most recent peer state.
