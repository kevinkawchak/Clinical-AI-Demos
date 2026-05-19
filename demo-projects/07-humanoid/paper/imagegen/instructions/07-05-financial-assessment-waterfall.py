"""Image 07-05: AE Response Network 5-Year TCO Waterfall.

Letter portrait, 8.5 x 11.0 inches, 300 dpi. Vertical waterfall with 16 bars
covering the network-wide 5-year total cost of ownership for the 3x H2 +
Per-Site Claude Opus 4-Site PAT-NET-001 deployment. USD thousands.
"""

from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("Agg")

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

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

BARS = [
    ("Year 0 Baseline Human On-Call x 4 Sites", 7800, "absolute", PALETTE["slate"]),
    ("+ 3x H2 Acquisition", 1080, "positive", PALETTE["deep_navy"]),
    ("+ 3x H2 5-Year Service Contract", 540, "positive", PALETTE["deep_navy"]),
    ("+ 4x Claude Opus 4.7 1M Per-Site Clusters", 2200, "positive", PALETTE["teal"]),
    ("+ Continental Coordination Bus Infra", 380, "positive", PALETTE["mauve"]),
    ("+ FAA Part 135 Drone Subscription", 240, "positive", PALETTE["mauve_dk"]),
    ("+ Hospital Charter Aircraft Reserve", 320, "positive", PALETTE["gold"]),
    ("+ Per-Site IRB Coordination Overhead", 280, "positive", PALETTE["burgundy"]),
    ("- Human Night-Shift Wage Offset", -3200, "negative", PALETTE["forest_green"]),
    ("- SAE Narrative Cycle Time Offset", -1450, "negative", PALETTE["forest_green"]),
    ("- HR 9505 SLA Penalty Avoidance", -3850, "negative", PALETTE["forest_green"]),
    ("- Cross-Site Audit Reconciliation Offset", -1280, "negative", PALETTE["forest_green"]),
    ("+ Annual O&M + Spare Parts (Per H2)", 720, "positive", PALETTE["gold"]),
    ("+ Cyber and HIPAA Audit Reserve", 420, "positive", PALETTE["burgundy"]),
    ("+ FDA RTCT Submission Bandwidth", 180, "positive", PALETTE["slate"]),
    ("Cumulative 5-Year Network TCO", None, "total", PALETTE["deep_navy"]),
]


def main(out_path: pathlib.Path) -> None:
    fig = plt.figure(figsize=(8.5, 11.0), facecolor="white")
    fig.text(
        0.06,
        0.975,
        "3x H2 + Per-Site Claude Opus 4-Site Network",
        fontsize=12.0,
        ha="left",
        color="black",
        fontweight="bold",
    )
    fig.text(
        0.06,
        0.957,
        "5-Year TCO Waterfall",
        fontsize=11.0,
        ha="left",
        color=PALETTE["slate"],
        fontweight="bold",
    )
    fig.text(
        0.06,
        0.940,
        "PAT-NET-001 24/7 AE Response, USD Thousands",
        fontsize=9.0,
        ha="left",
        color=PALETTE["slate"],
    )
    fig.text(0.94, 0.948, "Demo 07 / Image 05 of 10 / Portrait", fontsize=8.5, ha="right", color=PALETTE["slate"])

    ax = fig.add_axes([0.36, 0.115, 0.59, 0.79])
    ax.set_facecolor("white")

    n = len(BARS)
    running = 0.0
    max_running = 0.0
    bar_h = 0.74
    bar_centers = []
    prev_running = 0.0
    for i, (label, val, kind, color) in enumerate(BARS):
        y = i
        bar_centers.append(y)
        if kind == "absolute":
            ax.barh(y, val, height=bar_h, color=color, ec="black", lw=0.6, left=0)
            running = val
            ax.text(val + 120, y, f"${val:,}k", ha="left", va="center", fontsize=8.0, fontweight="bold")
        elif kind == "positive":
            ax.barh(y, val, height=bar_h, color=color, ec="black", lw=0.6, left=running)
            ax.text(running + val + 120, y, f"+${val:,}k", ha="left", va="center", fontsize=7.6, color=PALETTE["slate"])
            running += val
        elif kind == "negative":
            ax.barh(y, val, height=bar_h, color=color, ec="black", lw=0.6, left=running)
            ax.text(
                running + val - 120,
                y,
                f"-${-val:,}k",
                ha="right",
                va="center",
                fontsize=7.6,
                color=PALETTE["forest_green"],
                fontweight="bold",
            )
            running += val
        elif kind == "total":
            ax.barh(y, running, height=bar_h, color=color, ec="black", lw=1.2, left=0)
            ax.text(
                running + 120,
                y,
                f"${running:,.0f}k",
                ha="left",
                va="center",
                fontsize=9.0,
                fontweight="bold",
                color="black",
            )

        if kind in ("positive", "negative") and i > 0:
            ax.plot(
                [prev_running, prev_running],
                [y - bar_h / 2, y - 1 + bar_h / 2],
                color=PALETTE["slate"],
                lw=0.5,
                ls=":",
            )
        prev_running = running
        max_running = max(max_running, running)

    ax.axvline(BARS[0][1], color=PALETTE["slate"], lw=1.0, ls="--", alpha=0.6)
    ax.text(BARS[0][1] + 60, -0.5, "Baseline", fontsize=7.5, color=PALETTE["slate"], rotation=0, va="bottom")

    ax.set_yticks(bar_centers)
    ax.set_yticklabels([b[0] for b in BARS], fontsize=7.8, color="black")
    ax.invert_yaxis()
    ax.set_xlabel("USD Thousands (5-Year Network-Wide)", fontsize=9.5, color=PALETTE["slate"])
    ax.set_xlim(0, max_running * 1.18)
    ax.tick_params(axis="x", labelsize=8.0)
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    ax.spines["left"].set_color(PALETTE["slate"])
    ax.spines["bottom"].set_color(PALETTE["slate"])
    ax.grid(axis="x", color=PALETTE["light_gray"], lw=0.5, zorder=0)
    ax.set_axisbelow(True)

    callout = (
        "Callout: HR 9505 SLA penalty avoidance alone justifies the per-site Claude Opus cluster cost. "
        "Cross-site audit reconciliation offset is the second largest contributor."
    )
    fig.text(
        0.5,
        0.062,
        callout,
        fontsize=7.5,
        color="black",
        ha="center",
        va="center",
        wrap=True,
        bbox=dict(boxstyle="round,pad=0.45", fc=PALETTE["off_white"], ec=PALETTE["forest_green"], lw=1.0),
    )

    legend_handles = [
        mpatches.Patch(color=PALETTE["slate"], label="Baseline / Audit"),
        mpatches.Patch(color=PALETTE["deep_navy"], label="H2 Capex / Total"),
        mpatches.Patch(color=PALETTE["teal"], label="LLM Compute"),
        mpatches.Patch(color=PALETTE["mauve"], label="Coordination Bus"),
        mpatches.Patch(color=PALETTE["mauve_dk"], label="Drone Subscription"),
        mpatches.Patch(color=PALETTE["gold"], label="Charter / O&M"),
        mpatches.Patch(color=PALETTE["burgundy"], label="IRB / Cyber"),
        mpatches.Patch(color=PALETTE["forest_green"], label="Cost Offset (negative)"),
    ]
    leg = fig.legend(
        handles=legend_handles,
        loc="lower center",
        bbox_to_anchor=(0.5, 0.018),
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
