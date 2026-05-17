# Image Instruction 06-09: Tele-Surgical Strategic Quadrant Matrix

[![Demo](https://img.shields.io/badge/Demo-06-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/06-humanoid-tele-surgical-assistant.md)
[![Image](https://img.shields.io/badge/Image-09%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/06-tele-surgical-assistant)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/06-humanoid-tele-surgical-assistant-output/figures/06-09-strategic-quadrant-matrix.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

2x2 strategic quadrant. X axis: `Tele-Link Resilience Score (0 to 100)`. Y axis: `Operator Confirmation Punctuality (percent within 1 sec)`. Bubble size proportional to per-procedure cost in USD thousands.

## Title and Subtitle

- Title: `Apollo + Claude Opus 4.7 1M Tele-Surgical Strategic Quadrant`.
- Subtitle: `Tele-Link Resilience vs. Confirmation Punctuality - Reference vs. Baselines`.

## Header and Footer

- Header right: `Demo 06 / Image 09 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 06 Tele-Surgical Assistant`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Axes and Quadrants

- X: `Tele-Link Resilience Score`, 0 to 100, ticks every 10.
- Y: `Operator Confirmation Within 1 sec (percent)`, 80 to 100, ticks every 2.
- Medians at X = 70, Y = 95.
- Corners: `Reference` (top right), `Resilience Specialist` (top left), `Confirmation Specialist` (bottom right), `Legacy On-Site Surgeon` (bottom left).

## Bubble Series (8)

1. `Apollo + Claude Opus 4.7 1M (Reference)` Deep Navy.
2. `Atlas Electric + Claude Opus 4.7 1M` Teal.
3. `Tesla Optimus Gen 3 + GPT-5.5 Thinking` Gold.
4. `Figure 03 + Claude Sonnet 4.6` Mauve.
5. `Sanctuary Phoenix Gen 8 + Gemini 3 Pro` Forest Green.
6. `Human Patient-Side Assistant (Baseline)` Slate.
7. `Hybrid Apollo + Human Co-Assistant` Burgundy.
8. `On-Site Surgeon (No Tele-Surgery)` Mauve darker.

## Layout, Annotations, matplotlib Recipe, Validation

Same conventions as prior quadrant instructions.

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. 8 bubbles.
3. Quadrant medians.
4. Corner labels.
5. Migration-path arrow.
6. Reference circle around Apollo bubble.
7. Title, subtitle, header, footer present.
8. No em dash, no double dash, no triple dash.
9. No color outside palette.
10. No emoji.
