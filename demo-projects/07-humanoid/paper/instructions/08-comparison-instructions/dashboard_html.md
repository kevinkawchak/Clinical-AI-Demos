# Authoring Instructions for `reports/dashboard.html`

The future session writes this HTML during Commit 5 of 7.

## Purpose

A single-page HTML dashboard summarizing the 32-iteration run. Tabs for Response Time, Camaraderie, FDA RTCT, Patient Safety, Cost, Site Comparison, Configuration Ranking.

## Conventions

- Static HTML; no external CDN dependencies.
- Inline CSS for styling. Single dashes only. Black text on white background.
- Embedded SVG sparklines from `pandas.plotting`; PNGs from `figures/` for the heavy charts.
- Use plain `<a href="#tab-name">` anchors for tab navigation; no JavaScript framework.
- Total file size under 2 MB after PNG inlining.

## Required Tabs

1. Response Time
2. Camaraderie
3. FDA RTCT Compliance
4. Patient Safety
5. Cost
6. Site Comparison
7. Configuration Ranking

## Validation Rules

- HTML validates against W3C HTML5.
- All anchor IDs resolve.
- File loads in Firefox, Chrome, Safari without errors.

## Notes

- The dashboard is the interactive companion to the static Markdown report.
- A `python -m http.server` from `reports/` is sufficient to preview locally.
