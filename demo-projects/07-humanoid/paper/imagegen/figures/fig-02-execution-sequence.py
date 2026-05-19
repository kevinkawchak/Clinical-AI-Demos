"""Figure 2 replacement: PAT-NET-001 4-Site Execution Sequence (per tick).

Landscape full-page, 11.0 x 8.5 inches, 300 dpi. Renders the per-tick 1 Hz
execution sequence across all 4 sites with the LLM planner, broadcaster,
dispatcher, sensor refresh, audit hash extension, and the 60-second per-site
summary aggregate.
"""

from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("Agg")

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

PALETTE = {
    "deep_navy": "#1F3A68",
    "teal": "#2E8B8B",
    "burgundy": "#8B2E3F",
    "burgundy_dk": "#5A1E2A",
    "gold": "#C18A2C",
    "forest_green": "#2F6B3E",
    "slate": "#4A5568",
    "mauve": "#8B6B8B",
    "light_gray": "#E2E8F0",
    "off_white": "#F7FAFC",
}

SITES = [
    ("SF-01", "ABC", "6274ffb43..."),
    ("SD-01", "DEF", "93e5b2a36..."),
    ("BO-01", "GHI", "f26259454..."),
    ("AT-01", "JKL", "9ce5740a1..."),
]

ROWS = [
    ("T+0 dispatch init", "dispatch init\n3 robots roster"),
    ("T+0.0 tick 0", "LLMPlanner 1 Hz\nBroadcaster\nDispatcher\n3 acks 50 ms"),
    ("T+1.0 tick 1", "sensor refresh\nrole rebalance"),
    ("T+59 tick 59", "audit head extends"),
    ("T+60 summary", "60 decisions\npersisted"),
]


