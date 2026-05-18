# Authoring Instructions for `schemas/humanoid_command.schema.json`

The future session writes this JSON Schema at `demo-projects/07-humanoid/paper/instructions/schemas/humanoid_command.schema.json` during Commit 2 of 7.

## Purpose

Defines the per-robot command record that the per-site broadcaster decomposes the LLM broadcast into. One record per robot per tick.

## Schema

```
$schema: https://json-schema.org/draft/2020-12/schema
$id: humanoid_command
title: Humanoid Command
type: object
required:
  - command_id
  - tick
  - site
  - robot_id
  - role
  - target_pose_xyz
  - target_orientation_rpy
  - gripper_state
  - peer_robot_ids
  - synergy_score
  - audit_chain_prev_hash
properties:
  command_id: { type: string, pattern: "^cmd-[0-9a-f]{16}$" }
  tick: { type: integer, minimum: 0 }
  site: { type: string, enum: [SF-01, SD-01, BO-01, AT-01] }
  robot_id: { type: string }
  role: { type: string, enum: [Lead, Assist, Reserve] }
  target_pose_xyz:
    type: object
    required: [x, y, z]
    properties:
      x: { type: number, minimum: -50.0, maximum: 50.0 }
      y: { type: number, minimum: -50.0, maximum: 50.0 }
      z: { type: number, minimum: 0.0, maximum: 3.0 }
  target_orientation_rpy:
    type: object
    required: [roll, pitch, yaw]
    properties:
      roll: { type: number, minimum: -3.1416, maximum: 3.1416 }
      pitch: { type: number, minimum: -3.1416, maximum: 3.1416 }
      yaw: { type: number, minimum: -3.1416, maximum: 3.1416 }
  gripper_state:
    type: string
    enum: [open, closed, holding_epipen, holding_iv_tray, holding_oximeter, holding_ecg, holding_vagus_probe, holding_airway_kit]
  peer_robot_ids:
    type: array
    minItems: 2
    maxItems: 2
    items: { type: string }
  synergy_score: { type: number, minimum: 0.0, maximum: 1.0 }
  audit_chain_prev_hash: { type: string, pattern: "^[0-9a-f]{64}$" }
  notes: { type: string, maxLength: 256 }
```

## Validation Rules

- `peer_robot_ids` always has exactly 2 entries. This enforces the camarade pattern (3 robots per swarm, each robot knows its 2 peers).
- `target_pose_xyz` is in the shared site cartesian frame.
- `audit_chain_prev_hash` links to the prior command in the per-site audit chain.
- `synergy_score` is the LLM's self-estimate of swarm benefit for this tick.

## Notes

- One JSON Schema, draft 2020-12.
- Strict mode: no additional properties allowed. Add `additionalProperties: false` at the root.
