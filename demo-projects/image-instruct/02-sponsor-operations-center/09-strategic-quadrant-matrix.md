# Image Instruction 02-09: Sponsor Operations Center Strategic Quadrant Matrix

[![Demo](https://img.shields.io/badge/Demo-02-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/02-sponsor-humanoid-operations-center.md)
[![Image](https://img.shields.io/badge/Image-09%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/02-sponsor-operations-center)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/02-sponsor-humanoid-operations-center-output/figures/02-09-strategic-quadrant-matrix.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

2x2 strategic quadrant bubble matrix. X axis is `Cross-Trial Throughput` (documents per week across 5 trials). Y axis is `Safe Harbor Compliance Confidence` (0 to 1). Bubble size proportional to 168-hour weekly operating cost in USD thousands.

## Title and Subtitle

- Title: `Sponsor Operations Center Strategic Quadrant`.
- Subtitle: `Cross-Trial Throughput vs. Safe Harbor Compliance Confidence - 168-Hour Weekly Cycle`.

## Header and Footer

- Header right: `Demo 02 / Image 09 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 02 Sponsor Humanoid Operations Center`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Axes and Quadrant Labels

- X: `Cross-Trial Throughput (documents per week)`, 0 to 2000, ticks every 250.
- Y: `Safe Harbor Compliance Confidence (0 to 1)`, ticks every 0.1.
- Quadrant medians at X = 1000, Y = 0.95.
- Quadrant corner labels:
  - Top right: `Reference Stack`.
  - Top left: `Compliance-First`.
  - Bottom right: `Throughput-First`.
  - Bottom left: `Legacy CRO`.

## Bubble Series (8 configurations)

1. `5x Tesla Optimus + Sonnet 4.6 + Opus 4.7 1M Failover (v0.2.0 Reference)` (Deep Navy).
2. `5x Tesla Optimus + Opus 4.7 1M Always-On` (Teal).
3. `5x Boston Dynamics Atlas + Claude Opus 4.7 1M` (Deep Navy lighter).
4. `5x Figure 03 + GPT-5.5 Thinking` (Gold).
5. `5x Agility Digit V5 + Sonnet 4.6` (Mauve).
6. `Outsourced CRO + Human Aggregation` (Slate).
7. `Hybrid (3 Optimus + Human Aggregation)` (Burgundy).
8. `2x Optimus + Cloud-Only Sonnet (Lean)` (Forest Green).

Bubble labels with 2 or 3 character short codes (e.g., `O+SO` for Optimus + Sonnet/Opus).

## Layout, Annotations, matplotlib Recipe

Same conventions as 01-09. Diagonal arrow from Legacy CRO to Reference Stack labeled `Migration Path 2026 to 2028`. Reference circle around the v0.2.0 Reference bubble. Legend with 8 entries below the chart in 2 columns.

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. 8 bubbles plotted with colors and sizes.
3. Quadrant median lines visible.
4. 4 corner labels.
5. Migration-path arrow visible.
6. Reference circle around v0.2.0 bubble.
7. Title, subtitle, header, footer present.
8. No em dash, no double dash, no triple dash.
9. No color outside palette.
10. No emoji.
