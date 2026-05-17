# Image Instruction 03-01: Figure 03 + GPT-5.5 Thinking CAR-T Pharmacy Compounding Architecture

[![Demo](https://img.shields.io/badge/Demo-03-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/03-humanoid-pharmacy-imp-compounding.md)
[![Image](https://img.shields.io/badge/Image-01%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/03-pharmacy-imp-compounding)
[![Orientation](https://img.shields.io/badge/Orientation-Landscape-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/03-humanoid-pharmacy-imp-compounding-output/figures/03-01-system-architecture-control-loop.png`

## Page Size and DPI

- Letter landscape, 11.0 x 8.5 inches, 300 dpi, 3300 x 2550 pixels, white facecolor.

## Chart Type

System architecture flowchart for a Figure 03 humanoid plus GPT-5.5 Thinking on-prem (Ollama-style) control loop, compounding autologous CD19 CAR-T cell therapy in an ISO Class 5 clean room. Right one-third of the page renders the ISO Class 5 plus 7 plus 8 clean-room zoning with the Figure 03 station, biosafety cabinet, incubator, cryo bank, and exit airlock.

## Title and Subtitle

- Title: `Figure 03 + GPT-5.5 Thinking On-Prem CAR-T Pharmacy Compounding Control Loop`.
- Subtitle: `PAT-IMP-0001 Stage IV DLBCL Autologous CD19 CAR-T 2 x 10^7 cells per kg - 4-Hour Session, 100 ms LLM Cadence`.

## Header and Footer

- Header right: `Demo 03 / Image 01 of 10 / Landscape`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 03 Pharmacy IMP Compounding`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Layout Specification

- Left two-thirds (x 0.0 to 0.66) holds the architecture flowchart with three swimlanes.
- Right one-third (x 0.66 to 1.0) holds the clean room zoning.

## Inbound Lane (top, y 0.70 to 0.92)

Six rounded rectangles:

1. `Apheresis Bag (Patient T Cells)` (Mauve).
2. `Lentiviral Vector Vial` (Burgundy).
3. `Cytokine Cocktail Vials` (Mauve).
4. `Cryo Bank IDs and Lot Numbers` (Slate).
5. `USP 800 + USP 797 Reference SOPs` (Burgundy).
6. `21 CFR § 211 cGMP Batch Record Template` (Slate).

## Middle Lane (LLM + Figure 03 Loop, y 0.32 to 0.66)

Six rounded rectangles:

1. `Figure 03 Humanoid` (Deep Navy). Sub-label: `32 DOF, 1.68 m, 60 kg, 24-finger-joint hand 1 mm RMS, IP67`.
2. `Clean Room State Aggregator` (Slate). Sub-label: `temperature, particle count, biosafety cabinet airflow`.
3. `GPT-5.5 Thinking On-Prem (Ollama-style)` (Teal). Sub-label: `100 ms cadence, on-prem inference cluster`.
4. `IEC 62304 Software Lifecycle Verifier` (Burgundy). Sub-label: `class C medical device software`.
5. `Safety Arbiter` (Burgundy). Sub-label: `IEC 80601-2-77 + ISO 14644-1 clean-room safety; 5 ms E-stop`.
6. `Figure 03 Dispatcher` (Deep Navy). Sub-label: `8 N cumulative tip force CAR-T shear protection`.

Closed-loop return arrow from Dispatcher back to Figure 03.

## Outbound Lane (bottom, y 0.06 to 0.28)

Six rounded rectangles:

1. `Compounded CAR-T Infusion Bag` (Forest Green).
2. `Per-Step Batch Record Append (21 CFR § 211)` (Slate).
3. `Particle Count Log` (Slate).
4. `Biosafety Cabinet Airflow Log` (Slate).
5. `IMP Manifest Update (to Sponsor Demo 02)` (Mauve).
6. `Cryo Bank Re-Storage Event` (Mauve darker).

## Clean Room Zoning (right one-third)

Stylized clean-room plan:

- ISO Class 8 entry vestibule (light gray fill).
- ISO Class 7 gowning room (light Teal fill).
- ISO Class 5 main compounding zone (light Forest Green fill) with the Figure 03 silhouette at the biosafety cabinet.
- Cryo bank corner (Mauve fill).
- Incubator bank (Gold fill).
- Exit airlock (light gray fill).

## Annotations

- Pinned to Figure 03: `24-finger-joint hand at 1 mm RMS handles 1.5 mL T-cell aliquots without shear.`
- Pinned to GPT-5.5 Thinking: `Ollama-style on-prem deployment. Zero PHI egress. 100 ms per-tick budget for compounding step planning.`
- Pinned to Safety Arbiter: `5 ms surgical-grade E-stop. 8 N cumulative cross-hand tip-force ceiling for CAR-T cell viability.`

## Color Mapping

- Humanoid: Deep Navy.
- LLM: Teal.
- Safety / regulatory: Burgundy.
- Reagent inputs (T cells, vector, cytokines): Mauve.
- Output IMP: Forest Green.
- Audit / log: Slate.

## matplotlib Recipe

Same conventions as 01-01 and 02-01. `FancyBboxPatch`, `FancyArrowPatch` with closed-loop arc, three swimlanes, zoning overlay using filled `matplotlib.patches.Rectangle` with light alpha.

## Validation Checklist

1. PNG is 3300 x 2550 pixels.
2. ISO Class 5 zoning prominently shown on right one-third.
3. Figure 03 silhouette at biosafety cabinet in the Class 5 zone.
4. All three swimlanes labeled.
5. Closed-loop return arrow present.
6. Title, subtitle, header, footer present.
7. `§` appears in `21 CFR § 211`.
8. The `x 10^7` notation appears in the subtitle.
9. No em dash, no double dash, no triple dash.
10. No emoji.
