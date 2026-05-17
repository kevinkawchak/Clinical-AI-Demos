# Image Instruction 10-07: Home DCT Data and Consent Sankey

[![Demo](https://img.shields.io/badge/Demo-10-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/10-humanoid-decentralized-home-care.md)
[![Image](https://img.shields.io/badge/Image-07%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/10-decentralized-home-care)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/10-humanoid-decentralized-home-care-output/figures/10-07-sankey-flow-diagram.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

Sankey with 4 vertical levels showing data and consent flows from patient home to sponsor while honoring HR 9507.

## Title and Subtitle

- Title: `Figure 03 Field Home DCT Data and Consent Sankey`.
- Subtitle: `Patient Generation - Edge Inference - De-Identification - Federated Aggregator vs. Revoked`.

## Header and Footer

- Header right: `Demo 10 / Image 07 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 10 Decentralized Home Care`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Levels (4)

1. **Level 1 Patient-Generated Data**: `Vitals`, `Pill Adherence`, `Lu-177 Confirmation`, `Self-Report Tablet`, `Family Caregiver Note`.
2. **Level 2 Edge Inference (Claude Haiku 4.5 on Orin)**: `Tier A Anomaly`, `Tier B Routine`, `Tier C Caregiver-Bound`.
3. **Level 3 HR 9507 Verdict**: `Patient Approved`, `Patient Revoked`, `Patient Pending Re-Confirm`.
4. **Level 4 Terminal**: `Federated Aggregator (De-Identified)`, `Patient Personal Vault Only`, `Family Caregiver App`, `Dropped (Revoked)`.

## Color, Layout, Annotations, matplotlib Recipe

Same conventions as prior sankey instructions. Mauve for patient data, Teal for edge inference, Burgundy for HR 9507 verdicts, Forest Green / Slate / Gold / Burgundy darker for terminals. Pinned callout: `Zero PHI egress: only Tier A and Tier B with patient approval reach federated aggregator as de-identified summary. Revocation flow back to Patient Personal Vault.`

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. 4 columns with all listed nodes.
3. Flow widths proportional.
4. Level titles.
5. Callout.
6. Title, subtitle, header, footer present.
7. HR 9507 reference correct.
8. No em dash, no double dash, no triple dash.
9. No color outside palette.
10. No emoji.
