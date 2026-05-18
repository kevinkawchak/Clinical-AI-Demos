# Authoring Instructions for `schemas/ae_event.schema.json`

## Purpose

Defines an adverse event record. One record per AE detected across the 4-site network during the 168-hour week.

## Schema

```
$schema: https://json-schema.org/draft/2020-12/schema
$id: ae_event
title: Adverse Event
type: object
required:
  - ae_id
  - patient_id
  - site
  - detected_at_iso
  - detection_source
  - ae_type
  - initial_ctcae_grade
  - responding_swarm
  - first_robot_arrival_iso
  - resolution_iso_or_null
properties:
  ae_id: { type: string, pattern: "^ae-[0-9a-f]{16}$" }
  patient_id: { type: string, pattern: "^PAT-NET-001-P[0-9]{3}$" }
  site: { type: string, enum: [SF-01, SD-01, BO-01, AT-01] }
  detected_at_iso: { type: string, format: date-time }
  detection_source:
    type: string
    enum: [wearable_device, patient_self_report, ehr_signal, sponsor_rtct_mandate, doctor_observation]
  ae_type:
    type: string
    enum:
      - cytokine_release_syndrome
      - anaphylaxis
      - syncope
      - hypotension
      - hypertension_crisis
      - hypoxia
      - bleeding
      - thrombosis
      - infection_sepsis
      - seizure
      - cardiac_arrest
      - pulmonary_embolism
      - other
  initial_ctcae_grade: { type: integer, minimum: 1, maximum: 5 }
  responding_swarm:
    type: array
    minItems: 3
    maxItems: 3
    items: { type: string }
  first_robot_arrival_iso: { type: string, format: date-time }
  resolution_iso_or_null:
    type: [string, "null"]
    format: date-time
  physician_escalation_triggered: { type: boolean }
  fda_rtct_submission_id: { type: string }
  sponsor_acknowledgment_id: { type: string }
  notes: { type: string, maxLength: 1024 }
additionalProperties: false
```

## Validation Rules

- `patient_id` follows synthetic PAT-NET-001-PNNN pattern.
- `responding_swarm` always has exactly 3 robot IDs (all 3 camarades of the site swarm respond).
- `physician_escalation_triggered` is true if `initial_ctcae_grade` is 3 or higher.
- `fda_rtct_submission_id` is required if `initial_ctcae_grade` is 2 or higher.

## Notes

- About 84 AE records expected per 168-hour week (3 AEs/day x 4 sites x 7 days).
- About 24 SAE records (CTCAE grade 3+) expected.
- Stored in `data/week_ae_events.parquet` plus mirrored to JSONL for streaming.
