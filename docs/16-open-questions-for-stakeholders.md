# Open Questions For Stakeholders

## Current Status

As of `2026-04-23`, the repo has a schema, annotation guide, pilot governance package, report-v0 package, synthetic samples, a completed synthetic validation/audit/baseline dry run, and an approved 50-item pilot launch packet.

The remaining blocker before real data work is controlled launch detail: exact source, storage, access, retention, screenshot/link handling, and redaction limits must be written into the controlled launch record outside git. The dry run used synthetic examples only and does not answer any real-data evidence question below.

## Pilot Kickoff Questions

The approval decision has been recorded at the pilot level. These controlled-launch questions must still be answered before the first real item:

- What exact source or source list is approved, recorded outside git if sensitive?
- What exact raw-storage location is approved outside git?
- Who exactly may access raw evidence and derived annotation files?
- What exact retention/deletion rule applies to raw evidence and derived annotation files?
- What exact screenshot, URL, link, handle, and OCR redaction limits apply?
- Who confirms the controlled launch record before item 1?

Use `governance/pilot-launch/` as the non-sensitive index. Put sensitive exact values only in the approved controlled location.

## Criminal Investigation Stakeholders

- What counts as report-worthy Threads content from an investigative perspective?
- Are we studying illegal scam, suspicious fraud-like content, or high-risk lures?
- What evidence standard is useful before opening a case?
- Which scam types are currently most operationally painful?
- Are redirection handles, links, or comments more important than original post text?
- Can de-identified examples be shared for research?
- What must never be stored in the research repo?

## Anti-Fraud Office Stakeholders

- What review queue outcome would be useful: high-risk triage, subtype classification, evidence summary, or referral recommendation?
- What false positive rate is tolerable for a research prototype?
- Which categories should be prioritized: investment, loans, jobs, medical claims, impersonation, or other lures?
- Is Threads currently higher priority than other Meta surfaces?
- What reporting volume should the phase-1 sample reflect?
- What format should the final recommendation memo use?

## Legal And Policy Stakeholders

- What collection methods are permitted?
- What platform terms or policy constraints apply?
- Can public Threads examples be stored in redacted form?
- Can screenshots be retained, and under what restrictions?
- Can stakeholder-provided reports be used for annotation?
- What language should be used to avoid legal overclaiming?
- What is the retention and deletion requirement for raw evidence?

## Domain Reviewers

- Which signals are strong enough to mark `scam` under the research guideline?
- Which finance or marketing examples are commonly misread as scam-like?
- How should annotators handle celebrity references?
- How should annotators handle political or medical claims?
- What makes a case `uncertain` rather than `scam`?
- Which evidence fields are most useful during review?

## Engineering And Research Stakeholders

- Is CSV sufficient for first annotation, or is JSONL needed immediately?
- What OCR tool is acceptable for the first local experiment?
- Are LLM-assisted explanations permitted on redacted samples?
- What minimum metrics should decide phase-2 continuation?
- Who owns dataset versioning and schema changes?
