"""Controlled browser/API access helpers.

These helpers prepare and verify approved session-aware access paths. They do
not authorize collection, and they never print credential values or raw
responses. Raw API output, if explicitly requested by a run record, is written
only to the outside-git controlled store.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
import json
import os
import shutil
from typing import Any
from urllib import error, request
from urllib.parse import urlparse


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONTROLLED_STORE = REPO_ROOT.parent / f"{REPO_ROOT.name}-controlled-store"
DEFAULT_STORAGE_STATE = "browser_storage_state_0001.json"
DEFAULT_ENV_FILE = "API_CREDENTIALS.controlled.env"
PLACEHOLDER_MARKERS = ("CONTROLLED_", "FILL_", "REPLACE_", "PENDING_", "EXAMPLE_", "TEMPLATE_")


@dataclass(frozen=True)
class AccessCheck:
    name: str
    status: str
    detail: str


def controlled_store_path(path: str | Path | None = None) -> Path:
    return Path(path).expanduser().resolve() if path else DEFAULT_CONTROLLED_STORE


def ensure_controlled_store_layout(store: Path) -> list[Path]:
    created_or_existing: list[Path] = []
    for relative in (
        "SESSION-ARTIFACTS",
        "CREDENTIALS",
        "RAW/controlled-pilot",
        "AUTOMATION-LOGS",
        "REDACTED",
    ):
        path = store / relative
        path.mkdir(parents=True, exist_ok=True)
        created_or_existing.append(path)
    return created_or_existing


def load_env_file(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if not path.exists():
        return values
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key:
            values[key] = value
    return values


def check_api_env(env_path: Path) -> list[AccessCheck]:
    values = load_env_file(env_path)
    required_keys = (
        "META_API_ACCESS_TOKEN",
        "META_API_PROFILE",
        "RAW_OUTPUT_ROOT",
        "AUTOMATION_LOG_ROOT",
    )
    checks: list[AccessCheck] = []
    for key in required_keys:
        value = values.get(key, "")
        status = _secret_status(value)
        checks.append(AccessCheck(key, status, _value_shape(value)))

    optional_probe_url = values.get("META_API_PROBE_URL", "")
    checks.append(
        AccessCheck(
            "META_API_PROBE_URL",
            _url_status(optional_probe_url),
            _url_shape(optional_probe_url),
        )
    )
    return checks


def import_storage_state(source: Path, destination: Path) -> list[AccessCheck]:
    checks = validate_storage_state(source)
    if any(check.status == "error" for check in checks):
        return checks
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    return [*checks, AccessCheck("storage_state_imported", "ok", destination.name)]


def validate_storage_state(path: Path) -> list[AccessCheck]:
    if not path.exists():
        return [AccessCheck("storage_state_file", "missing", path.name)]
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [AccessCheck("storage_state_json", "error", f"invalid JSON: line {exc.lineno}")]

    checks: list[AccessCheck] = []
    cookies = payload.get("cookies")
    origins = payload.get("origins")
    checks.append(_typed_list_check("cookies", cookies))
    checks.append(_typed_list_check("origins", origins))
    if isinstance(cookies, list):
        checks.append(AccessCheck("cookie_count", "ok" if cookies else "warning", str(len(cookies))))
    if isinstance(origins, list):
        checks.append(AccessCheck("origin_count", "ok" if origins else "warning", str(len(origins))))
    return checks


def api_probe(
    env_path: Path,
    *,
    store: Path,
    run_id: str,
    dry_run: bool = True,
    timeout_seconds: int = 20,
) -> list[AccessCheck]:
    values = load_env_file(env_path)
    token = values.get("META_API_ACCESS_TOKEN", "")
    probe_url = values.get("META_API_PROBE_URL", "")
    checks = check_api_env(env_path)
    if not token or not probe_url:
        return [*checks, AccessCheck("api_probe", "not_ready", "token or probe URL missing")]
    if dry_run:
        return [*checks, AccessCheck("api_probe", "dry_run_ready", _url_shape(probe_url))]

    req = request.Request(
        probe_url,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
            "User-Agent": "threads-pilot-controlled-access/1.0",
        },
        method="GET",
    )
    timestamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    raw_path = store / "RAW" / "controlled-pilot" / f"{run_id}_api_probe_{timestamp}.json"
    log_path = store / "AUTOMATION-LOGS" / f"{run_id}_api_probe_{timestamp}.jsonl"
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        with request.urlopen(req, timeout=timeout_seconds) as response:  # noqa: S310 - controlled approved URL only.
            status_code = response.status
            body = response.read()
    except error.HTTPError as exc:
        status_code = exc.code
        body = exc.read()
    except error.URLError as exc:
        _write_controlled_log(log_path, run_id, "network_error", _url_shape(probe_url), str(exc.reason))
        return [*checks, AccessCheck("api_probe", "network_error", str(exc.reason))]

    raw_path.write_bytes(body)
    _write_controlled_log(log_path, run_id, "completed", _url_shape(probe_url), f"http_status={status_code}")
    return [
        *checks,
        AccessCheck("api_probe", "completed", f"http_status={status_code}"),
        AccessCheck("raw_output", "controlled_store_only", raw_path.name),
        AccessCheck("automation_log", "controlled_store_only", log_path.name),
    ]


def _write_controlled_log(path: Path, run_id: str, status: str, endpoint_shape: str, detail: str) -> None:
    event = {
        "timestamp_utc": datetime.now(UTC).isoformat(),
        "run_id": run_id,
        "status": status,
        "endpoint_shape": endpoint_shape,
        "detail": detail,
        "repo_visible_raw_output": False,
    }
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, ensure_ascii=True, sort_keys=True))
        handle.write("\n")


def _typed_list_check(name: str, value: Any) -> AccessCheck:
    if isinstance(value, list):
        return AccessCheck(name, "ok", "list")
    return AccessCheck(name, "error", f"expected list, got {type(value).__name__}")


def _value_shape(value: str) -> str:
    if not value:
        return "empty"
    if _looks_placeholder(value):
        return "placeholder_or_test_value"
    return "non_empty"


def _url_shape(value: str) -> str:
    if not value:
        return "empty"
    parsed = urlparse(value)
    host = parsed.netloc or "missing-host"
    path = parsed.path or "/"
    return f"{parsed.scheme or 'missing-scheme'}://{host}{path}"


def _secret_status(value: str) -> str:
    if not value:
        return "missing_or_empty"
    if _looks_placeholder(value):
        return "placeholder_or_test_value"
    return "present"


def _url_status(value: str) -> str:
    if not value:
        return "missing_or_empty"
    if _looks_placeholder(value):
        return "placeholder_or_test_value"
    parsed = urlparse(value)
    if not parsed.scheme or not parsed.netloc:
        return "invalid_url_shape"
    return "present"


def _looks_placeholder(value: str) -> bool:
    upper = value.upper()
    return any(marker in upper for marker in PLACEHOLDER_MARKERS)


def env_default(name: str, default: str) -> str:
    return os.environ.get(name, default)
