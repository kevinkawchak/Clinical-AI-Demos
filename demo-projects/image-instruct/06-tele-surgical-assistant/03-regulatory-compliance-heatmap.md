# Image Instruction 06-03: Tele-Surgical Regulatory and Risk Compliance Heatmap

[![Demo](https://img.shields.io/badge/Demo-06-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/06-humanoid-tele-surgical-assistant.md)
[![Image](https://img.shields.io/badge/Image-03%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/06-tele-surgical-assistant)
[![Orientation](https://img.shields.io/badge/Orientation-Landscape-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/06-humanoid-tele-surgical-assistant-output/figures/06-03-regulatory-compliance-heatmap.png`

## Page Size and DPI

- Letter landscape, 11.0 x 8.5 inches, 300 dpi, 3300 x 2550 pixels, white facecolor.

## Chart Type

Heatmap matrix. 12 surgical phases x 14 standards.

## Title and Subtitle

- Title: `Apollo + Claude Opus 4.7 1M Tele-Surgical Compliance Matrix`.
- Subtitle: `12 Whipple Phases x 14 Standards - PAT-TELE-0001 - 1,100-Mile Rural Tele-Surgery`.

## Header and Footer

- Header right: `Demo 06 / Image 03 of 10 / Landscape`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 06 Tele-Surgical Assistant`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Rows (12 Whipple Phases)

1. `Pre-Op Time-Out and Sign-In`.
2. `Anesthesia Induction`.
3. `Access (Trocar Placement)`.
4. `Tele-Link Verification`.
5. `Mobilization (Kocher Maneuver)`.
6. `Resection (Whipple Specimen)`.
7. `Frozen Section Pathology Round-Trip`.
8. `Reconstruction (Hepaticojejunostomy)`.
9. `Reconstruction (Gastrojejunostomy)`.
10. `Hemostasis Check`.
11. `Closure (Fascia + Skin)`.
12. `Post-Op Hand-Off to Recovery (Demo 04)`.

## Columns (14 Standards)

1. `21 CFR § 50` (Informed Consent).
2. `21 CFR § 312` (IND Application).
3. `21 CFR § 11` (Electronic Records).
4. `ICH E6(R3)` (GCP).
5. `IEC 80601-2-77` (Medical Robot Safety).
6. `ISO 10218` (Industrial Robot Safety).
7. `IEC 62366-1` (Usability Engineering).
8. `FDA Breakthrough Device Designation`.
9. `FDA Tele-Surgery Cross-State Guidance Draft April 2026`.
10. `Big Timber Montana Local Hospital Privileging`.
11. `University of Minnesota Masonic Tele-Privileging Agreement`.
12. `HIPAA 45 CFR § 164.514(b)` (Safe Harbor).
13. `DOD-Grade Encryption Standard (NSA Type 1)`.
14. `HR 9504` (Physical AI Clinical Error Reduction).

## Cell Values, Annotations, matplotlib Recipe

Same conventions as prior heatmap instructions. Outline `IEC 80601-2-77` and `FDA Tele-Surgery Cross-State Guidance Draft April 2026` columns with Burgundy and Gold respectively. Callout: `Operator-In-Loop confirmation gates every Apollo instrument exchange. 100 percent of IEC 80601-2-77 cells at level 4 hard-gated.`

## Validation Checklist

1. PNG is 3300 x 2550 pixels.
2. 12 x 14 heatmap.
3. Outlined columns.
4. Right margin callout.
5. Reference table.
6. Title, subtitle, header, footer present.
7. `§` throughout.
8. No em dash, no double dash, no triple dash.
9. No color outside palette.
10. No emoji.
