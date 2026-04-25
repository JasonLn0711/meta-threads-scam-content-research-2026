#!/usr/bin/env python3
"""Prepare controlled browser/API access paths without exposing secrets.

This script is repo-safe by default:

- it does not collect Threads items;
- it does not print token, cookie, or raw response values;
- it writes session/API artifacts only to the outside-git controlled store;
- it performs live API probing only when --execute-api-probe is provided.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src" / "data_collection"))

from session_access import (  # noqa: E402
    DEFAULT_ENV_FILE,
    DEFAULT_STORAGE_STATE,
    AccessCheck,
    api_probe,
    check_api_env,
    controlled_store_path,
    ensure_controlled_store_layout,
    import_storage_state,
    validate_storage_state,
)


RUN_ID = "CRAWL-THREADS-PILOT-V1-0008"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Prepare approved browser-rendered or API/session-aware access without storing secrets in git."
    )
    parser.add_argument(
        "--controlled-store",
        type=Path,
        help="Outside-git controlled store path. Defaults to the sibling controlled-store directory.",
    )
    parser.add_argument(
        "--init-controlled-store",
        action="store_true",
        help="Create expected controlled-store directories and safe template files.",
    )
    parser.add_argument(
        "--import-storage-state",
        type=Path,
        help="Import an approved Playwright-compatible storage_state JSON into controlled storage.",
    )
    parser.add_argument(
        "--check-storage-state",
        action="store_true",
        help="Check the controlled-store browser storage-state artifact shape.",
    )
    parser.add_argument(
        "--check-api-env",
        action="store_true",
        help="Check controlled API env key presence without printing values.",
    )
    parser.add_argument(
        "--api-dry-run",
        action="store_true",
        help="Check whether API probe inputs are present without making a network request.",
    )
    parser.add_argument(
        "--execute-api-probe",
        action="store_true",
        help="Execute the approved API probe and write raw output only to controlled storage.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print repo-safe JSON summary instead of a Markdown table.",
    )
    parser.add_argument(
        "--require-ready",
        action="store_true",
        help="Exit nonzero if any requested path is missing, warning, error, or not_ready.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    store = controlled_store_path(args.controlled_store)
    checks: list[AccessCheck] = []

    if args.init_controlled_store:
        paths = ensure_controlled_store_layout(store)
        checks.extend(AccessCheck("controlled_store_dir", "ok", path.name) for path in paths)
        checks.extend(write_templates(store))

    storage_state_path = store / "SESSION-ARTIFACTS" / DEFAULT_STORAGE_STATE
    if args.import_storage_state:
        checks.extend(import_storage_state(args.import_storage_state.expanduser().resolve(), storage_state_path))

    if args.check_storage_state:
        checks.extend(validate_storage_state(storage_state_path))

    env_path = store / "CREDENTIALS" / DEFAULT_ENV_FILE
    if args.check_api_env:
        checks.extend(check_api_env(env_path))

    if args.api_dry_run:
        checks.extend(api_probe(env_path, store=store, run_id=RUN_ID, dry_run=True))

    if args.execute_api_probe:
        checks.extend(api_probe(env_path, store=store, run_id=RUN_ID, dry_run=False))

    if not checks:
        checks.append(AccessCheck("nothing_requested", "warning", "choose an init/check/import/probe option"))

    print_checks(checks, as_json=args.json)
    if args.require_ready and any(check.status not in {"ok", "present", "dry_run_ready", "completed"} for check in checks):
        return 1
    return 0


def write_templates(store: Path) -> list[AccessCheck]:
    session_readme = store / "SESSION-ARTIFACTS" / "browser_storage_state_README.md"
    if not session_readme.exists():
        session_readme.write_text(
            """# Browser Storage State

Place the approved browser-rendered storage state here as:

```text
SESSION-ARTIFACTS/browser_storage_state_0001.json
```

Rules:

- This file must stay outside git.
- It must be exported only from the approved session/account/path.
- Do not commit cookies, local storage, browser profiles, screenshots, HAR files, or raw page output.
- Validate the shape with:

```bash
python scripts/prepare_controlled_access_path.py --check-storage-state
```
""",
            encoding="utf-8",
        )

    storage_template = store / "SESSION-ARTIFACTS" / "browser_storage_state_TEMPLATE.json"
    if not storage_template.exists():
        storage_template.write_text(
            json.dumps(
                {
                    "cookies": [],
                    "origins": [],
                    "notice": "Template only. Replace with approved exported storage_state as browser_storage_state_0001.json.",
                },
                indent=2,
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )

    env_template = store / "CREDENTIALS" / "API_CREDENTIALS.controlled.env.template"
    if not env_template.exists():
        env_template.write_text(
            """# CONTROLLED API CREDENTIAL TEMPLATE - DO NOT COMMIT VALUES
META_API_PROFILE=
META_API_CLIENT_ID=
META_API_CLIENT_SECRET=
META_API_ACCESS_TOKEN=
META_API_REFRESH_TOKEN=
META_API_PROBE_URL=
TOKEN_ROTATION_OWNER=
TOKEN_REVIEW_DATE=
ALLOWED_OPERATOR_IDS=
RAW_OUTPUT_ROOT=
AUTOMATION_LOG_ROOT=
""",
            encoding="utf-8",
        )

    return [
        AccessCheck("session_readme", "ok", session_readme.name),
        AccessCheck("storage_state_template", "ok", storage_template.name),
        AccessCheck("api_env_template", "ok", env_template.name),
    ]


def print_checks(checks: list[AccessCheck], *, as_json: bool = False) -> None:
    if as_json:
        print(json.dumps([check.__dict__ for check in checks], indent=2, sort_keys=True))
        return
    print("| Check | Status | Detail |")
    print("|---|---|---|")
    for check in checks:
        print(f"| `{check.name}` | `{check.status}` | {check.detail} |")


if __name__ == "__main__":
    raise SystemExit(main())
