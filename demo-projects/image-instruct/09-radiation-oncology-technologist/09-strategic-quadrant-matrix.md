# Image Instruction 09-09: Radiation Oncology Strategic Quadrant Matrix

[![Demo](https://img.shields.io/badge/Demo-09-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/09-humanoid-radiation-oncology-technologist.md)
[![Image](https://img.shields.io/badge/Image-09%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/09-radiation-oncology-technologist)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/09-humanoid-radiation-oncology-technologist-output/figures/09-09-strategic-quadrant-matrix.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

2x2 quadrant. X axis: `Patients Treated Per 8-Hour Shift`. Y axis: `Sub-Millimeter Alignment Reproducibility (percent)`. Bubble size proportional to per-shift operating cost.

## Title and Subtitle

- Title: `Atlas + Optimus + Claude Arbiter LINAC Strategic Quadrant`.
- Subtitle: `Throughput vs. Alignment Reproducibility - 10 Glioblastoma SRS Patients per Shift Target`.

## Header and Footer

- Header right: `Demo 09 / Image 09 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 09 Radiation Oncology Technologist`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Axes and Quadrants

- X: `Patients Per 8-Hour Shift`, 0 to 12, ticks every 2.
- Y: `Sub-Millimeter Alignment (percent)`, 90 to 100.
- Medians at X = 8, Y = 98.
- Corners: `Reference` (top right), `Precision Specialist` (top left), `Throughput Specialist` (bottom right), `Legacy Manual` (bottom left).

## Bubble Series (8)

1. `Atlas + Optimus + GR00T/Cosmos/Claude Arbiter (Reference)` Deep Navy.
2. `Atlas Only + Claude Opus 4.7 1M` Teal.
3. `Optimus Only + Claude Opus 4.7 1M` Teal lighter.
4. `Atlas + Optimus + Claude Opus Only (no GR00T)` Gold.
5. `Figure 03 Pair + Gemini 3 Pro` Mauve.
6. `Phoenix Pair + GR00T + Cosmos` Forest Green.
7. `Human RT Tech Team (Baseline)` Slate.
8. `Hybrid Atlas + Optimus + Human RT Tech Co-Watch` Burgundy.

## Layout, Annotations, matplotlib Recipe, Validation

Same conventions as prior quadrant instructions.

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. 8 bubbles.
3. Quadrant medians.
4. Corner labels.
5. Migration arrow.
6. Reference circle.
7. Title, subtitle, header, footer present.
8. No em dash, no double dash, no triple dash.
9. No color outside palette.
10. No emoji.
