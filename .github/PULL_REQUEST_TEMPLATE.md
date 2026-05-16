# Pull Request

## Summary

<!-- Describe the changes in 1-3 sentences -->

## Type of Change

- [ ] New demo prompt
- [ ] Documentation update
- [ ] Repository scaffolding (CI, governance, badges)
- [ ] Bug fix or correction
- [ ] Other (describe below)

## Safety and Compliance Checklist

- [ ] No patient data, PHI, or PII is committed
- [ ] No credentials, API keys, or tokens are committed
- [ ] Humanoid agent safety constraints are documented where applicable
- [ ] LLM control loop fail-safes are documented where applicable
- [ ] Regulatory references are accurate (FDA, ICH, 21 CFR, IEC, HIPAA)

## CI Checklist

- [ ] `ruff check .` passes
- [ ] `ruff format --check .` passes
- [ ] `yamllint -d relaxed .github/` passes
- [ ] All Markdown files use single dashes only
- [ ] All ASCII diagrams cap at 80 columns by 60 lines

## Related Repository

<!-- If this prompt references kevinkawchak/physical-ai-oncology-trials, list the directories used -->

## Notes
