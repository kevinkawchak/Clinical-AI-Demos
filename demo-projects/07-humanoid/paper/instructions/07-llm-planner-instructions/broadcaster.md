# Authoring Instructions for `src/broadcaster.py`

The future session writes this Python module during Commit 4 of 7.

## Purpose

Publishes the `llm_decision` record to the per-site broadcast bus where all 3 robots subscribe. One write per tick, atomic, durable for the on-prem audit chain.

## Key Behavior

- Subscribes to the LLM planner output.
- Publishes to `site/{site_id}/broadcast` topic.
- Writes a copy to `data/week_llm_decisions.jsonl` for the audit log.
- Computes and propagates the audit chain previous-hash.
- Tracks acknowledgments from all 3 robots within 500 ms.

## Required Interfaces

```
class Broadcaster:
    def __init__(self, site_id: str, output_jsonl: pathlib.Path) -> None: ...
    def publish(self, decision: dict) -> None: ...
    def ack(self, command_id: str, robot_id: str) -> None: ...
    def report_missing_acks(self, tick: int, deadline_ms: int = 500) -> list[str]: ...
```

## Suggested Skeleton

```
import json
import pathlib
import threading
import time


class Broadcaster:
    def __init__(self, site_id, output_jsonl):
        self.site_id = site_id
        self.output_jsonl = pathlib.Path(output_jsonl)
        self.expected_acks = {}
        self.received_acks = {}
        self.lock = threading.Lock()

    def publish(self, decision):
        with self.output_jsonl.open("a") as f:
            f.write(json.dumps(decision) + "\n")
        with self.lock:
            self.expected_acks[decision["tick"]] = set(sc["robot_id"] for sc in decision["sub_commands"])
            self.received_acks[decision["tick"]] = set()

    def ack(self, command_id, robot_id):
        # command_id encodes the tick somewhere in the audit log; for simplicity, ack against the latest tick
        with self.lock:
            for tick, expected in self.expected_acks.items():
                if robot_id in expected:
                    self.received_acks.setdefault(tick, set()).add(robot_id)
                    break

    def report_missing_acks(self, tick, deadline_ms=500):
        time.sleep(deadline_ms / 1000.0)
        with self.lock:
            expected = self.expected_acks.get(tick, set())
            received = self.received_acks.get(tick, set())
            return list(expected - received)
```

## Validation Rules

- All 3 robots in the swarm must acknowledge within 500 ms; otherwise the broadcaster reports a gap.
- One JSONL line per tick.
- The JSONL file rotates every 24 hours (one file per day per site) in production; in simulation, one file for the whole 168 hours is acceptable.

## Notes

- The acknowledgment path is the simplest reliability check. More sophisticated reliability would add per-robot sequence numbers and retransmit.
- The audit log is append-only. Never edit or remove lines.
