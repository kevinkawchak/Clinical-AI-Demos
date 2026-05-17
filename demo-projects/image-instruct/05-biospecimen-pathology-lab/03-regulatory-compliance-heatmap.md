# Image Instruction 05-03: Pathology Lab Regulatory and Risk Compliance Heatmap

[![Demo](https://img.shields.io/badge/Demo-05-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/05-humanoid-biospecimen-pathology-lab.md)
[![Image](https://img.shields.io/badge/Image-03%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/05-biospecimen-pathology-lab)
[![Orientation](https://img.shields.io/badge/Orientation-Landscape-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/05-humanoid-biospecimen-pathology-lab-output/figures/05-03-regulatory-compliance-heatmap.png`

## Page Size and DPI

- Letter landscape, 11.0 x 8.5 inches, 300 dpi, 3300 x 2550 pixels, white facecolor.

## Chart Type

Heatmap. 12 pathology tasks x 14 standards.

## Title and Subtitle

- Title: `Phoenix Gen 8 + Gemini/Qwen MCP Pathology Compliance Matrix`.
- Subtitle: `12 Pathology Tasks x 14 Standards - CAP, CLIA, 21 CFR § 58 GLP - 8 Specimens, 12-Hour Shift`.

## Header and Footer

- Header right: `Demo 05 / Image 03 of 10 / Landscape`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 05 Biospecimen Pathology Lab`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Rows (12 Tasks)

1. `Specimen Pickup and Cold Chain Start`.
2. `Gross Examination`.
3. `Formalin Fixation Setup`.
4. `Tissue Processor Load`.
5. `Paraffin Embedding`.
6. `Microtome Sectioning (4 to 5 micron)`.
7. `HE Staining`.
8. `IHC Staining (Antibody Panel)`.
9. `Slide Scanner Load`.
10. `Report Draft (Pathologist Co-Sign)`.
11. `LIS Update`.
12. `CAP Q-Probes Audit Append`.

## Columns (14 Standards)

1. `CAP Q-Probes Preanalytical`.
2. `CAP Q-Probes Analytical`.
3. `CAP Q-Probes Postanalytical`.
4. `CLIA Subpart K`.
5. `21 CFR § 58` (GLP).
6. `21 CFR § 11` (Electronic Records).
7. `21 CFR § 312` (IND Application).
8. `ICH E6(R3)` (GCP).
9. `IEC 80601-2-77` (Medical Robot Safety).
10. `IEC 61010-2-101` (IVD Equipment Safety).
11. `HIPAA 45 CFR § 164.514(b)` (Safe Harbor).
12. `OSHA 29 CFR § 1910.1030` (Bloodborne Pathogens).
13. `OSHA Formaldehyde Standard 29 CFR § 1910.1048`.
14. `ISO 15189` (Medical Lab QMS).

## Cell Values, Annotations, matplotlib Recipe

Same conventions as prior heatmap instructions. Outline `CAP Q-Probes Preanalytical` and `21 CFR § 58` columns. Callout: `Phoenix Gen 8 + MCP routes 100 percent of Safe Harbor cells through on-prem Qwen3 72B. Gemini 3 Pro cloud only for redacted general reasoning.`

## Validation Checklist

1. PNG is 3300 x 2550 pixels.
2. 12 x 14 heatmap, all cells colored.
3. Outlined columns (CAP and 21 CFR § 58).
4. Right margin callout.
5. Reference table.
6. Title, subtitle, header, footer present.
7. `§` throughout.
8. No em dash, no double dash, no triple dash.
9. No color outside palette.
10. No emoji.
