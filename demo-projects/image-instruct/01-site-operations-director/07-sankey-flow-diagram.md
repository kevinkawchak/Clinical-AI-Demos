# Image Instruction 01-07: Atlas Site Director Patient and Command Sankey Flow

[![Demo](https://img.shields.io/badge/Demo-01-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/01-humanoid-site-operations-director.md)
[![Image](https://img.shields.io/badge/Image-07%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/01-site-operations-director)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/01-humanoid-site-operations-director-output/figures/01-07-sankey-flow-diagram.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

Sankey diagram with 4 vertical levels (left to right) and proportional flow widths. The leftmost level is the source (patient cohort and inbound IMP); the rightmost level is the terminal status (treatment delivered, recovery, transfer, audit pass). Two intermediate levels are Atlas humanoid action categories and Claude Opus 4.7 decision categories.

## Title and Subtitle

- Title: `Atlas Electric Site Director 8-Hour Patient and Command Flow Sankey`.
- Subtitle: `Source to Terminal Status with Claude Opus 4.7 LLM Decision Routing - 10 Patients, 28,800 Ticks`.

## Header and Footer

- Header right: `Demo 01 / Image 07 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 01 Site Operations Director`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Levels (4 vertical columns)

1. **Level 1 Sources** (leftmost):
   - `4 NSCLC Patients`
   - `3 Breast Stage IIIA Patients`
   - `3 Colorectal Stage IIIB Patients`
   - `12 IMP Kits (Pharmacy Inbound)`
   - `8 Imaging Suite Time Slots`
2. **Level 2 Atlas Humanoid Action Categories**:
   - `Bay Allocation Walks`
   - `Pharmacy Pick-Up Walks`
   - `Recovery Reposition Walks (Braden)`
   - `Imaging Suite Handoffs`
   - `AE Bedside Response`
3. **Level 3 Claude Opus 4.7 Decision Categories**:
   - `Priority Reorder`
   - `Compliance Gate Pass`
   - `Compliance Gate Hold`
   - `AE Escalation Packet`
   - `Audit Append Only`
4. **Level 4 Terminal Status** (rightmost):
   - `Treatment Delivered`
   - `In Recovery`
   - `Cross-Bay Transfer`
   - `On-Call Physician Activated`
   - `Audit Log Pass`

## Flow Rules

- Every Level 1 entry connects to one or more Level 2 entries with widths proportional to the count of Atlas walks attributable to that source.
- Every Level 2 entry connects to one or more Level 3 entries with widths proportional to the count of Claude Opus decisions emitted for that action.
- Every Level 3 entry connects to one or more Level 4 entries with widths proportional to the count of terminal outcomes.
- Flow color matches the source-level color of the connection (Deep Navy for patient-derived flows, Mauve for pharmacy flows, Gold for imaging flows).

## Color Mapping

- Level 1 patient sources: Deep Navy variants (lighter by indication).
- Level 1 pharmacy: Mauve.
- Level 1 imaging: Gold.
- Level 2 Atlas actions: Deep Navy.
- Level 3 Claude Opus decisions: Teal.
- Level 4 terminal status: Forest Green for pass states, Burgundy for escalation, Slate for audit-only.
- Flow alpha at 0.50 to preserve readability.

## Layout Specification

- Chart area y 0.12 to 0.88, x 0.06 to 0.94.
- Node rectangles 0.02 wide, height proportional to total inbound or outbound flow.
- Gap between vertical nodes within a level 0.01 normalized.
- Node labels to the left of the leftmost column and to the right of the rightmost column. Intermediate column labels above each node.

## Annotations

- Annotate the top of each level column with its level title (`Patient and IMP Source`, `Atlas Humanoid Action`, `Claude Opus 4.7 Decision`, `Terminal Status`) in 11 pt semi-bold Deep Navy.
- Pinned callout near the right edge at y 0.40: `Audit Log Pass terminates 100 percent of compliance-gated flows. AE Escalation terminates within 90 seconds for CTCAE grade 3 or higher.`

## matplotlib Recipe

- Use manual quadratic Bezier polygons rather than `matplotlib.sankey.Sankey` (which is constrained for multi-level flows). For each flow, define a 4-point control polygon with two straight segments at the source and target plus two control points along the horizontal midline.
- Use `matplotlib.patches.PathPatch` with the Bezier path. `matplotlib.path.Path` with `Path.MOVETO`, `Path.CURVE4`, `Path.CURVE4`, `Path.CURVE4`, `Path.LINETO`, `Path.CURVE4`, `Path.CURVE4`, `Path.CURVE4`, `Path.CLOSEPOLY`.
- Use `matplotlib.patches.Rectangle` for node bars.
- Use `ax.text` for labels.

## Data Structure Future Author Provides

JSONL `sankey_flows.jsonl`:

```json
{"source": "4 NSCLC Patients", "target": "Bay Allocation Walks", "value": 480}
{"source": "Bay Allocation Walks", "target": "Priority Reorder", "value": 360}
```

The future author replaces example values with actual counts from `shift_humanoid_commands.parquet` aggregation.

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. 4 vertical levels with all listed nodes present.
3. Flow widths proportional to source values.
4. Source-color flow alpha 0.50.
5. Level titles at the top of each column.
6. Pinned callout present.
7. Title, subtitle, header, footer present.
8. No em dash, no double dash, no triple dash.
9. No color outside palette.
10. No emoji.
