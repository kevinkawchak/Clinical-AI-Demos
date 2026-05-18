# Authoring Instructions for `schemas/physician_escalation.schema.json`

## Purpose

Defines a human physician escalation record. CTCAE grade 3+ AEs require physician escalation before any IV access or invasive intervention.

## Schema

```
$schema: https://json-schema.org/draft/2020-12/schema
$id: physician_escalation
title: Physician Escalation
type: object
required:
  - escalation_id
  - ae_id
  - physician_id
  - paged_at_iso
  - ack_at_iso_or_null
  - on_site_at_iso_or_null
  - response_seconds
  - ack_within_60s
properties:
  escalation_id: { type: string, pattern: "^esc-[0-9a-f]{16}$" }
  ae_id: { type: string, pattern: "^ae-[0-9a-f]{16}$" }
  physician_id: { type: string }
  physician_role:
    type: string
    enum: [oncologist, er_physician, palliative_care, on_call_director, attending_nurse]
  paged_at_iso: { type: string, format: date-time }
  ack_at_iso_or_null: { type: [string, "null"], format: date-time }
  on_site_at_iso_or_null: { type: [string, "null"], format: date-time }
  response_seconds: { type: number, minimum: 0 }
  ack_within_60s: { type: boolean }
  channel: { type: string, enum: [secure_pager, phone, sms] }
  notes: { type: string, maxLength: 512 }
additionalProperties: false
```

## Validation Rules

- `ack_within_60s` is true if the difference between `ack_at_iso_or_null` and `paged_at_iso` is at most 60 seconds.

## Notes

- The Reserve robot emits this record on CTCAE grade 3+ detection.
- IV access is blocked at the swarm level until the physician acknowledges or arrives on-site.
