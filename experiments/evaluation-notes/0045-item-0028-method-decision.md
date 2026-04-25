# Item 0028 Method Decision

## Purpose

Record the repo-safe method decision before any item `0028` attempt.

This note contains no raw Threads content, item URLs, handles, screenshots, cookies, tokens, browser profiles, HAR files, raw visible text, raw reply text, raw storage paths, or sensitive investigative material.

## Current State

| Field | Value |
|---|---|
| Latest checkpoint | `CHK-THREADS-PILOT-V1-0027` |
| Strict-valid local records | 27 |
| Non-excluded records | 26 |
| Excluded method-review traces | 1 |
| Final `scam` records | 0 |
| Final high-risk records | 0 |
| API/session-aware path | blocked until `META_API_PROBE_URL` is supplied and checked |
| Browser/session path | mechanically works but has not yielded final high-risk examples |

## Method Decision

Status: `do_not_open_item_0028_with_same_browser_search_path`.

Before item `0028`, the project should choose one of:

- complete API/session-aware readiness and open a new API/session-aware run record;
- obtain targeted redacted stakeholder/CIB exemplars or pointers and open a controlled exemplar-intake record;
- pause collection and synthesize the 27-record checkpoint for reporting.

## Reason

Runs 0015 and 0016 improved mechanics, redaction, strict validation, second review, and recall-oriented candidate discovery. They did not solve the high-risk case-finding problem.

Continuing the same browser/session search-result method risks spending more review budget on false-positive pressure and medium-risk uncertainty boundaries. The next useful move should either improve access/context or use targeted redacted examples to calibrate high-risk evidence.

## Required Before Item 0028

- Record which path is chosen.
- Confirm access readiness or exemplar authorization.
- Define item and candidate caps.
- Keep raw/session/candidate or source-case material outside git.
- Preserve CIB false-negative preference at triage.
- Second-review all selected items before counting.
