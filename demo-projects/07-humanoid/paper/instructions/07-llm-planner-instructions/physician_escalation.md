# Authoring Instructions for `src/physician_escalation.py`

The future session writes this Python module during Commit 4 of 7.

## Purpose

Pages the on-call physician for CTCAE grade 3+ AEs and blocks any IV access until the physician acknowledges or arrives on-site. Emits records matching `schemas/physician_escalation.schema.json`.

## Key Behavior

- Subscribes to CTCAE grading records.
- On grade 3+ grading, pages the on-call physician via secure pager plus phone.
- Sets a 60-second acknowledgment SLA.
- Blocks the swarm-level `prepare_iv_access_tray` action from completing into IV insertion until physician ack.
- Records the escalation with full timeline.

## Required Interfaces

```
class PhysicianEscalation:
    def __init__(self, site_id: str, pager_config: dict) -> None: ...
    def trigger(self, ae_event: dict, grading: dict) -> dict: ...
    def wait_for_ack(self, escalation_id: str, timeout_s: int = 60) -> dict: ...
    def is_iv_access_blocked(self, ae_id: str) -> bool: ...
```

## Validation Rules

- All CTCAE grade 3+ events trigger an escalation record.
- `ack_within_60s` is true if the physician acknowledges within 60 seconds.
- IV access is blocked at the swarm level until ack or on-site arrival.

## Notes

- The Reserve robot owns this module. Lead and Assist focus on patient care.
- The HR 9504 Physical AI Clinical Error Reduction Act mandates physician-in-the-loop for grade 3+ AEs.
