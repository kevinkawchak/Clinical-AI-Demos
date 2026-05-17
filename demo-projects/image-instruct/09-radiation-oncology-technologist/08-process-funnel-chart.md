# Image Instruction 09-08: LINAC Beam-On Authorization Funnel

[![Demo](https://img.shields.io/badge/Demo-09-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/09-humanoid-radiation-oncology-technologist.md)
[![Image](https://img.shields.io/badge/Image-08%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/09-radiation-oncology-technologist)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/09-humanoid-radiation-oncology-technologist-output/figures/09-08-process-funnel-chart.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

7-stage funnel covering pre-treatment to beam-on authorization for one patient.

## Title and Subtitle

- Title: `LINAC Pre-Treatment to Beam-On Authorization Funnel`.
- Subtitle: `Per-Patient - From Setup to Authorized Beam-On - 10 Patients per 8-Hour Shift`.

## Header and Footer

- Header right: `Demo 09 / Image 08 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 09 Radiation Oncology Technologist`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Stages (7)

1. **Patient Scheduled** (Slate).
2. **Mask Immobilization Verified by Atlas** (Deep Navy).
3. **Patient Setup on 6D Couch by Atlas** (Deep Navy lighter).
4. **kV CBCT Acquired by Optimus** (Mauve).
5. **CBCT-CT Alignment Within Tolerance (Claude Opus Gate 2)** (Teal darker).
6. **Plan Authorization (Claude Opus Gate 1)** (Burgundy).
7. **Beam-On Authorized + LINAC Interlock Cleared** (Forest Green).

## Layout, Annotations, matplotlib Recipe, Validation

Same conventions as prior funnel instructions. Bottom note: `Approximately 10 minutes setup-to-beam-on per patient at v0.2.0 reference, down from 25 minutes manual.`

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. 7 stacked trapezoids.
3. Stage labels.
4. Filter rule column left.
5. Bottom note.
6. Title, subtitle, header, footer present.
7. No em dash, no double dash, no triple dash.
8. No color outside palette.
9. No emoji.
10. Cumulative pass rate right.
