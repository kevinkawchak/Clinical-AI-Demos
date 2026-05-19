"""Figure 3 replacement: Camarade Swarm Dance (10 second window).

Landscape full-page, 11.0 x 8.5 inches, 300 dpi. Renders a top-down view of
the patient bed and 3 Unitree H2 EDU robots (Lead, Assist, Reserve) over a
10 second 1 Hz peak adverse event window. Trails, velocity arrows, the
60 GHz UWB hand-off at t+6, and a synchronized timeline strip make the
spatial choreography legible at publication quality. Replaces the verbatim
ASCII figure that previously appeared in methods.tex.
"""

from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("Agg")

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Rectangle

PALETTE = {
    "deep_navy": "#1F3A68",
    "deep_navy_lt": "#3F5A88",
    "teal": "#2E8B8B",
    "teal_lt": "#5EBBBB",
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

PATIENT_BED = (0.0, 0.0)


def lead_trajectory(t):
    return PATIENT_BED[0] + 0.04 * np.cos(t * 0.4), PATIENT_BED[1] - 0.40 - 0.02 * np.sin(t * 0.4)


def assist_trajectory(t):
    if t < 6:
        theta = np.pi - t * 0.10
        return PATIENT_BED[0] - 0.80 * np.cos(theta), PATIENT_BED[1] + 0.80 * np.sin(theta)
    transit = (t - 6) / 2.0
    transit = min(transit, 1.0)
    x0, y0 = -0.80 * np.cos(np.pi - 0.60), 0.80 * np.sin(np.pi - 0.60)
    x_l, y_l = lead_trajectory(t)
    handoff_x = x_l - 0.40
    handoff_y = y_l + 0.05
    return x0 + (handoff_x - x0) * transit, y0 + (handoff_y - y0) * transit


def reserve_trajectory(t):
    theta = np.pi / 2 + 0.45 + t * 0.18
    return 1.50 * np.cos(theta), 1.50 * np.sin(theta)


def main(out_path: pathlib.Path) -> None:
    fig = plt.figure(figsize=(11.0, 8.5), facecolor="white")
    fig.text(
        0.05,
        0.965,
        "Camarade Swarm Dance: Top-Down Choreography over a 10 Second AE Peak",
        fontsize=15.0,
        ha="left",
        color="black",
        fontweight="bold",
    )
    fig.text(
        0.05,
        0.940,
        "Lead, Assist, Reserve trails at 1 Hz drive role rotation; hand-off at t+6 via 60 GHz UWB peer mesh",
        fontsize=10.0,
        ha="left",
        color=PALETTE["slate"],
    )
    fig.text(0.95, 0.915, "Figure 3 / Paper Figure Replacement", fontsize=8.5, ha="right", color=PALETTE["slate"])

    main_ax = fig.add_axes([0.04, 0.30, 0.62, 0.59])
    main_ax.set_aspect("equal")
    main_ax.set_xlim(-2.6, 2.6)
    main_ax.set_ylim(-1.7, 2.3)
    main_ax.set_facecolor(PALETTE["off_white"])

    main_ax.add_patch(Rectangle((-2.55, -1.65), 5.10, 3.90, fc="white", ec=PALETTE["slate"], lw=2.2, zorder=1))
    for x in np.linspace(-2.5, 2.5, 11):
        main_ax.plot([x, x], [-1.6, 2.2], color=PALETTE["light_gray"], lw=0.4, zorder=0)
    for y in np.linspace(-1.5, 2.2, 8):
        main_ax.plot([-2.55, 2.55], [y, y], color=PALETTE["light_gray"], lw=0.4, zorder=0)

    main_ax.text(0.0, 2.10, "north wall", ha="center", fontsize=8.5, color=PALETTE["slate"], style="italic")
    main_ax.text(0.0, -1.55, "south wall", ha="center", fontsize=8.5, color=PALETTE["slate"], style="italic")

    bed = Rectangle((-0.40, -0.25), 0.80, 0.50, fc=PALETTE["light_gray"], ec="black", lw=1.2, zorder=2)
    main_ax.add_patch(bed)
    main_ax.text(
        0.0,
        0.0,
        "Patient\nBed",
        ha="center",
        va="center",
        fontsize=9.0,
        color=PALETTE["slate"],
        fontweight="bold",
        zorder=3,
    )

    ts = np.arange(0, 10, 0.4)
    lead_pts = np.array([lead_trajectory(t) for t in ts])
    assist_pts = np.array([assist_trajectory(t) for t in ts])
    reserve_pts = np.array([reserve_trajectory(t) for t in ts])

    main_ax.plot(
        lead_pts[:, 0],
        lead_pts[:, 1],
        "-",
        color=PALETTE["deep_navy"],
        lw=2.0,
        alpha=0.85,
        zorder=4,
        label="Lead H2-A trail",
    )
    main_ax.plot(
        assist_pts[:, 0],
        assist_pts[:, 1],
        "-",
        color=PALETTE["teal"],
        lw=2.0,
        alpha=0.85,
        zorder=4,
        label="Assist H2-B trail",
    )
    main_ax.plot(
        reserve_pts[:, 0],
        reserve_pts[:, 1],
        "-",
        color=PALETTE["forest_green"],
        lw=2.0,
        alpha=0.85,
        zorder=4,
        label="Reserve H2-C trail",
    )

    for t in [0, 2, 4, 6, 8]:
        for traj, color in [
            (lead_trajectory, PALETTE["deep_navy"]),
            (assist_trajectory, PALETTE["teal"]),
            (reserve_trajectory, PALETTE["forest_green"]),
        ]:
            x, y = traj(t)
            main_ax.add_patch(Circle((x, y), 0.12, fc=color, ec="white", lw=1.0, zorder=5))
            main_ax.text(
                x, y, str(int(t)), ha="center", va="center", fontsize=7.0, color="white", fontweight="bold", zorder=6
            )

    main_ax.add_patch(Circle((0.0, 0.0), 0.60, fc="none", ec=PALETTE["burgundy"], lw=1.0, ls=":", alpha=0.6))
    main_ax.text(0.0, -0.62, "0.4 m Lead radius", fontsize=7.0, color=PALETTE["burgundy"], ha="center", style="italic")

    main_ax.add_patch(Circle((0.0, 0.0), 1.50, fc="none", ec=PALETTE["forest_green"], lw=1.0, ls=":", alpha=0.5))
    main_ax.text(
        1.50, -0.85, "1.5 m Reserve perimeter", fontsize=7.0, color=PALETTE["forest_green"], ha="left", style="italic"
    )

    x6_a, y6_a = assist_trajectory(6)
    x8_a, y8_a = assist_trajectory(8)
    handoff_arrow = FancyArrowPatch(
        (x6_a, y6_a),
        (x8_a, y8_a),
        arrowstyle="-|>",
        mutation_scale=18,
        color=PALETTE["gold"],
        lw=2.6,
        zorder=7,
    )
    main_ax.add_patch(handoff_arrow)
    main_ax.text(
        (x6_a + x8_a) / 2 - 0.05,
        (y6_a + y8_a) / 2 + 0.18,
        "60 GHz UWB\nhand-off (t+6 to t+8)",
        fontsize=8.0,
        color=PALETTE["burgundy_dk"],
        ha="left",
        fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.20", fc=PALETTE["off_white"], ec=PALETTE["gold"], lw=0.8),
    )

    main_ax.legend(
        loc="lower left",
        bbox_to_anchor=(0.0, 0.0),
        fontsize=7.5,
        ncol=1,
        framealpha=0.92,
        edgecolor=PALETTE["slate"],
    )
    main_ax.set_xlabel("x (meters) - east axis", fontsize=8.5, color=PALETTE["slate"])
    main_ax.set_ylabel("y (meters) - north axis", fontsize=8.5, color=PALETTE["slate"])
    main_ax.tick_params(axis="both", labelsize=7.5)

    time_ax = fig.add_axes([0.69, 0.55, 0.28, 0.34])
    time_ax.set_xlim(0, 10)
    time_ax.set_ylim(-0.5, 3.5)
    time_ax.set_facecolor("white")
    time_ax.set_xlabel("Time (seconds since AE peak)", fontsize=8.5, color=PALETTE["slate"])
    time_ax.set_xticks(range(0, 11, 2))
    time_ax.set_yticks([0, 1, 2, 3])
    time_ax.set_yticklabels(["Reserve", "Assist", "Lead", "Patient"], fontsize=8.0, color="black", fontweight="bold")
    time_ax.tick_params(axis="x", labelsize=7.5)
    time_ax.grid(color=PALETTE["light_gray"], lw=0.5, alpha=0.7)
    time_ax.set_axisbelow(True)

    time_ax.add_patch(Rectangle((0, 2.65), 10, 0.30, fc=PALETTE["deep_navy"], alpha=0.85))
    time_ax.text(
        5,
        2.80,
        "stay close to bedside (0.4 m offset)",
        ha="center",
        va="center",
        fontsize=7.0,
        color="white",
        fontweight="bold",
    )

    time_ax.add_patch(Rectangle((0, 1.65), 6, 0.30, fc=PALETTE["teal"], alpha=0.85))
    time_ax.add_patch(Rectangle((6, 1.65), 2, 0.30, fc=PALETTE["gold"], alpha=0.9))
    time_ax.add_patch(Rectangle((8, 1.65), 2, 0.30, fc=PALETTE["teal_lt"], alpha=0.85))
    time_ax.text(3, 1.80, "orbit 0.8 m west", ha="center", va="center", fontsize=6.8, color="white")
    time_ax.text(7, 1.80, "hand-off", ha="center", va="center", fontsize=6.8, color="white", fontweight="bold")
    time_ax.text(9, 1.80, "tool ready", ha="center", va="center", fontsize=6.8, color="white")

    time_ax.add_patch(Rectangle((0, 0.65), 10, 0.30, fc=PALETTE["forest_green"], alpha=0.85))
    time_ax.text(
        5, 0.80, "1.5 m perimeter watch", ha="center", va="center", fontsize=7.0, color="white", fontweight="bold"
    )

    time_ax.add_patch(Rectangle((5.8, -0.3), 0.4, 3.55, fc=PALETTE["burgundy"], alpha=0.50, zorder=0))
    time_ax.text(6.0, 3.30, "t+6 AE peak", ha="center", fontsize=7.5, color=PALETTE["burgundy"], fontweight="bold")

    notes_ax = fig.add_axes([0.69, 0.13, 0.28, 0.36])
    notes_ax.set_axis_off()
    notes_ax.set_xlim(0, 1)
    notes_ax.set_ylim(0, 1)
    notes_ax.add_patch(
        FancyBboxPatch(
            (0.02, 0.02),
            0.96,
            0.96,
            boxstyle="round,pad=0.02,rounding_size=0.04",
            fc=PALETTE["off_white"],
            ec=PALETTE["slate"],
            lw=1.0,
        )
    )
    notes_ax.text(0.06, 0.93, "Observations", fontsize=10.5, color=PALETTE["slate"], fontweight="bold")
    obs_lines = [
        "Lead remains within 0.4 m of patient bed",
        "Assist orbits 0.8 m to the west, ready",
        "Reserve circles 1.5 m perimeter, watching",
        "No robot enters peer 2 s motion envelope",
        "t+6: Lead requests secondary epinephrine;",
        "Assist arrives within 2 s via 60 GHz UWB",
        "Dexterous H2 EDU hand: 0.4 m hand-off,",
        "0 drops across 32-iteration sweep",
    ]
    for i, line in enumerate(obs_lines):
        notes_ax.text(0.06, 0.83 - i * 0.10, "- " + line, fontsize=7.8, color="black", va="top")

    legend_handles = [
        mpatches.Patch(color=PALETTE["deep_navy"], label="Lead H2-A"),
        mpatches.Patch(color=PALETTE["teal"], label="Assist H2-B"),
        mpatches.Patch(color=PALETTE["forest_green"], label="Reserve H2-C"),
        mpatches.Patch(color=PALETTE["gold"], label="UWB Hand-off Event"),
        mpatches.Patch(color=PALETTE["burgundy"], label="AE Peak (t+6)"),
        mpatches.Patch(color=PALETTE["light_gray"], label="Patient Bed"),
    ]
    leg = fig.legend(
        handles=legend_handles,
        loc="lower center",
        bbox_to_anchor=(0.5, 0.030),
        ncol=6,
        fontsize=7.8,
        framealpha=0.95,
        edgecolor=PALETTE["slate"],
    )
    leg.get_frame().set_facecolor("white")

    fig.text(
        0.05,
        0.005,
        "Clinical-AI-Demos v0.8.0 / Demo 07 Adverse Event Response / Paper Figure 3",
        fontsize=7.5,
        ha="left",
        color=PALETTE["slate"],
    )
    fig.text(
        0.95, 0.005, "DOI: 10.5281/zenodo.18445179 / MIT License", fontsize=7.5, ha="right", color=PALETTE["slate"]
    )

    fig.savefig(out_path, dpi=300, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    out = pathlib.Path(__file__).with_suffix(".png")
    main(out)
    print(f"Saved {out}")
