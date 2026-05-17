# Image Instruction 07-03: AE Response Regulatory and Risk Compliance Heatmap

[![Demo](https://img.shields.io/badge/Demo-07-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/07-humanoid-24-7-adverse-event-response.md)
[![Image](https://img.shields.io/badge/Image-03%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/07-adverse-event-response)
[![Orientation](https://img.shields.io/badge/Orientation-Landscape-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/07-humanoid-24-7-adverse-event-response-output/figures/07-03-regulatory-compliance-heatmap.png`

## Page Size and DPI

- Letter landscape, 11.0 x 8.5 inches, 300 dpi, 3300 x 2550 pixels, white facecolor.

## Chart Type

Heatmap matrix. 10 AE response phases x 14 frameworks. Plus a 4-row secondary heatmap below covering per-site differential compliance posture.

## Title and Subtitle

- Title: `3x H2 + Per-Site Claude Opus 4.7 1M AE Response Compliance Matrix`.
- Subtitle: `10 AE Response Phases x 14 Frameworks - PAT-NET-001 4-Site Network - 168-Hour Cycle`.

## Header and Footer

- Header right: `Demo 07 / Image 03 of 10 / Landscape`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 07 Adverse Event Response`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Rows (10 AE Phases)

1. `AE Detection (Sensor or Patient Self-Report)`.
2. `Per-Site Claude Opus Triage`.
3. `H2 Bedside Dispatch (within 90 s SLA)`.
4. `CTCAE Grading (HR 9505 1-hour SLA)`.
5. `On-Call Physician Activation`.
6. `Cross-Site Transit (FAA Drone / Charter)`.
7. `Cross-Site H2 Re-Dispatch`.
8. `Sponsor Acknowledgment (HR 9505 1 hour)`.
9. `MedDRA Coding and Submission`.
10. `Audit Reconciliation across 4 Sites`.

## Columns (14 Frameworks)

1. `21 CFR § 312` (IND Application).
2. `21 CFR § 314.80` (Post-Marketing AE Reporting).
3. `21 CFR § 50` (Informed Consent).
4. `ICH E2A` (Expedited AE Reporting).
5. `ICH E2D` (Post-Approval Safety).
6. `ICH E6(R3)` (GCP).
7. `IEC 80601-2-77` (Medical Robot Safety).
8. `MedDRA Coding Standard`.
9. `CTCAE v5.0` (Adverse Event Grading).
10. `HR 9504` (Physical AI Clinical Error Reduction).
11. `HR 9505` (Real-Time Patient-Sponsor Communication).
12. `HIPAA 45 CFR § 164.514(b)` (Safe Harbor).
13. `FDA RTCT April 2026`.
14. `FAA Medical Drone Operations (Part 135)`.

## Cell Values, Annotations, matplotlib Recipe

Same conventions as prior heatmap instructions. Outline `HR 9505` and `CTCAE v5.0` columns. Right margin callout: `H2 per-site dispatch consistently meets 90-second SLA. Cross-site transit relies on FAA Part 135 medical drone or hospital-charter aircraft within 30 minutes.`

Bottom 4-row sub-heatmap shows per-site posture (SF, SD, BO, AT) across the same 14 frameworks.

## Validation Checklist

1. PNG is 3300 x 2550 pixels.
2. Main 10 x 14 heatmap.
3. Sub-heatmap 4 x 14 below.
4. Outlined columns.
5. Callout box right margin.
6. Reference table.
7. Title, subtitle, header, footer present.
8. `§` throughout.
9. No em dash, no double dash, no triple dash.
10. No color outside palette.
