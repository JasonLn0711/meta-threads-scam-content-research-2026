# Versioning

This directory supports repo-level version tracking for the research scaffold.

Repo versions use `vMAJOR.MINOR.PATCH` and live in the root `VERSION` file. They describe changes to the repository's docs, governance process, scripts, templates, and research operating model. They do not replace dataset versions, schema versions, annotation guideline versions, experiment run names, or controlled API run records.

Use:

```bash
python3 scripts/record_version_update.py --bump patch \
  --summary "Clarify Meta Content Library retention wording" \
  --category governance \
  --path governance/data-governance.md \
  --detail "Clarified that raw API exports remain outside git." \
  --verification "git diff --check"
```

The script updates:

- `VERSION`
- `CHANGELOG.md`
- `versioning/version_log.csv`

Do not put raw evidence, handles, source URLs, credentials, screenshots, browser exports, run secrets, or controlled item-level details in version summaries.
