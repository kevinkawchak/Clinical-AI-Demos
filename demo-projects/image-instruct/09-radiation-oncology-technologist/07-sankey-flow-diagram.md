# Image Instruction 09-07: Radiation Oncology Patient and Dose Sankey

[![Demo](https://img.shields.io/badge/Demo-09-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/09-humanoid-radiation-oncology-technologist.md)
[![Image](https://img.shields.io/badge/Image-07%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/09-radiation-oncology-technologist)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/09-humanoid-radiation-oncology-technologist-output/figures/09-07-sankey-flow-diagram.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

Sankey with 4 vertical levels.

## Title and Subtitle

- Title: `Atlas + Optimus LINAC Patient and Dose Sankey`.
- Subtitle: `10 SRS Patients Through Authorization Gates to Per-Fraction Dose Reported`.

## Header and Footer

- Header right: `Demo 09 / Image 07 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 09 Radiation Oncology Technologist`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Levels (4)

1. **Level 1 Patient Cohort**: `10 Glioblastoma SRS Patients` split by mask type, tumor volume, position.
2. **Level 2 Atlas + Optimus Setup**: `Mask Verified`, `Patient on Couch`, `kV CBCT Acquired`, `Alignment Within 1 mm`, `Alignment Re-Try Needed`.
3. **Level 3 Claude Opus Arbiter Gate**: `Gate 1 Pass (Authorization)`, `Gate 2 Pass (CBCT Tolerance)`, `Gate 3 Pass (E-Stop Avoided)`, `Gate Held / Escalation`.
4. **Level 4 Terminal**: `16 Gy Delivered`, `Re-Treatment Required`, `Medical Event Triggered (NRC 10 CFR § 35)`, `Patient Re-Scheduled`.

## Color, Layout, Annotations, matplotlib Recipe

Same conventions as prior sankey instructions. Mauve for patient sources, Deep Navy for Atlas + Optimus actions, Teal darker for Claude Opus gates, Forest Green / Burgundy for terminals. Pinned callout: `100 percent of patients in this iteration set reach 16 Gy delivered. 0 medical events triggered. CBCT alignment within 1 mm in all cases at v0.2.0 reference.`

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. 4 columns with all listed nodes.
3. Flow widths proportional.
4. Level titles.
5. Callout.
6. Title, subtitle, header, footer present.
7. `§` in `NRC 10 CFR § 35`.
8. No em dash, no double dash, no triple dash.
9. No color outside palette.
10. No emoji.
