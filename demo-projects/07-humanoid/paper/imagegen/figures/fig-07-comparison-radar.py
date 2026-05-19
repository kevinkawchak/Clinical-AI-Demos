"""Figure 7 replacement: Weighted Comparison Radar (results section).

Landscape full-page, 11.0 x 8.5 inches, 300 dpi. Renders the weighted
7-dimension radar with the v0.4.0 H2 EDU camarade swarm reference, Atlas,
Optimus, and the 3 human paramedic team baseline. Weights sum to 1.00.
Replaces the verbatim ASCII figure that previously appeared in results.tex.
"""

from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

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

AXES = [
    ("Response Time", 0.25),
    ("Patient Safety", 0.20),
    ("FDA RTCT Compliance", 0.15),
    ("Camaraderie", 0.10),
    ("Cost", 0.10),
    ("Safety", 0.10),
    ("Patient Experience", 0.10),
]

SERIES = [
    ("v0.4.0 H2 EDU Camarade Swarm", [0.985, 0.97, 0.999, 0.985, 0.94, 0.97, 0.92], 0.953, PALETTE["deep_navy"], "-"),
    ("Atlas Electric", [0.88, 0.92, 0.93, 0.78, 0.71, 0.86, 0.84], 0.847, PALETTE["teal"], "-"),
    ("Tesla Optimus Gen 3", [0.83, 0.88, 0.91, 0.76, 0.80, 0.78, 0.86], 0.821, PALETTE["gold"], "-"),
    ("3 Human Paramedic Team", [0.55, 0.78, 0.74, 0.42, 0.60, 0.72, 0.95], 0.682, PALETTE["slate"], "--"),
]


def main(out_path: pathlib.Path) -> None:
    fig = plt.figure(figsize=(11.0, 8.5), facecolor="white")
    fig.text(
        0.05,
        0.965,
        "Weighted Comparison Radar: 7 Dimensions, Sum of Weights = 1.00",
        fontsize=15.0,
        ha="left",
        color="black",
        fontweight="bold",
    )
    fig.text(
        0.05,
        0.940,
        "v0.4.0 H2 EDU camarade swarm vs. Atlas, Optimus Gen 3, and 3-human paramedic team baseline",
        fontsize=10.0,
        ha="left",
        color=PALETTE["slate"],
    )
    fig.text(0.95, 0.915, "Figure 7 / Paper Figure Replacement", fontsize=8.5, ha="right", color=PALETTE["slate"])

    n = len(AXES)
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
    angles += angles[:1]

    ax = fig.add_axes([0.05, 0.14, 0.50, 0.72], projection="polar")
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_xticks(angles[:-1])
    labels = [f"{name}\n(w = {w:.2f})" for name, w in AXES]
    ax.set_xticklabels(labels, fontsize=8.5, color="black")
    ax.tick_params(axis="x", pad=12)
    ax.set_ylim(0, 1.0)
    ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
    ax.set_yticklabels(["0.2", "0.4", "0.6", "0.8", "1.0"], fontsize=8.0, color=PALETTE["slate"])
    ax.set_rlabel_position(360 / n / 2)
    ax.grid(color=PALETTE["light_gray"], lw=0.8)
    ax.spines["polar"].set_color(PALETTE["slate"])

    for label, values, score, color, style in SERIES:
        v = values + values[:1]
        ax.plot(angles, v, color=color, lw=2.2, ls=style, alpha=0.95, label=f"{label} (score {score:.3f})")
        ax.fill(angles, v, color=color, alpha=0.10)
        for a, val in zip(angles[:-1], values):
            ax.plot(a, val, "o", color=color, markersize=5.0, markeredgecolor="white", markeredgewidth=0.8)

    table_ax = fig.add_axes([0.62, 0.46, 0.35, 0.42])
    table_ax.set_axis_off()
    table_ax.set_xlim(0, 1)
    table_ax.set_ylim(0, 1)
    table_ax.add_patch(plt.Rectangle((0, 0), 1, 1, fc=PALETTE["off_white"], ec=PALETTE["slate"], lw=1.0))
    table_ax.text(
        0.5,
        0.94,
        "Weighted Score Ranking",
        ha="center",
        va="center",
        fontsize=11.0,
        color=PALETTE["slate"],
        fontweight="bold",
    )
    table_ax.text(0.05, 0.85, "Configuration", fontsize=8.5, color="black", fontweight="bold")
    table_ax.text(0.95, 0.85, "Score (0-1)", fontsize=8.5, color="black", fontweight="bold", ha="right")
    table_ax.plot([0.04, 0.96], [0.83, 0.83], color=PALETTE["slate"], lw=0.7)
    ranked = sorted(SERIES, key=lambda s: -s[2])
    for i, (label, _, score, color, _) in enumerate(ranked):
        y = 0.75 - i * 0.13
        table_ax.add_patch(plt.Circle((0.07, y), 0.022, fc=color, ec="black", lw=0.4))
        table_ax.text(0.12, y, label, fontsize=8.5, color="black", va="center")
        table_ax.text(0.95, y, f"{score:.3f}", ha="right", fontsize=9.5, color=color, fontweight="bold", va="center")

    table_ax.text(
        0.5,
        0.10,
        "Source: paper/execution/diagrams/04_comparison_radar.txt",
        ha="center",
        fontsize=7.5,
        color=PALETTE["slate"],
        style="italic",
    )

    weight_ax = fig.add_axes([0.62, 0.14, 0.35, 0.28])
    weight_ax.set_axis_off()
    weight_ax.set_xlim(0, 1)
    weight_ax.set_ylim(0, 1)
    weight_ax.add_patch(plt.Rectangle((0, 0), 1, 1, fc=PALETTE["off_white"], ec=PALETTE["slate"], lw=1.0))
    weight_ax.text(
        0.5,
        0.92,
        "Dimension Weights (sum 1.00)",
        ha="center",
        va="center",
        fontsize=10.5,
        color=PALETTE["slate"],
        fontweight="bold",
    )
    for i, (name, w) in enumerate(AXES):
        y = 0.80 - i * 0.10
        bar_w = w * 0.55
        weight_ax.add_patch(plt.Rectangle((0.45, y - 0.025), bar_w, 0.05, fc=PALETTE["deep_navy"], ec="black", lw=0.3))
        weight_ax.text(0.42, y, name, fontsize=7.8, color="black", ha="right", va="center")
        weight_ax.text(0.45 + bar_w + 0.02, y, f"{w:.2f}", fontsize=7.8, color=PALETTE["slate"], va="center")

    leg = ax.legend(
        loc="upper center",
        bbox_to_anchor=(0.5, -0.04),
        ncol=2,
        fontsize=7.8,
        framealpha=0.95,
        edgecolor=PALETTE["slate"],
    )
    leg.get_frame().set_facecolor("white")

    fig.text(
        0.05,
        0.020,
        "Clinical-AI-Demos v0.8.0 / Demo 07 Adverse Event Response / Paper Figure 7",
        fontsize=7.5,
        ha="left",
        color=PALETTE["slate"],
    )
    fig.text(
        0.95, 0.020, "DOI: 10.5281/zenodo.18445179 / MIT License", fontsize=7.5, ha="right", color=PALETTE["slate"]
    )

    fig.savefig(out_path, dpi=300, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    out = pathlib.Path(__file__).with_suffix(".png")
    main(out)
    print(f"Saved {out}")
