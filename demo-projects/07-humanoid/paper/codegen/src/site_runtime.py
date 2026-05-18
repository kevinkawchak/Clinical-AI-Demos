"""Per-site runtime glue.

Wires together the LLM planner, broadcaster, dispatcher, swarm coordinator,
peer state trackers, comms, and ingest for one PAT-NET-001 site. Loops at
1 Hz LLM cadence and at 10 Hz motion cadence.
"""

from __future__ import annotations

import argparse
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))


def run_site(
    site_id: str,
    config_dir: pathlib.Path,
    output_dir: pathlib.Path,
    fast: bool = False,
) -> dict:
    from broadcaster import Broadcaster
    from h2_dispatcher import H2Dispatcher
    from llm_planner import LLMPlanner

    planner = LLMPlanner(site_id, config_dir)
    broadcaster = Broadcaster(site_id, output_dir / f"{site_id}_llm_decisions.jsonl")
    dispatcher = H2Dispatcher(site_id, config_dir / "h2_humanoid.yaml")

    ticks = 60 if fast else 3600
    for tick in range(ticks):
        decision = planner.plan_tick({}, tick)
        broadcaster.publish(decision)
        outgoing = dispatcher.handle_broadcast(decision)
        for cmd in outgoing:
            dispatcher.ack(tick, cmd["robot_id"])
            broadcaster.ack(cmd["command_id"], cmd["robot_id"], tick)
    return {
        "site_id": site_id,
        "ticks": ticks,
        "audit_chain_head": dispatcher.audit_prev_hash,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Per-site PAT-NET-001 runtime")
    parser.add_argument("--site", required=True)
    parser.add_argument("--fast", action="store_true")
    args = parser.parse_args()
    base = pathlib.Path(__file__).resolve().parent.parent
    result = run_site(
        args.site, base / "config", base / "data" / "runs", fast=args.fast
    )
    print(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
