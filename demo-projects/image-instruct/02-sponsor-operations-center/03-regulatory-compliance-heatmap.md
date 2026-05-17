# Image Instruction 02-03: Sponsor Operations Regulatory and Risk Compliance Heatmap

[![Demo](https://img.shields.io/badge/Demo-02-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/02-sponsor-humanoid-operations-center.md)
[![Image](https://img.shields.io/badge/Image-03%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/02-sponsor-operations-center)
[![Orientation](https://img.shields.io/badge/Orientation-Landscape-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/02-sponsor-humanoid-operations-center-output/figures/02-03-regulatory-compliance-heatmap.png`

## Page Size and DPI

- Letter landscape, 11.0 x 8.5 inches, 300 dpi, 3300 x 2550 pixels, white facecolor.

## Chart Type

Annotated heatmap matrix. Rows are document classes flowing through the Sponsor Operations Center; columns are regulatory frameworks; cells colored by enforcement intensity. A second small heatmap below the main one breaks out the same matrix specifically for cross-trial signals.

## Title and Subtitle

- Title: `5x Optimus + Sonnet/Opus Sponsor Center Regulatory Enforcement Matrix`.
- Subtitle: `8 Document Classes x 16 Regulatory Frameworks - SPO-2026-001, 5 Trials, 168-Hour Cycle`.

## Header and Footer

- Header right: `Demo 02 / Image 03 of 10 / Landscape`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 02 Sponsor Humanoid Operations Center`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Rows (8 Document Classes)

1. `FDA RTCT Submission Packet`
2. `IRB Amendment Draft`
3. `CRA Call Summary`
4. `IMP Kit Manifest`
5. `AE Report (Site to Sponsor)`
6. `SAE Narrative`
7. `DSMB Monthly Summary`
8. `Sponsor SOP Update`

## Columns (16 Frameworks)

1. `21 CFR § 11` (Electronic Records and Signatures)
2. `21 CFR § 312` (IND Application)
3. `21 CFR § 50` (Informed Consent)
4. `ICH E6(R3)` (GCP)
5. `ICH E2A` (Expedited AE Reporting)
6. `ICH E2D` (Post-Approval Safety)
7. `21 CFR § 314.80` (Post-Marketing AE)
8. `HIPAA 45 CFR § 164.514(b)` (Safe Harbor)
9. `HIPAA 45 CFR § 164.502` (Minimum Necessary)
10. `EU GDPR Article 9` (Special Category Data)
11. `IEC 80601-2-77` (Medical Robot Safety)
12. `ISO 10218` (Industrial Robot Safety)
13. `HR 9504` (Physical AI Clinical Error Reduction)
14. `HR 9505` (Real-Time Patient-Sponsor Communication)
15. `FDA RTCT April 2026`
16. `DSMB Charter (Per-Trial)`

## Cell Values (8 x 16, integer 0 to 4)

Same scoring scheme as 01-03:
- 0 = N/A (Light Gray).
- 1 = Informational (Light Teal).
- 2 = Standard compliance (Forest Green 0.5 alpha).
- 3 = Active enforcement (Gold).
- 4 = Hard gate (Burgundy).

Each cell text shows the integer plus a 1-letter code (`L`, `H`, `E`, `R`) per 01-03 conventions.

## Bottom Sub-Heatmap (Cross-Trial Signals)

A second 5 x 16 heatmap below the main one with:

- Rows: the 5 active trials (`NSCLC IIIA`, `CRC IIB`, `Breast IIC`, `Prostate IIIA`, `Pancreatic IIA`).
- Columns: same 16 frameworks.
- Same color scheme. Captures per-trial regulatory exposure level.

## Annotations

- Outline `HIPAA 45 CFR § 164.514(b)` column with 1.5 pt Burgundy frame (primary failover gate).
- Outline `FDA RTCT April 2026` column with 1.5 pt Gold frame (primary submission window).
- Right margin callout box at y 0.50: `Failover to Claude Opus 4.7 1M cloud is hard-gated by the Safe Harbor column. 100 percent of cells in that column at level 4.`

## Right Margin Legend

- Discrete 5-step colorbar with labels matching 01-03.
- Per-framework short description table (16 rows).

## matplotlib Recipe

- Two stacked subplots: `gs = fig.add_gridspec(2, 2, height_ratios=[8, 5], width_ratios=[3, 1])`.
- Top-left: main 8 x 16 heatmap. Bottom-left: 5 x 16 sub-heatmap. Right column (top and bottom merged): legend and reference.
- `imshow` with custom `ListedColormap` and explicit `vmin`, `vmax`.

## Validation Checklist

1. PNG is 3300 x 2550 pixels.
2. Main heatmap 8 x 16 visible with every cell colored and annotated.
3. Sub-heatmap 5 x 16 below it.
4. Outlined columns (`HIPAA 45 CFR § 164.514(b)` Burgundy, `FDA RTCT April 2026` Gold).
5. Callout box visible on right margin.
6. Discrete colorbar with 5 steps.
7. Title, subtitle, header, footer present.
8. `§` appears throughout, not `SS` or `Section`.
9. No em dash, no double dash, no triple dash.
10. No emoji.
