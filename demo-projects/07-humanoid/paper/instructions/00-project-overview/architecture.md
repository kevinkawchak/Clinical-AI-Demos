# Architecture: Three Camarade H2 Humanoids per Site, Four Sites, One On-Prem LLM per Site

This document defines the system architecture that the future code generation pass must implement.

## Layer 1: Site

There are 4 PAT-NET-001 sites: San Francisco (SF-01), San Diego (SD-01), Boston (BO-01), Atlanta (AT-01). Each site is fully self-sufficient for AE response:

- 3 dedicated Unitree H2 humanoids parked at standby pods inside the site
- 1 dedicated Claude Opus 4.7 1M on-prem appliance with 200 ms median latency
- 1 dedicated broadcast bus that fans the per-tick command set to all 3 robots
- 1 dedicated sensor aggregator that joins per-robot sensor returns into a shared world model
- 1 dedicated AE intake feed from wearable devices, EHR, and patient self-report

There is no cross-site H2 transit in the v0.3.0 design. The original prompt 07 modeled cross-site van transit; in v0.3.0 the cross-site coordination bus carries only de-identified summaries for shared learning, not physical robot transfer. This reduces complexity and makes the swarm camaraderie at each site the focus of the simulation.

## Layer 2: Swarm at One Site

The 3 H2 humanoids at one site form a swarm. The swarm has:

- A static identity per robot: H2-A, H2-B, H2-C inside the site naming space (SF-01-H2-A through SF-01-H2-C, SD-01-H2-A through SD-01-H2-C, and so on)
- A dynamic role at every tick: Lead, Assist, Reserve
- A live peer-state model with 3 entries (self plus 2 peers), each with x, y, z, joint pose, battery, current task token, and current health status
- A live patient-state model with up to 4 entries during an AE (the patient plus up to 3 doctors, nurses, or attending physicians)

The roles rotate based on a priority score that combines proximity to the patient, battery, payload state, and task affinity. The Lead is responsible for the primary intervention. The Assist holds tools and provides backup. The Reserve provides perimeter security, monitors the patient remotely, and is the on-deck Lead.

## Layer 3: LLM Broadcaster

The per-site Claude Opus 4.7 1M instance produces one broadcast command per tick at 1 Hz. Each broadcast contains 3 named sub-commands (one for H2-A, one for H2-B, one for H2-C). The broadcast is published to the site bus in one atomic write. All 3 robots receive identical timestamps and acknowledge in the next tick.

The LLM has read access to the shared world model (patient state, peer-robot state, attending physician state) and write access to the broadcast topic only. The LLM never writes directly to a robot controller. The robot controllers subscribe to the broadcast topic and run their per-robot 10 Hz motion loop independently against the most recent broadcast tick.

## Layer 4: Physical Communication

The 3 robots within a site talk to each other physically through:

- 60 GHz ultra-wideband peer mesh at 5 ms round-trip for hand-off requests, sensor sharing, and proximity alerts
- IR-band line-of-sight beacons at 1 ms round-trip for E-stop propagation and shared cartesian frame alignment

Physical communication is independent of the Claude Code server. If the on-prem LLM is unreachable, the robots maintain a degraded swarm using the last received broadcast and live peer messaging only. This is the fallback mode.

## Layer 5: Intellectual Communication

The 3 robots within a site share intellectual context through:

- The on-prem Claude Code server compute fabric. Each robot publishes its current task token, its sensor digest, and its self-reported confidence to the shared world model.
- The Claude Opus 4.7 1M instance integrates the 3 streams into a single tick decision and broadcasts the next command.

Intellectual communication is the high-level loop. Physical communication is the low-level loop. The two run concurrently and do not block each other.

## Layer 6: Cross-Site Coordination Bus

The 4 sites talk to a central on-prem Claude Code compute bus that carries:

