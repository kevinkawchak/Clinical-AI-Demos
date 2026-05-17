# Image Instruction 04-07: PACU Recovery Patient Signal and LLM Tier Sankey

[![Demo](https://img.shields.io/badge/Demo-04-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/04-humanoid-post-op-recovery-nurse.md)
[![Image](https://img.shields.io/badge/Image-07%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/04-post-op-recovery-nurse)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/04-humanoid-post-op-recovery-nurse-output/figures/04-07-sankey-flow-diagram.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

Sankey with 4 vertical levels. Levels are: patient signal class, LLM tier handling, Digit V5 action category, terminal outcome.

## Title and Subtitle

- Title: `PAT-REC-0001 24-Hour Patient Signal and LLM Tier Routing Sankey`.
- Subtitle: `Haiku Default to Sonnet Escalation to Llama 4 70B Local PHI - Digit V5 Action - Outcome`.

## Header and Footer

- Header right: `Demo 04 / Image 07 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 04 Post-Op Recovery Nurse`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Levels (4)

1. **Level 1 Patient Signal Class**: `Vitals OK`, `Vitals Anomaly`, `Pain Spike`, `Bed Egress Detected`, `Chest Tube Drainage Anomaly`, `Companion Caregiver Call`.
2. **Level 2 LLM Tier**: `Tier 1 Haiku 4.5`, `Tier 2 Sonnet 4.6`, `Tier 3 Llama 4 70B (PHI)`.
3. **Level 3 Digit V5 Action**: `Reposition`, `Vitals Re-Check`, `Pain Re-Score`, `IV Pump Bolus Request`, `On-Call Physician Activation`, `Audit Log Append`.
4. **Level 4 Terminal Outcome**: `Resolved In-Place`, `Pending Surgeon Review`, `On-Call Physician Activated`, `Companion App Update Sent`.

## Color Mapping

- Patient signals: Mauve (vitals), Burgundy (anomaly, egress), Slate (caregiver call).
- LLM tiers: Teal lighter, mid, darker.
- Digit V5 actions: Deep Navy.
- Outcomes: Forest Green (Resolved), Gold (Pending), Burgundy (Physician Activated), Slate (App Update).

## Layout, Annotations, matplotlib Recipe, Validation

Same conventions as prior sankey instructions. Pinned callout: `Tier 3 Llama 4 70B handles 100 percent of PHI-bearing patient self-report. Zero PHI egress.`

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. 4 columns with all listed nodes.
3. Source-colored flows.
4. Level titles at top.
5. Pinned callout.
6. Title, subtitle, header, footer present.
7. No em dash, no double dash, no triple dash.
8. No color outside palette.
9. No emoji.
10. Flow alpha 0.50.
