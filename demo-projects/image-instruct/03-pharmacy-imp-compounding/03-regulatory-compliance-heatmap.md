# Image Instruction 03-03: Pharmacy CAR-T Regulatory and Risk Compliance Heatmap

[![Demo](https://img.shields.io/badge/Demo-03-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/03-humanoid-pharmacy-imp-compounding.md)
[![Image](https://img.shields.io/badge/Image-03%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/03-pharmacy-imp-compounding)
[![Orientation](https://img.shields.io/badge/Orientation-Landscape-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/03-humanoid-pharmacy-imp-compounding-output/figures/03-03-regulatory-compliance-heatmap.png`

## Page Size and DPI

- Letter landscape, 11.0 x 8.5 inches, 300 dpi, 3300 x 2550 pixels, white facecolor.

## Chart Type

Annotated heatmap. Rows are 10 CAR-T compounding phases. Columns are 14 regulatory and clean-room standards. Cells colored 0 to 4 per the shared scheme (Light Gray, Light Teal, Forest Green alpha 0.5, Gold, Burgundy).

## Title and Subtitle

- Title: `Figure 03 + GPT-5.5 Thinking CAR-T Compounding Compliance Matrix`.
- Subtitle: `10 Compounding Phases x 14 Standards - ISO Class 5 Clean Room - PAT-IMP-0001`.

## Header and Footer

- Header right: `Demo 03 / Image 03 of 10 / Landscape`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 03 Pharmacy IMP Compounding`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Rows (10 Compounding Phases)

1. `Gowning and Class 7 Entry`.
2. `Biosafety Cabinet Pre-Use Check`.
3. `Apheresis Bag Verification`.
4. `Lentiviral Vector Thaw`.
5. `T-Cell Activation Co-Culture`.
6. `T-Cell Expansion (60 to 180 minutes)`.
7. `Cytokine Cocktail Addition`.
8. `Final Wash and Concentration`.
9. `Compounded Bag Verification`.
10. `Batch Record Seal and Cryo Transfer`.

## Columns (14 Standards)

1. `USP 800` (Hazardous Drugs).
2. `USP 797` (Sterile Compounding).
3. `21 CFR § 211` (cGMP).
4. `21 CFR § 212` (Positron-Emission Tomography Drugs - reference baseline).
5. `21 CFR § 312` (IND Application).
6. `21 CFR § 11` (Electronic Records).
7. `ICH Q9(R1)` (Quality Risk Management).
8. `ICH Q10` (Pharmaceutical Quality System).
9. `IEC 62304` (Software Lifecycle).
10. `IEC 80601-2-77` (Medical Robot Safety).
11. `ISO 14644-1` (Clean Room).
12. `ISO 13485` (Medical Device QMS).
13. `EU Annex 1` (Manufacture of Sterile Medicinal Products).
14. `OSHA 29 CFR § 1910.1030` (Bloodborne Pathogens).

## Cell Values and Annotations

Integer 0 to 4 with 1-letter overlay (`L`, `H`, `E`, `R`). Outline `USP 800` with Burgundy frame (primary hazardous handling). Outline `21 CFR § 211` with Deep Navy frame (primary cGMP). Right margin callout: `Figure 03 hand 24-finger-joint 1 mm RMS plus GPT-5.5 Thinking 100 ms cadence holds all 10 phases at level 2 or above for the full 4-hour session at v0.2.0.`

## Right Margin Reference Table

14-row table of `Short Name` and `Full Reference`.

## matplotlib Recipe

Same conventions as 01-03 and 02-03. `imshow` with custom 5-level `ListedColormap`.

## Validation Checklist

1. PNG is 3300 x 2550 pixels.
2. 10 x 14 heatmap visible with every cell colored.
3. Outlined columns for `USP 800` (Burgundy) and `21 CFR § 211` (Deep Navy).
4. Callout box on right margin.
5. Reference table with all 14 standards.
6. Title, subtitle, header, footer present.
7. `§` appears throughout regulatory references.
8. No em dash, no double dash, no triple dash.
9. No color outside palette.
10. No emoji.
