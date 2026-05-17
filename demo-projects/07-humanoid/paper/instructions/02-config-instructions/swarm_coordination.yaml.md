# Authoring Instructions for `config/swarm_coordination.yaml`

The future session writes this YAML at `demo-projects/07-humanoid/paper/instructions/config/swarm_coordination.yaml` during Commit 1 of 7. This is a new file introduced in v0.3.0; it is not in the original prompt 07.

## Purpose

Defines the 4 camarade swarms and the role rotation policy that animates them.

## Fields

```
swarms:
  - swarm_id: SF-01-swarm
    site: SF-01
    members:
      - SF-01-H2-A
      - SF-01-H2-B
      - SF-01-H2-C

  - swarm_id: SD-01-swarm
    site: SD-01
    members:
      - SD-01-H2-D
      - SD-01-H2-E
      - SD-01-H2-F

  - swarm_id: BO-01-swarm
    site: BO-01
    members:
      - BO-01-H2-G
      - BO-01-H2-H
      - BO-01-H2-I

  - swarm_id: AT-01-swarm
    site: AT-01
    members:
      - AT-01-H2-J
      - AT-01-H2-K
      - AT-01-H2-L

roles:
  - role_id: Lead
    description: Primary AE responder, performs intervention, holds central tool tray.
    max_count_per_swarm: 1
    min_count_per_swarm: 1
  - role_id: Assist
    description: Secondary responder, holds backup tools, hand-off partner to Lead.
    max_count_per_swarm: 1
    min_count_per_swarm: 1
  - role_id: Reserve
    description: Perimeter watcher, on-deck Lead, manages physician escalation and FDA RTCT submission.
    max_count_per_swarm: 1
    min_count_per_swarm: 1

role_priority_weights:
  proximity_to_patient: 0.40
  battery_state_of_charge: 0.25
  payload_state: 0.15
  task_affinity: 0.10
  self_confidence: 0.10

rotation_policy:
  cadence_hz: 1
  algorithm: hungarian_bipartite_match
  cool_down_seconds: 5
  minimum_role_dwell_seconds: 3

comms_physical:
  uwb:
    band_ghz: 60
    range_m: 30
    cadence_hz: 200
    round_trip_ms: 5
    used_for:
      - hand_off_request
      - sensor_share
      - proximity_alert
      - shared_world_model_update
  ir_beacon:
    cadence_hz: 1000
    round_trip_ms: 1
    used_for:
      - e_stop_propagation
      - cartesian_frame_alignment

comms_intellectual:
  channel: site_publish_subscribe
  cadence_hz: 1
  contents:
    - self_state
    - sensor_digest
    - task_progress_token
    - self_confidence

camaraderie_invariants:
  no_envelope_violation: true
  handoff_within_seconds: 2
  peer_sensor_in_world_model_within_ticks: 1
  swarm_wide_estop_within_ms: 5
  self_state_publish_hz: 1
  defer_to_lead_during_ae: true
  willing_to_lead_when_asked: true

camarade_aggressiveness:
  default: 1.0
  sweep_values:
    - 0.5
    - 0.75
    - 1.0
    - 1.25

fallback:
  one_robot_down:
    swarm_size: 2
    rotation_axes:
      - Lead
      - Assist
    reserve_action: handled_by_remote_human
  two_robots_down:
    swarm_size: 1
    locked_out_tasks:
      - chest_compressions
      - three_arm_patient_lift
      - cumulative_force_over_15N
    physician_escalation_required: true
```

## Validation Rules

- 4 swarms, 1 per site, 3 members each.
- Role priority weights sum to 1.00.
- The 7 camaraderie invariants must all be enabled by default.
- `camarade_aggressiveness.default` is 1.0; sweep values cover the 4 iteration axis points.

## Notes

- `hungarian_bipartite_match` runs the assignment problem for 3 robots to 3 roles in O(27) per tick; trivial.
- `cool_down_seconds` prevents role thrashing.
- `minimum_role_dwell_seconds` enforces a 3 second minimum tenure in a role.
