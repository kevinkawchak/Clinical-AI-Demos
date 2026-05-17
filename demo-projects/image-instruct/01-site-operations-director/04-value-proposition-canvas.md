# Image Instruction 01-04: Atlas Site Director Value Proposition Canvas

[![Demo](https://img.shields.io/badge/Demo-01-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/01-humanoid-site-operations-director.md)
[![Image](https://img.shields.io/badge/Image-04%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/01-site-operations-director)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/01-humanoid-site-operations-director-output/figures/01-04-value-proposition-canvas.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

Strategyzer-style Value Proposition Canvas. Two top-level shapes: a square on the right (Value Map for Atlas + Claude Opus 4.7) and a circle on the left (Customer Profile for the Trial Site Operations stakeholder). Each shape is subdivided into three sub-panels.

## Title and Subtitle

- Title: `Atlas Electric + Claude Opus 4.7 1M Site Director Value Proposition Canvas`.
- Subtitle: `Stakeholder: Trial Site Operations Director, Investigator, and Sponsor CRA at PAT-SITE-001`.

## Header and Footer

- Header right: `Demo 01 / Image 04 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 01 Site Operations Director`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Layout Specification

- Title block y from 0.94 to 0.98.
- Subtitle y 0.91 to 0.93.
- Canvas area y 0.10 to 0.88, full width with 0.5 inch side margins.
- Value Map (square, right) at x 0.50 to 0.95, y 0.18 to 0.85. Subdivided horizontally into 3 stacked panels.
- Customer Profile (circle, left) centered at x 0.27, y 0.50, radius 0.22 normalized units. Internally divided into 3 sectors by 120-degree lines.
- A 1.5 pt Slate arrow points from the Value Map to the Customer Profile labeled `Fit`.

## Value Map Panels (right square, top to bottom)

1. **Products and Services** (Deep Navy header on Off-White panel):
   - `Atlas Electric Humanoid (28 DOF, 11 kg/arm, IP67) shift director on the floor 08:00 to 16:00 PDT`.
   - `Claude Opus 4.7 1M context on-prem planner at 1 Hz`.
   - `Safety Arbiter with IEC 80601-2-77 and ISO 10218 enforcement`.
   - `Per-tick audit log with hash-chained provenance`.
2. **Pain Relievers** (Burgundy header on Off-White panel):
   - `Eliminates the human shift director night-cover gap`.
   - `Routes IRB and 21 CFR § 312 gates 100 percent of the time`.
   - `Bounds cumulative cross-arm force at 15 N during patient transfer`.
   - `Logs every Atlas action with rationale for FDA RTCT inspection`.
3. **Gain Creators** (Forest Green header on Off-White panel):
   - `Reduces per-tick decision latency from 8 to 12 minutes (human) to 200 ms (Claude Opus)`.
   - `Frees the human director for cross-trial strategy work`.
   - `Provides continuous shift-coverage with no overtime`.
   - `Surfaces patient acuity signals 4 to 7 minutes earlier than human triage`.

## Customer Profile Sectors (left circle)

1. **Customer Jobs** (top 120-degree sector, Deep Navy):
   - `Coordinate 12 surgical bays, 24 recovery rooms, 8 imaging suites, 1 pharmacy clean room`.
   - `Allocate Atlas humanoid actions across competing priorities at 1-minute granularity`.
   - `Maintain ICH E6(R3) GCP compliance for 10 active patients`.
2. **Pains** (bottom-left 120-degree sector, Burgundy):
   - `Human shift director burnout from sustained 1-minute decision cadence`.
   - `Audit gaps when manual logging falls behind action cadence`.
   - `Cross-bay reassignment errors during simultaneous AE events`.
3. **Gains** (bottom-right 120-degree sector, Forest Green):
   - `Real-time bay status visibility for sponsor CRA dashboards`.
   - `Sub-second AE escalation to on-call physician`.
   - `Provable compliance posture for FDA RTCT inspection`.

## Color Mapping

- Value Map background: Off-White `#F7FAFC`. Header bars: Deep Navy, Burgundy, Forest Green per sub-panel.
- Customer Profile circle outline: Slate 2 pt. Sector divider lines: Slate 1 pt.
- Sector text headers in the matching color per the section above.

## matplotlib Recipe

- Use `matplotlib.patches.FancyBboxPatch` with rounded corners for the Value Map outer square and three inner panels.
- Use `matplotlib.patches.Circle` for the Customer Profile, then `matplotlib.patches.Wedge` for the three 120-degree sectors.
- Use `ax.text` with `wrap=True` and explicit `wrapping width` calculated from the panel size.
- Use `matplotlib.patches.FancyArrowPatch` for the `Fit` arrow connecting the two shapes.

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. Value Map square on the right with 3 stacked panels labeled and populated.
3. Customer Profile circle on the left with 3 sectors labeled and populated.
4. `Fit` arrow visible between the two shapes.
5. Title, subtitle, header, footer present.
6. `§` appears in `21 CFR § 312`.
7. No em dash, no double dash, no triple dash.
8. No color outside palette.
9. No emoji.
10. Text in every panel and sector fits without clipping.
