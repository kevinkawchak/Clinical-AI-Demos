"""Image 07-04: AE Response Value Proposition Canvas.

Letter portrait, 8.5 x 11.0 inches, 300 dpi. Strategyzer-style canvas with a
Value Map (square) on the left and Customer Profile (circle) on the right
joined by a Fit arrow. Used inside the Demo 07 paper imagegen tree.
"""

from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("Agg")

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

PALETTE = {
    "deep_navy": "#1F3A68",
    "teal": "#2E8B8B",
    "burgundy": "#8B2E3F",
    "gold": "#C18A2C",
    "forest_green": "#2F6B3E",
    "slate": "#4A5568",
    "mauve": "#8B6B8B",
    "light_gray": "#E2E8F0",
    "off_white": "#F7FAFC",
}


def panel(ax, x, y, w, h, color, header, lines, header_fc=None):
    box = FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.05", fc=PALETTE["off_white"], ec=color, lw=1.6
    )
    ax.add_patch(box)
    head = FancyBboxPatch(
        (x, y + h - 0.36), w, 0.36, boxstyle="round,pad=0.0,rounding_size=0.05", fc=color, ec=color, lw=1.0
    )
    ax.add_patch(head)
    ax.text(x + 0.10, y + h - 0.18, header, ha="left", va="center", fontsize=10.0, color="white", fontweight="bold")
    text_y = y + h - 0.55
    for line in lines:
        ax.text(x + 0.12, text_y, "- " + line, ha="left", va="top", fontsize=8.0, color="black", wrap=True)
        text_y -= 0.36


