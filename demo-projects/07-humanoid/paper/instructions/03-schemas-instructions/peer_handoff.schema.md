# Authoring Instructions for `schemas/peer_handoff.schema.json`

This is a new schema introduced in v0.3.0.

## Purpose

Defines a peer-to-peer tool hand-off record. The Lead asks the Assist for a tool, the Assist either confirms or declines, and the tool transfer happens within 2 seconds.

## Schema

```
$schema: https://json-schema.org/draft/2020-12/schema
$id: peer_handoff
title: Peer Hand-off
type: object
required:
  - handoff_id
  - requester_robot_id
  - responder_robot_id
  - tool
  - requested_at_ms
  - responded_at_ms_or_null
  - completed_at_ms_or_null
  - elapsed_seconds
  - sla_met
properties:
  handoff_id: { type: string, pattern: "^hof-[0-9a-f]{16}$" }
  requester_robot_id: { type: string }
  responder_robot_id: { type: string }
  tool:
    type: string
    enum: [epinephrine_auto_injector, iv_access_tray, vagus_nerve_stimulator_probe, portable_pulse_oximeter, portable_ecg, emergency_airway_kit]
  requested_at_ms: { type: integer, minimum: 0 }
  responded_at_ms_or_null: { type: [integer, "null"] }
  completed_at_ms_or_null: { type: [integer, "null"] }
  elapsed_seconds: { type: number, minimum: 0 }
  sla_met: { type: boolean }
  channel: { type: string, enum: [uwb_60ghz, ir_beacon] }
  decline_reason: { type: string, maxLength: 128 }
additionalProperties: false
```

## Validation Rules

- `sla_met` is true if `elapsed_seconds` is at most 2.0.
- A decline must include a `decline_reason`.

## Notes

- Hand-offs are tracked per-AE and aggregated into the `peer_handoff_p95_seconds` metric.
- A decline rate above 5 percent across iterations is a red flag for camaraderie quality.
