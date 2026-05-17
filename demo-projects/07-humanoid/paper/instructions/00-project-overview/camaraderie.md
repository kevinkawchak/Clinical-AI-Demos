# Camaraderie

The word camarade comes from the Spanish camarada, originally meaning a person who shares a room. In the context of these instructions, camarade means a robot that shares the AE scene with two peers and treats those peers as first-class actors in every decision.

Camaraderie is the central design property of the v0.3.0 swarm. Every file the future code generation session authors must reflect camaraderie. This document lists what that means concretely.

## In Configuration

- `config/swarm_coordination.yaml` defines named camarade groups: SF-01-swarm, SD-01-swarm, BO-01-swarm, AT-01-swarm. Each group has 3 robot IDs.
- `config/h2_humanoid.yaml` lists 12 humanoids, each tagged with a `camarade_group` field referencing the swarm it belongs to.
- `config/escalation_rules.yaml` includes peer-fault rules: if any robot in a camarade group reports a fault, the other 2 increase their tick polling rate from 1 Hz to 2 Hz for the next 60 seconds.

## In Schemas

- `schemas/humanoid_command.schema.json` includes a `peer_robot_ids` array with the 2 peer IDs, ensuring every command is aware of its 2 camarades.
- `schemas/swarm_message.schema.json` is the dedicated camarade peer-to-peer message envelope.
- `schemas/robot_camarade_state.schema.json` is a 1-per-robot state record published at 1 Hz with self_state plus peer_state_a plus peer_state_b.
- `schemas/ae_event.schema.json` includes a `responding_swarm` field with 3 robot IDs.
- `schemas/llm_decision.schema.json` is a 3-sub-command broadcast envelope. Each broadcast has 3 named sub-commands one per camarade. The broadcast also includes a `synergy_score` field measuring the expected camarade benefit over a single-robot response.

## In Source Code

- `src/swarm_coordinator.py` is the dedicated camaraderie logic module. It implements the priority score for role rotation, the peer-aware policy adapter, and the camaraderie invariants checker.
- `src/h2_dispatcher.py` accepts a 3-robot atomic broadcast rather than a 1-robot command at a time.
- `src/llm_planner.py` emits 3 sub-commands per tick in a single LLM call, not 3 separate calls.
- `src/comms_physical.py` handles the 60 GHz UWB peer mesh and the IR beacon for camarade-to-camarade physical communication.
- `src/comms_intellectual.py` handles the on-prem Claude Code compute fabric publish-subscribe channel for camarade-to-camarade intellectual communication.
- `src/peer_state_tracker.py` maintains the 3-entry peer state model per robot (self, peer_a, peer_b).
- `src/robot_loop.cpp` implements the 5 ms swarm-wide E-stop propagation from any camarade.

## In Iteration

- The 32 iteration sweep parameterizes camaraderie aggressiveness via a `camarade_aggressiveness` axis in `iterations.yaml`. Values run 0.5, 0.75, 1.0, 1.25. At 0.5, robots defer less to peers and act more independently. At 1.25, robots wait more for peer confirmation. The expected sweet spot is around 1.0.
- Each iteration outputs a `camaraderie_score` per AE, computed from the 7 camaraderie invariants pass rate.

## In Comparison

- `comparison_methodology.md` adds a Camaraderie dimension with weight 0.10. The full weight allocation is Response Time 0.25, Patient Safety 0.20, FDA RTCT Compliance 0.15, Camaraderie 0.10, Cost 0.10, Safety 0.10, Patient Experience 0.10.
- `metrics.schema.json` adds 4 camaraderie metrics: peer_handoff_p95_seconds, peer_sensor_share_p95_ms, role_rotation_count, camaraderie_invariants_pass_rate.
- `human_team_baseline.csv` is augmented with 3-paramedic baseline rows where a team of 3 humans responds in parallel; the synergy benefit of the camarade swarm should match or exceed the 3-paramedic team on response time and force budget.

## In Diagrams

- `diagrams/network_layout.txt` shows 12 H2 humanoids in 4 swarms of 3.
- `diagrams/ae_response_flow.txt` shows a 3-lane swimlane: Lead, Assist, Reserve.
- `diagrams/h2_rotation_timeline.txt` shows role rotation across a typical 90 second AE response.
- `diagrams/swarm_dance.txt` is a new diagram showing the camarade synchronization pattern over a 10 second window.

## In Figures

- `figures/01_swarm_architecture.png` shows the 3-robot camarade swarm at a single site.
- `figures/02_response_time_histogram.png` compares swarm response time to single-robot response time.
- `figures/03_camaraderie_heatmap.png` is a new figure showing the camaraderie invariants pass rate over the 168 hour week.
- `figures/04_role_rotation_timeline.png` shows how Lead, Assist, Reserve rotate during a typical AE.
- `figures/05_force_budget_distribution.png` shows the 22 N cumulative cross-robot force budget for 3-robot patient transfer.
- `figures/06_4site_comparison.png` compares the 4 sites on response time, camaraderie score, escalation count.

## In Reports

- The Markdown report has a dedicated Camaraderie section between the Response Time section and the FDA RTCT Compliance section.
- The PDF report includes the camaraderie heatmap figure on its own page.
- The HTML dashboard has a Camaraderie tab as the second tab after Response Time.

## The One Sentence Test

Every file the future session authors must pass the one-sentence test: "This file improves the camarade swarm." If a file does not improve the camarade swarm, do not author it. If a file weakens the camarade swarm, fix it before commit.
