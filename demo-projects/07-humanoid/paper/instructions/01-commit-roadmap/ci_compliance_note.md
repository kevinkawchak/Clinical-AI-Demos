# CI Compliance Notes for Commit 6

The future Claude Code Opus 4.7 1M Max session must confirm the CI workflow passes on Python 3.10, 3.11, and 3.12 before finalizing commit 6. The CI workflow at `.github/workflows/ci.yml` runs:

```
ruff check . --output-format=github
ruff format --check .
yamllint -d relaxed .github/
```

## Recurring Errors and Fixes

The v0.1.0 and v0.2.0 PRs sometimes had 3 failing checks (Cl / lint-and-format on 3.10, 3.11, 3.12). The root causes were:

1. New Python source under `demo-projects/` that did not match the existing `ruff.toml` per-file-ignores. Fix: confirm the entry `"demo-projects/**/*.py" = ["F401", "F402", "F821"]` is present. Add any new lint rule code triggered by v0.3.0 source.
2. YAML config files with multiple documents (using `---` separators). Fix: keep all v0.3.0 YAML single-document.
3. Markdown files with bad table separators. Fix: rely on the markdown table parser; do not invent custom separators.
4. Files with em dashes inserted by autocorrect. Fix: run the dash style check from `src/check_errors.py`.

## Pre-commit Checklist

The future session must run all of the following before committing:

```
# Python lint and format
ruff check . --output-format=github
ruff format --check .

# YAML lint
yamllint -d relaxed .github/

# JSON schema parse
for f in schemas/*.schema.json; do python -m json.tool "$f" > /dev/null; done

# YAML config parse
for f in config/*.yaml; do python -c "import yaml; yaml.safe_load(open('$f'))"; done

# Custom error scan
python src/check_errors.py

# Tests
pytest tests/ -q
```

All commands must exit 0.

## ruff.toml Confirmation

The repository root `ruff.toml` should remain unchanged for v0.3.0. The existing entry:

```
[lint.per-file-ignores]
"demo-projects/**/*.py" = ["F401", "F402", "F821"]
"national-repositories/**/*.py" = ["F401", "F402"]
```

The `"demo-projects/**/*.py"` pattern matches all v0.3.0 source under `demo-projects/07-humanoid/paper/instructions/src/`. No new per-file-ignores are expected; commit 6 confirms.

## Notes

- The 3 failing checks at Cl / lint-and-format are prevented by the pre-commit checklist.
- The commit 6 author must be diligent about running all 7 steps.
