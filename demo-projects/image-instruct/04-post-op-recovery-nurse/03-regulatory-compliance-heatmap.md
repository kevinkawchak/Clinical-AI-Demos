# Image Instruction 04-03: PACU Recovery Regulatory and Risk Compliance Heatmap

[![Demo](https://img.shields.io/badge/Demo-04-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/04-humanoid-post-op-recovery-nurse.md)
[![Image](https://img.shields.io/badge/Image-03%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/04-post-op-recovery-nurse)
[![Orientation](https://img.shields.io/badge/Orientation-Landscape-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/04-humanoid-post-op-recovery-nurse-output/figures/04-03-regulatory-compliance-heatmap.png`

## Page Size and DPI

- Letter landscape, 11.0 x 8.5 inches, 300 dpi, 3300 x 2550 pixels, white facecolor.

## Chart Type

Annotated heatmap. 12 PACU operational tasks x 14 standards.

## Title and Subtitle

- Title: `Digit V5 + Claude Haiku/Sonnet + Llama 4 PACU Compliance Matrix`.
- Subtitle: `12 PACU Tasks x 14 Standards - PAT-REC-0001 Day 0 Post-Op - 24-Hour Shift`.

## Header and Footer

- Header right: `Demo 04 / Image 03 of 10 / Landscape`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 04 Post-Op Recovery Nurse`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Rows (12 Tasks)

1. `Bedside Vitals Check`.
2. `Braden 2-Hour Reposition`.
3. `Chest Tube Drainage Read`.
4. `IV Pump Bolus Adjustment`.
5. `Pain Self-Report Pad Read`.
6. `Wound Visual Inspection (Camera)`.
7. `Oral Medication Administration Prep`.
8. `Companion Caregiver Update Call`.
9. `Audit Log Append`.
10. `On-Call Physician Escalation`.
11. `Hand-Off Summary to Day-Shift`.
12. `Patient Bed Egress Detection (Fall Risk)`.

## Columns (14 Standards)

1. `21 CFR § 50` (Informed Consent).
2. `21 CFR § 312` (IND Application).
3. `21 CFR § 11` (Electronic Records).
4. `ICH E6(R3)` (GCP).
5. `IEC 80601-2-77` (Medical Robot Safety).
6. `IEC 62366-1` (Usability Engineering).
7. `HIPAA 45 CFR § 164.514(b)` (Safe Harbor).
8. `HIPAA 45 CFR § 164.502` (Minimum Necessary).
9. `Braden Scale` (Pressure Injury Prevention).
10. `CTCAE v5.0` (Adverse Event Grading).
11. `Magnet Recognition Program Nursing Standards`.
12. `AHRQ Common Formats for Patient Safety`.
13. `The Joint Commission NPSG`.
14. `HR 9505 (Real-Time Patient-Sponsor Communication)`.

## Cell Values

Integer 0 to 4 with `L`, `H`, `E`, `R` overlay. Outline `Braden Scale` column with Forest Green frame and `IEC 80601-2-77` with Burgundy frame.

## Right Margin Callout

`Tier 3 Ollama Llama 4 70B local inference is mandatory for any cell touching Safe Harbor columns. Claude Haiku 4.5 routes there automatically when prompt contains PHI tokens.`

## matplotlib Recipe

Same conventions as 01-03, 02-03, 03-03.

## Validation Checklist

1. PNG is 3300 x 2550 pixels.
2. Heatmap 12 x 14 visible.
3. Outlined columns for Braden (Forest Green) and IEC 80601-2-77 (Burgundy).
4. Right margin callout present.
5. Reference table on right.
6. Title, subtitle, header, footer present.
7. `§` appears throughout.
8. No em dash, no double dash, no triple dash.
9. No color outside palette.
10. No emoji.
