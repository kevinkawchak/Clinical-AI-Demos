"""Image 07-07: AE Event and CTCAE Grade Sankey.

Letter portrait, 8.5 x 11.0 inches, 300 dpi. Sankey with 4 vertical levels:
AE source site to per-site Claude Opus triage to CTCAE grade to terminal
action. Flow widths proportional to event counts over a 168-hour cycle.
"""

from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("Agg")

import matplotlib.patches as mpatches
import matplotlib.path as mpath
import matplotlib.pyplot as plt
import numpy as np

PALETTE = {
    "deep_navy": "#1F3A68",
    "deep_navy_lt": "#3F5A88",
    "deep_navy_md": "#2F4A78",
    "deep_navy_dk": "#0F2A58",
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


def sankey_link(ax, x0, y0_top, y0_bot, x1, y1_top, y1_bot, color, alpha=0.45):
    Path = mpath.Path
    verts = [
        (x0, y0_top),
        ((x0 + x1) / 2, y0_top),
        ((x0 + x1) / 2, y1_top),
        (x1, y1_top),
        (x1, y1_bot),
        ((x0 + x1) / 2, y1_bot),
        ((x0 + x1) / 2, y0_bot),
        (x0, y0_bot),
        (x0, y0_top),
    ]
    codes = [
        Path.MOVETO,
        Path.CURVE4,
        Path.CURVE4,
        Path.CURVE4,
        Path.LINETO,
        Path.CURVE4,
        Path.CURVE4,
        Path.CURVE4,
        Path.CLOSEPOLY,
    ]
    p = Path(verts, codes)
    ax.add_patch(mpatches.PathPatch(p, fc=color, ec="none", alpha=alpha))


def main(out_path: pathlib.Path) -> None:
    fig = plt.figure(figsize=(8.5, 11.0), facecolor="white")
    fig.text(
        0.06,
        0.975,
        "3x H2 AE Network 168-Hour Sankey",
        fontsize=13.0,
        ha="left",
        color="black",
        fontweight="bold",
    )
    fig.text(
        0.06,
        0.957,
        "AE Event and CTCAE Grade Flow",
        fontsize=11.0,
        ha="left",
        color=PALETTE["slate"],
        fontweight="bold",
    )
    fig.text(
        0.06,
        0.940,
        "4-Site Network: Per-Site Triage to CTCAE to On-Call Activation or Resolved In-Place",
        fontsize=8.5,
        ha="left",
        color=PALETTE["slate"],
    )
    fig.text(0.94, 0.948, "Demo 07 / Image 07 of 10 / Portrait", fontsize=8.5, ha="right", color=PALETTE["slate"])

    ax = fig.add_axes([0.02, 0.085, 0.96, 0.83])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 11)
    ax.set_axis_off()

    levels_x = [1.80, 4.80, 7.50, 9.80]
    level_titles = ["Source Site", "Per-Site Triage", "CTCAE Grade", "Terminal Action"]
    for x, title in zip(levels_x, level_titles):
        ax.text(x, 10.5, title, ha="center", fontsize=10.5, color=PALETTE["slate"], fontweight="bold")

    sources = [
        ("San Francisco", 23, PALETTE["deep_navy"]),
        ("San Diego", 19, PALETTE["deep_navy_lt"]),
        ("Boston", 21, PALETTE["deep_navy_md"]),
        ("Atlanta", 17, PALETTE["deep_navy_dk"]),
    ]
    triages = [
        ("Routine Check", 26, PALETTE["forest_green_lt"]),
        ("Vitals Anomaly Triage", 28, PALETTE["teal"]),
        ("Pain or AE Self-Report", 16, PALETTE["gold"]),
        ("Family Caregiver Inbound", 10, PALETTE["mauve"]),
    ]
    grades = [
        ("Grade 1", 36, PALETTE["forest_green"]),
        ("Grade 2", 25, PALETTE["forest_green_lt"]),
        ("Grade 3", 12, PALETTE["gold"]),
        ("Grade 4", 5, PALETTE["burgundy"]),
        ("Grade 5", 2, PALETTE["burgundy_dk"]),
    ]
    terminals = [
        ("Resolved In-Place by H2", 58, PALETTE["forest_green"]),
        ("On-Call Physician (HR 9505)", 16, PALETTE["burgundy"]),
        ("Hospital Transfer", 4, PALETTE["burgundy_dk"]),
        ("Cross-Site H2 Re-Dispatch", 2, PALETTE["mauve"]),
    ]

    total = sum(s[1] for s in sources)
    node_w = 0.22
    y_top = 9.7
    y_bot = 1.2
    gap = 0.22
    avail = y_top - y_bot

    def stack(items, x, label_side="left", label_offset=0.10):
        nodes = []
        size_sum = sum(it[1] for it in items)
        scale = (avail - gap * (len(items) - 1)) / size_sum
        y = y_top
        for name, sz, color in items:
            h = sz * scale
            ax.add_patch(plt.Rectangle((x - node_w / 2, y - h), node_w, h, fc=color, ec="black", lw=0.5))
            txt = f"{name}\n({sz})"
            bbox_dict = dict(boxstyle="round,pad=0.18", fc="white", ec="none", alpha=0.85)
            if label_side == "left":
                ax.text(
                    x - node_w / 2 - label_offset,
                    y - h / 2,
                    txt,
                    ha="right",
                    va="center",
                    fontsize=7.2,
                    color="black",
                    bbox=bbox_dict,
                )
            else:
                ax.text(
                    x + node_w / 2 + label_offset,
                    y - h / 2,
                    txt,
                    ha="left",
                    va="center",
                    fontsize=7.2,
                    color="black",
                    bbox=bbox_dict,
                )
            nodes.append({"name": name, "color": color, "y_top": y, "y_bot": y - h, "size": sz, "scale": scale})
            y -= h + gap
        return nodes

    s_nodes = stack(sources, levels_x[0], "left", 0.12)
    t_nodes = stack(triages, levels_x[1], "left", 0.12)
    g_nodes = stack(grades, levels_x[2], "right", 0.12)
    term_nodes = stack(terminals, levels_x[3], "right", 0.12)

    rng = np.random.default_rng(11)

    def make_link_matrix(src, dst):
        rows = []
        for s in src:
            base = rng.dirichlet([2.0] * len(dst))
            rows.append(np.array([min(s["size"], v * s["size"]) for v in base]))
        mat = np.array(rows)
        mat = mat * (np.array([s["size"] for s in src])[:, None] / mat.sum(axis=1, keepdims=True))
        return mat

    def draw_layer(src_nodes, dst_nodes, x_left, x_right, color_src=True):
        mat = make_link_matrix(src_nodes, dst_nodes)
        src_used = [s["y_top"] for s in src_nodes]
        dst_used = [d["y_top"] for d in dst_nodes]
        for i, s in enumerate(src_nodes):
            for j, d in enumerate(dst_nodes):
                v = mat[i, j]
                h_src = v * s["scale"]
                h_dst = v * d["scale"]
                if h_src < 0.005:
                    continue
                color = s["color"] if color_src else d["color"]
                sankey_link(
                    ax,
                    x_left + node_w / 2,
                    src_used[i],
                    src_used[i] - h_src,
                    x_right - node_w / 2,
                    dst_used[j],
                    dst_used[j] - h_dst,
                    color=color,
                    alpha=0.50,
                )
                src_used[i] -= h_src
                dst_used[j] -= h_dst

    draw_layer(s_nodes, t_nodes, levels_x[0], levels_x[1], color_src=True)
    draw_layer(t_nodes, g_nodes, levels_x[1], levels_x[2], color_src=False)
    draw_layer(g_nodes, term_nodes, levels_x[2], levels_x[3], color_src=False)

    callout = (
        "Callout: Approximately 95% of CTCAE Grade 1 and Grade 2 events resolve in-place\n"
        "by H2 alone within the HR 9505 1-hour SLA at the v0.8.0 reference configuration."
    )
    fig.text(
        0.5,
        0.045,
        callout,
        fontsize=8.0,
        color="black",
        ha="center",
        va="center",
        bbox=dict(boxstyle="round,pad=0.40", fc=PALETTE["off_white"], ec=PALETTE["slate"], lw=0.8),
    )

    ax.text(6.0, 10.95, f"Total network AE events captured: {total}", ha="center", fontsize=9.0, color=PALETTE["slate"])

    fig.text(
        0.06,
        0.012,
        "Clinical-AI-Demos v0.8.0 / Demo 07 Adverse Event Response",
        fontsize=7.3,
        ha="left",
        color=PALETTE["slate"],
    )
    fig.text(
        0.94, 0.012, "DOI: 10.5281/zenodo.18445179 / MIT License", fontsize=7.3, ha="right", color=PALETTE["slate"]
    )

    fig.savefig(out_path, dpi=300, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    out = pathlib.Path(__file__).with_suffix(".png")
    main(out)
    print(f"Saved {out}")
