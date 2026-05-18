# Authoring Instructions for `reports/comparison_methodology.md`

The future session writes this Markdown during Commit 5 of 7.

## Purpose

Documents the comparison framework. The 3-robot camarade swarm is compared against three categories of baseline; the comparison drives the v0.3.0 release ranking.

## Content Skeleton

```
# Comparison Methodology for v0.3.0

## Categories

1. Prior versions of the same demo: v0.1.0 prompt 07 (3 H2 rotating fleet across 4 sites with cross-site van transit). Snapshot at `releases/v0.1.0/`.
2. Competitor humanoid configurations:
   - Boston Dynamics Atlas Electric (3 units per site)
   - Tesla Optimus Gen 3 (3 units per site)
   - Human paramedic rapid response team (3 humans per site)
3. Hybrid configurations:
   - 2 H2 plus 1 human paramedic per site
   - 1 H2 Lead plus 2 human paramedics per site

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

- Mann-Whitney U test between v0.3.0 and each baseline configuration with alpha 0.01.
- 32-iteration sample size yields good power for medium effect sizes.
```

## Validation Rules

- Weights sum to 1.00.
- 7 dimensions.
- 26 metrics keys total.

## Notes

- The Camaraderie dimension is new in v0.3.0. It is the test bench for the swarm pattern.
- The author's prior FAERS LLM paper (10.5281/zenodo.18029100) is cited as the precedent for LLM-driven adverse event work.
