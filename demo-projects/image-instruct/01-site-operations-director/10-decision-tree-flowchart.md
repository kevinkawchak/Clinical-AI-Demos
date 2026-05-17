# Image Instruction 01-10: Atlas + Claude Opus 4.7 Adverse Event Escalation Decision Tree Flowchart

[![Demo](https://img.shields.io/badge/Demo-01-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/01-humanoid-site-operations-director.md)
[![Image](https://img.shields.io/badge/Image-10%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/01-site-operations-director)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/01-humanoid-site-operations-director-output/figures/01-10-decision-tree-flowchart.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

Top-down decision tree flowchart. The root node is the triggering event. Diamond nodes are decision branches. Rectangle nodes are actions. Burgundy edge actions escalate. Forest Green edge actions resolve in-place. Slate edge actions log without further escalation.

## Title and Subtitle

- Title: `Atlas Electric + Claude Opus 4.7 1M Adverse Event Escalation Decision Tree`.
- Subtitle: `Per-Tick Branching at PAT-SITE-001 - From Patient Vitals Anomaly to Resolved or On-Call Physician Activated`.

## Header and Footer

- Header right: `Demo 01 / Image 10 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 01 Site Operations Director`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Tree Structure (root at top)

```
          [Patient Vitals Anomaly Detected]
                       |
        +-------------+-----------------+
        |                               |
 <CTCAE Grade>                      <Grade Unknown>
        |                               |
   +----+------+                  [Atlas Bedside Visit]
   |          |                          |
 1 or 2     3 or 4               <Vitals Within 2 sigma?>
   |          |                     |               |
[Atlas      [Burgundy             Yes              No
Bedside     On-Call                |                |
Visit]      Physician         [Atlas Logs       [Escalate to
                              Audit Only]       Claude Opus
                                                Re-Score]
                                                     |
                                              <New Grade>
                                                     |
                                           +---------+--------+
                                           |                  |
                                        1 or 2            3 or 4
                                           |                  |
                                     [Atlas Bedside    [Burgundy
                                      Visit]            On-Call
                                                        Physician]
```

## Nodes (each labeled)

Diamonds (decision):

1. `Patient Vitals Anomaly Detected (Root Trigger)`.
2. `CTCAE Grade (from Claude Opus inference)`.
3. `Atlas Camera + IMU Within 2 Sigma of Baseline?`.
4. `Claude Opus Re-Score Output`.

Rectangles (action):

1. `Atlas Bedside Visit (Priority 1.0)`.
2. `Atlas Logs Audit Only (no patient touch)`.
3. `Burgundy On-Call Physician Activation (HR 9505 1-hour acknowledgment SLA)`.
4. `Escalate to Claude Opus Re-Score (200 ms reasoning budget)`.

## Color and Edge Mapping

- Decision diamonds: Slate fill `#4A5568`, white text.
- Resolving action rectangles (Atlas bedside, Atlas logs): Forest Green fill `#2F6B3E`, white text.
- Escalating action rectangles (On-Call Physician): Burgundy fill `#8B2E3F`, white text.
- Reroute action rectangles (Claude Opus Re-Score): Teal fill `#2E8B8B`, white text.
- Edge color matches the action color at the receiving end.
- Edge labels (`Yes`, `No`, `1 or 2`, `3 or 4`, `Grade Unknown`) in 9 pt regular Slate above each edge.

## Annotations

- Annotation pinned to the Claude Opus Re-Score node: `Reasoning budget 200 ms median. Reads patient vitals plus Atlas camera frame plus last 5 minutes of bay status.`
- Annotation pinned to the On-Call Physician action: `HR 9505 requires 1-hour acknowledgment. Atlas remains bedside until acknowledged. Atlas captures continuous video clip starting at activation T-30 s.`
- Annotation pinned to the Atlas Bedside Visit action: `Cumulative force cap 15 N. E-stop budget 50 ms. Audit log entry every 1 second while at bedside.`

## Layout Specification

- Tree area y 0.12 to 0.85, x 0.05 to 0.95.
- Root node at y 0.80 centered.
- Levels descend by 0.15 normalized y each.
- Diamonds 0.10 wide x 0.06 tall.
- Rectangles 0.16 wide x 0.06 tall with rounded corners 0.01 radius.
- Edges: 1.2 pt with arrow head size 8.

## matplotlib Recipe

- Use `matplotlib.patches.Polygon` for diamond shapes (4 vertices).
- Use `matplotlib.patches.FancyBboxPatch` for rectangles with `boxstyle='round,pad=0.01,rounding_size=0.01'`.
- Use `matplotlib.patches.FancyArrowPatch` for edges with `arrowstyle='->,head_length=6,head_width=4'`.
- Position nodes at explicit `(x, y)` normalized coordinates per the structure above.

## Data Structure Future Author Provides

JSON `decision_tree.json`:

```json
{
  "nodes": [
    {"id": "root", "kind": "diamond", "label": "...", "x": 0.5, "y": 0.80},
    {"id": "grade", "kind": "diamond", "label": "...", "x": 0.3, "y": 0.65}
  ],
  "edges": [
    {"source": "root", "target": "grade", "label": "CTCAE Grade", "color": "#4A5568"}
  ]
}
```

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. Root node at the top, leaves at the bottom.
3. 4 decision diamonds and 4 action rectangles present.
4. All edges labeled.
5. Three pinned annotations present.
6. Title, subtitle, header, footer present.
7. No em dash, no double dash, no triple dash.
8. No color outside palette.
9. No emoji.
10. Tree fits within margins, no clipping at left or right edges.
