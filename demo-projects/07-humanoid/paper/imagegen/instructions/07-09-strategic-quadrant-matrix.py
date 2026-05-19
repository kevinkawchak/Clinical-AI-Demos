"""Image 07-09: AE Response Strategic Quadrant Matrix.

Letter portrait, 8.5 x 11.0 inches, 300 dpi. 2x2 quadrant. X axis is the
Network Coverage (Sites Concurrent), Y axis is the AE-to-Bedside SLA
adherence percent. Bubble sizes are proportional to annual operating cost.
"""

from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("Agg")

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

PALETTE = {
    "deep_navy": "#1F3A68",
    "teal": "#2E8B8B",
    "burgundy": "#8B2E3F",
    "gold": "#C18A2C",
    "forest_green": "#2F6B3E",
    "slate": "#4A5568",
    "mauve": "#8B6B8B",
    "mauve_dk": "#6B4B6B",
    "light_gray": "#E2E8F0",
    "off_white": "#F7FAFC",
}

CONFIGS = [
    ("3x H2 + Per-Site Claude Opus 4.7 1M (Reference)", 4, 98.5, 2.2, PALETTE["deep_navy"], True),
    ("3x Atlas Electric + Per-Site Claude Opus", 3, 91.0, 2.6, PALETTE["teal"], False),
    ("3x Tesla Optimus Gen 3 + Per-Site GPT-5.5", 3, 83.0, 2.4, PALETTE["gold"], False),
    ("2x Figure 03 + 2x Claude Sonnet 4.6", 2, 89.0, 1.6, PALETTE["mauve"], False),
    ("4x Phoenix Gen 8 + 4x Gemini 3 Pro", 4, 86.0, 3.4, PALETTE["forest_green"], False),
    ("1x H2 Per Site + Human On-Call", 4, 84.0, 1.9, PALETTE["burgundy"], False),
    ("Human On-Call Network (Baseline)", 4, 81.5, 1.4, PALETTE["slate"], False),
    ("Hybrid 3x H2 + 1 Human Per Site", 4, 96.0, 2.8, PALETTE["mauve_dk"], False),
]


