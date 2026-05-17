# Image Instruction 03-09: Pharmacy CAR-T Strategic Quadrant Matrix

[![Demo](https://img.shields.io/badge/Demo-03-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/03-humanoid-pharmacy-imp-compounding.md)
[![Image](https://img.shields.io/badge/Image-09%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/03-pharmacy-imp-compounding)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/03-humanoid-pharmacy-imp-compounding-output/figures/03-09-strategic-quadrant-matrix.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

2x2 strategic quadrant bubble matrix. X axis: `Cell Viability Outcome` (0 to 100 percent). Y axis: `Per-Batch Cost USD Thousands` (inverted; lower cost up). Bubble size proportional to throughput (batches per pharmacy per month).

## Title and Subtitle

- Title: `Figure 03 + GPT-5.5 Thinking CAR-T Strategic Quadrant`.
- Subtitle: `Cell Viability vs. Per-Batch Cost - PAT-IMP-0001 - Inverted Y So Lower Cost Up`.

## Header and Footer

- Header right: `Demo 03 / Image 09 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 03 Pharmacy IMP Compounding`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Axes and Quadrants

- X: `Cell Viability Outcome (percent)`, 70 to 100.
- Y: `Per-Batch Cost (USD Thousands)`, 0 to 600, inverted.
- Medians at X = 88, Y = 300.
- Quadrants:
  - Top right: `Reference Stack`.
  - Top left: `Cost-Efficient Specialist`.
  - Bottom right: `Viability-First Specialist`.
  - Bottom left: `Legacy Pharmacist`.

## Bubble Series (8)

1. `Figure 03 + GPT-5.5 Thinking on-prem (v0.2.0 Reference)` (Deep Navy).
2. `Sanctuary Phoenix Gen 8 + Claude Opus 4.7 1M` (Teal).
3. `Atlas Electric + Claude Opus 4.7 1M` (Deep Navy lighter).
4. `Optimus Gen 3 + GPT-5.5 Thinking` (Mauve).
5. `Human Pharmacist + Robot-Assist Pipette` (Slate).
6. `Hybrid Figure 03 + Human Pharmacist Co-Watch` (Burgundy).
7. `Digit V5 + Claude Sonnet 4.6 (Bench Variant)` (Gold).
8. `Neo Beta + Gemini 3 Pro (Bench Variant)` (Forest Green).

## Layout, Annotations, matplotlib Recipe

Same conventions as 01-09 and 02-09. Migration-path arrow Legacy to Reference Stack. Reference circle around v0.2.0 bubble.

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. 8 bubbles plotted.
3. Quadrant median lines.
4. 4 corner labels.
5. Migration-path arrow.
6. Reference circle around Figure 03 bubble.
7. Y axis inverted, lower cost at top.
8. Title, subtitle, header, footer present.
9. No em dash, no double dash, no triple dash.
10. No emoji.
