# Authoring Instructions: Shared Cloud Compute from a Central On-Premises Claude Code Server

The future session implements this architecture pattern in `src/llm_planner.py`, `src/comms_intellectual.py`, and `src/cross_site_bus.py`. This is one of the key v0.3.0 changes.

## Purpose

Describes how the per-site Claude Opus 4.7 1M deployments share a central compute fabric. Each site runs its own on-prem Anthropic appliance for local AE response; the central fabric is read-only for cross-site learning and fleet-level reporting.

## Architecture

```
+-------------------+         +-------------------+
| Site SF-01 LLM    |         | Site SD-01 LLM    |
| Claude Opus 4.7   |         | Claude Opus 4.7   |
| on-prem appliance |         | on-prem appliance |
| broadcasts to 3   |         | broadcasts to 3   |
| robots at 1 Hz    |         | robots at 1 Hz    |
+-------------------+         +-------------------+
        |                              |
        |  de-identified hourly        |
        |  summary (no PHI)            |
        v                              v
   +------------------------------------+
   | Central On-Prem Claude Code Server |
   | shared compute bus                 |
   | read-only observer for sites       |
   | aggregates cross-site metrics      |
   | publishes fleet learning gradients |
   +------------------------------------+
        ^                              ^
        |                              |
+-------------------+         +-------------------+
| Site BO-01 LLM    |         | Site AT-01 LLM    |
| Claude Opus 4.7   |         | Claude Opus 4.7   |
+-------------------+         +-------------------+
```

## Key Properties

1. The central server NEVER writes to any robot. It is a passive observer.
2. The central server only receives de-identified hourly summaries. No PHI traverses the bus.
3. The central server is the source of fleet-level metrics for the dashboard and the comparison report.
4. The central server hosts the shared Python compute kernel that LLM planners may consult for cross-site analytics.
5. If the central server is unreachable, every site continues independently. The local broadcast loop is unaffected.

## Implementation

- `src/cross_site_bus.py` runs on the central server. It accepts hourly summary POSTs from each site, validates them against `schemas/cross_site_summary.schema.json` (added in commit 6), and writes them to a shared DuckDB store.
- `src/llm_planner.py` may query the central server's read-only API for cross-site context but never depends on it for the per-tick broadcast.
- `src/comms_intellectual.py` uses a separate channel for the intra-site pub-sub; it does not talk to the central server.

## Validation Rules

- The central server never writes to a robot. All robot commands flow only through the per-site broadcasters.
- The cross-site bus has `phi_egress: forbidden` enforced via a payload allowlist.
- The cross-site summary cadence is 1 per hour; faster cadences are rejected to prevent inference of patient identity.

## Notes

- This pattern matches the federated learning architecture in `physical-ai-oncology-trials/federation/` but is specialized for AE response.
- The shared compute fabric is the substrate for the intellectual communication channel between robots within a site. Inter-site is observational only.