def main(out_path: pathlib.Path) -> None:
    fig = plt.figure(figsize=(8.5, 11.0), facecolor="white")
    fig.text(
        0.06,
        0.975,
        "3x H2 + Per-Site Claude Opus AE Strategic Quadrant",
        fontsize=13.0,
        ha="left",
        color="black",
        fontweight="bold",
    )
    fig.text(
        0.06,
        0.957,
        "Network Coverage vs. AE-to-Bedside SLA Adherence",
        fontsize=10.5,
        ha="left",
        color=PALETTE["slate"],
        fontweight="bold",
    )
    fig.text(
        0.06,
        0.940,
        "4-Site PAT-NET-001, Bubble size proportional to annual operating cost (USD M)",
        fontsize=8.5,
        ha="left",
        color=PALETTE["slate"],
    )
    fig.text(0.94, 0.948, "Demo 07 / Image 09 of 10 / Portrait", fontsize=8.5, ha="right", color=PALETTE["slate"])

    ax = fig.add_axes([0.16, 0.27, 0.80, 0.62])
    ax.set_xlim(0.4, 4.6)
    ax.set_ylim(80, 100)

    x_med, y_med = 2.0, 95.0
    ax.axvspan(0.5, x_med, ymin=(y_med - 80) / 20, ymax=1.0, fc=PALETTE["off_white"], alpha=0.55)
    ax.axvspan(x_med, 4.5, ymin=(y_med - 80) / 20, ymax=1.0, fc=PALETTE["light_gray"], alpha=0.40)
    ax.axvspan(0.5, x_med, ymin=0, ymax=(y_med - 80) / 20, fc="white", alpha=1.0)
    ax.axvspan(x_med, 4.5, ymin=0, ymax=(y_med - 80) / 20, fc=PALETTE["off_white"], alpha=0.55)
    ax.axvline(x_med, color=PALETTE["slate"], lw=1.0, ls="--", alpha=0.65)
    ax.axhline(y_med, color=PALETTE["slate"], lw=1.0, ls="--", alpha=0.65)

    ax.text(0.52, 99.5, "SLA Specialist", fontsize=9.0, color=PALETTE["slate"], fontweight="bold", alpha=0.55)
    ax.text(2.05, 99.5, "Reference Quadrant", fontsize=9.0, color=PALETTE["deep_navy"], fontweight="bold", alpha=0.55)
    ax.text(0.52, 80.6, "Legacy Manual", fontsize=9.0, color=PALETTE["slate"], fontweight="bold", alpha=0.55)
    ax.text(
        2.05,
        80.6,
        "Coverage Specialist",
        fontsize=9.0,
        color=PALETTE["slate"],
        fontweight="bold",
        alpha=0.55,
    )

    label_offsets = {
        0: (-2.30, -1.2),
        1: (-1.05, 1.4),
        2: (-1.10, -1.1),
        3: (-1.20, -0.7),
        4: (-1.25, -1.4),
        5: (-1.20, 1.3),
        6: (-1.20, 1.4),
        7: (-1.20, 1.1),
    }

    for i, (label, x, y, cost, color, is_ref) in enumerate(CONFIGS):
        size = 350 * cost
        ax.scatter([x], [y], s=size, c=color, alpha=0.55, edgecolors="black", lw=1.0, zorder=3)
        if is_ref:
            ax.scatter([x], [y], s=size * 1.55, facecolors="none", edgecolors=PALETTE["deep_navy"], lw=2.4, zorder=2)
        dx, dy = label_offsets.get(i, (0.20, 0.6))
        ha = "left" if dx >= 0 else "right"
        label_x = x + dx
        label_y = y + dy
        ax.annotate(
            label,
            xy=(x, y),
            xytext=(label_x, label_y),
            fontsize=7.6,
            color="black",
            ha=ha,
            va="center",
            arrowprops=dict(arrowstyle="-", color=PALETTE["slate"], lw=0.5, alpha=0.6),
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=color, lw=0.8, alpha=0.95),
        )

    arrow = FancyArrowPatch(
        (1.20, 86.0),
        (3.85, 97.5),
        arrowstyle="-|>",
        mutation_scale=22,
        color=PALETTE["gold"],
        lw=2.0,
        alpha=0.7,
        connectionstyle="arc3,rad=0.18",
        zorder=4,
    )
    ax.add_patch(arrow)
    ax.text(
        2.6,
        93.0,
        "Migration Path",
        fontsize=9.0,
        color=PALETTE["gold"],
        fontweight="bold",
        ha="center",
        bbox=dict(boxstyle="round,pad=0.25", fc=PALETTE["off_white"], ec=PALETTE["gold"], lw=0.8, alpha=0.95),
    )

    ax.set_xlabel("Network Coverage (Sites Concurrent)", fontsize=10.5, color="black")
    ax.set_ylabel("AE-to-Bedside SLA Adherence (percent, 90 s target)", fontsize=10.5, color="black")
    ax.set_xticks([1, 2, 3, 4])
    ax.set_yticks(np.arange(80, 101, 2))
    ax.tick_params(axis="both", labelsize=8.5)
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    ax.spines["left"].set_color(PALETTE["slate"])
    ax.spines["bottom"].set_color(PALETTE["slate"])
    ax.grid(color=PALETTE["light_gray"], lw=0.5, alpha=0.6, zorder=0)
    ax.set_axisbelow(True)

    legend_handles = [
        mpatches.Patch(color=PALETTE["deep_navy"], label="Reference: 3x H2 + Claude Opus"),
        mpatches.Patch(color=PALETTE["teal"], label="3x Atlas + Claude"),
        mpatches.Patch(color=PALETTE["gold"], label="3x Optimus + GPT"),
        mpatches.Patch(color=PALETTE["mauve"], label="2x Figure + Sonnet"),
        mpatches.Patch(color=PALETTE["forest_green"], label="4x Phoenix + Gemini"),
        mpatches.Patch(color=PALETTE["burgundy"], label="1x H2 + Human"),
        mpatches.Patch(color=PALETTE["slate"], label="Human Baseline"),
        mpatches.Patch(color=PALETTE["mauve_dk"], label="Hybrid 3x H2 + Human"),
    ]
    leg = fig.legend(
        handles=legend_handles,
        loc="lower center",
        bbox_to_anchor=(0.5, 0.10),
        ncol=4,
        fontsize=7.8,
        framealpha=0.95,
        edgecolor=PALETTE["slate"],
    )
    leg.get_frame().set_facecolor("white")

    size_legend = (
        "Bubble size scales with annual operating cost (USD M).\n"
        "Reference (deep navy) is the only configuration above both medians (95% SLA, 4-site)."
    )
    fig.text(
        0.5,
        0.045,
        size_legend,
        fontsize=7.8,
        color="black",
        ha="center",
        va="center",
        bbox=dict(boxstyle="round,pad=0.40", fc=PALETTE["off_white"], ec=PALETTE["slate"], lw=0.8),
    )

    fig.text(
        0.06,
        0.012,
        "Clinical-AI-Demos v0.8.0 / Demo 07 Adverse Event Response",
        fontsize=7.3,
        ha="left",
        color=PALETTE["slate"],
    )
    fig.text(
        0.94, 0.012, "DOI: 10.5281/zenodo.18445179 / MIT License", fontsize=7.3, ha="right", color=PALETTE["slate"]
    )

    fig.savefig(out_path, dpi=300, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    out = pathlib.Path(__file__).with_suffix(".png")
    main(out)
    print(f"Saved {out}")
