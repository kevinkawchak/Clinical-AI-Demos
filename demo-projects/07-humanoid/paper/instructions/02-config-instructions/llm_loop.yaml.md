# Authoring Instructions for `config/llm_loop.yaml`

The future session writes this YAML at `demo-projects/07-humanoid/paper/instructions/config/llm_loop.yaml` during Commit 1 of 7.

## Purpose

Defines the per-site Claude Opus 4.7 1M planning loop. The LLM emits 3 sub-commands per tick in one broadcast.

## Fields

```
llm:
  model: claude-opus-4-7
  context_window: 1000000
  deployment: on_prem
  latency_budget_ms: 200
  cadence_hz: 1
  redundant_failover_within_site: true

prompt:
  system_prompt_file: src/prompt_frozen.md
  reasoning_token_budget: 4096
  temperature_default: 0.0
  temperature_sweep:
    - 0.0
    - 0.1
    - 0.2
    - 0.3

broadcast:
  payload_kind: llm_decision
  sub_command_count: 3
  sub_command_target_roles:
    - Lead
    - Assist
    - Reserve
  synergy_score_required: true

world_model:
  patient_state_fields:
    - patient_id
    - vitals
    - ctcae_grade_current
    - position_xyz
    - ae_type
    - consent_state
  doctor_state_fields:
    - doctor_id
    - position_xyz
    - role
    - command_authority
  peer_robot_state_fields:
    - robot_id
    - position_xyz
    - joint_pose_summary
    - battery_soc
    - task_token
    - self_confidence

cross_site_observation:
  enabled: true
  read_only: true
  cadence_seconds: 3600
  contents:
    - peer_site_response_time_p95
    - peer_site_escalation_count
    - peer_site_swarm_uptime_percent

llm_response_schema_file: schemas/llm_decision.schema.json

fallback_no_llm:
  hold_last_broadcast_seconds: 3
  after_hold_elevate_reserve_to_lead: true
  after_hold_increase_motion_cadence_to_hz: 20
```

## Validation Rules

- `sub_command_count` equals 3 (one sub-command per robot per tick).
- `temperature_default` is 0.0 (deterministic).
- `latency_budget_ms` is 200.
- `llm_response_schema_file` points to the JSON Schema file authored in commit 2.

## Notes

- The cross-site observation channel feeds the LLM hourly digests from the other 3 sites. The LLM may use these for context but does not act on them directly.
- The fallback path triggers if the LLM is unreachable for 3 seconds. The Reserve becomes Lead; the motion cadence doubles to absorb the lost LLM tick.
