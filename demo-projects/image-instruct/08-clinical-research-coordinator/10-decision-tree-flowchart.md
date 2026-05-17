# Image Instruction 08-10: Neo Beta CRC Ensemble Routing Decision Tree

[![Demo](https://img.shields.io/badge/Demo-08-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/08-humanoid-clinical-research-coordinator.md)
[![Image](https://img.shields.io/badge/Image-10%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/08-clinical-research-coordinator)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/08-humanoid-clinical-research-coordinator-output/figures/08-10-decision-tree-flowchart.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

Top-down decision tree showing per-tick ensemble routing.

## Title and Subtitle

- Title: `Neo Beta CRC Ensemble Routing Decision Tree`.
- Subtitle: `Per-Tick - Language - Task Type - Model Selection - Action`.

## Header and Footer

- Header right: `Demo 08 / Image 10 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 08 Clinical Research Coordinator`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Tree Structure

```
              [Patient Utterance Received]
                        |
              <Language Detected>
              |        |       |       |       |
              EN      ES      ZH      TL      VI
              |        |       |       |       |
            <Task Type?> (same for all language branches)
              |
        +-----+-----+-----+
        |     |     |     |
     Medical Lang  Stipend HR Rights
       Q&A  Recital
        |     |     |     |
   [Claude  [Gemini [GPT-5.5 [Safety
    Opus    3 Pro  Thinking  Arbiter +
    4.7]   Multi-  Stipend   HR 9501-9507
            Lingual Payment   Enforcer]
            Recital] Logic]
                              |
                <Election Conflicts with Trial Protocol?>
                  |              |
                Yes             No
                  |              |
        [Neo Beta Refuse   [Neo Beta Capture
         + Log to IRB]      + Audit Append]
```

## Node Types and Colors

- Diamonds Slate.
- Teal lighter, mid, darker: 3 LLM model picks.
- Burgundy: Safety Arbiter and refusal.
- Forest Green: capture and audit append.

## Annotations

- Pinned to Language Detected diamond: `Gemini 3 Pro confidence > 0.99 across EN, ES, ZH, TL, VI at v0.2.0. Mismatch triggers human translator backup.`
- Pinned to Stipend GPT-5.5: `GPT-5.5 produces 1099-MISC-ready stipend payment authorization JSON. IRS reporting flag set per-patient.`
- Pinned to Safety Arbiter: `HR 9501 to 9507 hard-gates. Refusals are not silent; logged with reason code and trial protocol clause.`

## Layout, matplotlib Recipe, Validation

Same conventions as prior decision tree instructions.

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. 3 decision diamonds, 5+ action rectangles.
3. Language branch shown.
4. Edges labeled.
5. Pinned annotations.
6. Title, subtitle, header, footer present.
7. No em dash, no double dash, no triple dash.
8. No color outside palette.
9. No emoji.
10. Tree fits within margins.
