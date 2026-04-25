# Open Questions For Stakeholders

## Current Status

As of `2026-04-25`, the repo has a schema, annotation guide, pilot governance package, report-v0 package, synthetic samples, a completed synthetic validation/audit/baseline dry run, an approved 50-item pilot launch packet, 16 accepted controlled local records, and one excluded item 0017 method-review trace.

The controlled launch detail now lives outside git in the controlled launch record. Exact source, storage, access, retention, screenshot/link handling, and redaction limits must stay there, not in this repo. The current blocker is no longer item-1 readiness. Decision 0029 stopped the item 0017 extension because the approved evidence scope did not produce independent reviewable item-level evidence for higher-risk discovery.

Use `docs/51-stakeholder-evidence-expansion-memo.md` for the current evidence-scope decision request before any future item 0017 retry or item 0018 attempt.

## Pilot Kickoff Questions

The approval decision has been recorded at the pilot level. These controlled-launch questions are tracked in the outside-git controlled launch record and must be rechecked before any new source, method, or field change:

- What exact source or source list is approved, recorded outside git if sensitive?
- What exact raw-storage location is approved outside git?
- Who exactly may access raw evidence and derived annotation files?
- What exact retention/deletion rule applies to raw evidence and derived annotation files?
- What exact screenshot, URL, link, handle, and OCR redaction limits apply?
- Who confirms the controlled launch record before item 1?

Use `governance/pilot-launch/` as the non-sensitive index. Put sensitive exact values only in the approved controlled location.

## Controlled Launch Questions Before Item 1

These questions are the immediate blocker for real evidence operations:

| Area | Question |
|---|---|
| Source | What exact source or source category is approved for the first 10-15 items? |
| Storage | What exact raw-storage location is approved outside git? |
| Access | Which IDs may see raw evidence, redacted files, annotation files, and generated outputs? |
| Retention | What must be deleted or reviewed after the checkpoint and after the decision memo? |
| Redaction | What must be removed from screenshots, OCR text, URLs, links, handles, replies, and notes? |
| Screenshots | Are screenshots allowed, redacted-only, or not retained? |
| OCR | Is OCR allowed, and must it be risk-relevant excerpt only? |
| URLs and links | Are source URLs omitted, redacted, normalized, or fully stored? Are visible links domain-only? |
| Handles and contacts | Are contact handles category-only, redacted, or forbidden? |
| Role IDs | Which collector, annotator, reviewer, adjudicator, and research engineer IDs are approved? |
| Forbidden context | Which profile, account, landing-page, redirect-chain, or outside-source context is explicitly forbidden? |
| Signoff | Who can mark the controlled record `ready_for_first_10_15_items`? |
| Checkpoint | Who reviews the first 10-15 item checkpoint and decides whether 50 may continue? |

If any answer is incomplete for the current path, collection on that path remains paused and the repo should stay in synthetic-only tooling, planning, or governance-repair mode.

## Current Evidence-Expansion Questions After Run 0013

These questions now block any future item 0017 retry, item 0018 attempt, or higher-risk case-finding run:

| Area | Question |
|---|---|
| Tranche status | Do stakeholders accept stopping the current item 0017 extension and reporting the checkpoint as 16 accepted records plus 1 excluded trace? |
| Evidence families | Which evidence families are approved next: redacted stakeholder examples, risk-relevant OCR excerpts, narrow reply context, visible-link domain/category, redirect evidence, or none? |
| Screenshots/OCR | If screenshots or OCR are approved, may raw images be stored only in the controlled store with repo-safe OCR excerpts? |
| Reply context | If narrow reply context is approved, what maximum reply window is allowed and what redaction is mandatory? |
| Links and redirects | Is domain/category evidence enough, or is any landing-page or redirect-chain capture approved? |
| Candidate burden | What is the maximum number of candidates the next run may review? |
| Counting rule | Can a future evidence-expansion result count toward the 50-item pilot, or is it method-only? |
| Review ownership | Who second-reviews `uncertain`, low-confidence, or medium/high-risk candidates before they count? |

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
- Should model-assisted explanations remain out of scope until the manual pilot decision memo?
- What minimum evidence should decide continuation, pause, source narrowing, or later expansion?
- Who owns dataset versioning and schema changes?
