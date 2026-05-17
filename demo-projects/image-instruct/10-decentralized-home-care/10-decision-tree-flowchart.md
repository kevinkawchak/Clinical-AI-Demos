# Image Instruction 10-10: Home DCT HR 9507 Data Self-Custody Revocation Decision Tree

[![Demo](https://img.shields.io/badge/Demo-10-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/10-humanoid-decentralized-home-care.md)
[![Image](https://img.shields.io/badge/Image-10%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/10-decentralized-home-care)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/10-humanoid-decentralized-home-care-output/figures/10-10-decision-tree-flowchart.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

Top-down decision tree showing per-cycle HR 9507 data self-custody check including patient-initiated revocation.

## Title and Subtitle

- Title: `Figure 03 Field Home DCT HR 9507 Data Self-Custody Decision Tree`.
- Subtitle: `Per-Cycle - Patient Approval - Revocation Path - Aggregator Submission or Personal Vault`.

## Header and Footer

- Header right: `Demo 10 / Image 10 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 10 Decentralized Home Care`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Tree Structure

```
              [End-of-Cycle Summary Encoded]
                        |
              <Patient Approved Submission?>
                  |              |
                Yes             No (or Pending)
                  |              |
        [De-Identified      <Patient Action?>
         Submission to            |       |
         Federated           Revoke    No Action 24 h
         Aggregator]              |       |
                          [Summary    [Submit at Next
                           Discarded   Cycle After
                           + Personal  Re-Confirm]
                           Vault Only]
                                  |
                          <Patient Re-Confirms?>
                              |       |
                            Yes      No (Subsequent Cycles)
                              |       |
                       [Submit at  [Continue
                        Next Cycle]  Discarding +
                                     Notify Sponsor
                                     of Revocation
                                     Status]
```

## Node Types and Colors

- Diamonds Slate.
- Forest Green: submission approved.
- Burgundy: revocation paths.
- Mauve: patient personal vault retention.
- Teal lighter: pending re-confirm.

## Annotations

- Pinned to Patient Approval diamond: `HR 9507 primary right. Real-time tablet toggle. Patient may revoke at any time before queue-out.`
- Pinned to Summary Discarded: `Cycle data retained ONLY in Patient Personal Vault on the Orin AGX edge device. Sponsor receives only a revocation notice (no PHI).`
- Pinned to Subsequent Cycles Continue Discarding: `Sponsor cohort insights flagged with reduced patient count. Patient continues trial enrollment; only the federated aggregator stream is paused.`

## Layout, matplotlib Recipe, Validation

Same conventions as prior decision tree instructions.

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. 3 decision diamonds, 5+ action rectangles.
3. Edges labeled.
4. Pinned annotations.
5. Title, subtitle, header, footer present.
6. HR 9507 references throughout.
7. No em dash, no double dash, no triple dash.
8. No color outside palette.
9. No emoji.
10. Tree fits within margins.
