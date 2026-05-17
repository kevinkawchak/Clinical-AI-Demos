# Image Instruction 03-08: Pharmacy CAR-T Compounding Step Approval Funnel

[![Demo](https://img.shields.io/badge/Demo-03-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/03-humanoid-pharmacy-imp-compounding.md)
[![Image](https://img.shields.io/badge/Image-08%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/03-pharmacy-imp-compounding)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/03-humanoid-pharmacy-imp-compounding-output/figures/03-08-process-funnel-chart.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

Vertical process funnel, 7 trapezoidal stages. Filters compounding steps from candidate through final batch record seal.

## Title and Subtitle

- Title: `Figure 03 + GPT-5.5 Thinking Compounding Step Approval Funnel`.
- Subtitle: `Candidate Step to Batch Record Seal - 4-Hour CAR-T Session - PAT-IMP-0001`.

## Header and Footer

- Header right: `Demo 03 / Image 08 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 03 Pharmacy IMP Compounding`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Stages (7, top to bottom)

1. **Candidate Steps Proposed** (Teal): GPT-5.5 Thinking emits a candidate step in JSON.
2. **Within USP 800 + USP 797 Envelope** (Burgundy): hazardous-handling + sterile-compounding bounds.
3. **Within 8 N Tip Force Limit** (Deep Navy): cumulative cross-hand force projection check.
4. **Within 5 ms E-Stop Window** (Burgundy darker): clean-room E-stop budget check.
5. **IEC 62304 Class C Verifier Pass** (Slate): software-lifecycle verifier pass.
6. **Figure 03 Dispatcher Committed** (Deep Navy darker): physical motion command dispatched.
7. **Batch Record Append Sealed** (Forest Green): 21 CFR § 211 batch record appended and hash-chained.

## Layout, Annotations, matplotlib Recipe

Same conventions as 01-08 and 02-08. Left filter rule column. Right cumulative pass rate. Bottom note: `Approximately 7,200 batch-record entries per 4-hour session (1 per 2 seconds average).`

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. 7 stacked trapezoids narrowing downward.
3. Stage labels centered; counts and percentages on right.
4. Filter rule column on left.
5. Bottom note.
6. Title, subtitle, header, footer present.
7. `§` in `21 CFR § 211`.
8. No em dash, no double dash, no triple dash.
9. No color outside palette.
10. No emoji.
