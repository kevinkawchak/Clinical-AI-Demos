# Authoring Instructions for `config/site_coordination.yaml`

The future session writes this YAML at `demo-projects/07-humanoid/paper/instructions/config/site_coordination.yaml` during Commit 1 of 7.

## Purpose

Defines the per-site coordination policy: how the on-prem Claude Opus 4.7 1M instance at a site broadcasts to its 3 robots and how cross-site summaries are produced. This file is about within-site coordination plus cross-site digest emission. It is paired with `swarm_coordination.yaml` for the inter-robot swarm logic.

## Fields

```
broadcast:
  cadence_hz: 1
  payload_format: jsonl
  publish_topic: site/{site_id}/broadcast
  qos: at_least_once
  redundant_failover_within_site: true
  fan_out_targets: 3
  ack_timeout_ms: 500
  ack_required_count: 3

degraded_modes:
  no_llm_for_seconds: 3
  no_llm_action: hold_last_broadcast_and_elevate_reserve_to_lead
  no_peer_uwb_for_seconds: 1
  no_peer_uwb_action: fall_back_to_ir_beacon_handoff_at_100ms
  no_ir_beacon_for_seconds: 0.5
  no_ir_beacon_action: fall_back_to_uwb_e_stop_with_10ms_ceiling

cross_site_summary:
  cadence_seconds: 3600
  fields:
    - ae_count_by_grade
    - response_time_p50_seconds
    - response_time_p95_seconds
    - escalation_count
    - fda_rtct_1hr_compliance_rate
    - swarm_uptime_percent
    - peer_handoff_p95_seconds
    - camaraderie_invariants_pass_rate
    - fleet_battery_p10_percent
  egress_policy: phi_forbidden
  signing: ed25519_per_site

llm_resource_share:
  central_compute_bus_uri: tcp://central-compute:5050
  shared_workspace_quota_mb: 5000
  central_role: passive_observer_only
  central_writes_to_robots: forbidden
```

## Validation Rules

- `fan_out_targets` equals 3 (3 robots per site).
- `ack_required_count` equals 3 (all 3 robots must acknowledge each broadcast within the timeout).
- `egress_policy` on cross_site_summary equals `phi_forbidden`.
- `central_writes_to_robots` equals `forbidden` (the central compute bus does not bypass the per-site broadcaster).

## Notes

- The central compute bus is for shared learning and fleet-level reporting only. It does not participate in real-time AE response.
- The degraded modes spell out exactly what the swarm falls back to when components are unreachable. Test cases in commit 6 exercise each mode.
