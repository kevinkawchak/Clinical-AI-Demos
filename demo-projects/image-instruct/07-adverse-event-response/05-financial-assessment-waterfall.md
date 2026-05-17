# Image Instruction 07-05: AE Response Network 5-Year TCO Waterfall

[![Demo](https://img.shields.io/badge/Demo-07-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/07-humanoid-24-7-adverse-event-response.md)
[![Image](https://img.shields.io/badge/Image-05%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/07-adverse-event-response)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/07-humanoid-24-7-adverse-event-response-output/figures/07-05-financial-assessment-waterfall.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

Vertical waterfall, 16 bars covering network-wide 5-year TCO.

## Title and Subtitle

- Title: `3x H2 + Per-Site Claude Opus 4-Site Network 5-Year TCO Waterfall`.
- Subtitle: `PAT-NET-001 4-Site Network - 24/7 AE Response - USD Thousands`.

## Header and Footer

- Header right: `Demo 07 / Image 05 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 07 Adverse Event Response`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Bars (16)

1. `Year 0 Baseline 24/7 Human On-Call x 4 Sites` (Slate).
2. `+ 3x Unitree H2 Acquisition` (Deep Navy).
3. `+ 3x H2 5-Year Service Contract` (Deep Navy).
4. `+ 4x Claude Opus 4.7 1M On-Prem Per-Site Clusters` (Teal).
5. `+ Continental Coordination Bus Infra` (Mauve).
6. `+ FAA Part 135 Medical Drone Subscription` (Mauve darker).
7. `+ Hospital Charter Aircraft Reserve` (Gold).
8. `+ Per-Site IRB Coordination Overhead` (Burgundy).
9. `- Human Night-Shift On-Call Wage Offset` (Forest Green negative).
10. `- SAE Narrative Cycle Time Cost Offset` (Forest Green negative).
11. `- HR 9505 SLA Penalty Avoidance` (Forest Green negative).
12. `- Cross-Site Audit Reconciliation Manual Hours Offset` (Forest Green negative).
13. `+ Annual O and M plus Spare Parts (Per H2)` (Gold).
14. `+ Cyber and HIPAA Audit Reserve` (Burgundy).
15. `+ FDA RTCT Submission Bandwidth Allocation` (Slate).
16. `Cumulative 5-Year Network TCO` (Deep Navy total).

## Annotations

- Baseline dashed reference line at bar 1.
- Callout: `HR 9505 SLA penalty avoidance alone justifies cluster cost. Cross-site audit reconciliation offset is the second largest contributor.`

## Layout and matplotlib Recipe

Same conventions as prior waterfall instructions.

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. 16 bars with connectors.
3. Cumulative bar.
4. Baseline reference line.
5. Callout.
6. Title, subtitle, header, footer present.
7. No em dash, no double dash, no triple dash.
8. No color outside palette.
9. No emoji.
10. Bar labels unclipped.
