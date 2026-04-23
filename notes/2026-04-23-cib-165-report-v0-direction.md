# 2026-04-23 CIB/165 Report v0 Direction

## What Changed Today

The immediate deliverable changed from a concept-level stakeholder scoping memo to a real initial research report.

The report target is:

- Title: Threads scam-content research report v0.
- Deadline: 2026-04-30.
- Audience: CIB/165-facing review and internal research alignment.
- Scope: Threads only.
- Posture: research plan with concrete dataset, annotation, baseline, evaluation, governance, and budget sections.

## Strategic Judgment

Threads should remain the first execution surface because current stakeholder context suggests high report pressure there, and because the first evidence surfaces are practical:

- Text posts.
- Text plus image posts.
- Replies/comments.
- OCR from attached images and screenshots.
- Visible redirection signals.
- External links when present.

This is still not a production detector. The report should help decide what a lawful, review-supporting phase-1 MVP can realistically do under the NTD 1.8M research budget.

## Important Boundary

The CIB/165 context should be described as stakeholder background. It should not be treated as verified dataset evidence unless samples, authority, and data-handling rules are later provided.

Do not overclaim:

- No legal fraud determination.
- No automated enforcement.
- No broad Meta coverage.
- No automated Threads collection unless approved.
- No deepfake or video-heavy mainline in phase 1.

## Action Items

- [x] Create `reports/threads-scam-content-research-v0.md`.
- [x] Add a report index at `reports/README.md`.
- [x] Record a decision log for the April 30 report deadline.
- [x] Link the report from `README.md`.
- [x] Mention the April 30 milestone in `docs/18-recommended-path-v1.md`.
- [x] Update the planning repo W18 agenda and project file.
- [ ] Create Google Calendar focus blocks and a deadline marker.

## Implementation Note

The report package and planning agenda were implemented on `2026-04-23`.

Google Calendar creation was attempted through the connector, but create/read calls returned unsupported-tool errors. Because live calendar creation could not be verified, the planning repo now contains an importable `.ics` fallback:

```text
../planning-everything-track/data/projects/2026-04-meta-scam-ad-research/2026-04-27-30-cib-165-threads-report-v0-calendar-blocks.ics
```

## First-Principles Reasoning

The April 30 artifact must be a report, not another concept memo, because:

1. Threads report pressure needs to be translated into a research question before data work begins.
2. The project has no authorized real dataset yet, so the report must distinguish stakeholder context from evidence.
3. NTD 1.8M can support a governed dataset slice and baseline study, but not full Meta production detection.
4. Human-review triage is the correct phase-1 output because it preserves uncertainty and avoids legal overclaiming.
5. The report creates the approval and narrowing path needed before collection, annotation, or baseline claims.
