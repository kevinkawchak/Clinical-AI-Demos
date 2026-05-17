# Image Instruction 05-08: Pathology Specimen Turnaround Funnel

[![Demo](https://img.shields.io/badge/Demo-05-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/05-humanoid-biospecimen-pathology-lab.md)
[![Image](https://img.shields.io/badge/Image-08%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/05-biospecimen-pathology-lab)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/05-humanoid-biospecimen-pathology-lab-output/figures/05-08-process-funnel-chart.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

7-stage funnel showing specimen filter from pickup to pathologist co-sign.

## Title and Subtitle

- Title: `Phoenix Gen 8 + MCP Pathology 12-Hour Specimen Funnel`.
- Subtitle: `Pickup to Pathologist Co-Sign - 8 Specimens, CAP-Accredited`.

## Header and Footer

- Header right: `Demo 05 / Image 08 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 05 Biospecimen Pathology Lab`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Stages (7)

1. **Specimens Picked Up (Cold Chain Start)** (Mauve).
2. **Cold Ischemia Under 30 Minutes Met** (Burgundy).
3. **Gross Examination Done and MCP gross_examine Pass** (Slate).
4. **Formalin Fixation 6 to 24 Hour Window Met** (Burgundy darker).
5. **Microtome 4 to 5 Micron Section Within Tolerance** (Deep Navy).
6. **HE plus IHC Stain Pass MCP Verdict** (Forest Green).
7. **Pathologist Co-Sign Complete** (Forest Green darker).

## Layout, Annotations, matplotlib Recipe, Validation

Same conventions as prior funnel instructions. Bottom note: `Average end-to-end time per specimen at v0.2.0 reference is approximately 8 hours including formalin fixation.`

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
