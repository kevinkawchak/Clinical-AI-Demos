# Image Instruction 07-08: AE Detection to Sponsor Acknowledgment Funnel

[![Demo](https://img.shields.io/badge/Demo-07-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/07-humanoid-24-7-adverse-event-response.md)
[![Image](https://img.shields.io/badge/Image-08%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/07-adverse-event-response)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/07-humanoid-24-7-adverse-event-response-output/figures/07-08-process-funnel-chart.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

Vertical 7-stage funnel covering AE event lifecycle from detection to sponsor acknowledgment.

## Title and Subtitle

- Title: `3x H2 + Per-Site Claude Opus AE Lifecycle Funnel`.
- Subtitle: `Detection to Sponsor Acknowledgment - 168-Hour Cycle - 4-Site Network`.

## Header and Footer

- Header right: `Demo 07 / Image 08 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 07 Adverse Event Response`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Stages (7)

1. **AE Events Detected** (Burgundy): per-site sensor + self-report inbound.
2. **Per-Site Claude Opus Triage Pass** (Teal): triage rule pass.
3. **H2 Bedside Arrival Under 90 s** (Deep Navy).
4. **CTCAE Grading Under 1 Hour (HR 9505)** (Gold).
5. **On-Call Physician Acknowledged** (Burgundy darker).
6. **Sponsor Acknowledged Under 1 Hour (HR 9505)** (Burgundy darker).
7. **AE Closed and Audit Reconciled Cross-Site** (Forest Green).

## Layout, Annotations, matplotlib Recipe, Validation

Same conventions as prior funnel instructions. Bottom note: `Approximately 60 to 90 AE events per week network-wide. ~95 percent close within HR 9505 1-hour cumulative SLA at v0.2.0 reference.`

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. 7 stacked trapezoids.
3. Stage labels.
4. Filter rule column left.
5. Bottom note.
6. Title, subtitle, header, footer present.
7. No em dash, no double dash, no triple dash.
8. No color outside palette.
9. No emoji.
10. Cumulative pass rate right.
