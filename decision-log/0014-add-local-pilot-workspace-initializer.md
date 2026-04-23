# Decision 0014: Add Local Pilot Workspace Initializer

## Date

2026-04-23

## Decision

Add a repo-safe script and runbook for creating the first real pilot's local-only working files under ignored `data/interim/`.

The initializer creates empty CSV and Markdown files from approved templates only after the operator acknowledges that controlled launch details are complete outside git.

## Context

The project has a `go_with_limits` approval posture for a bounded 50-item Threads pilot, but real collection must not begin until exact source, storage, access, retention, and redaction limits are recorded in the controlled non-git location.

The team needs a concrete next step after that governance record is complete. Manual copying of templates is possible, but a small initializer reduces setup drift and makes the intended file set explicit.

## Options Considered

1. Continue with manual `cp` commands only.
2. Add a local workspace initializer that creates empty files from committed templates.
3. Add collection automation.

## Rationale

Option 2 gives the pilot team a repeatable local setup step without collecting data or adding automation. It keeps the workflow documentation-first and preserves the hard boundary that raw evidence stays outside git.

Option 1 is acceptable but easier to execute inconsistently. Option 3 is out of scope because automated Threads collection is not approved.

## Consequences

- The next pilot setup step is now `python scripts/init_pilot_workspace.py --ack-controlled-details`.
- The script refuses to write files without explicit acknowledgement.
- Local working files remain ignored by git.
- The repo still contains no real Threads evidence.
- Any sensitive launch details remain outside git.

## Follow-Up

After the controlled launch record is completed outside git, initialize the local workspace, collect only the first 10-15 items, and run the checkpoint protocol before continuing to 50.
