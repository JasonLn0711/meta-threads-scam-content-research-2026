# Decision 0036: Adopt Confirmed Scam Pointer Intake Method

## Date

2026-04-25

## Status

Accepted

## Decision

Adopt a repeatable confirmed-scam pointer intake method for future stakeholder/CIB-confirmed Threads scam examples.

Each pointer receives:

- controlled-store source pointer;
- controlled browser/API capture when approved;
- raw evidence outside git;
- redacted local manual entry and record;
- strict validation;
- second review;
- repo-safe run/evaluation note;
- taxonomy or baseline rule update only if the case teaches a reusable evidence family.

## Rationale

Confirmed pointers are high-yield for rule-library calibration, but they are not prevalence samples. The workflow needs to preserve evidence without letting raw investigative material leak into git or turning one scam method into an overbroad rule.

## Current Application

- Item `0028` established `implicit_dm_contact_request`.
- Item `0029` establishes `high_fee_course_or_membership_funnel`.

## Boundary

This decision does not authorize committing raw post text, raw replies, screenshots, full item URLs, raw handles, HTML, credentials, browser storage state, or stakeholder case IDs to git.
