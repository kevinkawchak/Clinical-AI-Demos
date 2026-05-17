# Image Instruction 04-08: PACU LLM Tier Escalation Funnel

[![Demo](https://img.shields.io/badge/Demo-04-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/04-humanoid-post-op-recovery-nurse.md)
[![Image](https://img.shields.io/badge/Image-08%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/04-post-op-recovery-nurse)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/04-humanoid-post-op-recovery-nurse-output/figures/04-08-process-funnel-chart.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

Vertical 7-stage funnel.

## Title and Subtitle

- Title: `Digit V5 PACU 24-Hour LLM Tier Escalation Funnel`.
- Subtitle: `Per-Tick from 86,400 Haiku Calls Down to On-Call Physician Activations`.

## Header and Footer

- Header right: `Demo 04 / Image 08 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 04 Post-Op Recovery Nurse`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Stages (7)

1. **Haiku 4.5 Tier 1 Ticks** (Teal): 86,400 across 24 hours.
2. **Haiku Confidence Below 0.85** (Teal lighter): escalation candidates.
3. **Sonnet 4.6 Tier 2 Invocations** (Teal darker): escalated reasoning.
4. **PHI-Bearing Reasoning Detected** (Burgundy): route to Tier 3.
5. **Ollama Llama 4 70B Tier 3 Calls** (Teal darkest): PHI handled locally.
6. **CTCAE Grade 3+ Predicted** (Burgundy darker): on-call physician trigger.
7. **On-Call Physician Activations (Final)** (Forest Green): HR 9505 SLA met.

## Layout, Annotations, matplotlib Recipe, Validation

Same conventions as prior funnel instructions. Left filter rule column. Right cumulative pass rate. Bottom note: `Approximately 2 to 5 on-call physician activations per 24-hour shift at v0.2.0.`

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. 7 trapezoidal stages narrowing downward.
3. Stage labels centered.
4. Filter rule column left.
5. Bottom note present.
6. Title, subtitle, header, footer present.
7. No em dash, no double dash, no triple dash.
8. No color outside palette.
9. No emoji.
10. HR 9505 reference correct.
