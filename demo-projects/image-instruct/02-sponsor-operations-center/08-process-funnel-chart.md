# Image Instruction 02-08: Sponsor Center FDA RTCT Submission Funnel

[![Demo](https://img.shields.io/badge/Demo-02-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/02-sponsor-humanoid-operations-center.md)
[![Image](https://img.shields.io/badge/Image-08%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/02-sponsor-operations-center)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/02-sponsor-humanoid-operations-center-output/figures/02-08-process-funnel-chart.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

Vertical process funnel with 7 trapezoidal stages. Tracks an inbound CRA call or AE report through Safe Harbor, Sonnet draft, Opus review, regulatory completeness checks, and final FDA RTCT submission.

## Title and Subtitle

- Title: `Optimus + Sonnet/Opus Sponsor Center: FDA RTCT Submission Funnel`.
- Subtitle: `Inbound Site Document to FDA RTCT Submission - Weekly Cycle Across 5 Trials`.

## Header and Footer

- Header right: `Demo 02 / Image 08 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 02 Sponsor Humanoid Operations Center`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Stages (7, top to bottom)

1. **Inbound Site Documents Total** (Teal): aggregate inbound stream from all 5 sites in 1 week.
2. **Passes Safe Harbor PHI Gate** (Burgundy): subset that the HIPAA 45 CFR § 164.514(b) gate clears.
3. **Sonnet 4.6 Drafts Within Budget** (Teal lighter): subset where Sonnet 4.6 produces a draft within the 100 ms per-tick budget.
4. **Opus 4.7 1M Review Confirms** (Teal darker): subset where Opus 4.7 review confirms regulatory completeness.
5. **5x Optimus Co-Sign and Archive** (Deep Navy): subset where 1 of the 5 Optimus humanoids physically signs (electronic 21 CFR § 11 signature plus physical countersign on dossier shelf).
6. **DSMB Charter Compatibility Check** (Forest Green): subset that passes the per-trial DSMB charter check.
7. **FDA RTCT Portal Submission** (Gold): subset successfully submitted to the FDA Real-Time Continuous Trials portal.

## Layout, Annotations, matplotlib Recipe

Same conventions as 01-08. Left margin shows the filter rule per stage. Right margin shows cumulative pass rate. Bottom note: `Average end-to-end time from inbound document to FDA RTCT submission target under 4 hours at v0.2.0.`

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. 7 trapezoidal stages stacked, narrowing downward.
3. Stage labels centered inside, counts and percentages on right.
4. Left filter rule column populated.
5. Bottom note present.
6. Title, subtitle, header, footer present.
7. `§` appears throughout regulatory references.
8. No em dash, no double dash, no triple dash.
9. No color outside palette.
10. No emoji.
