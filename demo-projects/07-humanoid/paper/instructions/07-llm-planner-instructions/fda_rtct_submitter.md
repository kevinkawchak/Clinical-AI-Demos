# Authoring Instructions for `src/fda_rtct_submitter.py`

The future session writes this Python module during Commit 4 of 7.

## Purpose

Submits CTCAE grade 2 or higher AE records to the FDA RTCT pilot intake API within 1 hour per HR 9505 SLA. Emits records matching `schemas/fda_rtct_submission.schema.json`.

## Key Behavior

- Watches `data/week_ae_events.parquet` plus `data/week_ctcae_gradings.parquet` for grade 2+ events.
- Within 60 seconds of grading, constructs an FDA RTCT submission payload.
- POSTs to the simulated endpoint `https://rtct-pilot.fda.gov.simulated/api/v1/submit`.
- Records the submission with hash chain and ed25519 signature.
- Tracks SLA compliance: `sla_met` is true if submitted within 3600 seconds of AE detection.

## Required Interfaces

```
class FDARTCTSubmitter:
    def __init__(self, site_id: str, key_path: pathlib.Path) -> None: ...
    def watch_and_submit(self, ae_events: list[dict], gradings: list[dict]) -> list[dict]: ...
    def build_payload(self, ae: dict, grading: dict) -> dict: ...
    def sign(self, payload: dict) -> str: ...
    def submit(self, payload: dict) -> dict: ...
```

## Validation Rules

- SLA met if submission within 3600 seconds.
- Payload includes the audit chain previous-hash plus the ed25519 signature.
- Synthetic FDA endpoint in simulation; real endpoint in production.

## Notes

- The Reserve robot in the camarade swarm is responsible for invoking this submitter. Lead and Assist focus on patient care.
- The 1-hour SLA is the binding patient right under HR 9505 Real-Time Patient-Sponsor Direct Communication Act.
