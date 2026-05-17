# Authoring Instructions for `schemas/sponsor_acknowledgment.schema.json`

## Purpose

Defines a sponsor acknowledgment record per HR 9505 Real-Time Patient-Sponsor Direct Communication Act. The sponsor must acknowledge a CTCAE grade 3+ AE within 1 hour of the AE event.

## Schema

```
$schema: https://json-schema.org/draft/2020-12/schema
$id: sponsor_acknowledgment
title: Sponsor Acknowledgment
type: object
required:
  - acknowledgment_id
  - ae_id
  - sponsor_id
  - submitted_at_iso
  - acknowledged_at_iso_or_null
  - sla_seconds_elapsed
  - sla_met
properties:
  acknowledgment_id: { type: string, pattern: "^ack-[0-9a-f]{16}$" }
  ae_id: { type: string, pattern: "^ae-[0-9a-f]{16}$" }
  sponsor_id: { type: string }
  submitted_at_iso: { type: string, format: date-time }
  acknowledged_at_iso_or_null: { type: [string, "null"], format: date-time }
  sla_seconds_elapsed: { type: number, minimum: 0 }
  sla_met: { type: boolean }
  channel: { type: string, enum: [secure_email, sponsor_portal_api, secure_pager] }
  notes: { type: string, maxLength: 256 }
additionalProperties: false
```

## Validation Rules

- `sla_met` is true if `sla_seconds_elapsed` is at most 3600.
- `acknowledged_at_iso_or_null` is null until the sponsor responds.

## Notes

- The Reserve robot in the swarm is responsible for emitting this record when it detects the corresponding AE event and a CTCAE grade 3+ grading.
