"""Image 07-10: AE Cross-Site Rotation Decision Tree.

Letter portrait, 8.5 x 11.0 inches, 300 dpi. Top-down decision tree showing
local response vs. cross-site transit logic when an AE surge is detected at
2 or more concurrent CTCAE Grade 3+ events.
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
    "mauve_dk": "#6B4B6B",
    "light_gray": "#E2E8F0",
    "off_white": "#F7FAFC",
}


def rect_node(ax, cx, cy, w, h, label, color, font_color="white"):
    ax.add_patch(
        FancyBboxPatch(
            (cx - w / 2, cy - h / 2),
            w,
            h,
            boxstyle="round,pad=0.04,rounding_size=0.08",
            fc=color,
            ec="black",
            lw=0.9,
        )
    )
    ax.text(cx, cy, label, ha="center", va="center", fontsize=8.5, color=font_color, fontweight="bold")


def diamond_node(ax, cx, cy, w, label, color):
    diamond = plt.Polygon(
        [(cx, cy + w / 2), (cx + w, cy), (cx, cy - w / 2), (cx - w, cy)],
        fc=color,
        ec="black",
        lw=1.0,
    )
    ax.add_patch(diamond)
    ax.text(cx, cy, label, ha="center", va="center", fontsize=8.5, color="white", fontweight="bold")


def edge(ax, x0, y0, x1, y1, label=None, label_color=None):
    arrow = FancyArrowPatch(
        (x0, y0),
        (x1, y1),
        arrowstyle="-|>",
        mutation_scale=14,
        color=PALETTE["slate"],
        lw=1.3,
    )
    ax.add_patch(arrow)
    if label:
        mx, my = (x0 + x1) / 2, (y0 + y1) / 2
        ax.text(
            mx,
            my,
            label,
            ha="center",
            va="center",
            fontsize=8.0,
            color=label_color or PALETTE["slate"],
            fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.20", fc="white", ec=PALETTE["slate"], lw=0.6),
        )


def annotation(ax, cx, cy, text, color):
    ax.text(
        cx,
        cy,
        text,
        ha="left",
        va="center",
        fontsize=7.3,
        color="black",
        bbox=dict(boxstyle="round,pad=0.30", fc=PALETTE["off_white"], ec=color, lw=0.8),
    )


def main(out_path: pathlib.Path) -> None:
    fig = plt.figure(figsize=(8.5, 11.0), facecolor="white")
    fig.text(
        0.06,
        0.975,
        "3x H2 + Per-Site Claude Opus AE Cross-Site",
        fontsize=12.5,
        ha="left",
        color="black",
        fontweight="bold",
    )
    fig.text(
        0.06,
        0.957,
        "Rotation Decision Tree",
        fontsize=11.0,
        ha="left",
        color=PALETTE["slate"],
        fontweight="bold",
    )
    fig.text(
        0.06,
        0.940,
        "Cross-Site AE Surge: Local Capacity, Transit, H2 Re-Dispatch",
        fontsize=8.8,
        ha="left",
        color=PALETTE["slate"],
    )
    fig.text(0.94, 0.948, "Demo 07 / Image 10 of 10 / Portrait", fontsize=8.5, ha="right", color=PALETTE["slate"])

    ax = fig.add_axes([0.02, 0.06, 0.96, 0.88])
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 11)
    ax.set_axis_off()

    rect_node(ax, 5.0, 10.0, 3.6, 0.55, "Cross-Site AE Surge Detected", PALETTE["burgundy"])
    annotation(
        ax,
        7.05,
        10.0,
        "Detected when per-site Claude Opus reports\n>= 2 concurrent CTCAE Grade 3+ events.",
        PALETTE["burgundy"],
    )

    diamond_node(ax, 5.0, 8.85, 1.3, "Local Site\nHas H2?", PALETTE["slate"])
    edge(ax, 5.0, 9.72, 5.0, 9.18)

    rect_node(ax, 2.0, 7.55, 2.6, 0.55, "Local H2 Responds", PALETTE["forest_green"])
    edge(ax, 3.95, 8.65, 2.85, 7.85, "Yes", PALETTE["forest_green"])

    diamond_node(ax, 7.5, 7.45, 1.4, "Cross-Site\nTransit\nFeasible?", PALETTE["slate"])
    edge(ax, 6.05, 8.65, 7.50, 7.95, "No", PALETTE["burgundy"])

    diamond_node(ax, 5.5, 5.55, 1.25, "Distance to\nNearest H2?", PALETTE["slate"])
    edge(ax, 7.20, 6.85, 6.05, 5.95, "Yes", PALETTE["forest_green"])

    rect_node(ax, 9.05, 5.55, 1.80, 0.65, "Activate Human\nOn-Call Backup\nPer Site", PALETTE["burgundy_dk"])
    edge(ax, 7.95, 6.85, 8.85, 5.95, "No", PALETTE["burgundy"])
    annotation(
        ax,
        8.10,
        4.45,
        "Severe weather or\nFAA NOTAM issued.",
        PALETTE["burgundy"],
    )

    rect_node(ax, 3.30, 3.85, 2.30, 0.65, "FAA Part 135\nMedical Drone", PALETTE["mauve"])
    edge(ax, 4.95, 4.85, 3.95, 4.30, "< 500 mi", PALETTE["forest_green"])

    rect_node(ax, 7.30, 3.85, 2.30, 0.65, "Hospital Charter\nAircraft", PALETTE["gold"])
    edge(ax, 6.05, 4.85, 6.85, 4.30, "> 500 mi", PALETTE["burgundy"])

    annotation(
        ax,
        0.10,
        3.85,
        "Drone folds H2 onto platform.\nBattery hot-swap in transit.",
        PALETTE["mauve"],
    )
    annotation(
        ax,
        7.30,
        2.85,
        "Hospital-charter aircraft\nfrom nearest H2-resident site.",
        PALETTE["gold"],
    )

    rect_node(ax, 5.30, 1.85, 3.40, 0.65, "H2 Bedside Arrival\nunder 30 min SLA", PALETTE["deep_navy"])
    edge(ax, 3.40, 3.40, 4.85, 2.30)
    edge(ax, 7.10, 3.40, 5.85, 2.30)

    annotation(
        ax,
        0.10,
        1.85,
        "Cross-site transit SLA\nresolves the surge.",
        PALETTE["deep_navy"],
    )

    legend_handles = [
        mpatches.Patch(color=PALETTE["burgundy"], label="Surge Trigger / On-Call Backup"),
        mpatches.Patch(color=PALETTE["slate"], label="Decision Diamond"),
        mpatches.Patch(color=PALETTE["forest_green"], label="Local Response"),
        mpatches.Patch(color=PALETTE["mauve"], label="Drone Transit Modality"),
        mpatches.Patch(color=PALETTE["gold"], label="Charter Modality"),
        mpatches.Patch(color=PALETTE["deep_navy"], label="H2 Action"),
        mpatches.Patch(color=PALETTE["burgundy_dk"], label="Human On-Call Backup"),
    ]
    leg = fig.legend(
        handles=legend_handles,
        loc="lower center",
        bbox_to_anchor=(0.5, 0.022),
        ncol=4,
        fontsize=7.5,
        framealpha=0.95,
        edgecolor=PALETTE["slate"],
    )
    leg.get_frame().set_facecolor("white")

    fig.text(
        0.06,
        0.005,
        "Clinical-AI-Demos v0.8.0 / Demo 07 Adverse Event Response",
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
