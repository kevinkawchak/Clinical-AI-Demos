# Authoring Instructions for `config/escalation_rules.yaml`

The future session writes this YAML at `demo-projects/07-humanoid/paper/instructions/config/escalation_rules.yaml` during Commit 1 of 7.

## Purpose

Defines the rules that trigger human-physician escalation and FDA RTCT submission.

## Fields

```
ctcae_escalation:
  grade_threshold: 3
  action:
    - notify_on_call_physician
    - prepare_iv_access_tray
    - hold_iv_access_until_physician_present
    - log_to_audit_chain
  notification_channel: secure_pager_plus_phone
  ack_required_seconds: 60

fda_rtct_1hr_submission:
  trigger: ctcae_grade_2_or_higher
  sla_seconds: 3600
  payload_schema: schemas/fda_rtct_submission.schema.json
  hash_chain_enabled: true
  signing: ed25519_per_site
  source: hr_9505_realtime_sponsor.tex

sponsor_acknowledgment:
  trigger: ctcae_grade_3_or_higher
  sla_seconds: 3600
  payload_schema: schemas/sponsor_acknowledgment.schema.json
  source: hr_9505_realtime_sponsor.tex

swarm_fault_escalation:
  one_robot_fault_action:
    - elevate_reserve_to_lead
    - increase_polling_hz: 2
    - log_fault_to_audit_chain
  two_robot_fault_action:
    - notify_physician_immediately
    - lock_out_shared_force_tasks
    - request_physician_on_site_within_seconds: 300
  three_robot_fault_action:
    - notify_physician_immediately
    - notify_on_call_director
    - swarm_unavailable_flag: true

perimeter_breach_escalation:
  trigger: unauthorized_person_within_meters: 2.0
  action:
    - reserve_robot_intercepts
    - lead_continues_intervention
    - log_breach_to_audit_chain

battery_low_escalation:
  threshold_percent: 25
  action:
    - elevate_reserve_to_lead
    - swap_hot_battery_within_seconds: 90
    - log_swap_to_audit_chain
```

## Validation Rules

- `grade_threshold` is 3 for CTCAE escalation.
- `sla_seconds` is 3600 (1 hour) for FDA RTCT submission and sponsor acknowledgment.
- Battery threshold is 25 percent.
- All escalation paths log to the audit chain.

## Notes

- The `hash_chain_enabled` flag enables a Merkle-style audit chain rooted at the site daily. The root is published to the cross-site bus once per day for tamper detection.
- The `signing: ed25519_per_site` setting requires each site to have a long-lived ed25519 key pair. The public key is in `config/network.yaml` extensions in commit 6.
