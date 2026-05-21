# Meta Research Tools Manager Organization Page Snapshot

- Date recorded: 2026-05-21
- Source: user-provided screenshot
- Visible page: Meta Research Tools Manager application draft
- Visible URL pattern: `www.facebook.com/research-tools-manager/applications/[redacted-application-id]`
- Repo-safe privacy note: the logged-in account name, application ID, department-level affiliation details, role, profile URL, and any completed application values that directly identify the applicant are not recorded in full in git.

## Visible Page State

- Left navigation title: `Research Tools Manager`
- Left navigation selected item: `Your application`
- Application status badge: `Draft`
- Main page heading: `Application`
- Section navigation:
  - `Personal information` shows a completed green check.
  - `Organization` is active.
  - `Research details` is listed after organization and is not yet completed.
  - `Collaborators` is listed after research details and is not yet completed.
  - `Terms and Conditions` is listed last and is not yet completed.
- Main panel title: `Organization`
- Main panel helper text: `Provide information about your affiliated organization.`
- Buttons visible: `Back`, `Save`, and `Next`.
- `Next` appears enabled in the visible screenshot.

## Visible Fields

| Field | Required? | UI note |
|---|---|---|
| Organization name | Required | Search / free-text style field with search icon. |
| Organization country | Required | Dropdown. |
| Organization type | Required | Dropdown. |
| Organization website | Required | Free-text URL field. |
| Department name | Required | Free-text field. |
| Your role at organization | Required | Dropdown. |
| Link to your profile or page on your organization's website | Required | URL field for verifying affiliation. |

The profile/page helper text says acceptable links may include:

- an active organizational web profile or bio;
- an organizational directory or staff list;
- the webpage of the research group or lab.

The UI note says LinkedIn profiles, GitHub Pages, and personal websites are not
permitted.

## Filled Page State From Screenshot

| Field | Repo-safe observed status | Notes |
|---|---|---|
| Organization name | Filled: `National Yang Ming Chiao Tung University` | Public institutional name retained. |
| Organization country | Filled: `Taiwan` | Public country-level value retained. |
| Organization type | Filled: `Academic institution` | Public institution-type value retained. |
| Organization website | Filled: `https://www.nycu.edu.tw/` | Public institutional website retained. |
| Department name | Filled; value redacted in git | Actual value stored only in ignored private local note if needed. |
| Your role at organization | Filled; value redacted in git | Actual value stored only in ignored private local note if needed. |
| Link to your profile or page on your organization's website | Filled; URL redacted in git | Actual value stored only in ignored private local note if needed. |

## Repo-Safe Interpretation

- The organization page appears complete enough for `Next` to be enabled.
- The institution, country, type, and main website are consistent with an
  academic research-access application.
- The profile/page link should be checked before submission. If it only points
  to a department homepage and does not verify the applicant's affiliation,
  replace it with a stronger organization-hosted profile, directory, advisor lab
  page, or research group page that can verify the applicant.
- Do not use LinkedIn, GitHub Pages, or a personal website for the affiliation
  verification field.

## First-Principle Filling Strategy

The organization page should prove institutional accountability. It should help
Meta and CASD verify that the applicant is affiliated with a legitimate academic
organization and that the requested research access is institutionally grounded.

Use exact official organization information and an organization-hosted
affiliation link. Do not use this page to describe scam detection, CIB
operations, raw evidence, or project claims.

## Repo Boundary

This note records the form structure and repo-safe filling status. The full
filled values are kept only in ignored local private storage if needed. Do not
commit application IDs, account identity, private application screenshots,
department-level personal affiliation details, profile URLs that identify the
applicant, or any CV / email / ORCID details unless explicitly approved and
redacted.
