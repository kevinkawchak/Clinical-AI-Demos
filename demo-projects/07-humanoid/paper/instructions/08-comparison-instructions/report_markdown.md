# Authoring Instructions for `reports/report.md` (and `reports/report.pdf`)

The future session writes this Markdown during Commit 5 of 7.

## Purpose

The canonical comparison report. Markdown source plus a PDF rendering. Read by stakeholders and regulators.

## Required Sections

```
# Demo 07 v0.3.0: 3-Robot Camarade Swarm 24/7 AE Response (Comparison Report)

## Executive Summary

## Network Overview
  - PAT-NET-001, 4 sites, 12 H2 humanoids, 168-hour window
  - Cite the thesis from `00-project-overview/thesis.md`

## Response Time
  - p50 across 4 sites: target under 90 seconds
  - p95 across 4 sites
  - Comparison to v0.1.0, Atlas, Optimus, human paramedic team
  - Figure: `figures/02_response_time_histogram.png`

## Camaraderie
  - 7 invariants pass rate (target above 0.95)
  - Peer hand-off p95 (target under 2 seconds)
  - Role rotation count per AE
  - Figure: `figures/03_camaraderie_heatmap.png`
  - Figure: `figures/04_role_rotation_timeline.png`

## FDA RTCT Compliance
  - 1-hour SLA compliance rate (target above 0.99)
  - Hash chain integrity (target true)
  - Cite HR 9504 and HR 9505

## Patient Safety
  - E-stop reliability (target above 0.999)
  - Force budget compliance (target above 0.999)
  - Envelope violations (target 0)
  - Figure: `figures/05_force_budget_distribution.png`

## Cost
  - 5-year TCO
  - Amortized cost per AE

## Site Comparison
  - Figure: `figures/06_4site_comparison.png`

## Configuration Ranking
  - Weighted score per configuration
  - Statistical significance versus baseline

## Discussion
  - Synergy benefit observed over single-robot baseline
  - Camarade swarm reduces single-robot error potential by a factor of 3 (per thesis)

## Footnotes
  - HR 9504 Physical AI Clinical Error Reduction Act (verbatim source from companion repo)
  - HR 9505 Real-Time Patient-Sponsor Direct Communication Act (verbatim source from companion repo)
  - FDA April 2026 RTCT guidance (verbatim source from companion repo)
  - Cite the author's prior FAERS LLM paper: DOI 10.5281/zenodo.18029100
```

## PDF Rendering

```
pandoc reports/report.md -o reports/report.pdf --pdf-engine=xelatex
```

If pandoc with xelatex is not available, the future session uses `weasyprint reports/report.md` or commits the Markdown only.

## Validation Rules

- All section headings present.
- All figure references resolve to existing PNGs.
- Single dashes only.
- No PHI.

## Notes

- The report is intentionally short (under 8 pages PDF). Detailed tables live in the appendix subdirectory.
- The Camaraderie section is the v0.3.0 differentiator and must be the second main section after Response Time.
