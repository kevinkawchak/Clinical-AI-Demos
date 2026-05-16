# Security Policy

## Scope

This repository contains demonstration prompts for humanoid agents and large language models deployed in **oncology clinical trial** environments. Security issues may affect patient safety, regulatory compliance, humanoid behavioral integrity, and protected health information (PHI). We take all reports seriously.

## Reporting a Vulnerability

**Do not open a public GitHub issue for security vulnerabilities.**

Instead, report vulnerabilities privately by emailing the maintainer or using [GitHub's private vulnerability reporting](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-managing-vulnerabilities/privately-reporting-a-security-vulnerability) on this repository.

Include:
1. Description of the vulnerability
2. Steps to reproduce
3. Affected component (e.g., demo prompt path, CI workflow, badge URL)
4. Potential impact (data exposure, incorrect clinical guidance, humanoid safety gap)

You should receive an acknowledgment within 7 days. A fix or mitigation plan will be communicated within 30 days for confirmed issues.

## Supported Versions

| Version | Supported |
|---------|-----------|
| Latest (main branch) | Yes |
| Older commits | Best-effort only |

## Security Considerations for Deployers

This repository is intended for **engineers and clinical trial operations teams building humanoid + LLM systems for oncology trials**. If you are using these prompts to author downstream demonstrations, you are responsible for:

### Protected Health Information (PHI)
- Never commit patient data, imaging, or identifiers to this repository or forks.
- Use the `privacy/de-identification/` pipeline from kevinkawchak/physical-ai-oncology-trials before any data enters version control.
- Follow your institution's HIPAA Security Rule policies (45 CFR 164.302-318).

### Humanoid Agent Safety
- The prompts in this repository specify force limits, E-stop latencies, and human-in-the-loop checkpoints. Do not weaken these constraints in derived work.
- Cumulative cross-arm force limits and inter-humanoid coordination protocols must be enforced when multiple humanoids share a workspace.
- Heartbeat watchdogs and emergency-park budgets must remain at the documented thresholds (typically 5 ms E-stop latency for surgical contexts, 100 ms for non-surgical patient interaction).

### LLM Control Loop Safety
- On-prem LLM deployments must never expose patient data over public networks.
- Cloud LLM fallbacks must redact PHI before egress (see Safe Harbor 45 CFR 164.514(b)).
- Human reviewers must remain in the loop for any irreversible clinical action.

### Regulatory Compliance
- Demo prompts reference 21 CFR Part 50, 21 CFR Part 312, ICH E6(R3), IEC 62304, IEC 80601-2-77, HIPAA, and FDA AI/ML Guidance. These are reference citations, not legal advice.
- Any deployment in a clinical setting must undergo your institution's validation, verification, and change-control processes per IEC 62304 and 21 CFR Part 11.

### Infrastructure
- Pin all dependency versions when authoring downstream demos.
- Run simulations and LLM inference on isolated compute; do not co-locate with systems that store PHI unless properly segmented.
- Audit access to any system that processes clinical trial data.

## Dependencies

This project does not bundle Python or other runtime dependencies. The CI workflow runs `ruff` and `yamllint` for static analysis only. Downstream demos authored from these prompts should integrate `pip-audit` or Dependabot for production forks.
