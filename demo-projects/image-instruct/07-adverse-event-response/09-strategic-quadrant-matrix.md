# Image Instruction 07-09: AE Response Strategic Quadrant Matrix

[![Demo](https://img.shields.io/badge/Demo-07-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/07-humanoid-24-7-adverse-event-response.md)
[![Image](https://img.shields.io/badge/Image-09%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/07-adverse-event-response)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/07-humanoid-24-7-adverse-event-response-output/figures/07-09-strategic-quadrant-matrix.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

2x2 quadrant. X axis: `Network Coverage Sites Concurrent`. Y axis: `AE-to-Bedside SLA Adherence (90 s; percent)`. Bubble size proportional to annual operating cost USD millions.

## Title and Subtitle

- Title: `3x H2 + Per-Site Claude Opus AE Network Strategic Quadrant`.
- Subtitle: `Network Coverage vs. AE-to-Bedside SLA Adherence - 4-Site PAT-NET-001`.

## Header and Footer

- Header right: `Demo 07 / Image 09 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 07 Adverse Event Response`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Axes and Quadrants

- X: `Network Coverage Sites Concurrent`, 1 to 4.
- Y: `AE-to-Bedside SLA Adherence (percent)`, 80 to 100, ticks every 2.
- Medians at X = 2, Y = 95.
- Corners: `Reference` (top right), `SLA Specialist` (top left), `Coverage Specialist` (bottom right), `Legacy Manual` (bottom left).

## Bubble Series (8)

1. `3x Unitree H2 + Per-Site Claude Opus 4.7 1M (Reference)` Deep Navy.
2. `3x Atlas Electric + Per-Site Claude Opus 4.7 1M` Teal.
3. `3x Tesla Optimus Gen 3 + Per-Site GPT-5.5 Thinking` Gold.
4. `2x Figure 03 + 2x Claude Sonnet 4.6` Mauve.
5. `4x Phoenix Gen 8 + 4x Gemini 3 Pro` Forest Green.
6. `1x H2 Per Site + Human On-Call` Burgundy.
7. `Human On-Call Network (Baseline)` Slate.
8. `Hybrid 3x H2 + 1 Human Per Site` Mauve darker.

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