def main(out_path: pathlib.Path) -> None:
    fig = plt.figure(figsize=(8.5, 11.0), facecolor="white")

    fig.text(
        0.06,
        0.975,
        "3x H2 + Per-Site Claude Opus 4.7 1M AE Response",
        fontsize=13.5,
        ha="left",
        color="black",
        fontweight="bold",
    )
    fig.text(
        0.06,
        0.957,
        "Value Proposition Canvas",
        fontsize=11.0,
        ha="left",
        color=PALETTE["slate"],
        fontweight="bold",
    )
    fig.text(
        0.06,
        0.940,
        "Stakeholders: Sponsor Pharmacovigilance, On-Call Physician, Patient, Site Investigator",
        fontsize=8.5,
        ha="left",
        color=PALETTE["slate"],
    )
    fig.text(0.94, 0.948, "Demo 07 / Image 04 of 10 / Portrait", fontsize=8.5, ha="right", color=PALETTE["slate"])

    ax = fig.add_axes([0.04, 0.08, 0.92, 0.84])
    ax.set_xlim(0, 8.5)
    ax.set_ylim(0, 11)
    ax.set_axis_off()

    ax.text(2.10, 9.55, "Value Map", ha="center", fontsize=11.5, color=PALETTE["slate"], fontweight="bold")
    map_outer = FancyBboxPatch(
        (0.10, 5.00),
        4.00,
        4.20,
        boxstyle="round,pad=0.02,rounding_size=0.15",
        fc=PALETTE["light_gray"],
        ec=PALETTE["slate"],
        lw=1.5,
        alpha=0.35,
    )
    ax.add_patch(map_outer)

    panel(
        ax,
        0.25,
        7.55,
        3.70,
        1.85,
        PALETTE["deep_navy"],
        "Products and Services",
        [
            "3x Unitree H2 rotating across 4-site network",
            "Per-site Claude Opus 4.7 1M on-prem at 1 Hz",
            "Continental coordination bus (de-identified)",
            "FAA Part 135 drone / charter for H2 transit",
        ],
    )

    panel(
        ax,
        0.25,
        5.50,
        1.80,
        1.90,
        PALETTE["burgundy"],
        "Pain Relievers",
        [
            "Eliminates 24/7",
            "staffing gap",
            "Night-shift coverage",
            "IP65 outdoor H2",
            "5 ms E-stop",
        ],
    )

    panel(
        ax,
        2.15,
        5.50,
        1.80,
        1.90,
        PALETTE["forest_green"],
        "Gain Creators",
        [
            "CTCAE under 1 h",
            "AE-bedside under 90 s",
            "Sponsor SAE down 80%",
            "Hash-chained audit",
        ],
    )

    ax.text(6.40, 9.55, "Customer Profile", ha="center", fontsize=11.5, color=PALETTE["slate"], fontweight="bold")
    circle = plt.Circle((6.40, 7.20), 1.95, fc=PALETTE["light_gray"], ec=PALETTE["slate"], lw=1.5, alpha=0.35)
    ax.add_patch(circle)

    rx = 1.90
    cx_c, cy_c = 6.40, 7.20
    for theta_start, theta_end, color in [
        (np.pi / 2 - 0.5, np.pi / 2 + 0.5, PALETTE["deep_navy"]),
        (np.pi + 0.10, 3 * np.pi / 2 - 0.10, PALETTE["burgundy"]),
        (3 * np.pi / 2 + 0.10, 2 * np.pi - 0.10, PALETTE["forest_green"]),
    ]:
        th = np.linspace(theta_start, theta_end, 24)
        pts = np.column_stack([cx_c + rx * np.cos(th), cy_c + rx * np.sin(th)])
        pts = np.vstack([[cx_c, cy_c], pts, [cx_c, cy_c]])
        ax.add_patch(plt.Polygon(pts, fc=color, ec="white", lw=1.0, alpha=0.20))

    job_lines = [
        "Detect and respond at",
        "4 sites continuously",
        "Meet HR 9505 1-h SLA",
        "Coordinate cross-site",
        "humanoid rotation",
    ]
    pain_lines = [
        "Night-shift gaps",
        "Cross-site coordination",
        "Manual reconciliation",
    ]
    gain_lines = [
        "24/7 SLA provability",
        "Single audit pane",
        "CTCAE consistency",
    ]

    box_jobs = FancyBboxPatch(
        (5.45, 7.95),
        1.90,
        1.30,
        boxstyle="round,pad=0.02,rounding_size=0.04",
        fc="white",
        ec=PALETTE["deep_navy"],
        lw=1.4,
    )
    ax.add_patch(box_jobs)
    ax.text(6.40, 9.05, "Customer Jobs", ha="center", fontsize=9.5, color=PALETTE["deep_navy"], fontweight="bold")
    for i, line in enumerate(job_lines):
        ax.text(6.40, 8.80 - i * 0.17, line, ha="center", fontsize=7.3, color="black")

    box_pains = FancyBboxPatch(
        (4.65, 5.50),
        1.50,
        1.55,
        boxstyle="round,pad=0.02,rounding_size=0.04",
        fc="white",
        ec=PALETTE["burgundy"],
        lw=1.4,
    )
    ax.add_patch(box_pains)
    ax.text(5.40, 6.85, "Pains", ha="center", fontsize=9.5, color=PALETTE["burgundy"], fontweight="bold")
    for i, line in enumerate(pain_lines):
        ax.text(5.40, 6.55 - i * 0.30, line, ha="center", fontsize=7.0, color="black")

    box_gains = FancyBboxPatch(
        (6.65, 5.50),
        1.65,
        1.55,
        boxstyle="round,pad=0.02,rounding_size=0.04",
        fc="white",
        ec=PALETTE["forest_green"],
        lw=1.4,
    )
    ax.add_patch(box_gains)
    ax.text(7.45, 6.85, "Gains", ha="center", fontsize=9.5, color=PALETTE["forest_green"], fontweight="bold")
    for i, line in enumerate(gain_lines):
        ax.text(7.45, 6.55 - i * 0.30, line, ha="center", fontsize=7.0, color="black")

    arrow = FancyArrowPatch(
        (4.05, 7.20),
        (4.55, 7.20),
        arrowstyle="-|>",
        mutation_scale=28,
        color=PALETTE["gold"],
        lw=3.6,
    )
    ax.add_patch(arrow)
    ax.text(4.30, 7.55, "Fit", ha="center", fontsize=12, color=PALETTE["gold"], fontweight="bold")

    metrics_box = FancyBboxPatch(
        (0.30, 1.30),
        7.90,
        3.70,
        boxstyle="round,pad=0.02,rounding_size=0.08",
        fc=PALETTE["off_white"],
        ec=PALETTE["slate"],
        lw=1.2,
    )
    ax.add_patch(metrics_box)
    ax.text(
        4.25,
        4.65,
        "Key Outcome Metrics at v0.5.0 Reference",
        ha="center",
        fontsize=11.5,
        color=PALETTE["slate"],
        fontweight="bold",
    )

    rows = [
        ("AE-to-Bedside p50", "67.5 s", "90 s SLA", PALETTE["forest_green"]),
        ("AE-to-Bedside p95", "88.2 s", "90 s SLA", PALETTE["forest_green"]),
        ("FDA RTCT 1-h SLA", "99.9%", "HR 9505", PALETTE["forest_green"]),
        ("Camaraderie Pass Rate", "98.5%", "7 invariants", PALETTE["forest_green"]),
        ("Sponsor SAE Narrative", "-80% time", "12 to 1 h", PALETTE["forest_green"]),
        ("Cross-Site Transit SLA", "< 30 min", "Drone or charter", PALETTE["gold"]),
        ("AE Events per Week (net)", "60 to 90", "4 sites total", PALETTE["slate"]),
    ]
    row_top = 4.30
    col_xs = [0.55, 3.20, 4.50, 6.40]
    col_headers = ["Metric", "Value", "Target / Source", "Status"]
    for cx, ch in zip(col_xs, col_headers):
        ax.text(cx, row_top, ch, ha="left", fontsize=8.5, color=PALETTE["slate"], fontweight="bold")
    for i, (m, v, t, c) in enumerate(rows):
        ry = row_top - 0.36 - i * 0.36
        ax.plot([0.50, 8.10], [ry + 0.16, ry + 0.16], color=PALETTE["light_gray"], lw=0.5)
        ax.text(col_xs[0], ry, m, fontsize=8.0, color="black")
        ax.text(col_xs[1], ry, v, fontsize=8.0, color=c, fontweight="bold")
        ax.text(col_xs[2], ry, t, fontsize=8.0, color="black")
        ax.add_patch(plt.Circle((col_xs[3] + 0.15, ry + 0.06), 0.08, fc=c, ec="black", lw=0.4))
        ax.text(col_xs[3] + 0.35, ry, "On-target", fontsize=7.8, color=c)

    legend_handles = [
        mpatches.Patch(color=PALETTE["deep_navy"], label="Products / Customer Jobs"),
        mpatches.Patch(color=PALETTE["burgundy"], label="Pain Relievers / Pains"),
        mpatches.Patch(color=PALETTE["forest_green"], label="Gain Creators / Gains"),
        mpatches.Patch(color=PALETTE["gold"], label="Fit / Transit reserve"),
    ]
    leg = fig.legend(
        handles=legend_handles,
        loc="lower center",
        bbox_to_anchor=(0.5, 0.04),
        ncol=4,
        fontsize=7.8,
        framealpha=0.95,
        edgecolor=PALETTE["slate"],
    )
    leg.get_frame().set_facecolor("white")

    fig.text(
        0.06,
        0.020,
        "Clinical-AI-Demos v0.8.0 / Demo 07 Adverse Event Response",
        fontsize=7.5,
        ha="left",
        color=PALETTE["slate"],
    )
    fig.text(
        0.94, 0.020, "DOI: 10.5281/zenodo.18445179 / MIT License", fontsize=7.5, ha="right", color=PALETTE["slate"]
    )

    fig.savefig(out_path, dpi=300, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    out = pathlib.Path(__file__).with_suffix(".png")
    main(out)
    print(f"Saved {out}")
