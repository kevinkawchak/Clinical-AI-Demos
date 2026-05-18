# Authoring Instructions for `schemas/robot_camarade_state.schema.json`

This is a new schema introduced in v0.3.0.

## Purpose

The per-robot self-plus-peers state record published at 1 Hz to the shared world model. Each robot in the swarm reads the 3 records (its own plus its 2 peers') every tick.

## Schema

```
$schema: https://json-schema.org/draft/2020-12/schema
$id: robot_camarade_state
title: Robot Camarade State
type: object
required:
  - state_id
  - robot_id
  - site
  - timestamp_iso
  - self_state
  - peer_state_a
  - peer_state_b
properties:
  state_id: { type: string, pattern: "^st-[0-9a-f]{16}$" }
  robot_id: { type: string }
  site: { type: string, enum: [SF-01, SD-01, BO-01, AT-01] }
  timestamp_iso: { type: string, format: date-time }
  self_state:
    type: object
    required: [position_xyz, joint_pose_digest, battery_soc, gripper_state, current_role, task_token, self_confidence]
    properties:
      position_xyz:
        type: object
        required: [x, y, z]
        properties:
          x: { type: number }
          y: { type: number }
          z: { type: number }
      joint_pose_digest: { type: string, pattern: "^[0-9a-f]{32}$" }
      battery_soc: { type: number, minimum: 0.0, maximum: 1.0 }
      gripper_state: { type: string }
      current_role: { type: string, enum: [Lead, Assist, Reserve] }
      task_token: { type: string }
      self_confidence: { type: number, minimum: 0.0, maximum: 1.0 }
  peer_state_a:
    type: object
    required: [peer_robot_id, last_seen_iso, position_xyz_estimate, battery_soc_estimate, current_role_estimate, comms_channel_observed]
    properties:
      peer_robot_id: { type: string }
      last_seen_iso: { type: string, format: date-time }
      position_xyz_estimate:
        type: object
        required: [x, y, z]
        properties:
          x: { type: number }
          y: { type: number }
          z: { type: number }
      battery_soc_estimate: { type: number, minimum: 0.0, maximum: 1.0 }
      current_role_estimate: { type: string, enum: [Lead, Assist, Reserve] }
      comms_channel_observed: { type: string, enum: [uwb_60ghz, ir_beacon, intellectual_pubsub, none] }
  peer_state_b:
    type: object
    required: [peer_robot_id, last_seen_iso, position_xyz_estimate, battery_soc_estimate, current_role_estimate, comms_channel_observed]
    properties:
      peer_robot_id: { type: string }
      last_seen_iso: { type: string, format: date-time }
      position_xyz_estimate:
        type: object
        required: [x, y, z]
        properties:
          x: { type: number }
          y: { type: number }
          z: { type: number }
      battery_soc_estimate: { type: number, minimum: 0.0, maximum: 1.0 }
      current_role_estimate: { type: string, enum: [Lead, Assist, Reserve] }
      comms_channel_observed: { type: string, enum: [uwb_60ghz, ir_beacon, intellectual_pubsub, none] }
additionalProperties: false
```

## Validation Rules

- `peer_state_a.peer_robot_id` and `peer_state_b.peer_robot_id` are the 2 other robots in the same camarade group.
- All position coordinates are in the shared site cartesian frame.
- `self_confidence` is the robot's self-reported confidence in its current task.

## Notes

- This record is the foundation of camaraderie. Each robot owns its own version and publishes it at 1 Hz.
- The LLM broadcaster reads the 3 records (one per robot per swarm) at every tick and emits the next broadcast.
