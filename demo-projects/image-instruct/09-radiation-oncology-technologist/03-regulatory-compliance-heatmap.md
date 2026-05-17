# Image Instruction 09-03: Radiation Oncology Regulatory and Risk Compliance Heatmap

[![Demo](https://img.shields.io/badge/Demo-09-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/09-humanoid-radiation-oncology-technologist.md)
[![Image](https://img.shields.io/badge/Image-03%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/09-radiation-oncology-technologist)
[![Orientation](https://img.shields.io/badge/Orientation-Landscape-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/09-humanoid-radiation-oncology-technologist-output/figures/09-03-regulatory-compliance-heatmap.png`

## Page Size and DPI

- Letter landscape, 11.0 x 8.5 inches, 300 dpi, 3300 x 2550 pixels, white facecolor.

## Chart Type

Heatmap. 12 LINAC vault tasks x 14 standards.

## Title and Subtitle

- Title: `Atlas + Optimus + GR00T/Cosmos/Claude Arbiter LINAC Compliance Matrix`.
- Subtitle: `12 LINAC Tasks x 14 Standards - 10 Glioblastoma SRS Patients - Single-Fraction 16 Gy`.

## Header and Footer

- Header right: `Demo 09 / Image 03 of 10 / Landscape`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 09 Radiation Oncology Technologist`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Rows (12 LINAC Vault Tasks)

1. `Pre-Treatment Mask Verification (Atlas)`.
2. `Patient Setup on 6D Couch`.
3. `kV CBCT Image Acquisition`.
4. `CBCT-CT Alignment Check`.
5. `Plan Authorization (Claude Opus Gate 1)`.
6. `HyperArc Beam-On Authorization (Claude Opus Gate 2)`.
7. `Inter-Arc 6D Couch Repositioning`.
8. `Beam-Off Verification`.
9. `Post-Treatment Patient Egress (Atlas)`.
10. `Dose Report Generation`.
11. `NRC 10 CFR § 35 Medical Event Check (Claude Opus Gate 3)`.
12. `AAPM TG-142 LINAC QA Snapshot`.

## Columns (14 Standards)

1. `AAPM TG-100` (Risk-Informed QM).
2. `AAPM TG-142` (LINAC QA).
3. `AAPM TG-218` (IMRT QA).
4. `NRC 10 CFR § 35` (Medical Use of Byproduct Material).
5. `NRC 10 CFR § 20` (Standards for Protection Against Radiation).
6. `21 CFR § 1020.30` (Diagnostic X-Ray Standard).
7. `21 CFR § 312` (IND Application).
8. `IEC 80601-2-77` (Medical Robot Safety).
9. `IEC 60601-2-1` (LINAC Safety).
10. `IEC 62083` (RT Planning System).
11. `ISO 10218` (Industrial Robot Safety).
12. `HIPAA 45 CFR § 164.514(b)` (Safe Harbor).
13. `Joint Commission ROAP`.
14. `ASTRO White Papers on Adaptive RT`.

## Cell Values, Annotations, matplotlib Recipe

Same conventions as prior heatmap instructions. Outline `NRC 10 CFR § 35` and `AAPM TG-100` columns with Burgundy and Gold. Callout: `Claude Opus 4.7 1M arbiter gates 100 percent of treatment authorizations. NVIDIA GR00T + Cosmos handle real-time perception and motion prediction at 100 ms.`

## Validation Checklist

1. PNG is 3300 x 2550 pixels.
2. 12 x 14 heatmap.
3. Outlined columns (`NRC 10 CFR § 35` Burgundy, `AAPM TG-100` Gold).
4. Right margin callout.
5. Reference table.
6. Title, subtitle, header, footer present.
7. `§` throughout.
8. No em dash, no double dash, no triple dash.
9. No color outside palette.
10. No emoji.
