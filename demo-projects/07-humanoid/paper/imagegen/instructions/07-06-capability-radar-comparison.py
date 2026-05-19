"""Image 07-06: AE Response Capability Radar Comparison.

Letter portrait, 8.5 x 11.0 inches, 300 dpi. Radar chart with 8 axes and 4
polygons comparing the reference 3x H2 + per-site Claude Opus 4.7 1M
configuration against Atlas + Claude, Optimus + GPT, and a human on-call
network baseline.
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
    "gold": "#C18A2C",
    "forest_green": "#2F6B3E",
    "slate": "#4A5568",
    "mauve": "#8B6B8B",
    "light_gray": "#E2E8F0",
    "off_white": "#F7FAFC",
}

AXES = [
    "Per-Site AE-to-Bedside SLA\n(90 s target)",
    "Cross-Site Transit SLA\n(30 min target)",
    "HR 9505 1-Hour SLA\nAdherence",
    "CTCAE Grading Consistency\nAcross Sites",
    "H2 Outdoor IP65\nResilience",
    "Continental Coordination\nBus Latency",
    "Cross-Site Audit\nReconciliation Completeness",
    "Per-Site Cost\nEfficiency",
]

SERIES = [
    (
        "3x H2 EDU + Per-Site Claude Opus 4.7 1M (Reference)",
        [0.985, 0.92, 0.999, 0.97, 0.95, 0.82, 0.96, 0.88],
        PALETTE["deep_navy"],
        "solid",
    ),
    (
        "3x Atlas Electric + Per-Site Claude Opus 4.7 1M",
        [0.91, 0.88, 0.98, 0.93, 0.55, 0.95, 0.92, 0.72],
        PALETTE["teal"],
        "solid",
    ),
    (
        "3x Tesla Optimus Gen 3 + Per-Site GPT-5.5 Thinking",
        [0.83, 0.83, 0.93, 0.82, 0.55, 0.85, 0.78, 0.78],
        PALETTE["gold"],
        "solid",
    ),
    ("Human On-Call Network (Baseline)", [0.55, 0.61, 0.74, 0.55, 0.70, 0.40, 0.45, 0.62], PALETTE["slate"], "dashed"),
]


def main(out_path: pathlib.Path) -> None:
    fig = plt.figure(figsize=(8.5, 11.0), facecolor="white")
    fig.text(
        0.06,
        0.975,
        "3x H2 + Per-Site Claude Opus AE Response",
        fontsize=13.0,
        ha="left",
        color="black",
        fontweight="bold",
    )
    fig.text(
        0.06,
        0.957,
        "Capability Radar Comparison",
        fontsize=11.0,
        ha="left",
        color=PALETTE["slate"],
        fontweight="bold",
    )
    fig.text(
        0.06,
        0.940,
        "H2 + Claude vs. Atlas + Claude vs. Optimus + GPT vs. Human On-Call Baseline",
        fontsize=8.5,
        ha="left",
        color=PALETTE["slate"],
    )
    fig.text(0.94, 0.948, "Demo 07 / Image 06 of 10 / Portrait", fontsize=8.5, ha="right", color=PALETTE["slate"])

    n = len(AXES)
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
    angles += angles[:1]

    ax = fig.add_axes([0.12, 0.30, 0.76, 0.58], projection="polar")
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(AXES, fontsize=8.0, color="black")
    ax.tick_params(axis="x", pad=18)

    ax.set_ylim(0, 1.0)
    ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
    ax.set_yticklabels(["0.2", "0.4", "0.6", "0.8", "1.0"], fontsize=7.5, color=PALETTE["slate"])
    ax.set_rlabel_position(180 / n)
    ax.grid(color=PALETTE["light_gray"], lw=0.8)
    ax.spines["polar"].set_color(PALETTE["slate"])

    for ring in [0.2, 0.4, 0.6, 0.8]:
        ax.fill_between(
            np.linspace(0, 2 * np.pi, 100),
            ring - 0.005,
            ring + 0.005,
            color=PALETTE["light_gray"],
            alpha=0.15,
        )

    for label, values, color, style in SERIES:
        v = values + values[:1]
        ax.plot(angles, v, color=color, lw=2.0, ls="-" if style == "solid" else (0, (4, 2)), label=label, alpha=0.9)
        ax.fill(angles, v, color=color, alpha=0.10 if style == "solid" else 0.05)
        for a, val in zip(angles[:-1], values):
            ax.plot(a, val, "o", color=color, markersize=4.5, markeredgecolor="white", markeredgewidth=0.8)

    callout = (
        "Callout: H2 leads on Outdoor IP65 Resilience and Per-Site SLA.\n"
        "Atlas leads on Coordination Bus Latency. Human network only leads\n"
        "on adaptive cross-site escalation routing (not shown on radar)."
    )
    fig.text(
        0.5,
        0.215,
        callout,
        fontsize=8.0,
        color="black",
        ha="center",
        va="center",
        bbox=dict(boxstyle="round,pad=0.40", fc=PALETTE["off_white"], ec=PALETTE["slate"], lw=0.8),
    )

    legend_handles = []
    for label, values, color, style in SERIES:
        ls_p = "-" if style == "solid" else "--"
        legend_handles.append(plt.Line2D([0], [0], color=color, lw=2.0, ls=ls_p, marker="o", markersize=5, label=label))
    leg = fig.legend(
        handles=legend_handles,
        loc="lower center",
        bbox_to_anchor=(0.5, 0.08),
        ncol=1,
        fontsize=8.5,
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
