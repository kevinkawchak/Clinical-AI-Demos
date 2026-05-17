# Image Instruction 04-09: PACU Recovery Strategic Quadrant Matrix

[![Demo](https://img.shields.io/badge/Demo-04-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/04-humanoid-post-op-recovery-nurse.md)
[![Image](https://img.shields.io/badge/Image-09%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/04-post-op-recovery-nurse)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/04-humanoid-post-op-recovery-nurse-output/figures/04-09-strategic-quadrant-matrix.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

2x2 quadrant bubble matrix. X axis: `Vitals Check On-Time Rate (percent)`. Y axis: `Pressure Injury Incidence per 100 Bed-Nights (inverted; lower is better)`. Bubble size proportional to per-bed annual cost in USD thousands.

## Title and Subtitle

- Title: `Digit V5 + Claude Tier Stack PACU Strategic Quadrant`.
- Subtitle: `Vitals On-Time Rate vs. Pressure Injury Incidence per 100 Bed-Nights - Reference vs. Baselines`.

## Header and Footer

- Header right: `Demo 04 / Image 09 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 04 Post-Op Recovery Nurse`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Axes and Quadrants

- X: `Vitals Check On-Time Rate (percent)` 70 to 100, ticks every 5.
- Y: `Pressure Injury Incidence per 100 Bed-Nights` 0 to 8, inverted (0 at top).
- Medians at X = 90, Y = 3.
- Corners: Top right `Reference`, Top left `Outcome-First`, Bottom right `Cadence-First`, Bottom left `Legacy Manual`.

## Bubble Series (8)

1. `Digit V5 + Haiku 4.5 / Sonnet 4.6 / Llama 4 70B (Reference)` Deep Navy.
2. `Neo Beta + Claude Opus 4.7 1M` Teal.
3. `Optimus Gen 3 + GPT-5.5 Thinking` Gold.
4. `Figure 03 + Claude Sonnet 4.6` Mauve.
5. `Apollo + Claude Opus 4.7 1M` Burgundy.
6. `Atlas Electric + Claude Opus 4.7 1M` Deep Navy lighter.
7. `Human Night-Shift Nurse (Baseline)` Slate.
8. `Hybrid Digit V5 + Human Charge Nurse` Forest Green.

## Layout, Annotations, matplotlib Recipe, Validation

Same conventions as prior quadrant instructions.

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. 8 bubbles plotted.
3. Quadrant medians visible.
4. Corner labels.
5. Migration arrow.
6. Reference circle around Digit V5 bubble.
7. Title, subtitle, header, footer present.
8. No em dash, no double dash, no triple dash.
9. No color outside palette.
10. No emoji.
