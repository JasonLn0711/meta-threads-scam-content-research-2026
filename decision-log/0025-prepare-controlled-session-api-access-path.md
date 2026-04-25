# Decision 0025: Prepare Controlled Session/API Access Path

## Date

2026-04-25

## Decision

Prepare both approved access-path options before item 0016:

1. a controlled-store browser storage-state/session artifact path, and
2. an API/session-aware client path that keeps tokens, cookies, raw responses, and automation logs outside git.

This decision authorizes access-path preparation only. It does not authorize item collection, raw evidence in git, browser profile export to git, landing-page capture, redirect expansion, profile review, bulk scraping, or legal determinations.

## Context

Risk-probe runs 0005 and 0006 did not return extractable item content through public unauthenticated browser-rendered access. Run 0007 reviewed the approved access material and found governance/credential material in the controlled store, but no loadable browser storage-state/session artifact and no ready API/session-aware client path.

The project therefore needs a prepared access path before any item 0016 attempt.

## Options Considered

| Option | Decision |
|---|---|
| Keep trying more public unauthenticated query strings | Rejected; this repeats the access-mode failure. |
| Copy session/cookie/API material into git for convenience | Rejected; violates governance and evidence handling. |
| Prepare a browser storage-state slot and validator in controlled storage | Accepted. |
| Prepare an API/session-aware client helper that writes raw output only to controlled storage | Accepted. |
| Execute item 0016 immediately | Rejected; real approved access material is not ready yet. |

## Rationale

The dataset should not advance by weakening evidence controls. A prepared access path lets the team move quickly once an approved session artifact or API probe URL is available, while keeping secrets and raw outputs out of the repository.

## Consequences

- Run 0008 records access-path preparation only.
- Item 0016 remains uncreated.
- Browser execution remains blocked until a real approved storage-state/session artifact exists in controlled storage and passes shape validation.
- API execution remains blocked until controlled API env values include a real approved token and probe URL and the dry-run readiness check passes.
- Raw API output, automation logs, cookies, tokens, browser profiles, HAR files, screenshots, URLs, handles, and raw item content remain outside git.

## Follow-Up

Before item 0016:

1. Export or place the approved browser storage state in controlled storage, then validate it, or fill the approved API probe env values outside git and run the dry-run check.
2. Open the next execution run record.
3. Attempt only one controlled item.
4. If one real item is selected, build `manual_entry_0016.json`, build `manual_record_0016.json`, strict-validate, and record the aggregate result.
