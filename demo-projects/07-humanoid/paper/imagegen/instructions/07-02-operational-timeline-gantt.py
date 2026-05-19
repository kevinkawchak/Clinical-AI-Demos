"""Image 07-02: H2 168-Hour 4-Site AE Response Weekly Gantt.

Letter landscape, 11.0 x 8.5 inches, 300 dpi. 9 task swimlanes + 4 per-site
Claude Opus overlay rows. Night windows highlighted, daily separators, pinned
annotations at Wed 14:00 and Fri 10:00.
"""

from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("Agg")

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

PALETTE = {
    "deep_navy": "#1F3A68",
    "deep_navy_lt": "#3F5A88",
    "deep_navy_md": "#2F4A78",
    "teal": "#2E8B8B",
    "teal_lt": "#5EBBBB",
    "teal_dk": "#1E6B6B",
    "teal_md": "#3F9C9C",
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


def main(out_path: pathlib.Path) -> None:
    rng = np.random.default_rng(2026)
    fig = plt.figure(figsize=(11.0, 8.5), facecolor="white")

    fig.text(
        0.06,
        0.965,
        "3x Unitree H2 + Per-Site Claude Opus 4.7 1M 168-Hour Weekly Gantt",
        fontsize=15.5,
        ha="left",
        color="black",
        fontweight="bold",
    )
    fig.text(
        0.06,
        0.940,
        "PAT-NET-001 4-Site Network: 604,800 LLM Ticks Per Site, Cross-Site Rotation Schedule",
        fontsize=10.5,
        ha="left",
        color=PALETTE["slate"],
    )
    fig.text(
        0.94,
        0.915,
        "Demo 07 / Image 02 of 10 / Landscape",
        fontsize=8.5,
        ha="right",
        color=PALETTE["slate"],
    )

    ax = fig.add_axes([0.20, 0.13, 0.76, 0.73])
    ax.set_xlim(0, 168)
    ax.set_facecolor("white")

    lanes = [
        ("Claude Opus 4.7 1M SF-01", PALETTE["teal"], "llm"),
        ("Claude Opus 4.7 1M SD-01", PALETTE["teal_lt"], "llm"),
        ("Claude Opus 4.7 1M BO-01", PALETTE["teal_dk"], "llm"),
        ("Claude Opus 4.7 1M AT-01", PALETTE["teal_md"], "llm"),
        ("H2-1 Rotation Schedule", PALETTE["deep_navy"], "rotation"),
        ("H2-2 Rotation Schedule", PALETTE["deep_navy_lt"], "rotation"),
        ("H2-3 Rotation Schedule", PALETTE["deep_navy_md"], "rotation"),
        ("AE Events Detected (CTCAE)", PALETTE["burgundy"], "ae"),
        ("Cross-Site Transit (Drone / Charter)", PALETTE["mauve"], "transit"),
        ("H2 Battery Hot-Swap (5h cycle)", PALETTE["slate"], "battery"),
        ("On-Call Physician (HR 9505)", PALETTE["burgundy_dk"], "phys"),
        ("Sponsor Acknowledgment (HR 9505 1h)", PALETTE["gold"], "sponsor"),
        ("Cross-Site Audit Reconciliation", PALETTE["forest_green"], "audit"),
    ]
    n = len(lanes)
    lane_height = 0.78

    for d in range(8):
        x = d * 24
        ax.axvline(x, color=PALETTE["light_gray"], lw=0.8, zorder=0)
    for d in range(7):
        night_start = d * 24 + 22
        night_end = (d + 1) * 24 + 6
        ax.add_patch(
            plt.Rectangle(
                (night_start, -0.5),
                night_end - night_start,
                n + 0.5,
                fc=PALETTE["light_gray"],
                ec="none",
                alpha=0.35,
                zorder=0,
            )
        )

    for i, (label, color, kind) in enumerate(lanes):
        y = n - 1 - i
        ax.text(
            -2.5,
            y + lane_height / 2,
            label,
            ha="right",
            va="center",
            fontsize=8.0,
            color="black",
        )
        if kind == "llm":
            for d in range(7):
                for tick in np.linspace(d * 24 + 0.5, d * 24 + 23.5, 12):
                    ax.plot(
                        [tick, tick],
                        [y + 0.10, y + 0.68],
                        color=color,
                        lw=0.7,
                        alpha=0.85,
                    )
        elif kind == "rotation":
            site_cycle = [PALETTE["deep_navy"], PALETTE["teal"], PALETTE["forest_green"], PALETTE["mauve"]]
            seg_h = 24
            offset = (i - 4) * 6
            for seg in range(7):
                start = seg * seg_h
                color_seg = site_cycle[(seg + offset // 6) % 4]
                ax.add_patch(
                    plt.Rectangle((start, y + 0.20), seg_h - 1, 0.50, fc=color_seg, ec="black", lw=0.4, alpha=0.85)
                )
                if seg % 2 == 0:
                    ax.text(
                        start + seg_h / 2,
                        y + 0.45,
                        ["SF", "SD", "BO", "AT"][(seg + offset // 6) % 4],
                        ha="center",
                        va="center",
                        fontsize=6.5,
                        color="white",
                        fontweight="bold",
                    )
        elif kind == "ae":
            event_times = rng.uniform(0, 168, size=72)
            grades = rng.choice([1, 2, 3, 4], size=72, p=[0.45, 0.30, 0.18, 0.07])
            color_by_grade = {
                1: PALETTE["forest_green"],
                2: PALETTE["gold"],
                3: PALETTE["burgundy"],
                4: PALETTE["burgundy_dk"],
            }
            for t, g in zip(event_times, grades):
                ax.add_patch(plt.Rectangle((t, y + 0.20 + (g - 1) * 0.10), 0.6, 0.10, fc=color_by_grade[g], ec="none"))
            ax.text(170, y + 0.40, "G1-G4", fontsize=6.5, color=PALETTE["slate"], va="center")
        elif kind == "transit":
            transit_starts = [38, 92, 130]
            transit_dur = [0.5, 0.45, 0.55]
            for s, dur in zip(transit_starts, transit_dur):
                ax.add_patch(plt.Rectangle((s, y + 0.20), dur, 0.50, fc=color, ec="black", lw=0.5))
        elif kind == "battery":
            for hour in range(0, 168, 5):
                ax.add_patch(plt.Rectangle((hour, y + 0.20), 0.25, 0.50, fc=color, ec="none"))
        elif kind == "phys":
            phys_times = rng.uniform(0, 168, size=28)
            for t in phys_times:
                ax.add_patch(plt.Rectangle((t, y + 0.20), 0.8, 0.50, fc=color, ec="none", alpha=0.85))
        elif kind == "sponsor":
            for hour in range(2, 168, 4):
                ax.add_patch(plt.Rectangle((hour, y + 0.20), 1.0, 0.50, fc=color, ec="black", lw=0.3, alpha=0.85))
        elif kind == "audit":
            for hour in range(0, 168, 24):
                ax.add_patch(plt.Rectangle((hour + 22, y + 0.20), 2.0, 0.50, fc=color, ec="black", lw=0.4))

    ax.set_ylim(-0.5, 15.5)
    ax.set_yticks([])

    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    ax.set_xticks([d * 24 + 12 for d in range(7)])
    ax.set_xticklabels(days, fontsize=9.5, fontweight="bold")
    ax.tick_params(axis="x", which="major", length=0)
    sec = ax.secondary_xaxis("top")
    sec.set_xticks([d * 24 for d in range(8)])
    sec.set_xticklabels([f"{(d * 24) % 168:d}h" for d in range(8)], fontsize=7.5, color=PALETTE["slate"])
    sec.tick_params(axis="x", which="major", length=3)

    for spine in ["top", "right", "left"]:
        ax.spines[spine].set_visible(False)
    ax.spines["bottom"].set_color(PALETTE["slate"])

    wed_x = 2 * 24 + 14
    ax.annotate(
        "Mid-week peak AE detection.\nCross-site transit triggered SF to LA.",
        xy=(wed_x, 13.0),
        xytext=(6, 14.6),
        fontsize=7.8,
        color=PALETTE["burgundy_dk"],
        ha="left",
        va="center",
        arrowprops=dict(arrowstyle="->", color=PALETTE["burgundy_dk"], lw=1.0),
        bbox=dict(boxstyle="round,pad=0.3", fc=PALETTE["off_white"], ec=PALETTE["burgundy_dk"], lw=0.8),
    )
    fri_x = 4 * 24 + 10
    ax.annotate(
        "Sponsor mid-week DSMB digest.\nAll CTCAE Grade 3+ events reviewed.",
        xy=(fri_x, 13.0),
        xytext=(104, 14.6),
        fontsize=7.8,
        color=PALETTE["gold"],
        ha="left",
        va="center",
        arrowprops=dict(arrowstyle="->", color=PALETTE["gold"], lw=1.0),
        bbox=dict(boxstyle="round,pad=0.3", fc=PALETTE["off_white"], ec=PALETTE["gold"], lw=0.8),
    )

    legend_handles = [
        mpatches.Patch(color=PALETTE["teal"], label="Per-Site Claude Opus tick (1 Hz)"),
        mpatches.Patch(color=PALETTE["deep_navy"], label="H2 Rotation Assignment"),
        mpatches.Patch(color=PALETTE["forest_green"], label="CTCAE Grade 1 / Audit"),
        mpatches.Patch(color=PALETTE["gold"], label="CTCAE Grade 2 / Sponsor cycle"),
        mpatches.Patch(color=PALETTE["burgundy"], label="CTCAE Grade 3 / Physician"),
        mpatches.Patch(color=PALETTE["burgundy_dk"], label="CTCAE Grade 4"),
        mpatches.Patch(color=PALETTE["mauve"], label="Cross-Site Transit"),
        mpatches.Patch(color=PALETTE["slate"], label="Battery Hot-Swap"),
        mpatches.Patch(color=PALETTE["light_gray"], label="Night Window 22:00 to 06:00"),
    ]
    leg = fig.legend(
        handles=legend_handles,
        loc="lower center",
        bbox_to_anchor=(0.5, 0.02),
        ncol=5,
        fontsize=7.8,
        framealpha=0.95,
        edgecolor=PALETTE["slate"],
    )
    leg.get_frame().set_facecolor("white")

    fig.text(
        0.06,
        0.06,
        "Clinical-AI-Demos v0.8.0 / Demo 07 Adverse Event Response",
        fontsize=7.5,
        ha="left",
        color=PALETTE["slate"],
    )
    fig.text(0.94, 0.06, "DOI: 10.5281/zenodo.18445179 / MIT License", fontsize=7.5, ha="right", color=PALETTE["slate"])

    fig.savefig(out_path, dpi=300, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    out = pathlib.Path(__file__).with_suffix(".png")
    main(out)
    print(f"Saved {out}")
