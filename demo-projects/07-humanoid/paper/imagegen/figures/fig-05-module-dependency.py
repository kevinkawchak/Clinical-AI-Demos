"""Figure 5 replacement: Per-Site Module Dependency at One 1 Hz Tick.

Portrait full-page, 8.5 x 11.0 inches, 300 dpi. Renders the per-site
dependency graph from sensor frame ingest at 10 Hz, through the 1 Hz LLM
planner broadcast, through 3 robots, through xyz safety and the 10 Hz
robot_loop, to FDA RTCT submission. Every node names a single file in
paper/codegen/src/.
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


def node(ax, cx, cy, w, h, title, subtitle, color, font_color="white"):
    ax.add_patch(
        FancyBboxPatch(
            (cx - w / 2, cy - h / 2),
            w,
            h,
            boxstyle="round,pad=0.04,rounding_size=0.08",
            fc=color,
            ec="black",
            lw=1.0,
        )
    )
    ax.text(cx, cy + 0.10, title, ha="center", va="center", fontsize=8.5, color=font_color, fontweight="bold")
    if subtitle:
        ax.text(cx, cy - 0.13, subtitle, ha="center", va="center", fontsize=7.0, color=font_color, style="italic")


def edge(ax, x0, y0, x1, y1, label=None):
    arrow = FancyArrowPatch(
        (x0, y0),
        (x1, y1),
        arrowstyle="-|>",
        mutation_scale=14,
        color=PALETTE["slate"],
        lw=1.2,
    )
    ax.add_patch(arrow)
    if label:
        mx, my = (x0 + x1) / 2, (y0 + y1) / 2
        ax.text(
            mx + 0.05,
            my,
            label,
            fontsize=7.0,
            color=PALETTE["slate"],
            bbox=dict(boxstyle="round,pad=0.18", fc="white", ec=PALETTE["slate"], lw=0.5),
        )


def main(out_path: pathlib.Path) -> None:
    fig = plt.figure(figsize=(8.5, 11.0), facecolor="white")
    fig.text(
        0.06,
        0.975,
        "Per-Site Module Dependency at One 1 Hz Tick",
        fontsize=13.5,
        ha="left",
        color="black",
        fontweight="bold",
    )
    fig.text(
        0.06,
        0.957,
        "Sensor frame to FDA RTCT submission via Claude Opus 4.7 1M broadcast and 3 H2 EDU robots",
        fontsize=9.0,
        ha="left",
        color=PALETTE["slate"],
    )
    fig.text(0.94, 0.978, "Figure 5 / Paper Figure Replacement", fontsize=8.5, ha="right", color=PALETTE["slate"])

    ax = fig.add_axes([0.04, 0.05, 0.92, 0.89])
    ax.set_xlim(0, 8.5)
    ax.set_ylim(0, 11)
    ax.set_axis_off()

    node_w, node_h = 3.4, 0.62

    node(
        ax, 4.25, 10.20, node_w, node_h, "sensor_to_xyz.py", "RGB-D + IR + UWB Kalman fusion at 10 Hz", PALETTE["mauve"]
    )
    node(ax, 4.25, 9.20, node_w, node_h, "comms_intellectual.py", "Pub-sub on Claude Code bus", PALETTE["teal"])
    node(
        ax,
        4.25,
        8.20,
        node_w + 0.40,
        node_h + 0.10,
        "llm_planner.py (1 Hz)",
        "Claude Opus 4.7 1M, prompt_frozen.md, llm_decision schema",
        PALETTE["deep_navy"],
    )
    node(
        ax,
        4.25,
        7.15,
        node_w + 0.40,
        node_h + 0.10,
        "broadcaster.py + h2_dispatcher.py",
        "atomic publish, 3 acks / 500 ms, SHA-256 audit chain",
        PALETTE["deep_navy"],
    )

    robot_y = 5.95
    robot_w = 1.95
    robot_h = 0.62
    for cx, name, color, role in [
        (1.50, "H2-A", PALETTE["forest_green"], "Lead"),
        (4.25, "H2-B", PALETTE["teal"], "Assist"),
        (7.00, "H2-C", PALETTE["mauve"], "Reserve"),
    ]:
        node(ax, cx, robot_y, robot_w, robot_h, name, role, color)

    node(ax, 2.50, 4.65, 2.30, node_h, "comms_physical.py", "60 GHz UWB 200 Hz + IR 1000 Hz", PALETTE["gold"])
    node(ax, 6.00, 4.65, 2.30, node_h, "swarm_coordinator.py", "Hungarian match + 7 invariants", PALETTE["gold"])

    node(
        ax,
        4.25,
        3.45,
        node_w + 0.40,
        node_h,
        "xyz_safety.py guards",
        "force budget 15 / 5 N + 1.2 / 0.4 m + 22 N",
        PALETTE["burgundy"],
    )
    node(
        ax,
        4.25,
        2.45,
        node_w + 0.40,
        node_h,
        "robot_loop.cpp (10 Hz motion loop)",
        "quintic blending + 5 ms E-stop",
        PALETTE["deep_navy"],
    )
    node(
        ax,
        4.25,
        1.45,
        node_w + 0.40,
        node_h,
        "ctcae_grader.py + physician_escalation.py",
        "CTCAE v5.0 + Grade 3+ pager + IV block",
        PALETTE["burgundy_dk"],
    )

    node(
        ax,
        4.25,
        0.45,
        4.40,
        node_h,
        "fda_rtct_submitter.py",
        "HR 9505 1 hour SLA + ed25519 signed submission",
        PALETTE["forest_green"],
    )

    edge(ax, 4.25, 9.89, 4.25, 9.51, "10 Hz")
    edge(ax, 4.25, 8.89, 4.25, 8.55, "")
    edge(ax, 4.25, 7.85, 4.25, 7.50, "1 broadcast")
    edge(ax, 4.25, 6.80, 4.25, 6.32, "3 sub commands")

    for cx in [1.50, 4.25, 7.00]:
        edge(ax, 4.25, 6.75, cx, robot_y + robot_h / 2, "")

    edge(ax, 1.50, robot_y - robot_h / 2, 2.50, 4.96)
    edge(ax, 4.25, robot_y - robot_h / 2, 4.00, 4.96)
    edge(ax, 7.00, robot_y - robot_h / 2, 6.00, 4.96)

    edge(ax, 2.50, 4.34, 4.00, 3.76)
    edge(ax, 6.00, 4.34, 4.50, 3.76)

    edge(ax, 4.25, 3.14, 4.25, 2.76, "10 Hz")
    edge(ax, 4.25, 2.14, 4.25, 1.76)
    edge(ax, 4.25, 1.14, 4.25, 0.76)

    legend_handles = [
        mpatches.Patch(color=PALETTE["mauve"], label="Sensor"),
        mpatches.Patch(color=PALETTE["teal"], label="Comms"),
        mpatches.Patch(color=PALETTE["deep_navy"], label="LLM / Dispatch / Motion"),
        mpatches.Patch(color=PALETTE["forest_green"], label="Robot Lead / Submitter"),
        mpatches.Patch(color=PALETTE["gold"], label="Physical / Swarm"),
        mpatches.Patch(color=PALETTE["burgundy"], label="Safety / Grader"),
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
        "Clinical-AI-Demos v0.8.0 / Demo 07 Adverse Event Response / Paper Figure 5",
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