- De-identified hourly summaries (AE counts by CTCAE grade, response time statistics, robot battery state of fleet, escalation counts)
- Federated learning gradient updates (optional, post-hoc, batched per day)
- Zero PHI; all patient identifiers are removed before cross-site transit

The cross-site bus does not drive any per-tick decision. It is only used for shared learning and for fleet-level reporting.

## Decision Cadence Summary

| Layer | Cadence | Latency Budget | Role |
|-------|---------|----------------|------|
| Sensor aggregator | 10 Hz | 5 ms | Build per-site world model |
| LLM broadcaster | 1 Hz | 200 ms | Author tick command for all 3 robots |
| Robot controller | 10 Hz | 5 ms | Drive joints from last broadcast |
| 60 GHz UWB peer mesh | 200 Hz | 5 ms round trip | Hand-off, sensor share, proximity |
| IR beacon | 1000 Hz | 1 ms round trip | E-stop and frame alignment |
| Cross-site summary | 1 per hour | 30 s | Fleet-level reporting |

## Failure Modes

- Site LLM down: robots degrade to last broadcast plus peer mesh. The Reserve becomes Lead if the original Lead loses LLM contact for more than 3 s.
- Single robot down: swarm contracts to 2 robots. Roles re-elect among the remaining 2 every tick.
- Two robots down: swarm contracts to 1 robot. That robot operates within a strict reduced-scope protocol that locks out shared force tasks (chest compressions, 3-arm patient lift) and triggers physician escalation immediately.
- 60 GHz UWB mesh down: physical comms fall back to IR beacons only. Hand-off requests gate on a 100 ms confirmation rather than 5 ms.
- IR beacon down: E-stop falls back to the 60 GHz channel with a 10 ms ceiling.

## Inputs

The future Claude Code Opus 4.7 1M Max session must read these companion repository files:

- `kevinkawchak/physical-ai-oncology-trials/new-trial/national-24-7-trial/README.md`
- `kevinkawchak/physical-ai-oncology-trials/new-trial/national-24-7-trial/FDA-April-2026/`
- `kevinkawchak/physical-ai-oncology-trials/new-trial/national-24-7-trial/Background-A/`
- `kevinkawchak/physical-ai-oncology-trials/new-trial/national-24-7-trial/Background-B/`
- `kevinkawchak/physical-ai-oncology-trials/new-trial/national-24-7-trial/hour-00/` through `hour-55/` (verbatim)
- `kevinkawchak/physical-ai-oncology-trials/patients/paper/full-paper/sections/hr_9505_realtime_sponsor.tex`
- `kevinkawchak/physical-ai-oncology-trials/patients/paper/full-paper/sections/hr_9504_error_reduction.tex`
- `kevinkawchak/physical-ai-oncology-trials/patient-journey/stage_09_surveillance.py`
- `kevinkawchak/physical-ai-oncology-trials/agentic-ai/examples-agentic-ai/03_realtime_adaptive_treatment_agent.py`
- `kevinkawchak/physical-ai-oncology-trials/agentic-ai/examples-agentic-ai/05_safety_constrained_agent_executor.py`
- `kevinkawchak/physical-ai-oncology-trials/regulatory/ich-gcp/gcp_compliance_checker.py`
- `kevinkawchak/physical-ai-oncology-trials/regulatory/fda-compliance/fda_submission_tracker.py`
- `kevinkawchak/physical-ai-oncology-trials/regulatory-submit/audit_trail.py`
- `kevinkawchak/physical-ai-oncology-trials/privacy/breach-response/breach_response_protocol.py`
- `kevinkawchak/physical-ai-oncology-trials/unification/usl/humanoids/usl_humanoid_scoring.py`
- `kevinkawchak/physical-ai-oncology-trials/competitions/instructions/chunking_strategy.md`
- `kevinkawchak/physical-ai-oncology-trials/competitions/instructions/competition_protocol.md`

The future session must NOT read `extra-hours/` from the companion repository. The original prompt 07 included `extra-hours/`; v0.3.0 explicitly excludes it.
