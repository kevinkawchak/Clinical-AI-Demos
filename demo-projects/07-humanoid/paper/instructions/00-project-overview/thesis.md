# Thesis

On-premises repository based LLMs provide commands to humanoid robots based on real-time sensor data and controlled via x, y, z coordinates to administer synergistic treatment to patients adverse events. This workflow minimizes single robot error potential.

## Why On-Premises

The Claude Opus 4.7 1M instance lives on the same physical site as the 3 H2 humanoids. There is no public cloud call in the per-tick decision loop. The on-prem deployment is required because:

- PHI never leaves the site. Patient state, vital signs, CTCAE grade, attending physician name, all stay inside the site network.
- Latency stays under 200 ms median. A public cloud round trip from a rural Atlanta clinic to a far-region cloud endpoint adds 80 ms to 150 ms of one-way network latency, which would consume the entire budget.
- The site survives a wide-area outage. Power, network, or cloud provider outages do not stop the AE response loop.

## Why Repository Based

The LLM reads from and writes to a git-backed repository at every tick:

- Read: the current world model (patient, doctors, peer robots), the current AE intake feed, the CTCAE grading table, the HR 9505 SLA timer.
- Write: the broadcast command set, the audit log line, the escalation log line.

A git-backed repository gives:

- Cryptographic provenance via commit hash for every tick decision (HR 9504 Physical AI Clinical Error Reduction Act).
- Reproducibility for the 32 iteration deterministic sweep.
- A natural integration point for FDA RTCT submission (the audit log lives in the repository).
- A canonical store for the world model that all 3 robots share through the shared file system mount.

## Why Real-Time Sensor Data

The LLM decides at 1 Hz, the robots move at 10 Hz, and the inter-robot peer mesh runs at 200 Hz. Every decision is anchored to sensor readings within the same tick. The sensor stack per robot is:

- Stereo RGB-D head camera (10 Hz, 5 megapixel)
- Force-torque sensor at every wrist (200 Hz, 0.1 N resolution)
- Tactile pad on every fingertip (500 Hz, 0.05 N resolution)
- Joint encoder on every joint (1000 Hz, 0.01 degree resolution)
- Microphone array (16 kHz, 4 channels) for verbal AE detection
- Pulse oximeter (10 Hz, 1 percent SpO2 resolution) when attached to the patient
- Portable ECG (1000 Hz, 5 lead) when attached to the patient
- IR beacon transceiver (1000 Hz)
- 60 GHz UWB transceiver (200 Hz)

Every sensor return is timestamped to within 1 ms of the site reference clock and is integrated into the shared world model within 1 tick of arrival.

## Why X, Y, Z Coordinates

The LLM emits robot commands in x, y, z coordinates expressed in a shared site cartesian frame, not in joint space. This is important because:

- The LLM does not need to model joint kinematics for 39 DOF per robot times 3 robots equals 117 DOF total per site. That would be expensive and fragile.
- The LLM does need to reason about positions in space, distances between robots, distances from robots to the patient, distances from robots to obstacles. Cartesian space is the natural language for that.
- The per-robot inverse kinematics solver runs locally on the robot controller at 10 Hz and converts the cartesian command to joint targets. The solver is the same on all 3 robots and is shared infrastructure.
- A cartesian command is small. A 6-axis pose (x, y, z, roll, pitch, yaw) plus a gripper state takes 7 floats. A 39-DOF joint command takes 39 floats. The cartesian command is 5.5 times smaller per robot and 16.7 times smaller per swarm.

## Why Synergistic Treatment

A synergistic treatment is one where the outcome of the 3-robot intervention is strictly better than the outcome of any 1-robot intervention. Examples in the AE response context:

- Chest compressions plus simultaneous airway management plus simultaneous IV preparation: 3-robot parallel work cuts the time-to-stable from 4 minutes (1 robot serial) to under 90 seconds (3 robots parallel).
- Patient lift plus simultaneous stretcher positioning plus simultaneous tool fetch: 3-robot parallel work avoids any patient drop risk because the lift load is split across 3 arms with a 22 N cumulative cross-robot force ceiling.
- Epinephrine administration plus simultaneous pulse oximetry plus simultaneous family communication: 3 robots can run all 3 tasks in parallel without any robot context-switching.

The key is parallel work with explicit hand-off and shared force budgets. This is the synergy that the swarm provides over a single-robot AE responder.

## Why Minimizes Single Robot Error Potential

A single robot can:

- Misread a sensor and act on the misread
- Run out of battery mid-intervention
- Get stuck in a path that does not lead to the patient
- Drop a tool
- Fail an IK solve and freeze

With 3 robots in a camarade swarm, each of these errors is caught by a peer within 1 to 2 ticks:

- Peer cross-checks every Lead sensor reading at 1 Hz. A 5 percent disagreement triggers a re-read.
- Peer takes over on Lead low battery within 1 tick of the threshold crossing.
- Peer reroutes around a stuck Lead within 2 ticks.
- Peer hands a fresh tool to a Lead within 2 seconds of a drop.
- Peer steps into the Lead joint trajectory within 5 ticks of a freeze.

Formally, if `p` is the probability of a single robot making a critical error on a given tick, then the probability of an uncorrected error in the swarm is approximately `p ** 2` (since 2 peers must also fail to catch it). At p equals 0.001, the swarm-level uncorrected error rate is around 0.000001, a 1000x reduction.

This is the practical justification for the camarade swarm.
