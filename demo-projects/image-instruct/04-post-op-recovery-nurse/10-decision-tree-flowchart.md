# Image Instruction 04-10: PACU Patient Deterioration Decision Tree

[![Demo](https://img.shields.io/badge/Demo-04-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/04-humanoid-post-op-recovery-nurse.md)
[![Image](https://img.shields.io/badge/Image-10%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/04-post-op-recovery-nurse)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/04-humanoid-post-op-recovery-nurse-output/figures/04-10-decision-tree-flowchart.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

Top-down decision tree.

## Title and Subtitle

- Title: `Digit V5 + Claude Tier PACU Patient Deterioration Decision Tree`.
- Subtitle: `Vitals Anomaly Detected - Triage - Tier Routing - Action - On-Call Activation`.

## Header and Footer

- Header right: `Demo 04 / Image 10 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 04 Post-Op Recovery Nurse`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Tree Structure

```
              [Vitals Anomaly Detected]
                        |
              <Haiku Confidence >= 0.85?>
                  |              |
                Yes             No
                  |              |
        [Digit V5 Vitals    [Escalate to
         Re-Check]            Sonnet 4.6]
                                |
                      <Contains PHI?>
                          |        |
                         No       Yes
                          |        |
                  [Sonnet Plan   [Route to
                   Action]        Llama 4 70B Local]
                                       |
                                  <CTCAE Grade?>
                                       |
                              +--------+--------+
                              |        |        |
                            <=2       3        4
                              |        |        |
                       [Digit V5  [On-Call    [Code Team
                        Action]    Physician   Activation
                                   Activation]  + Surgeon]
```

## Node Types and Colors

- Diamonds Slate.
- Forest Green: Digit V5 in-place action.
- Teal lighter, mid, darker: tier routing.
- Burgundy: on-call physician.
- Burgundy darker: code team activation.

## Annotations

- Pinned to PHI diamond: `If Tier 2 prompt contains 18 HIPAA identifiers, route to Tier 3 Llama 4 70B local. No cloud inference.`
- Pinned to On-Call Physician: `HR 9505 acknowledgment SLA 1 hour. Digit V5 captures continuous video clip starting at activation T-30 s.`
- Pinned to Code Team: `Digit V5 stays bedside, hands off chest compressions to human team, continues vitals capture.`

## Layout, matplotlib Recipe, Validation

Same conventions as prior decision tree instructions.

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. Root at top, leaves at bottom.
3. 3 decision diamonds, 5+ action rectangles.
4. Edges labeled.
5. Pinned annotations present.
6. Title, subtitle, header, footer present.
7. No em dash, no double dash, no triple dash.
8. No color outside palette.
9. No emoji.
10. Tree fits within margins.
