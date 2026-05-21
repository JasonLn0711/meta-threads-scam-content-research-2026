# Meta Research Tools Manager Collaborators Page Snapshot

- Date recorded: 2026-05-21
- Source: user-provided screenshot of the Meta Research Tools Manager application draft
- Page section: `Collaborators`
- URL / application identifier: intentionally omitted from git
- Screenshot files: not stored in git
- Repo-safe privacy note: this note records the collaborator-page field states only. It does not record the visible application ID, logged-in account identity, screenshots, collaborator email addresses, invitation links, access credentials, raw Threads evidence, handles, URLs, or item-level controlled artifacts.

## Visible Page State

- Visible application title at the top: `Metadata-Driven Public Scam Pattern Analysis and Reviewer Su`
- Left application list item: truncated application title with `Draft` status
- Left application stepper state:
  - `Personal information`: completed
  - `Organization`: completed
  - `Research details`: completed
  - `Collaborators`: active
  - `Terms and Conditions`: not yet completed in the visible screenshot
- Main panel title: `Collaborators`
- Main panel status marker: optional page
- Bottom controls visible: `Back`, `Save`, and `Next`
- `Next` appears enabled even though no collaborator email is filled.

## Visible Instructions

The visible helper text explains that:

- the lead researcher can add collaborators to the research program;
- each invitee receives an email with a link;
- the link takes the invitee to an application where they can enter their details;
- the invitee can submit an application to join the research program;
- a `Learn more about inviting collaborators` link is available.

## Filled And Empty Fields

| Field / control | Observed value / state | Repo interpretation |
|---|---|---|
| Collaborator email | Blank | No collaborator email is filled in the visible screenshot. |
| Collaborator email placeholder | `Organizational email` | Future collaborator invitations should use organizational email addresses. |
| Additional collaborator row | Not present | No additional collaborator field has been added beyond the first visible blank field. |
| Row actions / overflow menu | Visible ellipsis control | Available, but no row action was used in the screenshot. |
| `Add another` button | Visible | Can add another collaborator email field; not used in the screenshot. |
| `Back` button | Visible | Navigates to the prior section. |
| `Save` button | Visible | Save control is available. |
| `Next` button | Visible and appears enabled | The optional collaborator page can likely be skipped with no collaborator email. |

## Current Draft Status

- Collaborator count filled in visible form: `0`
- Collaborator email fields present: `1`
- Collaborator email fields filled: `0`
- Collaborator email fields blank: `1`
- No collaborator invitation appears to have been sent from the visible page.
- No collaborator personal data is recorded in git.

## Submission Boundary

This page is optional in the visible UI, but the project should not treat collaborator handling as casual.

Before submission:

- Decide whether any collaborator must be added before the lead application is submitted.
- If collaborators are added, use organizational email addresses.
- Do not record collaborator email addresses, invitation links, application IDs, collaborator application status, or collaborator personal details in git.
- Repo-visible planning may record only aggregate state, such as `0 collaborators added`, `collaborator_invites_pending`, or `collaborators_approved`, unless a later explicit governance decision approves a redacted artifact.

## Governance Reading

The collaborator step matters because collaborators become part of the governed research program:

- each collaborator is invited by the lead researcher;
- each collaborator enters their own details;
- each collaborator submits an application to join the research program;
- collaborator access should not be assumed until the relevant application is approved;
- collaborator data access should follow the same official-access, minimization, storage, export, and publication limits as the lead researcher.

Current safe action from the visible screenshot:

- It is acceptable to proceed with zero collaborators only if the research program genuinely does not need collaborator access at submission time.
- If collaborators are needed for NYCU, CIB, annotation, or engineering roles, their exact access role and institutional email should be decided outside git before adding them.
