# Image Instruction 05-10: Pathology MCP Tool Routing Decision Tree

[![Demo](https://img.shields.io/badge/Demo-05-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/05-humanoid-biospecimen-pathology-lab.md)
[![Image](https://img.shields.io/badge/Image-10%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/05-biospecimen-pathology-lab)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/05-humanoid-biospecimen-pathology-lab-output/figures/05-10-decision-tree-flowchart.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

Top-down decision tree showing MCP tool selection and PHI routing decisions.

## Title and Subtitle

- Title: `Phoenix Gen 8 MCP Tool Routing and PHI Decision Tree`.
- Subtitle: `Tool Call - PHI Detection - Cloud or On-Prem - Phoenix Action - Audit`.

## Header and Footer

- Header right: `Demo 05 / Image 10 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 05 Biospecimen Pathology Lab`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Tree Structure

```
                  [MCP Tool Call Received]
                            |
                  <PHI Tag Present?>
                      |              |
                    Yes             No
                      |              |
            [Route to Qwen3 72B   <General Reasoning Task?>
             On-Prem (PHI)]            |              |
                      |               Yes             No
                      |                |              |
                <Tool Type>     [Route to Gemini  [Local Phoenix
                      |          3 Pro Cloud]     Direct Action]
            +---------+---------+      |
            |                   |      |
        Stain Task        Other   <Confidence >= 0.85?>
            |                   |       |        |
        [Phoenix Stainer   [Phoenix    Yes      No
         Arm Action]        General           |
                            Action]   [Phoenix [Escalate to
                                       Action] Pathologist]
```

## Node Types and Colors

- Diamonds Slate.
- Teal lighter: Gemini 3 Pro cloud.
- Teal darker: Qwen3 72B on-prem.
- Deep Navy: Phoenix Gen 8 action.
- Mauve: stain-specific routing.
- Burgundy: escalate to pathologist.

## Annotations

- Pinned to PHI diamond: `MCP server tags each prompt with PHI markers; presence triggers Qwen3 72B routing.`
- Pinned to Phoenix Stainer Arm: `EM-shielded chassis; 10 ms benchtop E-stop; 10 N cumulative force.`
- Pinned to Escalate to Pathologist: `Confidence below 0.85 holds Phoenix at current state; pathologist receives slide image plus tool-call rationale.`

## Layout, matplotlib Recipe, Validation

Same conventions as prior decision tree instructions.

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. 4 decision diamonds.
3. 6+ action rectangles.
4. Edges labeled.
5. Pinned annotations.
6. Title, subtitle, header, footer present.
7. No em dash, no double dash, no triple dash.
8. No color outside palette.
9. No emoji.
10. Tree fits within margins.
