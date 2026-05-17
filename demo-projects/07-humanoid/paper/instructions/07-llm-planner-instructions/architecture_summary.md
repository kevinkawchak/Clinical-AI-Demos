# LLM Planner Architecture Summary

This is a single-page summary of the LLM planner pieces in commit 4. The future session uses this as a coding compass.

## Tick by Tick (Inside One Site)

```
t = 0
  +-> sensor aggregator collects readings from 3 robots
  +-> peer state tracker updates self plus 2 peers per robot
  +-> world model snapshot built (patient, doctors, peer robots)
  +-> LLM planner builds prompt from snapshot
  +-> LLM planner calls on-prem Claude Opus 4.7 1M with budget 200 ms
  +-> response parsed into llm_decision record with 3 sub_commands
  +-> validate against schemas/llm_decision.schema.json
  +-> broadcaster publishes to site/{site_id}/broadcast
  +-> dispatcher fans out 3 humanoid_command records
  +-> all 3 robots ack within 500 ms
  +-> audit chain prev hash advances

t = 1
  +-> repeat
```

## Two Important Properties

1. The LLM emits a single broadcast carrying 3 sub-commands. It never calls the LLM 3 times. This enforces shared compute and the camarade pattern.
2. The broadcast is atomic and the audit chain links sequential broadcasts. The site can prove which command was active at any given tick.

## Module Roles

| Module | Role | Cadence |
|--------|------|---------|
| `src/llm_planner.py` | Builds prompt, calls LLM, parses response, validates | 1 Hz |
| `src/broadcaster.py` | Publishes broadcast, tracks acks, writes audit log | 1 Hz |
| `src/h2_dispatcher.py` | Fans out broadcast into 3 humanoid_command records | 1 Hz |
| `src/swarm_coordinator.py` | Computes priority score, assigns roles, checks invariants | 1 Hz |
| `src/peer_state_tracker.py` | Maintains self plus 2 peer state model | 1 Hz |
| `src/comms_physical.py` | UWB and IR beacon messages | 200 Hz / 1000 Hz |
| `src/comms_intellectual.py` | Pub-sub state and progress | 1 Hz |
| `src/sensor_to_xyz.py` | Projects sensors into shared cartesian frame | 10 Hz |
| `src/cartesian_planner.py` | Authors smooth trajectories | On demand |
| `src/xyz_safety.py` | Validates cartesian commands | 1 Hz |
| `src/ctcae_grader.py` | Grades AEs per CTCAE v5.0 | On AE |
| `src/fda_rtct_submitter.py` | Submits AE to FDA pilot within 1 hour | On AE grade 2+ |
| `src/physician_escalation.py` | Pages physician on grade 3+ | On AE grade 3+ |
| `src/cross_site_bus.py` | Aggregates de-identified hourly summaries | 1 per hour |

## Glue: `src/site_runtime.py`

A small entry point that wires the above modules together for one site. Authored in commit 4. Reads `config/network.yaml` to find the site, builds the world model, starts the LLM planner loop, listens for AE events from the ingest service.

```
from h2_dispatcher import H2Dispatcher
from llm_planner import LLMPlanner
from broadcaster import Broadcaster
from swarm_coordinator import SwarmCoordinator
from peer_state_tracker import PeerStateTracker


def run_site(site_id: str, config_dir: pathlib.Path, output_dir: pathlib.Path) -> None:
    planner = LLMPlanner(site_id, config_dir)
    broadcaster = Broadcaster(site_id, output_dir / f"{site_id}_llm_decisions.jsonl")
    dispatcher = H2Dispatcher(site_id, config_dir / "network.yaml")
    swarm = SwarmCoordinator(f"{site_id}-swarm", config_dir / "swarm_coordination.yaml")
    # build per robot peer state trackers
    # subscribe to sensor stream, AE intake feed
    # at every 1 Hz tick: build world model, plan, publish, dispatch, collect acks
```

## Notes

- This file is the integration test reading aid. It does not introduce new behavior.
- The actual `site_runtime.py` source is authored as part of commit 4; this document describes the wiring.
