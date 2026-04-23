# Decision 0019: Correct Controlled-Store Artifact Status

## Identity

- Date: 2026-04-23
- Status: accepted
- Owner: Jason

## Decision

Correct the outside-git controlled store so controlled pilot artifacts are not labeled as examples, samples, or synthetic files.

The repo-visible rule is:

- Controlled-store files may be real, sensitive, or item-level pilot artifacts.
- Raw evidence, credentials, session artifacts, screenshots, URLs, handles, OCR, redirect chains, and item-level sensitive outputs remain outside git.
- Git-facing docs should refer to the controlled store only through non-sensitive controlled references and governance status.
- Do not copy controlled-store contents into repo docs unless a later redaction/publication decision explicitly permits a narrow derivative.

## Context

The outside-git controlled-store directory had multiple files and paths labeled with `example`, `sample`, or `synthetic` language even though the project owner clarified that those files should be treated as real controlled files. This created a safety risk: future researchers or agents could mistake controlled pilot artifacts for harmless dry-run examples and mishandle them.

## Options Considered

| Option | Pros | Cons | Decision |
|---|---|---|---|
| Leave labels unchanged | No immediate doc churn | Preserves a misleading safety signal | Rejected |
| Commit a redacted copy into git for clarity | Easy for future readers to inspect | Risks normalizing item-level controlled evidence in repo | Rejected |
| Correct controlled-store labels outside git and update repo governance language | Keeps sensitive material outside git while making status clear | Requires future agents to respect the outside-git boundary | Accepted |

## Consequences

- Controlled-store paths and metadata should use controlled-pilot language, not synthetic/example language.
- Repo status language should say that item-level controlled pilot artifacts, if present, live outside git.
- Older synthetic dry-run records remain valid only for the actual synthetic datasets and rehearsals already documented in this repo.
- The next blocker is operational practice: controlled rehearsal validation, redaction review, and the first 10-15 item checkpoint.

## Follow-Up

- Keep controlled-store scans limited to filenames, manifests, and governance metadata unless explicit review authority is recorded.
- Before any future commit, check that no raw or controlled item-level artifacts have entered git.
- If a new controlled-store artifact is mislabeled as synthetic or example material, correct the controlled-store label first and then update only non-sensitive repo references.
