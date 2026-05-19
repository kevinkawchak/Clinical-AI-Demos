"""Figure 1 replacement: PAT-NET-001 Continental Adverse Event Response Network.

Landscape full-page, 11.0 x 8.5 inches, 300 dpi. Shows the 4-site continental
network (San Francisco, San Diego, Boston, Atlanta) with the cross-site
coordination bus and a single-site swarm layout with the Lead, Assist, and
Reserve roles for the 3 Unitree H2 EDU robots. Replaces the verbatim ASCII
figure that previously appeared in introduction.tex.
"""

from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("Agg")

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch

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
    ("San Francisco", "SF-01", "H2-A H2-B H2-C", 0.55, 1.50, "Lead H2-A"),
    ("San Diego", "SD-01", "H2-D H2-E H2-F", 3.20, 1.50, "Lead H2-D"),
    ("Boston", "BO-01", "H2-G H2-H H2-I", 5.85, 1.50, "Lead H2-G"),
    ("Atlanta", "AT-01", "H2-J H2-K H2-L", 8.50, 1.50, "Lead H2-J"),
]


def draw_site_card(ax, x0, y0, name, site_id, robots):
    w, h = 2.10, 2.35
    ax.add_patch(
        FancyBboxPatch(
            (x0, y0),
            w,
            h,
            boxstyle="round,pad=0.04,rounding_size=0.10",
            fc=PALETTE["off_white"],
            ec=PALETTE["slate"],
            lw=1.4,
        )
    )
    ax.text(x0 + w / 2, y0 + h - 0.20, name, ha="center", fontsize=10.5, color=PALETTE["slate"], fontweight="bold")
    ax.text(x0 + w / 2, y0 + h - 0.40, f"Site {site_id}", ha="center", fontsize=8.0, color=PALETTE["slate"])

    llm_y = y0 + h - 0.78
    ax.add_patch(
        FancyBboxPatch(
            (x0 + 0.10, llm_y),
            w - 0.20,
            0.30,
            boxstyle="round,pad=0.01",
            fc=PALETTE["teal"],
            ec="black",
            lw=0.7,
        )
    )
    ax.text(
        x0 + w / 2,
        llm_y + 0.15,
        "Claude Opus 4.7 1M (on-prem)",
        ha="center",
        va="center",
        fontsize=7.5,
        color="white",
        fontweight="bold",
    )

    bus_y = llm_y - 0.36
    ax.add_patch(
        FancyBboxPatch(
            (x0 + 0.10, bus_y),
            w - 0.20,
            0.26,
            boxstyle="round,pad=0.01",
            fc=PALETTE["slate"],
            ec="black",
            lw=0.7,
        )
    )
    ax.text(x0 + w / 2, bus_y + 0.13, "Broadcast Bus 1 Hz", ha="center", va="center", fontsize=7.0, color="white")

    robot_y = bus_y - 0.55
    robot_w = (w - 0.40) / 3
    role_labels = ["Lead", "Assist", "Reserve"]
    role_colors = [PALETTE["deep_navy"], PALETTE["teal"], PALETTE["forest_green"]]
    ids = robots.split()
    for i, (rid, role, color) in enumerate(zip(ids, role_labels, role_colors)):
        rx = x0 + 0.10 + i * robot_w + i * 0.05
        ax.add_patch(
            FancyBboxPatch(
                (rx, robot_y),
                robot_w,
                0.42,
                boxstyle="round,pad=0.01",
                fc=color,
                ec="black",
                lw=0.6,
            )
        )
        ax.text(
            rx + robot_w / 2,
            robot_y + 0.28,
            rid,
            ha="center",
            va="center",
            fontsize=7.0,
            color="white",
            fontweight="bold",
        )
        ax.text(rx + robot_w / 2, robot_y + 0.10, role, ha="center", va="center", fontsize=6.5, color="white")

    note_y = robot_y - 0.32
    ax.text(
        x0 + w / 2,
        note_y,
        "Roles rotate at every 1 Hz tick",
        ha="center",
        fontsize=6.8,
        color=PALETTE["slate"],
        style="italic",
    )


