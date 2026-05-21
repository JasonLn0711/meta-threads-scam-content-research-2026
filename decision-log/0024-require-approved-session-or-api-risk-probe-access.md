# Decision 0024: Require Approved Session Or API Risk-Probe Access

## Date

2026-04-24

## Decision

Do not create item 0016 from the public unauthenticated browser-rendered risk-probe runs. Before item 16, open a new run record that confirms an approved browser-rendered session/access path or approved API/session-aware path.

This decision does not authorize raw credential storage in git, user browser profile export, bulk scraping, profile review, landing-page capture, redirect-chain expansion, screenshots/OCR, broad reply capture, or legal determinations.

## Context

Decision 0023 required a risk-probe method before item 16 because the first 15 controlled local records produced no medium/high-risk examples.

Two public browser-rendered risk-probe experiments were run:

- Run 0005 used multi-term domain plus signal-family probes.
- Run 0006 used normalized no-space risk-probe phrases and excluded exact query echoes.

Both runs returned HTTP 200 responses but no extractable real item content. The visible page text was query echo or generic user-interface/onboarding text. No `manual_entry_0016.json` was created.

## Options Considered

| Option | Decision |
|---|---|
| Treat query text as item evidence | Rejected; this would contaminate labels. |
| Create item 0016 from UI text | Rejected; UI text is not Threads item evidence. |
| Keep trying more public unauthenticated risk-probe query strings | Rejected for now; runs 0005 and 0006 show access-mode failure, not just seed wording failure. |
| Move to approved session/API access-path review | Accepted. |

## Rationale

The project needs high-risk candidate discovery, but the integrity of the dataset matters more than filling the next item number.

The risk-probe method is still valid as a candidate-generation design. The failed part is the current access path: it does not expose item content for these probes. The next controlled step should therefore test the same guardrailed method through an approved session-aware or API-aware path.

## Consequences

- Item 0016 remains uncreated.
- Runs 0005 and 0006 are recorded as no-extractable-item method experiments.
- The next run record must explicitly confirm session/API access handling before collection.
- Query terms remain candidate-generation probes only and cannot become labels.
- The 50-item pilot remains blocked from continuation until the access-path problem is resolved and a later checkpoint records adequate composition.

## Follow-Up

Before item 16:

1. Open a new run record for the approved session/API risk-probe path.
2. Confirm credentials, cookies, browser profiles, tokens, HAR files, raw output, source URLs, handles, and screenshots remain outside git.
3. Reuse the risk-probe seed matrix or a narrower owner-approved subset.
4. Build and strict-validate a local record only if a real item can be redacted into approved fields.
5. Record no extractable item if the access path still fails.
