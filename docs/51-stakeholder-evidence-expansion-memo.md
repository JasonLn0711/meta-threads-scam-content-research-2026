# Stakeholder Evidence Expansion Memo After Item 0017 Stop

## Purpose

Summarize the current governed pilot state after item 0017 was stopped, and define the stakeholder decision needed before any future item 0017 retry, item 0018 attempt, or higher-risk case-finding expansion.

This memo does not authorize collection. It contains no raw Threads content, item URLs, handles, screenshots, cookies, tokens, browser profiles, HAR files, raw visible text, raw storage paths, credential values, or sensitive investigative material.

## Current Pilot State

| Measure | Repo-safe result |
|---|---|
| Date of synthesis | `2026-04-25` |
| Dataset ID | `threads_pilot_v1_2026-05` |
| Accepted local records | 16 |
| Excluded local traces | 1 item 0017 method-review trace |
| Accepted label mix | 15 `non_scam`, 1 `uncertain`, 0 `scam` |
| Accepted risk mix | 16 `low`, 0 `medium`, 0 `high` |
| Current visible evidence mix | no accepted record is marked as image, reply, or external-link based |
| Current source path | controlled browser-rendered session path, one item at a time |
| Raw evidence in git | no |
| Item 0018 status | blocked |

The accepted records are useful for testing redaction, schema validation, comparator handling, and false-positive pressure. They are not enough for high-risk scam-like case analysis or broad pilot completion.

## Why Item 0017 Was Stopped

Item 0017 was not stopped because the browser session, schema, or validation pipeline failed. It was stopped because the approved field scope did not produce independent reviewable item-level evidence.

The project tested:

- topic-only seeds, which overproduced ordinary discussion and low-risk comparators;
- risk-probe seed matrices, which still could not create reviewable item evidence from query terms alone;
- query-echo filtering, which prevented retrieval hints from becoming labels;
- domain-only visible-link evidence plus redirect-category and narrow reply-context feasibility, which found aggregate external-domain signals but no reviewable candidate.

The current blocker is evidence sufficiency. More seeds under the same boundary would mostly add review burden and false-positive pressure.

## What Stakeholders Need To Decide

Before any new collection run, stakeholders should decide whether the next step is:

| Option | Meaning | Collection status |
|---|---|---|
| stop current tranche | Keep accepted records at 16 and move to method reporting only. | no collection |
| provide redacted stakeholder examples | Use already-approved, de-identified examples to calibrate high-risk evidence standards. | only if source, storage, and redaction are approved |
| approve a narrow evidence-expansion run | Permit a new run record with one or more additional evidence fields. | collection only after run record |
| keep current field scope | Continue only with text-first/browser-session evidence. | not recommended for high-risk discovery |

## Evidence Expansion Options

| Evidence family | Why it may help | Main risk | Suggested boundary |
|---|---|---|---|
| Stakeholder-provided redacted exemplars | Gives known high-risk or report-worthy examples without searching broadly. | Source permission and de-identification quality. | 1-2 redacted examples first; raw/source case IDs outside git. |
| Redacted screenshot or OCR excerpt | Many lures may hide in images, cards, or screenshot-style posts. | Personal data and image-retention burden. | Risk-relevant OCR excerpt only; raw image in controlled store; no screenshot in git. |
| Narrow adjacent reply context | Funnel behavior may appear in replies rather than the top-level item. | Capturing unrelated people or broad comments. | Small fixed reply window; aggregate/redacted only; no handles in git. |
| Visible link domain and category | May identify funnel behavior without storing full URLs. | Domain evidence alone can overstate risk. | Domain/category only; no full URL in git; not enough by itself for `scam`. |
| Redirect or landing-page evidence | May reveal destination risk beyond Threads. | Much larger platform, privacy, and legal scope. | Defer unless separately approved with exact capture, storage, and stop rules. |
| Profile/account context | May reveal coordinated behavior. | High privacy and scope expansion. | Out of scope for the next run unless explicitly approved. |

## Recommended Next Approval Request

The most conservative useful next request is a one-run evidence-expansion feasibility study, not immediate scale-up.

Suggested boundary for a future run record:

- target at most 1 selected item;
- review at most 5 candidates;
- keep one browser-rendered page/object at a time;
- allow only risk-relevant OCR excerpt, narrow adjacent reply-context summary, and domain/category link evidence if explicitly approved;
- keep screenshots, raw URLs, handles, full raw text, cookies, browser profiles, and session artifacts outside git;
- continue to forbid profile graph review, broad comments, landing-page capture, and full redirect-chain capture unless separately approved;
- second-review any `uncertain`, low-confidence, or medium/high-risk candidate before it counts;
- stop if the candidate cannot be reduced to approved redacted fields.

## Decision Request

Stakeholders should answer these questions before collection resumes:

1. Is the current 16-record checkpoint enough for method reporting, or should the project attempt a narrow evidence-expansion run?
2. Which evidence families are approved for the next run?
3. What raw-storage, access, retention, and redaction controls apply to those evidence families?
4. What is the maximum candidate-review burden for the next run?
5. Who second-reviews any `uncertain`, low-confidence, or medium/high-risk item?
6. What result would justify continuing toward the 50-item pilot rather than stopping or revising scope?
