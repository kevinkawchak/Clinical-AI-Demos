# Authoring Instructions for `config/h2_humanoid.yaml`

The future session writes this YAML at `demo-projects/07-humanoid/paper/instructions/config/h2_humanoid.yaml` during Commit 1 of 7.

## Purpose

Defines the 12 Unitree H2 humanoids across the 4 sites. Each robot has a stable identity, a camarade group, and inheritable specs.

## Fields

```
platform: Unitree H2
specs:
  dof: 39
  height_m: 1.8
  mass_kg: 70
  payload_per_arm_kg: 10
  battery_hours: 5
  battery_hotswap: true
  ingress_protection: IP65
  outdoor_rated: true
  e_stop_latency_ms: 5
  per_arm_force_compression_N: 15
  per_arm_force_default_N: 5
  inter_robot_min_distance_rest_m: 1.2
  inter_robot_min_distance_handoff_m: 0.4
  cumulative_cross_robot_force_N: 22

response_kit:
  - epinephrine_auto_injector
  - iv_access_tray
  - vagus_nerve_stimulator_probe
  - portable_pulse_oximeter
  - portable_ecg
  - emergency_airway_kit

robots:
  # San Francisco swarm
  - robot_id: SF-01-H2-A
    site: SF-01
    camarade_group: SF-01-swarm
    starting_role: Lead
    serial_synthetic: H2-2026-001
  - robot_id: SF-01-H2-B
    site: SF-01
    camarade_group: SF-01-swarm
    starting_role: Assist
    serial_synthetic: H2-2026-002
  - robot_id: SF-01-H2-C
    site: SF-01
    camarade_group: SF-01-swarm
    starting_role: Reserve
    serial_synthetic: H2-2026-003

  # San Diego swarm
  - robot_id: SD-01-H2-D
    site: SD-01
    camarade_group: SD-01-swarm
    starting_role: Lead
    serial_synthetic: H2-2026-004
  - robot_id: SD-01-H2-E
    site: SD-01
    camarade_group: SD-01-swarm
    starting_role: Assist
    serial_synthetic: H2-2026-005
  - robot_id: SD-01-H2-F
    site: SD-01
    camarade_group: SD-01-swarm
    starting_role: Reserve
    serial_synthetic: H2-2026-006

  # Boston swarm
  - robot_id: BO-01-H2-G
    site: BO-01
    camarade_group: BO-01-swarm
    starting_role: Lead
    serial_synthetic: H2-2026-007
  - robot_id: BO-01-H2-H
    site: BO-01
    camarade_group: BO-01-swarm
    starting_role: Assist
    serial_synthetic: H2-2026-008
  - robot_id: BO-01-H2-I
    site: BO-01
    camarade_group: BO-01-swarm
    starting_role: Reserve
    serial_synthetic: H2-2026-009

  # Atlanta swarm
  - robot_id: AT-01-H2-J
    site: AT-01
    camarade_group: AT-01-swarm
    starting_role: Lead
    serial_synthetic: H2-2026-010
  - robot_id: AT-01-H2-K
    site: AT-01
    camarade_group: AT-01-swarm
    starting_role: Assist
    serial_synthetic: H2-2026-011
  - robot_id: AT-01-H2-L
    site: AT-01
    camarade_group: AT-01-swarm
    starting_role: Reserve
    serial_synthetic: H2-2026-012
```

## Validation Rules

- Exactly 12 robots.
- Exactly 4 camarade groups, each with 3 robots.
- Every camarade group has 1 Lead, 1 Assist, 1 Reserve at start.
- Synthetic serials only.

## Notes

- The `starting_role` is the role at simulation t=0. Roles rotate at every tick based on the priority score in `swarm_coordination.yaml`.
- The `camarade_group` field is the foreign key from `swarm_coordination.yaml` and is required.
- The `response_kit` is shared across all 12 robots; each robot carries the full kit.