def main(out_path: pathlib.Path) -> None:
    fig = plt.figure(figsize=(11.0, 8.5), facecolor="white")
    fig.text(
        0.05,
        0.965,
        "PAT-NET-001 Continental Adverse Event Response Network",
        fontsize=15.0,
        ha="left",
        color="black",
        fontweight="bold",
    )
    fig.text(
        0.05,
        0.940,
        "4 sites, 12 Unitree H2 EDU robots, 4 on-prem Claude Opus 4.7 1M deployments, 1 Hz LLM broadcast cadence",
        fontsize=10.0,
        ha="left",
        color=PALETTE["slate"],
    )
    fig.text(0.95, 0.915, "Figure 1 / Paper Figure Replacement", fontsize=8.5, ha="right", color=PALETTE["slate"])

    ax = fig.add_axes([0.03, 0.07, 0.94, 0.84])
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 8.5)
    ax.set_axis_off()

    bus_y_main = 5.45
    ax.add_patch(
        FancyBboxPatch(
            (0.45, bus_y_main),
            10.10,
            0.55,
            boxstyle="round,pad=0.02,rounding_size=0.10",
            fc=PALETTE["slate"],
            ec="black",
            lw=1.2,
        )
    )
    ax.text(
        5.5,
        bus_y_main + 0.28,
        "Cross Site Coordination Bus (de-identified hourly summaries only)",
        ha="center",
        va="center",
        fontsize=11.0,
        color="white",
        fontweight="bold",
    )

    for name, site_id, robots, x, y, lead in SITES:
        draw_site_card(ax, x, y, name, site_id, robots)
        arrow_up = FancyArrowPatch(
            (x + 1.05, y + 2.35),
            (x + 1.05, bus_y_main),
            arrowstyle="<|-|>",
            mutation_scale=14,
            color=PALETTE["slate"],
            lw=1.4,
        )
        ax.add_patch(arrow_up)

    legend_lines = [
        ("Inter robot: 60 GHz UWB peer mesh + IR beacon line-of-sight", PALETTE["forest_green"]),
        ("LLM to robot: 1 Hz broadcast publish-subscribe", PALETTE["teal"]),
        ("Cross site: de-identified hourly summaries only (no PHI)", PALETTE["slate"]),
        ("Platform: Unitree H2 EDU; compute slot upgradeable to Jetson AGX Thor 2070 TOPS", PALETTE["deep_navy"]),
    ]
    note_box = FancyBboxPatch(
        (0.45, 6.30),
        10.10,
        1.55,
        boxstyle="round,pad=0.02,rounding_size=0.08",
        fc=PALETTE["off_white"],
        ec=PALETTE["slate"],
        lw=1.0,
    )
    ax.add_patch(note_box)
    ax.text(0.65, 7.62, "Network Conventions", fontsize=10.0, color=PALETTE["slate"], fontweight="bold")
    for i, (line, color) in enumerate(legend_lines):
        cy = 7.40 - i * 0.25
        ax.add_patch(Circle((0.80, cy + 0.05), 0.07, fc=color, ec="black", lw=0.4))
        ax.text(0.95, cy + 0.05, line, fontsize=8.5, va="center", color="black")

    legend_handles = [
        mpatches.Patch(color=PALETTE["teal"], label="Per-Site LLM"),
        mpatches.Patch(color=PALETTE["slate"], label="Broadcast Bus"),
        mpatches.Patch(color=PALETTE["deep_navy"], label="Lead H2"),
        mpatches.Patch(color=PALETTE["teal"], label="Assist H2"),
        mpatches.Patch(color=PALETTE["forest_green"], label="Reserve H2"),
    ]
    leg = fig.legend(
        handles=legend_handles,
        loc="lower center",
        bbox_to_anchor=(0.5, 0.025),
        ncol=5,
        fontsize=8.0,
        framealpha=0.95,
        edgecolor=PALETTE["slate"],
    )
    leg.get_frame().set_facecolor("white")

    fig.text(
        0.05,
        0.005,
        "Clinical-AI-Demos v0.8.0 / Demo 07 Adverse Event Response / Paper Figure 1",
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
