"""Figure 6 replacement: AE Response Swimlane (single AE, 90 seconds).

Landscape full-page, 11.0 x 8.5 inches, 300 dpi. Renders the 90-second
adverse event response swimlane for Lead, Assist, and Reserve roles.
Replaces the verbatim ASCII figure that previously appeared in methods.tex.
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
    "forest_green_lt": "#5F9B6E",
    "slate": "#4A5568",
    "mauve": "#8B6B8B",
    "light_gray": "#E2E8F0",
    "off_white": "#F7FAFC",
}

TIMES = [0, 5, 15, 18, 22, 30, 45, 60, 75, 90]

LEAD_EVENTS = [
    (0, "AE detected", PALETTE["burgundy"]),
    (5, "Move to bedside", PALETTE["deep_navy"]),
    (15, "Epinephrine ready", PALETTE["gold"]),
    (18, "Epinephrine injected", PALETTE["burgundy_dk"]),
    (22, "Verify SpO2 reading", PALETTE["forest_green"]),
    (30, "Secondary intervention", PALETTE["burgundy"]),
    (45, "Continuous monitoring", PALETTE["teal"]),
    (60, "Transfer to physician", PALETTE["mauve"]),
    (75, "Step back, observe", PALETTE["slate"]),
    (90, "Ready for next AE", PALETTE["forest_green"]),
]
ASSIST_EVENTS = [
    (0, "AE detected, prep tools", PALETTE["burgundy"]),
    (5, "Move to backup position", PALETTE["deep_navy"]),
    (15, "Hand-off epinephrine", PALETTE["gold"]),
    (18, "Pulse oximeter ready", PALETTE["teal"]),
    (22, "Hand-off pulse oximeter", PALETTE["gold"]),
    (30, "ECG leads attached", PALETTE["teal"]),
    (45, "Vital sign relay", PALETTE["teal"]),
    (60, "Tool inventory restock", PALETTE["mauve"]),
    (75, "Step back, observe", PALETTE["slate"]),
    (90, "Ready for next AE", PALETTE["forest_green"]),
]
RESERVE_EVENTS = [
    (0, "AE detected, scan area", PALETTE["burgundy"]),
    (5, "Stand 1.5 m off side", PALETTE["forest_green"]),
    (15, "Page on-call physician", PALETTE["burgundy_dk"]),
    (18, "Log to audit chain", PALETTE["slate"]),
    (22, "Monitor doctor proximity", PALETTE["teal"]),
    (30, "FDA RTCT submission", PALETTE["forest_green_lt"]),
    (45, "Physician arrival", PALETTE["mauve"]),
    (60, "Sponsor ack log", PALETTE["gold"]),
    (75, "Step back, observe", PALETTE["slate"]),
    (90, "Ready for next AE", PALETTE["forest_green"]),
]


def time_to_x(t, x_left, x_right):
    positions = {0: 0.00, 5: 0.10, 15: 0.22, 18: 0.32, 22: 0.42, 30: 0.55, 45: 0.70, 60: 0.82, 75: 0.92, 90: 1.00}
    frac = positions.get(t, t / 90)
    return x_left + frac * (x_right - x_left)


def main(out_path: pathlib.Path) -> None:
    fig = plt.figure(figsize=(11.0, 8.5), facecolor="white")
    fig.text(
        0.05,
        0.965,
        "AE Response Swimlane: Single AE Event, 90 Second Window",
        fontsize=15.0,
        ha="left",
        color="black",
        fontweight="bold",
    )
    fig.text(
        0.05,
        0.940,
        "Lead, Assist, and Reserve coordination from detection to ready state; HR 9505 + FDA RTCT submission inline",
        fontsize=10.0,
        ha="left",
        color=PALETTE["slate"],
    )
    fig.text(0.95, 0.915, "Figure 6 / Paper Figure Replacement", fontsize=8.5, ha="right", color=PALETTE["slate"])

    ax = fig.add_axes([0.04, 0.13, 0.92, 0.78])
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 8.5)
    ax.set_axis_off()

    x_left = 1.55
    x_right = 10.55

    lanes = [
        ("Lead (H2-A)", PALETTE["deep_navy"], 6.20, LEAD_EVENTS),
        ("Assist (H2-B)", PALETTE["teal"], 4.05, ASSIST_EVENTS),
        ("Reserve (H2-C)", PALETTE["forest_green"], 1.90, RESERVE_EVENTS),
    ]
    lane_h = 1.65

    for name, color, y_center, events in lanes:
        ax.add_patch(
            FancyBboxPatch(
                (0.10, y_center - lane_h / 2),
                10.80,
                lane_h,
                boxstyle="round,pad=0.02,rounding_size=0.05",
                fc=PALETTE["off_white"],
                ec=color,
                lw=1.6,
            )
        )
        ax.add_patch(
            FancyBboxPatch(
                (0.20, y_center - lane_h / 2 + 0.10),
                1.20,
                lane_h - 0.20,
                boxstyle="round,pad=0.02,rounding_size=0.05",
                fc=color,
                ec="black",
                lw=0.8,
            )
        )
        ax.text(
            0.80, y_center, name, ha="center", va="center", fontsize=11.0, color="white", fontweight="bold", rotation=90
        )

        for t, label, ec in events:
            x = time_to_x(t, x_left, x_right)
            tile_w = 0.78 if t in (0, 5) else (0.78 if t > 22 else 0.74)
            tile_h = 1.35
            tile_y = y_center
            ax.add_patch(
                FancyBboxPatch(
                    (x - tile_w / 2, tile_y - tile_h / 2),
                    tile_w,
                    tile_h,
                    boxstyle="round,pad=0.02,rounding_size=0.06",
                    fc=ec,
                    ec="black",
                    lw=0.6,
                    alpha=0.92,
                )
            )
            words = label.split()
            wrapped = "\n".join([" ".join(words[i : i + 2]) for i in range(0, len(words), 2)])
            ax.text(
                x,
                tile_y + 0.10,
                wrapped,
                ha="center",
                va="center",
                fontsize=6.2,
                color="white",
                fontweight="bold",
            )
            ax.text(
                x, tile_y - 0.55, f"t+{t}s", ha="center", va="center", fontsize=6.8, color="white", fontweight="bold"
            )

    timeline_y = 0.55
    ax.plot([x_left, x_right], [timeline_y, timeline_y], color=PALETTE["slate"], lw=2.0)
    for t in TIMES:
        x = time_to_x(t, x_left, x_right)
        ax.plot([x, x], [timeline_y - 0.10, timeline_y + 0.10], color=PALETTE["slate"], lw=1.5)
        ax.text(x, timeline_y - 0.30, f"t+{t}s", ha="center", fontsize=8.0, color=PALETTE["slate"])

    ax.text(
        0.80, timeline_y, "Timeline", ha="center", va="center", fontsize=9.0, color=PALETTE["slate"], fontweight="bold"
    )

    sla_y = 7.65
    sla_box = FancyBboxPatch(
        (0.10, sla_y - 0.25),
        10.80,
        0.55,
        boxstyle="round,pad=0.02,rounding_size=0.05",
        fc=PALETTE["off_white"],
        ec=PALETTE["slate"],
        lw=1.0,
    )
    ax.add_patch(sla_box)
    sla_text = (
        "All 3 robots arrive within 90 s. Hand-offs complete within 2 s via 60 GHz UWB. "
        "Reserve performs FDA RTCT submission in parallel with Lead intervention. "
        "Platform: Unitree H2 EDU with 6 dexterous fingers and 0.05 N tactile resolution; "
        "Jetson AGX Thor 2070 TOPS upgrade path on every robot."
    )
    ax.text(0.30, sla_y + 0.02, sla_text, fontsize=8.0, color="black", va="center", wrap=True)

    legend_handles = [
        mpatches.Patch(color=PALETTE["burgundy"], label="AE Detection"),
        mpatches.Patch(color=PALETTE["deep_navy"], label="Position / Move"),
        mpatches.Patch(color=PALETTE["gold"], label="Tool Hand-off"),
        mpatches.Patch(color=PALETTE["burgundy_dk"], label="Intervention"),
        mpatches.Patch(color=PALETTE["teal"], label="Monitoring"),
        mpatches.Patch(color=PALETTE["mauve"], label="Physician / Restock"),
        mpatches.Patch(color=PALETTE["forest_green"], label="Ready State"),
        mpatches.Patch(color=PALETTE["forest_green_lt"], label="FDA RTCT Submission"),
        mpatches.Patch(color=PALETTE["slate"], label="Audit / Observe"),
    ]
    leg = fig.legend(
        handles=legend_handles,
        loc="lower center",
        bbox_to_anchor=(0.5, 0.035),
        ncol=5,
        fontsize=7.6,
        framealpha=0.95,
        edgecolor=PALETTE["slate"],
    )
    leg.get_frame().set_facecolor("white")

    fig.text(
        0.05,
        0.012,
        "Clinical-AI-Demos v0.8.0 / Demo 07 Adverse Event Response / Paper Figure 6",
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
