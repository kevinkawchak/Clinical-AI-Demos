# Authoring Instructions for `schemas/ctcae_grading.schema.json`

## Purpose

Defines a CTCAE grading record produced by `src/ctcae_grader.py`. One record per AE per re-grade event.

## Schema

```
$schema: https://json-schema.org/draft/2020-12/schema
$id: ctcae_grading
title: CTCAE Grading
type: object
required:
  - grading_id
  - ae_id
  - graded_at_iso
  - grader
  - ctcae_version
  - ctcae_grade
  - ctcae_term
  - confidence
properties:
  grading_id: { type: string, pattern: "^grd-[0-9a-f]{16}$" }
  ae_id: { type: string, pattern: "^ae-[0-9a-f]{16}$" }
  graded_at_iso: { type: string, format: date-time }
  grader:
    type: string
    enum: [llm_per_site, on_call_physician, attending_physician, swarm_consensus]
  ctcae_version: { type: string, const: "5.0" }
  ctcae_grade: { type: integer, minimum: 1, maximum: 5 }
  ctcae_term: { type: string }
  confidence: { type: number, minimum: 0.0, maximum: 1.0 }
  rationale: { type: string, maxLength: 512 }
  superseded_by: { type: [string, "null"] }
additionalProperties: false
```

## Validation Rules

- `ctcae_version` is locked to `"5.0"`.
- `ctcae_grade` is 1 to 5.
- `grader` enum includes `swarm_consensus` for when all 3 robots in a camarade swarm independently grade the same AE and the system picks the majority.

## Notes

- The HR 9505 1-hour CTCAE grading SLA applies. The first grading record must arrive within 3600 seconds of `detected_at_iso` from the AE event.
- Re-grades are common as the situation evolves; older grading records are linked via `superseded_by`.
