# Authoring Instructions for `schemas/fda_rtct_submission.schema.json`

## Purpose

Defines an FDA RTCT submission record per FDA April 2026 guidance. CTCAE grade 2 or higher AEs are submitted to the FDA RTCT pilot within 1 hour.

## Schema

```
$schema: https://json-schema.org/draft/2020-12/schema
$id: fda_rtct_submission
title: FDA RTCT Submission
type: object
required:
  - submission_id
  - ae_id
  - site
  - submitted_at_iso
  - fda_rtct_endpoint
  - sla_seconds_elapsed
  - sla_met
  - audit_chain_prev_hash
properties:
  submission_id: { type: string, pattern: "^fda-[0-9a-f]{16}$" }
  ae_id: { type: string, pattern: "^ae-[0-9a-f]{16}$" }
  site: { type: string, enum: [SF-01, SD-01, BO-01, AT-01] }
  submitted_at_iso: { type: string, format: date-time }
  fda_rtct_endpoint: { type: string, format: uri }
  sla_seconds_elapsed: { type: number, minimum: 0 }
  sla_met: { type: boolean }
  audit_chain_prev_hash: { type: string, pattern: "^[0-9a-f]{64}$" }
  hash_chain_signature: { type: string }
  notes: { type: string, maxLength: 512 }
additionalProperties: false
```

## Validation Rules

- `sla_met` is true if `sla_seconds_elapsed` is at most 3600.
- `audit_chain_prev_hash` and `hash_chain_signature` are required (HR 9504 Physical AI Clinical Error Reduction Act).

## Notes

- The FDA RTCT endpoint is a synthetic URL in the simulated runs. In production it would be the FDA pilot intake API.
