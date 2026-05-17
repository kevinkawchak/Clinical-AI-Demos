# Image Instruction 05-09: Pathology Lab Strategic Quadrant Matrix

[![Demo](https://img.shields.io/badge/Demo-05-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/05-humanoid-biospecimen-pathology-lab.md)
[![Image](https://img.shields.io/badge/Image-09%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/05-biospecimen-pathology-lab)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/05-humanoid-biospecimen-pathology-lab-output/figures/05-09-strategic-quadrant-matrix.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

2x2 quadrant bubble matrix. X axis: `IHC Stain Consistency (percent)`. Y axis: `Turnaround Time Hours (inverted; lower is better)`. Bubble size proportional to per-specimen cost.

## Title and Subtitle

- Title: `Phoenix Gen 8 + MCP Pathology Strategic Quadrant`.
- Subtitle: `IHC Stain Consistency vs. Turnaround Time - Per-Specimen, CAP-Accredited`.

## Header and Footer

- Header right: `Demo 05 / Image 09 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 05 Biospecimen Pathology Lab`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Axes and Quadrants

- X: `IHC Stain Consistency (percent)`, 70 to 100.
- Y: `Turnaround Time Hours`, 4 to 24, inverted.
- Medians at X = 88, Y = 12.
- Corners: `Reference` (top right), `Consistency Specialist` (top left), `Speed Specialist` (bottom right), `Legacy Manual` (bottom left).

## Bubble Series (8)

1. `Phoenix Gen 8 + Gemini/Qwen MCP (Reference)` Deep Navy.
2. `Figure 03 + Claude Opus 4.7 1M` Teal.
3. `Atlas Electric + GPT-5.5 Thinking` Gold.
4. `Optimus Gen 3 + Gemini 3 Pro` Mauve.
5. `Digit V5 + Sonnet 4.6` Forest Green.
6. `Human Pathology Tech (Baseline)` Slate.
7. `Hybrid Phoenix + Human Tech Co-Watch` Burgundy.
8. `Cobot-Stainer + Human (no humanoid)` Mauve darker.

## Layout, Annotations, matplotlib Recipe, Validation

Same conventions as prior quadrant instructions.

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. 8 bubbles.
3. Quadrant medians.
4. Corner labels.
5. Migration arrow.
6. Reference circle around Phoenix bubble.
7. Title, subtitle, header, footer present.
8. No em dash, no double dash, no triple dash.
9. No color outside palette.
10. No emoji.
