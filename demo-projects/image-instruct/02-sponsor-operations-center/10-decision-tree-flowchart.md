# Image Instruction 02-10: Sonnet to Opus Failover Decision Tree Flowchart

[![Demo](https://img.shields.io/badge/Demo-02-brightgreen.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/blob/main/demo-projects/02-sponsor-humanoid-operations-center.md)
[![Image](https://img.shields.io/badge/Image-10%20of%2010-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos/tree/main/demo-projects/image-instruct/02-sponsor-operations-center)
[![Orientation](https://img.shields.io/badge/Orientation-Portrait-orange.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)
[![DPI](https://img.shields.io/badge/DPI-300-blue.svg)](https://github.com/kevinkawchak/Clinical-AI-Demos)

## Output Filename

`demo-projects/02-sponsor-humanoid-operations-center-output/figures/02-10-decision-tree-flowchart.png`

## Page Size and DPI

- Letter portrait, 8.5 x 11.0 inches, 300 dpi, 2550 x 3300 pixels, white facecolor.

## Chart Type

Top-down decision tree flowchart. Root: inbound document arrives at the Sponsor Operations Center. Branches: Safe Harbor verdict, Sonnet 4.6 confidence, token budget, regulatory criticality. Terminal nodes: published to FDA RTCT, IRB, DSMB; or held for manual review; or routed to Opus 4.7 1M cloud failover.

## Title and Subtitle

- Title: `Sponsor Center Sonnet to Opus Failover Decision Tree`.
- Subtitle: `Inbound Document - Safe Harbor - Sonnet Confidence - Opus Failover - Optimus Co-Sign`.

## Header and Footer

- Header right: `Demo 02 / Image 10 of 10 / Portrait`.
- Footer left: `Clinical-AI-Demos v0.2.0 / Demo 02 Sponsor Humanoid Operations Center`.
- Footer right: `DOI: 10.5281/zenodo.18445179 / MIT License`.

## Tree Structure (root at top)

```
              [Inbound Document Arrives]
                        |
              <Safe Harbor PHI Gate>
                  |              |
                Pass            Block (Manual Review)
                  |
            <Token Budget Within 1M>
                  |              |
                Yes              No
                  |              |
        <Sonnet 4.6 Conf >= 0.85?>          [Pre-Chunk + Re-Run]
                  |          |                       |
                Yes         No                      Back to top
                  |          |
        [Sonnet  [Opus 4.7 1M
         Draft]   Failover]
            |          |
        [Optimus     [Optimus
         Co-Sign       Co-Sign
         Archive]      Archive]
            |          |
        <Criticality Tier>
                |
       +--------+--------+
       |        |        |
      Tier 1  Tier 2   Tier 3
       |        |        |
    [Publish  [Publish  [Sponsor SOP
     FDA RTCT  IRB or    Internal Only]
     Portal]   DSMB
              Portal]
```

## Node Types and Colors

- Diamonds (Slate fill, white text): decision points.
- Forest Green rectangles: pass-through publish actions.
- Teal rectangles: Sonnet 4.6 actions.
- Teal darker rectangles: Opus 4.7 1M actions.
- Deep Navy rectangles: Optimus co-sign actions.
- Burgundy rectangles: hold / block actions.
- Gold rectangles: FDA RTCT publish; Burgundy IRB; Forest Green DSMB; Slate Sponsor SOP Internal.

## Annotations

- Annotation pinned to Safe Harbor diamond: `HIPAA 45 CFR § 164.514(b); 18 identifiers stripped pre-failover.`
- Annotation pinned to Sonnet confidence diamond: `Confidence below 0.85 triggers cloud failover. Confidence threshold tunable per trial.`
- Annotation pinned to Optimus Co-Sign: `21 CFR § 11 electronic signature plus 1 of 5 Optimus humanoids physically countersigns to bond paper at the bench.`

## Layout, matplotlib Recipe

Same conventions as 01-10. Diamonds via `matplotlib.patches.Polygon`; rectangles via `matplotlib.patches.FancyBboxPatch`; edges via `matplotlib.patches.FancyArrowPatch`.

## Validation Checklist

1. PNG is 2550 x 3300 pixels.
2. Root node at top, leaf nodes at bottom.
3. 5 decision diamonds, 8+ action rectangles.
4. All edges labeled (`Yes`, `No`, `Pass`, `Block`, `Tier 1`, etc.).
5. Three pinned annotations present.
6. Title, subtitle, header, footer present.
7. `§` appears throughout regulatory references.
8. No em dash, no double dash, no triple dash.
9. No color outside palette.
10. No emoji.
