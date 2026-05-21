# Decision 0023: Add Automated Versioning And Change Log

- Date: 2026-05-21
- Status: accepted

## Decision

Add a repo-level versioning system with a current version in `VERSION`, a detailed human-readable `CHANGELOG.md`, a machine-readable `versioning/version_log.csv`, and a small local script for controlled version bumps.

The initial repository operating version is:

```text
v1.2.6
```

## Context

The project has moved from a scaffold into a governed research operating system with multiple decision records, pilot gates, source-intake rules, baseline candidates, and official API-access boundaries.

The recent Breeze Guard 26 and Meta Content Library/API updates changed enough of the planning surface that future changes need a visible version trail. The existing dataset/schema/guideline version references are not sufficient because they track research artifacts, not repository operating changes.

## Options Considered

1. Keep only decision records.
2. Add a manual Markdown changelog.
3. Add a repo-level `VERSION`, detailed Markdown changelog, CSV log, and a local update script.

## Rationale

Option 3 gives the project a lightweight but auditable change trail without turning the repo into a product platform.

The script requires explicit human summaries and does not auto-collect, inspect, or summarize sensitive research evidence. That keeps it within the repository's documentation-first and governance-first boundaries.

## Consequences

- Future substantive repo changes should update `VERSION`, `CHANGELOG.md`, and `versioning/version_log.csv`.
- Large scope, data-access, privacy, schema, or claim-boundary changes should also receive a decision record.
- Dataset versions, schema versions, guideline versions, and experiment run names remain separate from repo operating versions.
- Version logs must not contain raw evidence, credentials, handles, controlled URLs, screenshots, or sensitive run details.

## Follow-Up

Use `scripts/record_version_update.py` for future version bumps, starting from `v1.2.6`.