def main(out_path: pathlib.Path) -> None:
    fig = plt.figure(figsize=(11.0, 8.5), facecolor="white")
    fig.text(
        0.05,
        0.965,
        "PAT-NET-001 4-Site Execution Sequence (Per 1 Hz Tick)",
        fontsize=15.0,
        ha="left",
        color="black",
        fontweight="bold",
    )
    fig.text(
        0.05,
        0.940,
        "Same per-site dispatch + LLM decision + audit chain extension, repeated across SF-01, SD-01, BO-01, AT-01",
        fontsize=10.0,
        ha="left",
        color=PALETTE["slate"],
    )
    fig.text(0.95, 0.915, "Figure 2 / Paper Figure Replacement", fontsize=8.5, ha="right", color=PALETTE["slate"])

    ax = fig.add_axes([0.04, 0.15, 0.92, 0.74])
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 8.5)
    ax.set_axis_off()

    header_y = 7.95
    col_w = 2.30
    label_w = 1.90
    col_xs = [label_w + 0.30 + i * (col_w + 0.05) for i in range(4)]
    for (site, robots, audit_head), x in zip(SITES, col_xs):
        ax.add_patch(
            FancyBboxPatch(
                (x, header_y),
                col_w,
                0.55,
                boxstyle="round,pad=0.02,rounding_size=0.06",
                fc=PALETTE["deep_navy"],
                ec="black",
                lw=0.9,
            )
        )
        ax.text(
            x + col_w / 2,
            header_y + 0.28,
            site,
            ha="center",
            va="center",
            fontsize=11.0,
            color="white",
            fontweight="bold",
        )

    row_h = 0.92
    row_start = header_y - row_h - 0.15
    for r, (label, _) in enumerate(ROWS):
        y = row_start - r * (row_h + 0.12)
        ax.add_patch(
            FancyBboxPatch(
                (0.10, y),
                label_w + 0.10,
                row_h,
                boxstyle="round,pad=0.02,rounding_size=0.06",
                fc=PALETTE["off_white"],
                ec=PALETTE["slate"],
                lw=1.0,
            )
        )
        ax.text(
            label_w / 2 + 0.15,
            y + row_h / 2,
            label,
            ha="center",
            va="center",
            fontsize=9.0,
            color=PALETTE["slate"],
            fontweight="bold",
        )

    cells = [
        ["dispatch init\n3 robots: " + s[1] for s in SITES],
        ["LLMPlanner 1 Hz\nBroadcaster\nDispatcher\n3 acks 50 ms" for _ in SITES],
        ["sensor refresh\nrole rebalance" for _ in SITES],
        ["audit head=\n" + s[2] for s in SITES],
        ["60 decisions\npersisted" for _ in SITES],
    ]
    row_colors = [PALETTE["deep_navy"], PALETTE["teal"], PALETTE["mauve"], PALETTE["gold"], PALETTE["forest_green"]]

    for r, (row, color) in enumerate(zip(cells, row_colors)):
        y = row_start - r * (row_h + 0.12)
        for c, (text, x) in enumerate(zip(row, col_xs)):
            ax.add_patch(
                FancyBboxPatch(
                    (x, y),
                    col_w,
                    row_h,
                    boxstyle="round,pad=0.02,rounding_size=0.05",
                    fc=color,
                    ec="black",
                    lw=0.7,
                    alpha=0.90,
                )
            )
            ax.text(
                x + col_w / 2,
                y + row_h / 2,
                text,
                ha="center",
                va="center",
                fontsize=8.0,
                color="white",
                fontweight="bold",
            )
            if r < len(ROWS) - 1:
                arrow = FancyArrowPatch(
                    (x + col_w / 2, y),
                    (x + col_w / 2, y - 0.18),
                    arrowstyle="-|>",
                    mutation_scale=10,
                    color=PALETTE["slate"],
                    lw=0.9,
                )
                ax.add_patch(arrow)

    agg_y = row_start - len(ROWS) * (row_h + 0.12) - 0.05
    agg_box = FancyBboxPatch(
        (label_w + 0.30, agg_y - 0.55),
        col_w * 4 + 0.15,
        1.25,
        boxstyle="round,pad=0.02,rounding_size=0.10",
        fc=PALETTE["slate"],
        ec="black",
        lw=1.2,
    )
    ax.add_patch(agg_box)
    ax.text(
        label_w + 0.30 + (col_w * 4 + 0.15) / 2,
        agg_y + 0.52,
        "Aggregate",
        ha="center",
        va="center",
        fontsize=11.0,
        color="white",
        fontweight="bold",
    )
    agg_lines = [
        "week_runner: 3600 ticks per site",
        "iterate.py: 32 iterations",
        "runner (Rust release): 32 sweeps",
        "average p50 response time 67.5 s",
        "camaraderie pass rate 0.985",
    ]
    n_per_row = 3
    for i, line in enumerate(agg_lines):
        col = i % n_per_row
        row = i // n_per_row
        cx = label_w + 0.55 + col * (col_w + 0.05)
        cy = agg_y + 0.20 - row * 0.32
        ax.text(cx, cy, "- " + line, ha="left", va="center", fontsize=8.0, color="white")

    ax.text(
        label_w + 0.30,
        agg_y - 0.62,
        "Each per-site column carries one Claude Opus 4.7 1M decision at the 1 Hz tick boundary.",
        fontsize=8.0,
        color=PALETTE["slate"],
        style="italic",
    )

    legend_handles = [
        mpatches.Patch(color=PALETTE["deep_navy"], label="T+0 dispatch init"),
        mpatches.Patch(color=PALETTE["teal"], label="Tick 0 LLM decision"),
        mpatches.Patch(color=PALETTE["mauve"], label="Tick 1 sensor refresh"),
        mpatches.Patch(color=PALETTE["gold"], label="Tick 59 audit hash extend"),
        mpatches.Patch(color=PALETTE["forest_green"], label="T+60 per-site summary"),
        mpatches.Patch(color=PALETTE["slate"], label="Cross-site aggregate"),
    ]
    leg = fig.legend(
        handles=legend_handles,
        loc="lower center",
        bbox_to_anchor=(0.5, 0.040),
        ncol=6,
        fontsize=7.8,
        framealpha=0.95,
        edgecolor=PALETTE["slate"],
    )
    leg.get_frame().set_facecolor("white")

    fig.text(
        0.05,
        0.012,
        "Clinical-AI-Demos v0.8.0 / Demo 07 Adverse Event Response / Paper Figure 2",
        fontsize=7.5,
        ha="left",
        color=PALETTE["slate"],
    )
    fig.text(
        0.95, 0.012, "DOI: 10.5281/zenodo.18445179 / MIT License", fontsize=7.5, ha="right", color=PALETTE["slate"]
    )

    fig.savefig(out_path, dpi=300, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    out = pathlib.Path(__file__).with_suffix(".png")
    main(out)
    print(f"Saved {out}")
