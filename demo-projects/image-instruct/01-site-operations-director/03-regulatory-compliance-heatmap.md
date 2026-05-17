# Image Instruction 01-03: Atlas + Claude Opus Regulatory and Risk Compliance Heatmap Matrix

[![Demo](https://img.shields.io/badge/Demo-01-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/01-humanoid-site-operations-director.md)
[![Image](https://img.shields.io/badge/Image-03%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/01-site-operations-director)
[![Orientation](https://img.shields.io/badge/Orientation-Landscape-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/01-humanoid-site-operations-director-output/figures/01-03-regulatory-compliance-heatmap.png`

## Page Size and DPI

- Letter landscape, 11.0 x 8.5 inches, 300 dpi, 3300 x 2550 pixels, white facecolor.

## Chart Type

Annotated heatmap matrix. Rows are operational phases of the Atlas Electric 8-hour day shift. Columns are regulatory and risk frameworks the Claude Opus 4.7 1M planner consults at each LLM tick. Cells are colored by compliance impact level on a 0 to 4 scale; cell text shows the impact level and a short rationale code.

## Title and Subtitle

- Title: `Atlas Electric Site Operations: Regulatory and Risk Compliance Matrix`.
- Subtitle: `12 Operational Phases x 14 Regulatory Frameworks - PAT-SITE-001 San Francisco`.

## Header and Footer

- Header right: `Demo 01 / Image 03 of 10 / Landscape`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 01 Site Operations Director`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Layout Specification

- Heatmap occupies the left 0.72 of the page width and y from 0.10 to 0.85.
- Right 0.25 of the page width holds the legend, colorbar, and per-framework reference table.
- 0.3 inch margin on all sides.

## Rows (12 Operational Phases)

1. `08:00 Shift Start Audit Snapshot`
2. `08:30 First Bay Allocation Sweep`
3. `09:00 IMP Pharmacy Pick-Up Round`
4. `10:00 Imaging Suite Coordination`
5. `11:00 Recovery Room Reposition (Braden)`
6. `12:00 Cross-Bay AE Triage Window`
7. `13:00 Surgical Bay Reassignment`
8. `14:00 Shift-Midpoint Compliance Snapshot`
9. `14:30 Pharmacy Clean Room Re-Entry`
10. `15:00 Recovery Room Reposition (Braden)`
11. `15:30 Pre-Shift Handoff Preparation`
12. `16:00 Day Shift End Audit Snapshot`

## Columns (14 Regulatory and Risk Frameworks)

1. `21 CFR § 50` (Informed Consent)
2. `21 CFR § 312` (IND Application)
3. `21 CFR § 11` (Electronic Records)
4. `ICH E6(R3)` (GCP)
5. `IEC 80601-2-77` (Medical Robot Safety)
6. `IEC 62304` (Software Lifecycle)
7. `ISO 10218` (Industrial Robot Safety)
8. `HIPAA 45 CFR § 164.514(b)` (Safe Harbor)
9. `HR 9504` (Physical AI Clinical Error Reduction)
10. `HR 9505` (Real-Time Patient-Sponsor Communication)
11. `CTCAE v5.0` (Adverse Event Grading)
12. `Braden Scale` (Pressure Injury Prevention)
13. `FDA RTCT April 2026`
14. `OSHA Bloodborne Pathogens 29 CFR § 1910.1030`

## Cell Values (12 x 14)

The future author maps each (phase, framework) cell to an integer 0 to 4:

- 0 = Not applicable (light gray `#E2E8F0`).
- 1 = Informational reference (Light Teal `#A8D5D5`).
- 2 = Standard compliance check (Forest Green `#2F6B3E` at 0.5 alpha).
- 3 = Active enforcement (Gold `#C18A2C`).
- 4 = Hard gate (Burgundy `#8B2E3F`).

Cell text shows the integer in the center plus a one-letter code in the bottom-right corner:

- `L` for log only.
- `H` for hold (Atlas pauses pending human review).
- `E` for escalation (Claude Opus issues a CTCAE escalation packet).
- `R` for refusal (Atlas refuses the action and emits a refusal record).

## Colormap

Use a manually constructed `matplotlib.colors.ListedColormap` from the 5 colors above (one per integer level). Add a discrete colorbar with the labels: `0 N/A`, `1 Info`, `2 Std`, `3 Active`, `4 Gate`.

## Annotations

- Outline the column for `IEC 80601-2-77` with a 1.5 pt Burgundy frame as the primary safety standard for the humanoid loop.
- Outline the column for `21 CFR § 312` with a 1.5 pt Deep Navy frame as the primary IND framework.
- Add a callout box in the right margin at y 0.60 to 0.75: `Atlas + Claude Opus 4.7 hard-gates 100 percent of level 4 cells before any humanoid motion command leaves the dispatcher.`

## Right Margin Reference Table (14 rows)

Two columns: `Short Name` and `Full Reference`. 9 pt regular Slate, Light Gray header.

## matplotlib Recipe

- Use `ax.imshow(matrix, cmap=custom_cmap, vmin=-0.5, vmax=4.5)` with aspect `auto`.
- Annotate each cell with `ax.text(x, y, str(value), ha='center', va='center', fontsize=9, color='white' if level >= 3 else '#1F3A68')`.
- Set tick labels with `ax.set_xticks(range(14))` and `ax.set_xticklabels(...)` rotated 45 degrees.
- For the right margin reference table use `ax.table` on a second `axes` placed at `[0.75, 0.10, 0.22, 0.75]`.

## Validation Checklist

1. PNG is 3300 x 2550 pixels.
2. Heatmap shows 12 rows x 14 columns with every cell colored.
3. Discrete 5-step colorbar present with correct labels.
4. Outlined columns for `IEC 80601-2-77` and `21 CFR § 312` visible.
5. Callout box in right margin present.
6. Reference table on the right with all 14 frameworks listed.
7. Title, subtitle, header, footer present.
8. `§` appears, not `SS` or `Section`.
9. No em dash, no double dash, no triple dash.
10. No emoji.
