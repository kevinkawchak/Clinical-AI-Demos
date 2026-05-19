"""Image 07-01: 3x Unitree H2 + Per-Site Claude Opus 4.7 1M AE Response Architecture.

Letter landscape, 11.0 x 8.5 inches, 300 dpi, 3300 x 2550 pixels, white facecolor.
Renders a 4-site PAT-NET-001 architecture flowchart with per-site Claude Opus 4.7 1M
deployments, a continental coordination bus, 3 H2 humanoid silhouettes, and a
bottom SLA timeline. Single dashes only. Section sign for HIPAA references.
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
    "gold": "#C18A2C",
    "forest_green": "#2F6B3E",
    "slate": "#4A5568",
    "mauve": "#8B6B8B",
    "light_gray": "#E2E8F0",
    "off_white": "#F7FAFC",
    "pure_white": "#FFFFFF",
}

SITES = [
    ("San Francisco", "SF-01", "H2-A H2-B H2-C"),
    ("San Diego", "SD-01", "H2-D H2-E H2-F"),
    ("Boston", "BO-01", "H2-G H2-H H2-I"),
    ("Atlanta", "AT-01", "H2-J H2-K H2-L"),
]


def draw_h2_silhouette(ax, x, y, scale=1.0, color="#1F3A68"):
    head = plt.Circle((x, y + 0.32 * scale), 0.11 * scale, fc=color, ec="black", lw=0.6)
    body = mpatches.FancyBboxPatch(
        (x - 0.12 * scale, y - 0.20 * scale),
        0.24 * scale,
        0.40 * scale,
        boxstyle="round,pad=0.01",
        fc=color,
        ec="black",
        lw=0.6,
    )
    arm_l = plt.Rectangle(
        (x - 0.20 * scale, y - 0.05 * scale), 0.08 * scale, 0.25 * scale, fc=color, ec="black", lw=0.5
    )
    arm_r = plt.Rectangle(
        (x + 0.12 * scale, y - 0.05 * scale), 0.08 * scale, 0.25 * scale, fc=color, ec="black", lw=0.5
    )
    leg_l = plt.Rectangle(
        (x - 0.10 * scale, y - 0.50 * scale), 0.08 * scale, 0.30 * scale, fc=color, ec="black", lw=0.5
    )
    leg_r = plt.Rectangle(
        (x + 0.02 * scale, y - 0.50 * scale), 0.08 * scale, 0.30 * scale, fc=color, ec="black", lw=0.5
    )
    for p in [body, arm_l, arm_r, leg_l, leg_r]:
        ax.add_patch(p)
    ax.add_patch(head)


def draw_site_card(ax, x0, y0, width, height, site_name, site_id, robots, resident=True):
    card = FancyBboxPatch(
        (x0, y0),
        width,
        height,
        boxstyle="round,pad=0.02,rounding_size=0.08",
        fc=PALETTE["off_white"],
        ec=PALETTE["slate"],
        lw=1.5,
    )
    ax.add_patch(card)
    ax.text(
        x0 + width / 2,
        y0 + height - 0.16,
        site_name,
        ha="center",
        va="center",
        fontsize=10.5,
        fontweight="bold",
        color=PALETTE["slate"],
    )
    ax.text(
        x0 + width / 2,
        y0 + height - 0.32,
        f"Site {site_id}",
        ha="center",
        va="center",
        fontsize=7.5,
        color=PALETTE["slate"],
    )

    inner_x = x0 + 0.10
    inner_w = width - 0.20

    llm_y = y0 + height - 0.66
    ax.add_patch(
        FancyBboxPatch(
            (inner_x, llm_y), inner_w, 0.28, boxstyle="round,pad=0.01", fc=PALETTE["teal"], ec="black", lw=0.7
        )
    )
    ax.text(
        inner_x + inner_w / 2,
        llm_y + 0.14,
        "Claude Opus 4.7 1M On-Prem",
        ha="center",
        va="center",
        fontsize=7.8,
        color="white",
        fontweight="bold",
    )

    vit_y = llm_y - 0.36
    ax.add_patch(
        FancyBboxPatch(
            (inner_x, vit_y), inner_w, 0.28, boxstyle="round,pad=0.01", fc=PALETTE["mauve"], ec="black", lw=0.7
        )
    )
    ax.text(
        inner_x + inner_w / 2,
        vit_y + 0.14,
        "Patient Vitals + Sensor Mesh",
        ha="center",
        va="center",
        fontsize=7.0,
        color="white",
    )

    ae_y = vit_y - 0.36
    ax.add_patch(
        FancyBboxPatch(
            (inner_x, ae_y), inner_w, 0.28, boxstyle="round,pad=0.01", fc=PALETTE["burgundy"], ec="black", lw=0.7
        )
    )
    ax.text(
        inner_x + inner_w / 2,
        ae_y + 0.14,
        "AE Inbound: Staff, Patient, Family",
        ha="center",
        va="center",
        fontsize=6.8,
        color="white",
    )

    h2_y = ae_y - 0.52
    h2_color = PALETTE["deep_navy"] if resident else PALETTE["light_gray"]
    ax.add_patch(
        FancyBboxPatch(
            (inner_x, h2_y),
            inner_w,
            0.44,
            boxstyle="round,pad=0.01",
            fc=h2_color,
            ec="black",
            lw=0.7,
            alpha=1.0 if resident else 0.6,
        )
    )
    label = f"Unitree H2 (resident)\n{robots}" if resident else "H2 not resident (rotated)"
    ax.text(
        inner_x + inner_w / 2,
        h2_y + 0.22,
        label,
        ha="center",
        va="center",
        fontsize=6.8,
        color="white" if resident else PALETTE["slate"],
        fontweight="bold",
    )

    phys_y = h2_y - 0.36
    ax.add_patch(
        FancyBboxPatch((inner_x, phys_y), inner_w, 0.28, boxstyle="round,pad=0.01", fc="#5A1E2A", ec="black", lw=0.7)
    )
    ax.text(
        inner_x + inner_w / 2,
        phys_y + 0.14,
        "On-Call Physician + Sponsor (HR 9505)",
        ha="center",
        va="center",
        fontsize=6.5,
        color="white",
    )


def main(out_path: pathlib.Path) -> None:
    fig = plt.figure(figsize=(11.0, 8.5), facecolor="white")

    fig.text(
        0.06,
        0.965,
        "3x Unitree H2 + Per-Site Claude Opus 4.7 1M 24/7 Adverse Event Response Network",
        fontsize=15.5,
        ha="left",
        color="black",
        fontweight="bold",
    )
    fig.text(
        0.06,
        0.940,
        "PAT-NET-001 4-Site Continental Network: 168 Hours, 604,800 LLM Ticks at 1 Hz Per Site",
        fontsize=10.5,
        ha="left",
        color=PALETTE["slate"],
    )
    fig.text(0.94, 0.915, "Demo 07 / Image 01 of 10 / Landscape", fontsize=8.5, ha="right", color=PALETTE["slate"])

    ax = fig.add_axes([0.04, 0.105, 0.92, 0.79])
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 8.5)
    ax.set_axis_off()

    bus_y = 4.85
    ax.add_patch(
        FancyBboxPatch(
            (0.6, bus_y),
            9.8,
            0.55,
            boxstyle="round,pad=0.02,rounding_size=0.08",
            fc=PALETTE["slate"],
            ec="black",
            lw=1.2,
        )
    )
    ax.text(
        5.5,
        bus_y + 0.28,
        "Continental AE Coordination Bus (de-identified summaries only, 1 Hz sync)",
        ha="center",
        va="center",
        fontsize=10.5,
        color="white",
        fontweight="bold",
    )

    card_w = 2.30
    card_h = 2.85
    card_y = bus_y + 0.75
    card_xs = [0.55, 2.95, 5.35, 7.75]
    residency = [True, False, True, True]
    for (name, site_id, robots), x0, resident in zip(SITES, card_xs, residency):
        draw_site_card(ax, x0, card_y, card_w, card_h, name, site_id, robots, resident=resident)
        arrow = FancyArrowPatch(
            (x0 + card_w / 2, card_y),
            (x0 + card_w / 2, bus_y + 0.55),
            arrowstyle="-|>",
            mutation_scale=14,
            color=PALETTE["slate"],
            lw=1.5,
        )
        ax.add_patch(arrow)
        arrow2 = FancyArrowPatch(
            (x0 + card_w / 2 + 0.1, bus_y + 0.55),
            (x0 + card_w / 2 + 0.1, card_y),
            arrowstyle="-|>",
            mutation_scale=14,
            color=PALETTE["teal"],
            lw=1.3,
        )
        ax.add_patch(arrow2)

    for i, x in enumerate([2.5, 5.5, 8.5]):
        draw_h2_silhouette(ax, x, bus_y - 0.55, scale=0.9, color=PALETTE["deep_navy"])
        ax.text(x, bus_y - 1.15, f"H2-{i + 1} rotating", ha="center", fontsize=7.5, color=PALETTE["slate"])

    rot_text = (
        "H2 rotation balances load across 4 sites. Cross-site transit SLA under 30 min "
        "via FAA Part 135 medical drone or hospital charter aircraft."
    )
    ax.text(
        5.5,
        bus_y - 1.55,
        rot_text,
        ha="center",
        fontsize=8.0,
        color=PALETTE["slate"],
        style="italic",
    )

    sla_y = 1.20
    sla_top = 2.65
    ax.add_patch(
        FancyBboxPatch(
            (0.4, sla_y - 0.20),
            10.2,
            sla_top - sla_y + 0.45,
            boxstyle="round,pad=0.01,rounding_size=0.05",
            fc=PALETTE["off_white"],
            ec=PALETTE["slate"],
            lw=1.0,
        )
    )
    ax.text(
        0.55,
        sla_top + 0.10,
        "Service Level Agreements (logarithmic time axis, 0 to 60 min)",
        ha="left",
        fontsize=10,
        color=PALETTE["slate"],
        fontweight="bold",
    )

    axis_left = 1.50
    axis_right = 10.30
    bar_height = 0.28
    ticks = [(0, "0 s"), (0.0667, "90 s"), (0.20, "5 min"), (0.40, "15 min"), (0.50, "30 min"), (1.0, "60 min")]
    for frac, lbl in ticks:
        xt = axis_left + frac * (axis_right - axis_left)
        ax.plot([xt, xt], [sla_y, sla_y + 1.40], color=PALETTE["light_gray"], lw=0.7, zorder=0)
        ax.text(xt, sla_y - 0.21, lbl, ha="center", fontsize=7.5, color=PALETTE["slate"])

    site_bar_end = axis_left + 0.0667 * (axis_right - axis_left)
    ax.add_patch(
        plt.Rectangle(
            (axis_left, sla_y + 0.95),
            site_bar_end - axis_left,
            bar_height,
            fc=PALETTE["forest_green"],
            ec="black",
            lw=0.6,
        )
    )
    ax.text(
        axis_left,
        sla_y + 1.42,
        "Per-Site SLA: AE-to-Bedside under 90 s",
        ha="left",
        fontsize=8.5,
        color="black",
        fontweight="bold",
    )

    cross_bar_end = axis_left + 0.50 * (axis_right - axis_left)
    ax.add_patch(
        plt.Rectangle(
            (axis_left, sla_y + 0.50),
            cross_bar_end - axis_left,
            bar_height,
            fc=PALETTE["forest_green"],
            ec="black",
            lw=0.6,
            alpha=0.85,
        )
    )
    ax.text(
        axis_left,
        sla_y + 0.42,
        "Cross-Site SLA: Transit + Arrival under 30 min",
        ha="left",
        fontsize=8.5,
        color="black",
        fontweight="bold",
    )

    hr_bar_end = axis_left + 1.0 * (axis_right - axis_left)
    ax.add_patch(
        plt.Rectangle(
            (axis_left, sla_y + 0.05), hr_bar_end - axis_left, bar_height, fc=PALETTE["burgundy"], ec="black", lw=0.6
        )
    )
    ax.text(
        axis_left,
        sla_y - 0.06,
        "HR 9505 SLA: CTCAE Grading + Sponsor Ack within 1 hour",
        ha="left",
        fontsize=8.5,
        color="black",
        fontweight="bold",
    )

    note_text = "No PHI leaves a site boundary. Each site retains independent IRB review."
    ax.text(
        5.5, sla_top + 0.30, note_text, ha="center", va="bottom", fontsize=8.5, color=PALETTE["slate"], style="italic"
    )

    legend_handles = [
        mpatches.Patch(color=PALETTE["teal"], label="Per-Site LLM (Claude Opus 4.7 1M)"),
        mpatches.Patch(color=PALETTE["mauve"], label="Patient Vitals / Sensor"),
        mpatches.Patch(color=PALETTE["burgundy"], label="AE Inbound / On-Call"),
        mpatches.Patch(color=PALETTE["deep_navy"], label="Unitree H2 EDU"),
        mpatches.Patch(color=PALETTE["forest_green"], label="On-Time SLA Band"),
        mpatches.Patch(color=PALETTE["slate"], label="Coordination Bus"),
    ]
    leg = fig.legend(
        handles=legend_handles,
        loc="lower center",
        bbox_to_anchor=(0.5, 0.048),
        fontsize=7.8,
        ncol=6,
        framealpha=0.95,
        edgecolor=PALETTE["slate"],
    )
    leg.get_frame().set_facecolor("white")

    fig.text(
        0.06,
        0.012,
        "Clinical-AI-Demos v0.8.0 / Demo 07 Adverse Event Response",
        fontsize=8,
        ha="left",
        color=PALETTE["slate"],
    )
    fig.text(0.94, 0.012, "DOI: 10.5281/zenodo.18445179 / MIT License", fontsize=8, ha="right", color=PALETTE["slate"])

    fig.savefig(out_path, dpi=300, facecolor="white", bbox_inches=None)
    plt.close(fig)


if __name__ == "__main__":
    out = pathlib.Path(__file__).with_suffix(".png")
    main(out)
    print(f"Saved {out}")
