# Comparison Methodology for v0.4.0

## Categories

1. Prior versions of the same demo: v0.1.0 prompt 07 (3 H2 rotating fleet across 4 sites). Snapshot at `releases/v0.1.0/`.
2. Competitor humanoid configurations:
   - Boston Dynamics Atlas Electric (3 units per site)
   - Tesla Optimus Gen 3 (3 units per site)
   - Figure 03 (3 units per site)
   - Apptronik Apollo (3 units per site)
   - Human paramedic rapid response team (3 humans per site)
3. Hybrid configurations:
   - 2 Unitree H2 EDU plus 1 human paramedic per site
   - 1 Unitree H2 EDU Lead plus 2 human paramedics per site

## Weights

| Dimension | Weight |
|-----------|--------|
| Response Time | 0.25 |
| Patient Safety | 0.20 |
| FDA RTCT Compliance | 0.15 |
| Camaraderie | 0.10 |
| Cost (5-year TCO) | 0.10 |
| Safety (cumulative force, E-stop reliability) | 0.10 |
| Patient Experience | 0.10 |

Weights sum to 1.00.

## Metrics

The 26-key `metrics.schema.json` covers:

- 8 Response Time keys (per-site p50, p95, fastest, slowest, etc.)
- 6 Patient Safety keys (E-stop reliability, force budget compliance, etc.)
- 4 FDA RTCT keys (1-hour compliance rate, hash chain integrity, etc.)
- 4 Camaraderie keys (peer_handoff_p95_seconds, peer_sensor_share_p95_ms, role_rotation_count, camaraderie_invariants_pass_rate)
- 4 other (cost amortized per AE, patient survey score, swarm uptime percent, fleet battery state)

## Aggregation

- Per-iteration metric is the median across the 168-hour run.
- Per-configuration metric is the median across the 32 iterations.
- Per-category ranking is the weighted sum of the dimension scores.

## Statistical Comparison

- Mann-Whitney U test between v0.4.0 and each baseline configuration with alpha 0.01.
- 32-iteration sample size yields good power for medium effect sizes.

## Robot Platform Differentiation

The Unitree H2 EDU has two leading features that differentiate it from competitor humanoids in the comparison:

1. Dexterous hand movements: 6 fingers per hand with tactile pads (0.05 N resolution) at each fingertip. This lets one robot hand off an epinephrine auto-injector or pulse oximeter to a peer at a 0.4 m hand-off distance within 2 seconds without dropping. Atlas, Optimus, Figure, and Apollo use simpler grippers that struggle with the 0.4 m hand-off at this speed.

2. Compute module upgradeability to Jetson AGX Thor (2070 TOPS): the on-robot compute slot accepts the Jetson AGX Thor module delivering 2070 TOPS of AI inference. This drives the on-board 10 Hz motion loop, the 1000 Hz IR beacon listener, the 200 Hz UWB peer mesh, and the 39 joint controller in parallel, with headroom for a Claude Haiku 4.5 sidecar.

## Notes

- The Camaraderie dimension is new in v0.4.0. It is the test bench for the swarm pattern.
- The author's prior FAERS LLM paper (DOI 10.5281/zenodo.18029100) is cited as the precedent for LLM-driven adverse event work.
