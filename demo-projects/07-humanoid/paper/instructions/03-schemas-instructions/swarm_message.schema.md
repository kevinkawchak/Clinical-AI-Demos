# Authoring Instructions for `schemas/swarm_message.schema.json`

This is a new schema introduced in v0.3.0. The future session writes it during Commit 2 of 7.

## Purpose

Defines the inter-robot camarade message envelope used for physical and intellectual peer communication. One record per peer-to-peer message.

## Schema

```
$schema: https://json-schema.org/draft/2020-12/schema
$id: swarm_message
title: Swarm Camarade Message
type: object
required:
  - message_id
  - sender_robot_id
  - receiver_robot_ids
  - channel
  - payload_kind
  - timestamp_ms
  - payload
properties:
  message_id: { type: string, pattern: "^msg-[0-9a-f]{16}$" }
  sender_robot_id: { type: string }
  receiver_robot_ids:
    type: array
    minItems: 1
    maxItems: 2
    items: { type: string }
  channel: { type: string, enum: [uwb_60ghz, ir_beacon, intellectual_pubsub] }
  payload_kind:
    type: string
    enum:
      - handoff_request
      - handoff_ack
      - sensor_share
      - proximity_alert
      - e_stop_propagation
      - cartesian_frame_align
      - task_progress_token
      - self_confidence
      - role_request_change
      - peer_fault_alert
  timestamp_ms: { type: integer, minimum: 0 }
  payload:
    oneOf:
      - type: object
      - type: array
      - type: string
      - type: number
  priority:
    type: string
    enum: [low, normal, high, critical]
    default: normal
additionalProperties: false
```

## Validation Rules

- `receiver_robot_ids` is at most 2 because each swarm has exactly 3 robots.
- `channel` enum includes the 3 channels: 60 GHz UWB, IR beacon, intellectual pub-sub.
- E-stop payload_kind defaults to critical priority.
- handoff_request must be answered with handoff_ack within 2 seconds.

## Notes

- This schema is consumed by `src/comms_physical.py` and `src/comms_intellectual.py`.
- Sample messages live in `data/samples.jsonl`.
