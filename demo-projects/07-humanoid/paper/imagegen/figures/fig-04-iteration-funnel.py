"""Figure 4 replacement: 32 Iteration Sweep and Compare Funnel.

Portrait full-page, 8.5 x 11.0 inches, 300 dpi. Renders the iteration sweep
pipeline: iterations.yaml -> generate_lhs(n=32) -> per-iteration WeekRunner
-> build_index -> build_aggregate -> compute.py 26 key vector -> compare
agent. Replaces the verbatim ASCII figure that previously appeared in
methods.tex.
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

STEPS = [
    (
        "config/iterations.yaml",
        [
            "seed: [1..8]",
            "llm_temperature: [0.0, 0.1, 0.2, 0.3]",
            "ae_arrival_jitter_s: [0, 30, 60, 120]",
            "response_time_variance: [0.0, 0.05, 0.1, 0.2]",
            "camarade_aggressiveness: [0.5, 0.75, 1.0, 1.25]",
            "iteration_count: 32",
        ],
        PALETTE["mauve"],
        "Input axes",
    ),
    (
        "generate_lhs(n=32)",
        [
            "Latin Hypercube sampler",
            "Deterministic seed scheduling",
            "32 sample combinations",
        ],
        PALETTE["teal"],
        "Sampling",
    ),
    (
        "for each iter in 32:\n  run_iteration()",
        [
            "WeekRunner in fast mode",
            "4-site ProcessPool",
            "3600 ticks per site",
        ],
        PALETTE["deep_navy"],
        "Execution",
    ),
    (
        "build_index()",
        [
            "data/iterations/index.jsonl",
            "32 lines, 1 line per iteration",
        ],
        PALETTE["gold"],
        "Index assembly",
    ),
    (
        "build_aggregate()",
        [
            "data/iterations/aggregate.duckdb",
            "15 columns, ready for SQL",
        ],
        PALETTE["gold"],
        "DuckDB aggregate",
    ),
    (
        "compute.py 26 key vector",
        [
            "vs human_team_baseline",
            "weighted score 0.953",
        ],
        PALETTE["forest_green"],
        "Metric compute",
    ),
    (
        "compare_agent.py",
        [
            "Natural language compare narrative",
            "Reads compute output + baselines",
        ],
        PALETTE["burgundy"],
        "Narrative",
    ),
]


def main(out_path: pathlib.Path) -> None:
    fig = plt.figure(figsize=(8.5, 11.0), facecolor="white")
    fig.text(
        0.06,
        0.975,
        "32 Iteration Sweep and Compare Funnel",
        fontsize=13.5,
        ha="left",
        color="black",
        fontweight="bold",
    )
    fig.text(
        0.06,
        0.957,
        "Latin Hypercube sweep across 5 axes; DuckDB aggregate; 26-key vs human team baseline",
        fontsize=9.5,
        ha="left",
        color=PALETTE["slate"],
    )
    fig.text(0.94, 0.978, "Figure 4 / Paper Figure Replacement", fontsize=8.5, ha="right", color=PALETTE["slate"])

    ax = fig.add_axes([0.04, 0.06, 0.92, 0.88])
    ax.set_xlim(0, 8.5)
    ax.set_ylim(0, 11)
    ax.set_axis_off()

    box_w = 6.0
    box_h_default = 1.04
    box_h_first = 1.50
    gap = 0.18
    n = len(STEPS)
    top_y = 10.10
    cx = 4.25

    y_running = top_y
    for i, (title, lines, color, kind) in enumerate(STEPS):
        box_h = box_h_first if i == 0 else box_h_default
        y = y_running
        ax.add_patch(
            FancyBboxPatch(
                (cx - box_w / 2, y - box_h),
                box_w,
                box_h,
                boxstyle="round,pad=0.02,rounding_size=0.10",
                fc=PALETTE["off_white"],
                ec=color,
                lw=2.0,
            )
        )
        ax.add_patch(
            FancyBboxPatch(
                (cx - box_w / 2, y - 0.32),
                box_w,
                0.32,
                boxstyle="round,pad=0.0,rounding_size=0.10",
                fc=color,
                ec=color,
                lw=1.0,
            )
        )
        ax.text(
            cx - box_w / 2 + 0.15,
            y - 0.16,
            title,
            ha="left",
            va="center",
            fontsize=9.5,
            color="white",
            fontweight="bold",
        )
        ax.text(
            cx + box_w / 2 - 0.15,
            y - 0.16,
            kind,
            ha="right",
            va="center",
            fontsize=8.5,
            color="white",
            style="italic",
        )

        for j, line in enumerate(lines):
            ax.text(cx - box_w / 2 + 0.30, y - 0.50 - j * 0.16, "- " + line, fontsize=7.6, color="black", va="top")

        ax.text(
            cx + box_w / 2 + 0.10,
            y - box_h / 2,
            f"Step {i + 1} of {n}",
            ha="left",
            va="center",
            fontsize=7.5,
            color=PALETTE["slate"],
            style="italic",
        )

        if i < n - 1:
            arrow = FancyArrowPatch(
                (cx, y - box_h),
                (cx, y - box_h - gap + 0.04),
                arrowstyle="-|>",
                mutation_scale=22,
                color=PALETTE["slate"],
                lw=2.2,
            )
            ax.add_patch(arrow)
        y_running = y - box_h - gap

    legend_handles = [
        mpatches.Patch(color=PALETTE["mauve"], label="Input axes"),
        mpatches.Patch(color=PALETTE["teal"], label="Sampling"),
        mpatches.Patch(color=PALETTE["deep_navy"], label="Execution"),
        mpatches.Patch(color=PALETTE["gold"], label="Index / Aggregate"),
        mpatches.Patch(color=PALETTE["forest_green"], label="Metric Compute"),
        mpatches.Patch(color=PALETTE["burgundy"], label="Narrative"),
    ]
    leg = fig.legend(
        handles=legend_handles,
        loc="lower center",
        bbox_to_anchor=(0.5, 0.025),
        ncol=6,
        fontsize=7.6,
        framealpha=0.95,
        edgecolor=PALETTE["slate"],
    )
    leg.get_frame().set_facecolor("white")

    fig.text(
        0.06,
        0.005,
        "Clinical-AI-Demos v0.8.0 / Demo 07 Adverse Event Response / Paper Figure 4",
        fontsize=7.3,
        ha="left",
        color=PALETTE["slate"],
    )
    fig.text(
        0.94, 0.005, "DOI: 10.5281/zenodo.18445179 / MIT License", fontsize=7.3, ha="right", color=PALETTE["slate"]
    )

    fig.savefig(out_path, dpi=300, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    out = pathlib.Path(__file__).with_suffix(".png")
    main(out)
    print(f"Saved {out}")
