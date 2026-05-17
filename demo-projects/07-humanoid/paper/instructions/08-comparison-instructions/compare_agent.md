# Authoring Instructions for `src/compare_agent.py`

The future session writes this Python module during Commit 5 of 7.

## Purpose

Uses an LLM agent to author the natural-language comparison narrative for `reports/report.md`. Reads `reports/comparison.json` and produces the narrative.

## Required Interfaces

```
def build_agent(prompt_frozen_path: pathlib.Path) -> Callable: ...
def compare(comparison_json: dict, frozen_prompt: str) -> str: ...
def write_report(narrative: str, output_path: pathlib.Path) -> None: ...
```

## Suggested Skeleton

```
import json
import pathlib


def build_agent(prompt_frozen_path):
    prompt = prompt_frozen_path.read_text()
    def agent(payload):
        # call on-prem Claude Opus 4.7 1M with the frozen prompt plus the payload
        # in simulation: deterministic stub returning a templated narrative
        return f"# Comparison Narrative\n\n## Summary\nv0.3.0 camarade swarm achieved median response time {payload['v0_3_0']['response_time_p50_seconds']:.1f} s."
    return agent


def compare(comparison_json, frozen_prompt):
    agent = build_agent(pathlib.Path("src/prompt_frozen.md"))
    return agent(comparison_json)


def write_report(narrative, output_path):
    output_path.write_text(narrative)
```

## Validation Rules

- Narrative includes per-dimension comparisons.
- Camaraderie section appears between Response Time and FDA RTCT Compliance.
- The author's prior DOI 10.5281/zenodo.18029100 is cited in the narrative footer.

## Notes

- The frozen prompt locks the agent's behavior so comparison narrative is reproducible across runs.
- LLM stub returns a templated narrative; production calls the on-prem appliance.
