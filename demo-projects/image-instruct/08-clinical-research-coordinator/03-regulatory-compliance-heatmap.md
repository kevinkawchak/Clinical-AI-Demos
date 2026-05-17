# Image Instruction 08-03: CRC Regulatory and Risk Compliance Heatmap

[![Demo](https://img.shields.io/badge/Demo-08-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/08-humanoid-clinical-research-coordinator.md)
[![Image](https://img.shields.io/badge/Image-03%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/08-clinical-research-coordinator)
[![Orientation](https://img.shields.io/badge/Orientation-Landscape-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/08-humanoid-clinical-research-coordinator-output/figures/08-03-regulatory-compliance-heatmap.png`

## Page Size and DPI

- Letter landscape, 11.0 x 8.5 inches, 300 dpi, 3300 x 2550 pixels, white facecolor.

## Chart Type

Heatmap. 12 CRC tasks x 14 standards.

## Title and Subtitle

- Title: `Neo Beta + Multi-Model Ensemble CRC Compliance Matrix`.
- Subtitle: `12 CRC Tasks x 14 Standards - TRIAL-NSCLC-3A - 12 Patients - 5 Language Preferences`.

## Header and Footer

- Header right: `Demo 08 / Image 03 of 10 / Landscape`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 08 Clinical Research Coordinator`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Rows (12 CRC Tasks)

1. `Patient Pre-Screen (Telephone or Tablet)`.
2. `Patient Self-Selection Form (HR 9501)`.
3. `Humanoid Choice Form (HR 9502)`.
4. `Procedural Modification Capture (HR 9503)`.
5. `Informed Consent Recital (Multilingual)`.
6. `Eligibility Check`.
7. `Stipend Payment Authorization (HR 9507 + GPT-5.5)`.
8. `Data Self-Custody Election (HR 9507)`.
9. `Sample Collection Scheduling`.
10. `Follow-Up Visit Booking`.
11. `IRB Daily Audit Log Append`.
12. `Site CRA Daily Roll-Up`.

## Columns (14 Standards)

1. `21 CFR § 50` (Informed Consent).
2. `21 CFR § 56` (IRB).
3. `21 CFR § 312` (IND Application).
4. `21 CFR § 11` (Electronic Records).
5. `ICH E6(R3)` (GCP).
6. `IEC 80601-2-77` (Medical Robot Safety).
7. `HIPAA 45 CFR § 164.514(b)` (Safe Harbor).
8. `HIPAA 45 CFR § 164.502` (Minimum Necessary).
9. `HR 9501` (Patient Self-Selection).
10. `HR 9502` (Humanoid Choice).
11. `HR 9503` (Procedural Modification).
12. `HR 9507` (Data Self-Custody).
13. `LEP Title VI Civil Rights Act` (Multilingual Access).
14. `IRS 1099-MISC Reporting (Stipend Payment)`.

## Cell Values, Annotations, matplotlib Recipe

Same conventions as prior heatmap instructions. Outline `HR 9501` to `HR 9507` columns with Burgundy frames (patient rights hard-gates). Right margin callout: `Neo Beta refuses any action violating HR 9501 to 9507. Refusals logged with hash-chained provenance for IRB audit.`

## Validation Checklist

1. PNG is 3300 x 2550 pixels.
2. 12 x 14 heatmap.
3. Outlined HR 9501-9507 columns.
4. Right margin callout.
5. Reference table.
6. Title, subtitle, header, footer present.
7. `§` throughout.
8. No em dash, no double dash, no triple dash.
9. No color outside palette.
10. No emoji.
