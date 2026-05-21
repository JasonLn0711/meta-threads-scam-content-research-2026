# Meta Research Tools Manager Submission Review Status Page Snapshot

- Date recorded: 2026-05-21
- Source: user-provided screenshot of the Meta Research Tools Manager application after submission
- Page state: application submitted and under independent review
- URL / application identifier: intentionally omitted from git
- Screenshot files: not stored in git
- Repo-safe privacy note: this note records the post-submission review status, visible application progress, research-tool access state, and next gates. It does not record the visible application ID, logged-in account identity, screenshot file, personal legal identity, access credentials, cleanroom details, raw Threads evidence, handles, URLs, collaborator emails, invitation links, or item-level controlled artifacts.

## Visible Page State

- Main page title / application title: `Metadata-Driven Public Scam Pattern Analysis and Reviewer Su`
- Left navigation title: `Research Tools Manager`
- Left application list: selected application entry with truncated title `Metadata-Driven Public Sca...`
- Draft badge: not visible in this post-submission screenshot
- Status banner heading: `Application under independent review`
- Submission date shown by the UI: `May 21, 2026`
- Review body named by the UI: `Secure Data Access Center, CASD`
- Review-time statement shown by the UI: reviews typically take `2-3 weeks`

## Review Progress Rail

| Stage | Visible state | Repo interpretation |
|---|---|---|
| `Submission` | Completed with green check | The application has been submitted. |
| `CASD review` | Current / in progress | Independent review is the active stage. |
| `Meta processing` | Pending | Do not assume Meta processing has started. |
| `Approval` | Pending | Access is not approved yet. |

Approximate CASD review expectation from the visible `2-3 weeks` statement:

- Submission date: 2026-05-21
- Two-week mark: 2026-06-04
- Three-week mark: 2026-06-11

These are planning estimates only. The official Research Tools Manager status remains the source of truth.

## Research Details Card

Visible card heading:

```text
Your research details
```

Visible submitted research program title:

```text
Metadata-Driven Public Scam Pattern Analysis and Reviewer Su
```

Repo interpretation:

- The submitted title still appears to end at `Su`, consistent with the earlier 60-character field-limit observation.
- This is now the submitted title in the visible status page unless the application later allows revision.

Visible submitted research-program description:

- The same public-interest, metadata-first, AI-assisted reviewer workflow description recorded earlier remains visible in the post-submission status page.
- The canonical full text is recorded in [2026-05-21-meta-research-tools-manager-research-details-page.md](2026-05-21-meta-research-tools-manager-research-details-page.md).

Visible organization line:

```text
National Yang Ming Chiao Tung University
```

Visible terms link:

```text
Terms and Conditions (view)
```

Repo interpretation:

- The application summary is visible after submission.
- Terms remain viewable after submission.
- This page confirms the application reached the review stage, but it does not grant data access.

## Research Tools Access Card

Visible card heading:

```text
Your research tools access
```

Visible requested tools:

| Tool | Visible description | Visible control | Repo interpretation |
|---|---|---|---|
| `Meta Content Library` | Web-based, controlled-access environment optimized for browsing and monitoring public data. | `Open` button visible | Requested tool is listed, but access is still pending. Do not treat the `Open` button as approval. |
| `Meta Content Library API` | Hosted on Meta Secure Research Environment. Supports programmatic queries of the data and is designed for computational researchers familiar with R or Python. | `Open` button visible | API route is listed, but access is still pending and should be assumed available only after approval and official access details. |

Repo interpretation:

- The application requested both Meta Content Library and Meta Content Library API.
- The API route is tied to Meta Secure Research Environment in the visible page.
- This status page does not authorize live collection, cleanroom use, API calls, downloads, export, scraping, or production detection.

## Researchers Card

Visible card heading:

```text
Researchers
```

Visible controls and states:

| Field / control | Visible state | Repo-safe record |
|---|---|---|
| `Invite collaborators` | Button visible | Collaborator invitation remains available after submission. |
| Lead researcher entry | One lead researcher row visible | Personal name is intentionally omitted from this git note. |
| Access status | `Access pending` | Lead researcher does not yet have approved access. |
| Role badge | `Lead` | The visible researcher row is the lead applicant. |

Repo interpretation:

- Current visible researcher count: `1`
- Current visible collaborator count beyond lead: `0`
- Current access state: `pending`
- Any collaborator invitation after submission should still use organizational email and should not be recorded in git.

## Current End-To-End Application Progress

| Area | Current state |
|---|---|
| Personal information | Completed before submission |
| Organization | Completed before submission |
| Research details | Completed and visible in submitted summary |
| Collaborators | Completed/skipped with zero filled collaborator emails in earlier screenshot |
| Terms and Conditions | Completed before submission; terms remain viewable |
| Final application submission | Completed on 2026-05-21 |
| CASD review | In progress / independent review |
| Meta processing | Not yet reached in visible progress rail |
| Approval | Not yet reached |
| Lead researcher access | `Access pending` |
| Tool access | MCL web and MCL API listed, but not yet approved for use |

## Operational Meaning For This Repo

This page changes the repo state from application preparation to review tracking.

Allowed repo-visible work now:

- record review status and non-sensitive timeline updates;
- prepare IRB/ethics, storage, retention, deletion, citation, and publication plans;
- prepare reviewer-assist research design that does not require live MCL/API access;
- keep official-documentation drift checks ready for the next stage;
- maintain aggregate-only planning and controlled-access boundaries.

Not allowed from this page alone:

- live MCL UI collection;
- MCL API calls;
- scraping, crawling, browser automation, or unofficial data access;
- local export or download of Meta Data;
- cleanroom export;
- production detection;
- legal or enforcement determination;
- public accusation of accounts;
- raw evidence in git.

## Next Gates

1. Wait for CASD independent review result.
2. Track the expected review window as approximately 2026-06-04 to 2026-06-11, while treating Research Tools Manager as the source of truth.
3. If CASD approves, wait for Meta processing and access details before any tool use.
4. If revision is requested, update the research title, collaborator state, governance language, or documentation evidence as needed.
5. If approved, create a controlled access activation record before any MCL UI or API run.
6. If rejected, record the rejection reason in a repo-safe way and decide whether to revise, resubmit, or park official-access work.

## First-Principle Reading

The scarce resource is now review trust and patience, not more form text.

The project has crossed the submission threshold, but it has not crossed the access threshold. The correct operating posture is:

> Submitted for independent CASD review; access pending; no collection or API use until approval and controlled activation.
