# Authoring Instructions for `src/xyz_safety.py`

The future session writes this Python module during Commit 3 of 7.

## Purpose

Validates x, y, z commands before they leave the dispatcher. Catches commands that would put a robot outside the site frame bounds, inside a peer's 2-second envelope, or into a known no-fly zone (oxygen tank rack, fragile imaging equipment).

## Key Behavior

- Reads `config/site_frame_bounds.yaml` (added in commit 6) for per-site no-fly zones.
- Validates each `humanoid_command` against:
  - Frame bounds: x in [-50, 50] m, y in [-50, 50] m, z in [0, 3] m.
  - Peer 2-second envelope: target pose is at least 0.4 m from any peer's projected position 2 seconds from now.
  - Patient envelope: only Lead may enter the 0.4 m patient envelope; Assist may enter on explicit handoff; Reserve may not enter.
- Returns a pass/fail tuple plus a reason string.

## Required Interfaces

```
def validate_command(command: dict, peer_states: list[dict], patient_state: dict, site_bounds: dict) -> tuple[bool, str]: ...
def predict_peer_position(peer_state: dict, seconds_ahead: float) -> dict: ...
def in_no_fly_zone(pose: dict, no_fly_zones: list[dict]) -> bool: ...
```

## Validation Rules

- Reject any command with frame bound violation.
- Reject any Assist or Reserve command that would put the robot inside 0.4 m of the patient without a Lead handoff.
- Reject any command intersecting a no-fly zone.

## Notes

- Reasons are logged with the command_id for forensic analysis.
- Commands that fail validation are replaced by a hold-in-place command for the current tick; the LLM is notified for the next tick.
