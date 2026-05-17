# Image Instruction 09-10: Radiation Oncology CBCT Tolerance Decision Tree

[![Demo](https://img.shields.io/badge/Demo-09-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/09-humanoid-radiation-oncology-technologist.md)
[![Image](https://img.shields.io/badge/Image-10%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/09-radiation-oncology-technologist)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/09-humanoid-radiation-oncology-technologist-output/figures/09-10-decision-tree-flowchart.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

Top-down decision tree for CBCT-CT alignment verification and Claude Opus Gate 2 escalation.

## Title and Subtitle

- Title: `LINAC CBCT Alignment Tolerance Decision Tree (Claude Opus Gate 2)`.
- Subtitle: `kV CBCT Acquired - Alignment Check - Tolerance Escalation - Beam-On or Re-Align`.

## Header and Footer

- Header right: `Demo 09 / Image 10 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 09 Radiation Oncology Technologist`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Tree Structure

```
              [kV CBCT Acquired by Optimus]
                        |
              <Alignment Within 1 mm?>
                  |              |
                Yes             No
                  |              |
        [Atlas Confirms     [Atlas Re-Verifies
         Mask Position]      Mask Position]
                  |                |
        [Claude Opus       <Re-Verification Pass?>
         Gate 2 Pass]            |        |
                  |             Yes       No
        [Beam-On                |          |
         Authorized]      [Optimus Re-     [Claude Opus
                          Acquire CBCT]    Escalation
                                  |        Gate]
                          <Within 1 mm?>          |
                              |        |    <Escalation Verdict?>
                            Yes       No      |              |
                              |        |    Approve         Hold
                       [Beam-On  [Plan Re-   |                |
                        Authorized] Author   [Beam-On      [Re-Schedule
                                    +        Authorized,  Patient + Notify
                                    Re-Run]  Append      Radiation
                                             Rationale]   Oncologist]
```

## Node Types and Colors

- Diamonds Slate.
- Forest Green: pass to beam-on.
- Burgundy: escalation hold.
- Deep Navy: Atlas/Optimus actions.
- Teal darker: Claude Opus arbiter.
- Mauve: patient re-schedule.

## Annotations

- Pinned to Alignment diamond: `Sub-millimeter tolerance. AAPM TG-100 risk-informed thresholds apply.`
- Pinned to Claude Opus Escalation Gate: `Reads CBCT image plus CT plan plus historical alignment statistics for this patient. 200 ms reasoning budget.`
- Pinned to Beam-On Authorized: `LINAC interlock cleared. Atlas withdraws to safe pose. Optimus initiates HyperArc.`

## Layout, matplotlib Recipe, Validation

Same conventions as prior decision tree instructions.

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. 4 decision diamonds, 5+ action rectangles.
3. Edges labeled.
4. Pinned annotations.
5. Title, subtitle, header, footer present.
6. No em dash, no double dash, no triple dash.
7. No color outside palette.
8. No emoji.
9. Tree fits within margins.
10. Root at top.
