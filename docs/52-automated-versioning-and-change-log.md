# Automated Versioning And Change Log

## Purpose

The repository now uses a repo-level operating version such as `v1.2.6` to make research-scope changes traceable.

This version is for the repository as a research operating system: docs, governance rules, templates, scripts, decision records, and process design. It is not the dataset version, schema version, annotation guideline version, baseline run name, model version, or API run identifier.

## Current Version Source

The current repo version is stored in:

```text
VERSION
```

The human-readable log is:

```text
CHANGELOG.md
```

The machine-readable log is:

```text
versioning/version_log.csv
```

## Version Format

Use:

```text
vMAJOR.MINOR.PATCH
```

Examples:

- `v1.2.6`
- `v1.3.0`
- `v2.0.0`

## Bump Rules

Use a major bump when a change materially alters the research contract or operating boundary.

Examples:

- Changing the repo from research scaffold to production prototype.
- Changing the approved data-access route or adding a new class of authorized automated collection.
- Breaking the `thread_item_schema_v1` contract.
- Changing privacy, retention, redaction, or authorization gates in a way that affects real controlled data.
- Reframing the claim boundary from suspicion triage to legal, financial, or medical adjudication.

Use a minor bump when a change adds a meaningful non-breaking capability, process, document, or experiment path.

Examples:

- Adding a new governed source-intake route.
- Adding a new baseline candidate that remains deferred or controlled.
- Adding a new template, runbook, report package, or decision workflow.
- Adding optional fields or documentation without breaking existing records.
- Adding a script that supports repo-safe validation, reporting, or version logging.

Use a patch bump when a change corrects, clarifies, or tightens an existing artifact without changing its contract.

Examples:

- Fixing wording, links, examples, or command syntax.
- Clarifying a limitation or caveat.
- Updating a non-sensitive status note.
- Correcting a typo or small routing issue.

## Required Log Fields

Every version entry should record:

- UTC timestamp.
- Previous version.
- New version.
- Bump type.
- Change categories.
- Short summary.
- Detailed changes.
- Affected paths.
- Decision-record references, if any.
- Verification performed.
- Source references, if any.
- Sensitive-data check.

## Automation

Use:

```bash
python3 scripts/record_version_update.py --bump patch \
  --summary "Clarify versioning policy wording" \
  --category governance \
  --path docs/52-automated-versioning-and-change-log.md \
  --detail "Clarified that repo versions do not replace dataset manifests." \
  --verification "git diff --check"
```

The script updates `VERSION`, prepends a Markdown entry to `CHANGELOG.md`, and appends a row to `versioning/version_log.csv`.

Use `--dry-run` first when checking the next version number:

```bash
python3 scripts/record_version_update.py --dry-run --bump minor \
  --summary "Dry run only"
```

## What Not To Log

Do not log:

- Raw Threads evidence.
- Source URLs for controlled examples.
- Account handles.
- Screenshots or screenshot paths that reveal controlled evidence.
- Browser exports.
- API credentials, tokens, cookies, or session artifacts.
- Exact operational details that belong only in the outside-git controlled run record.

The version log is repo-safe metadata only.

## Relationship To Decision Logs

Decision records explain why a governance, scope, data-access, or design decision changed.

Version logs explain what repository artifacts changed and how the repo version moved.

Large changes should usually have both:

- A decision record in `decision-log/`.
- A version entry in `CHANGELOG.md` and `versioning/version_log.csv`.

## Initial Baseline

`v1.2.6` is the initial repo operating version after the Breeze Guard 26 and Meta Content Library/API updates were recorded. Future updates should move forward from that baseline.
