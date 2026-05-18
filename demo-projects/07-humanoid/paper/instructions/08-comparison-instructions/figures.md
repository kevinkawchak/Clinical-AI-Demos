# Authoring Instructions for `figures/*.png`

The future session writes these 6 PNG files during Commit 5 of 7. All at 300 dpi, white facecolor, matplotlib only.

## Files and Specs

### `figures/01_swarm_architecture.png`

A landscape Letter (11.0 x 8.5 in, 3300 x 2550 px) figure showing the 3-robot camarade swarm at one site. Shows:

- The patient bed at center
- 3 H2 humanoids around the bed labeled Lead, Assist, Reserve
- The on-prem Claude Opus 4.7 1M broadcaster
- The site broadcast bus
- The 60 GHz UWB peer mesh and IR beacon channels
- Arrows for sensor return paths

Matplotlib recipe: `FancyBboxPatch` for the patient bed; `Polygon` for each robot; `FancyArrowPatch` for the channels.

### `figures/02_response_time_histogram.png`

A portrait Letter (8.5 x 11.0 in, 2550 x 3300 px) histogram comparing AE response time distributions across:

- v0.3.0 camarade swarm
- v0.1.0 rotating fleet
- 3-human paramedic team baseline
- Atlas Electric configuration
- Tesla Optimus Gen 3 configuration

Matplotlib recipe: `ax.hist` with 5 series, stepfilled, alpha 0.5, x-axis in seconds, vertical line at 90 s SLA.

### `figures/03_camaraderie_heatmap.png`

A landscape Letter figure showing the 7 camaraderie invariants pass rate across the 168 hours (24 hour cells x 7 days) for one representative iteration.

Matplotlib recipe: `imshow` with a custom `ListedColormap` from Forest Green (1.0 pass) to Burgundy (0.0 pass).

### `figures/04_role_rotation_timeline.png`

A portrait Letter figure showing a representative 90-second AE response with role rotations between Lead, Assist, Reserve.

Matplotlib recipe: `broken_barh` with 3 lanes, color-coded by robot ID.

### `figures/05_force_budget_distribution.png`

A portrait Letter figure showing the cumulative cross-robot force distribution during 3-robot patient transfer events.

Matplotlib recipe: `ax.violinplot` plus a horizontal line at the 22 N ceiling.

### `figures/06_4site_comparison.png`

A landscape Letter figure with a 4-panel grid comparing the 4 sites on:

- Response time p50
- Camaraderie invariants pass rate
- Escalation count
- Battery state of charge p10

Matplotlib recipe: 2x2 subplots, each panel a bar plot.

## Common Conventions

- DejaVu Sans typography.
- Color palette: Deep Navy #1F3A68, Teal #2E8B8B, Burgundy #8B2E3F, Gold #C18A2C, Forest Green #2F6B3E, Slate #4A5568, Mauve #8B6B8B, Light Gray #E2E8F0, Off-White #F7FAFC, Pure White #FFFFFF.
- Header band with title (16 pt) plus subtitle (10 pt).
- Footer band with `Clinical-AI-Demos v0.3.0 / Demo 07` (left) and `DOI: 10.5281/zenodo.18445179 / MIT License` (right) at 8 pt.
- `fig.savefig(..., dpi=300, facecolor="white")`.
- `matplotlib.use("Agg")` so the script runs headless.

## Validation Rules

- 6 PNG files.
- All at 300 dpi.
- All white facecolor.
- No emoji, no dark mode, no inline color directives.

## Notes

- These figures inherit conventions from `demo-projects/image-instruct/07-adverse-event-response/` of the repository.
- The Camaraderie heatmap (figure 03) is the v0.3.0 differentiator.
