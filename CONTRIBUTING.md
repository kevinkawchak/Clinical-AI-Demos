# Contributing

Contributions are welcome from engineers, clinicians, and researchers working on humanoid agents and large language models for Physical AI oncology clinical trials.

## What We Accept

| Contribution Type | Examples |
|-------------------|----------|
| New demo prompts | Additional humanoid + LLM perspectives not covered in the existing 10 prompts |
| Prompt refinements | Stronger downstream LLM processing instructions, more precise file references |
| Repository scaffolding | CI workflow improvements, badge updates, documentation cross-links |
| Cross-references | Better integration with kevinkawchak/physical-ai-oncology-trials inputs |
| Bug fixes | Corrections to file paths, regulatory citations, humanoid specifications |

## Requirements for All Contributions

1. **Humanoid + LLM influence**: Every new demo prompt must feature a clear humanoid platform (Atlas, Optimus, Figure, Digit, Apollo, Phoenix, Neo, H2, or comparable) and an explicit on-prem or cloud LLM control loop (Claude, GPT, Gemini, Ollama, or comparable).
2. **Oncology trial relevance**: Demos must address surgical, patient care, sponsor operations, pharmacy, pathology, telesurgery, adverse event, research coordination, radiation oncology, or decentralized home care tasks inside oncology clinical trials.
3. **Companion alignment**: Prompts must reference exact directories and files from kevinkawchak/physical-ai-oncology-trials when leveraging existing assets as inputs.
4. **CI cleanliness**: New files must not introduce ruff or yamllint failures.

## Development Workflow

### 1. Fork and Branch

```bash
git clone https://github.com/<your-fork>/Clinical-AI-Demos.git
cd Clinical-AI-Demos
git checkout -b your-branch-name
```

### 2. Install Development Tools

```bash
pip install ruff yamllint
```

### 3. Make Changes

- Follow the prompt template documented in `demo-projects/README.md`.
- Cap ASCII diagrams at 80 columns by 60 lines.
- Use single dashes only inside Markdown prose. No em dashes, no double dashes, no triple dashes.
- Use black text only. No color overrides.

### 4. Lint and Format

```bash
ruff check .
ruff format --check .
yamllint -d relaxed .github/
```

### 5. Submit a Pull Request

- Fill out the PR template completely, including the safety and compliance checklist.
- Reference any related issues.
- Confirm CI passes on Python 3.10, 3.11, and 3.12 before requesting review.

## Prompt Authoring Style

- Each prompt must be a self-contained Claude Code task brief.
- Prompts may name the future downstream LLM session as Claude Code Opus 4.7 1M Max, Claude Sonnet 4.6, or an on-prem Ollama configuration.
- Inputs from kevinkawchak/physical-ai-oncology-trials must be listed with exact path prefixes (no glob shorthands that hide which files are read).
- Output trees must list the future-authored files explicitly, sized in approximate KB.
- Per-commit roadmaps must use the seven-commit single-PR pattern documented in `national-repositories/build-national.md`.

## Safety and Compliance

- Any code or prompt that automates clinical workflows must document the required human oversight steps.
- Do not introduce changes that bypass safety gates, force limits, E-stop latency budgets, or human-in-the-loop requirements.
- Regulatory and privacy references must cite the correct CFR title, ICH section, IEC standard, or HIPAA rule.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
