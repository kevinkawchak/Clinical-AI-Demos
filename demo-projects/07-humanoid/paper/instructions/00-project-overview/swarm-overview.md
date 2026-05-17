# Swarm Overview: The 3 H2 Camarade Pattern

The 3 Unitree H2 humanoids at each PAT-NET-001 site act as a swarm. This document defines what swarm means in this context, and what behaviors the future code generation pass must implement.

## Definition

A swarm is a group of robots that:

1. Share a common goal at every tick. The goal is set by the per-site Claude Opus 4.7 1M broadcaster.
2. Share a common world model. Each robot writes to the shared model and reads from the shared model every tick.
3. Self-organize into dynamic roles. The roles are Lead, Assist, Reserve, and are reassigned by the broadcaster every tick.
4. Communicate continuously. Physical comms run at 200 Hz to 1000 Hz; intellectual comms run at 1 Hz.
5. Adapt to peers. Each robot has a peer-aware policy that treats the other 2 robots as first-class actors, not as background.

## Roles

### Lead

The Lead is the primary AE responder. Lead is the robot closest to the patient at the start of the AE and with the highest battery and highest task affinity for the current AE type. The Lead:

- Approaches the patient first within 90 seconds of AE detection
- Performs the primary intervention (epinephrine, pulse oximetry, vagus nerve stimulator probe, etc.)
- Communicates verbally with the patient and the attending physician
- Holds the central tool inventory on the Lead chest tray

### Assist

The Assist is the secondary responder. Assist is the second closest robot to the patient at AE start, or a robot that the Lead can hand tools to within 2 seconds. The Assist:

- Holds and stages backup tools (second epinephrine, IV access tray, emergency airway kit)
- Hands tools to the Lead on request via 60 GHz UWB peer mesh
- Maintains a 0.4 m to 1.2 m distance from the Lead during shared task work
- Steps into Lead role on Lead fault or low battery

### Reserve

The Reserve is the perimeter watcher. Reserve is the third robot. The Reserve:

- Maintains a 1.5 m to 2.0 m perimeter around the AE scene
- Watches for second-affected patients, family members, environmental hazards
- Holds the on-deck Lead position; ready to swap in if Assist becomes Lead
- Manages communication with on-call human physician and FDA RTCT submission

## Role Rotation

Roles can rotate at every tick. The broadcaster computes a priority score for each (robot, role) pair and assigns the maximum bipartite match per tick. The priority score is a weighted sum:

- 0.40 proximity to patient (Manhattan distance in shared cartesian frame)
- 0.25 battery state of charge
- 0.15 payload state (do they already hold the tool they would need)
- 0.10 task affinity (Lead history on this AE type)
- 0.10 confidence (their own self-reported confidence over the last 10 ticks)

## Physical Communication

The robots talk to each other physically through 60 GHz ultra-wideband and IR-band line-of-sight beacons. The physical channel handles:

- Hand-off requests (Lead asks Assist for epinephrine; Assist must reply within 200 ms with a tool location packet)
- Sensor sharing (Reserve sees a hazard the Lead missed; Reserve pushes a hazard packet to all peers within 100 ms)
- E-stop propagation (any robot raising E-stop must propagate to peers within 5 ms via UWB, 1 ms via IR beacon)
- Cartesian frame alignment (every 1 s, each pair of robots reconciles their local frame to a shared site-level frame using cooperative IR beacons)

## Intellectual Communication

The robots share intellectual context through the on-prem Claude Code server. Each robot publishes:

- A 1 Hz sensor digest (vital signs read, environmental measurements, last tool position)
- A 1 Hz self-confidence value (0.0 to 1.0)
- A 1 Hz task progress token (intervention step number out of N steps)

The LLM broadcaster integrates all 3 streams and emits the next 3-robot command set in one atomic message.

## Adaptation

The swarm adapts to three classes of input:

1. Patients: vital signs, position, CTCAE grade, AE type, patient ID, consent state
2. Doctors: on-site attending physician position, role (oncologist, ER physician, palliative care, etc.), command authority (a CTCAE grade 3+ AE requires the attending physician to authorize any IV access)
3. Other robots: peer position, peer pose, peer battery, peer task token, peer confidence

The adaptation policy is a function `policy(self_state, peer_state, patient_state, physician_state) -> command_token`. The function is evaluated locally at 10 Hz for motion and is overridden by the LLM broadcaster at 1 Hz for task assignment.

## Camaraderie Invariants

The following invariants must hold for the swarm to qualify as a camarade swarm:

1. No robot ever moves into a peer's planned 2 second motion envelope without an explicit hand-off request.
2. Every tool hand-off completes within 2 seconds of the request.
3. Every peer-reported sensor reading is integrated into the world model within 1 tick.
4. Every E-stop raised by one robot stops all 3 within 5 ms.
5. Every robot reports its own state at 1 Hz so the LLM never has to ask.
6. Every robot defers to the Lead within its current AE response.
7. Every robot is willing to become Lead if asked. No robot refuses on the grounds of role.

## What This Replaces

The original prompt 07 had a 3-robot rotating fleet across 4 sites. v0.3.0 replaces that with a 3-robot per-site fleet (12 total) and adds:

- Broadcast publish-subscribe protocol
- Peer-aware role rotation
- 60 GHz UWB plus IR beacon physical channel
- Shared world model
- Camaraderie invariants
- Single-robot fallback mode
- Cross-site bus for de-identified summaries only (no robot transit)
