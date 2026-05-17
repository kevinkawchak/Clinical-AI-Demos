# Image Instruction 03-06: Pharmacy CAR-T Compounding Capability Radar

[![Demo](https://img.shields.io/badge/Demo-03-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/03-humanoid-pharmacy-imp-compounding.md)
[![Image](https://img.shields.io/badge/Image-06%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/03-pharmacy-imp-compounding)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/03-humanoid-pharmacy-imp-compounding-output/figures/03-06-capability-radar-comparison.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

Radar (spider) chart with 8 axes and 4 polygons.

## Title and Subtitle

- Title: `Figure 03 + GPT-5.5 Thinking CAR-T Capability Radar`.
- Subtitle: `Figure 03 + GPT vs. Phoenix + Claude vs. Atlas + Opus vs. Human Pharmacist - 4-Hour Compounding`.

## Header and Footer

- Header right: `Demo 03 / Image 06 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 03 Pharmacy IMP Compounding`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Axes (8 dimensions, 0 to 100)

1. `Hand Dexterity (1 mm RMS target)`.
2. `Cell Viability Outcome`.
3. `Cumulative Tip Force Margin Below 8 N`.
4. `E-Stop Latency Performance (5 ms target)`.
5. `Per-Step Batch Record Latency`.
6. `Particle Count Stability (ISO 14644-1)`.
7. `USP 800 Chain-of-Custody Audit Completeness`.
8. `Per-Batch Cost Efficiency`.

## Series (4 polygons)

1. `Figure 03 + GPT-5.5 Thinking on-prem` (Deep Navy fill 0.35 alpha).
2. `Sanctuary Phoenix Gen 8 + Claude Opus 4.7 1M` (Teal fill 0.30 alpha).
3. `Boston Dynamics Atlas Electric + Claude Opus 4.7 1M` (Gold fill 0.30 alpha).
4. `Human Pharmacist (Baseline)` (Slate fill 0.25 alpha dashed outline).

## Layout, Annotations, matplotlib Recipe

Same conventions as 01-06. Callout: `Figure 03 leads on Hand Dexterity and Per-Step Batch Record Latency. Phoenix Gen 8 leads on Particle Count Stability. Human leads on adaptive recovery from unexpected vial breakage.`

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. 4 polygons with assigned fills.
3. 8 axis labels unclipped.
4. Reference rings 25, 50, 75, 100.
5. Legend at bottom with 4 entries.
6. Title, subtitle, header, footer present.
7. No em dash, no double dash, no triple dash.
8. No color outside palette.
9. No emoji.
10. Callout text present above legend.
