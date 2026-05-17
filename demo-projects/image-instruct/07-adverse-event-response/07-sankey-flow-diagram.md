# Image Instruction 07-07: AE Event and CTCAE Grade Sankey

[![Demo](https://img.shields.io/badge/Demo-07-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/07-humanoid-24-7-adverse-event-response.md)
[![Image](https://img.shields.io/badge/Image-07%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/07-adverse-event-response)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/07-humanoid-24-7-adverse-event-response-output/figures/07-07-sankey-flow-diagram.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

Sankey with 4 vertical levels: AE source -> per-site Claude Opus triage -> CTCAE grade -> terminal action.

## Title and Subtitle

- Title: `3x H2 AE Network 168-Hour AE Event and CTCAE Grade Sankey`.
- Subtitle: `4-Site Network - Per-Site Triage to CTCAE to On-Call Activation or Resolved In-Place`.

## Header and Footer

- Header right: `Demo 07 / Image 07 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 07 Adverse Event Response`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Levels (4)

1. **Level 1 Source Site**: `San Francisco`, `San Diego`, `Boston`, `Atlanta`.
2. **Level 2 Per-Site Claude Opus Triage**: `Routine Check`, `Vitals Anomaly Triage`, `Pain or AE Self-Report`, `Family Caregiver Inbound`.
3. **Level 3 CTCAE Grade**: `Grade 1`, `Grade 2`, `Grade 3`, `Grade 4`, `Grade 5`.
4. **Level 4 Terminal**: `Resolved In-Place by H2`, `On-Call Physician Activated (HR 9505)`, `Hospital Transfer`, `Cross-Site H2 Re-Dispatch`.

## Color, Layout, Annotations, matplotlib Recipe

Same conventions as prior sankey instructions. 4 per-site colors (Deep Navy variants). Grade colors progress from Forest Green (Grade 1) to Burgundy (Grade 4/5). Pinned callout: `Approximately 95 percent of CTCAE Grade 1 and 2 events resolved in-place by H2 alone within HR 9505 SLA at v0.2.0.`

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. 4 columns with all listed nodes.
3. Flow widths proportional.
4. Level titles.
5. Callout.
6. Title, subtitle, header, footer present.
7. No em dash, no double dash, no triple dash.
8. No color outside palette.
9. No emoji.
10. Flow alpha 0.50.
