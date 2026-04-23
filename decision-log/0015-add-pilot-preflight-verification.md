# Decision 0015: Add Pilot Preflight Verification

## Date

2026-04-23

## Decision

Add a repo-safe pilot preflight verifier that checks structural readiness before the first real Threads pilot item is collected.

The verifier checks required artifacts, JSON parsing, CSV/schema consistency, `.gitignore` protections, tracked-file hygiene, local raw-folder hygiene, and optional local workspace readiness.

## Context

The project has a bounded `go_with_limits` approval posture and a local workspace initializer. The remaining launch risk is that item 1 could begin with a missing template, schema drift, bad ignore rule, tracked raw-data path, or incomplete local workspace.

Human governance still owns exact source, storage, access, retention, and redaction limits outside git. A script cannot inspect or approve those sensitive records.

## Options Considered

1. Rely only on human checklists.
2. Add a mechanical preflight verifier before item 1.
3. Add a collection assistant that validates while gathering real data.

## Rationale

Option 2 reduces preventable launch mistakes without automating collection or expanding scope. It fits the repo's documentation-first, experiment-second, code-third posture because it protects the approved workflow rather than replacing governance.

Option 1 leaves easy-to-catch drift unchecked. Option 3 is out of scope because real collection automation is not approved.

## Consequences

- Operators can run `python scripts/check_pilot_preflight.py` for repo-only checks.
- Before item 1, operators can run `python scripts/check_pilot_preflight.py --before-item-1 --ack-controlled-details`.
- Preflight errors block collection until fixed.
- The script does not collect data and does not inspect controlled records outside git.
- Generated preflight reports should stay local-only unless fully non-sensitive and approved.

## Follow-Up

Use the preflight after local workspace initialization and before the first 10-15 item checkpoint. If warnings repeat, update the runbooks or templates before continuing the pilot.
