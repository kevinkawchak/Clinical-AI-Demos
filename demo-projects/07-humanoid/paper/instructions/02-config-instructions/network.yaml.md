# Authoring Instructions for `config/network.yaml`

The future Claude Code Opus 4.7 1M Max session writes this YAML at `demo-projects/07-humanoid/paper/instructions/config/network.yaml` during Commit 1 of 7.

## Purpose

Defines the PAT-NET-001 4-site continental network. One file, one YAML document (no `---` document separator). UTF-8.

## Fields

```
network_id: PAT-NET-001
name: Physical AI Oncology Trial Network 001
release_version: 0.3.0
release_date: 2026-05-17

sites:
  - site_id: SF-01
    name: San Francisco
    timezone: America/Los_Angeles
    address_synthetic: 1 Mission Center, San Francisco, CA
    enrolled_patients: 50
    active_trials: 5
    h2_count: 3
    llm_instance_count: 1
    broadcast_bus_uri: tcp://sf01-broadcast:5001

  - site_id: SD-01
    name: San Diego
    timezone: America/Los_Angeles
    address_synthetic: 1 Torrey Pines, San Diego, CA
    enrolled_patients: 50
    active_trials: 5
    h2_count: 3
    llm_instance_count: 1
    broadcast_bus_uri: tcp://sd01-broadcast:5001

  - site_id: BO-01
    name: Boston
    timezone: America/New_York
    address_synthetic: 1 Longwood Avenue, Boston, MA
    enrolled_patients: 50
    active_trials: 5
    h2_count: 3
    llm_instance_count: 1
    broadcast_bus_uri: tcp://bo01-broadcast:5001

  - site_id: AT-01
    name: Atlanta
    timezone: America/New_York
    address_synthetic: 1 Emory Lane, Atlanta, GA
    enrolled_patients: 50
    active_trials: 5
    h2_count: 3
    llm_instance_count: 1
    broadcast_bus_uri: tcp://at01-broadcast:5001

cross_site_bus:
  enabled: true
  protocol: protobuf
  cadence_seconds: 3600
  payload_kind: de_identified_summary
  payload_max_kb: 50
  phi_egress: forbidden

monitoring_window_hours: 168
llm_cadence_hz: 1
motion_cadence_hz: 10
uwb_cadence_hz: 200
ir_beacon_cadence_hz: 1000
```

## Validation Rules

- 4 sites, no more, no less.
- Each site has exactly 3 H2 robots and exactly 1 LLM instance.
- `monitoring_window_hours` is 168.
- `phi_egress` on cross_site_bus must be `forbidden`.
- The total enrolled_patients across sites is 200.

## Notes

- Single document YAML. Do not include a `---` separator at the top.
- Synthetic addresses only. No real facility identifiers.
- The `broadcast_bus_uri` host names are placeholders; the docker-compose service names match.
