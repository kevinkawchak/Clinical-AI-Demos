# Image Instruction 08-07: CRC Patient Enrollment Flow Sankey

[![Demo](https://img.shields.io/badge/Demo-08-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/08-humanoid-clinical-research-coordinator.md)
[![Image](https://img.shields.io/badge/Image-07%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/08-clinical-research-coordinator)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/08-humanoid-clinical-research-coordinator-output/figures/08-07-sankey-flow-diagram.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

Sankey with 4 vertical levels.

## Title and Subtitle

- Title: `Neo Beta CRC Patient Enrollment Flow Sankey`.
- Subtitle: `Language - Ensemble Routing - HR Election - Enrollment Outcome - 12 Patients, 8-Hour Shift`.

## Header and Footer

- Header right: `Demo 08 / Image 07 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 08 Clinical Research Coordinator`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Levels (4)

1. **Level 1 Patient Language**: `English`, `Spanish`, `Mandarin`, `Tagalog`, `Vietnamese`.
2. **Level 2 Ensemble Routing**: `Claude Opus (Medical Q&A)`, `Gemini 3 Pro (Language)`, `GPT-5.5 (Stipend)`, `Combined Routing`.
3. **Level 3 HR Election**: `HR 9501 Self-Selection Yes`, `HR 9502 Humanoid Choice Yes`, `HR 9503 Procedural Modification Requested`, `HR 9507 Data Self-Custody Elected`.
4. **Level 4 Enrollment Outcome**: `Enrolled`, `Withdrew During Consent`, `Pending Follow-Up`, `Ineligible`.

## Color, Layout, Annotations, matplotlib Recipe

Same conventions as prior sankey instructions. 5 language colors (Slate variants), Teal for LLM routing, Burgundy for HR elections, Forest Green / Gold / Mauve for outcomes. Pinned callout: `100 percent of patients receive HR 9501 to 9507 rights election in their preferred language at v0.2.0.`

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
