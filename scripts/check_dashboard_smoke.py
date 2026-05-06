#!/usr/bin/env python3
"""Read-only dashboard readiness smoke check."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from urllib.parse import urlparse

REPO_ROOT = Path(__file__).resolve().parents[1]
DASHBOARD_DIR = REPO_ROOT / "surface" / "dashboard"


class SmokeFailure(Exception):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SmokeFailure(message)


def load_json(path: Path) -> object:
    require(path.is_file(), f"missing required file: {path.relative_to(REPO_ROOT)}")
    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        raise SmokeFailure(f"invalid JSON in {path.relative_to(REPO_ROOT)}: {exc}") from exc


def require_string(record: dict[str, object], key: str, label: str) -> str:
    value = record.get(key)
    require(isinstance(value, str) and value.strip(), f"{label} has invalid {key!r}")
    return value


def check_dashboard_files() -> None:
    required_files = [
        DASHBOARD_DIR / "app" / "layout.tsx",
        DASHBOARD_DIR / "app" / "page.tsx",
        DASHBOARD_DIR / "app" / "styles.css",
        DASHBOARD_DIR / "next.config.mjs",
        DASHBOARD_DIR / "package-lock.json",
        DASHBOARD_DIR / "package.json",
        DASHBOARD_DIR / "public" / "crypto.json",
        DASHBOARD_DIR / "public" / "events.json",
        DASHBOARD_DIR / "tsconfig.json",
    ]
    for path in required_files:
        require(path.is_file(), f"missing required file: {path.relative_to(REPO_ROOT)}")


def check_public_json_is_tracked() -> None:
    paths = [
        "surface/dashboard/public/events.json",
        "surface/dashboard/public/crypto.json",
    ]
    result = subprocess.run(
        ["git", "-C", str(REPO_ROOT), "ls-files", "--error-unmatch", *paths],
        capture_output=True,
        text=True,
    )
    require(
        result.returncode == 0,
        f"dashboard public JSON is not fully tracked: {result.stderr.strip()}",
    )


def check_package_scripts() -> None:
    package = load_json(DASHBOARD_DIR / "package.json")
    require(isinstance(package, dict), "package.json must contain an object")
    scripts = package.get("scripts")
    require(isinstance(scripts, dict), "package.json missing scripts object")
    for script_name in ("dev", "build", "start"):
        require(
            isinstance(scripts.get(script_name), str),
            f"package.json missing {script_name} script",
        )

    lockfile = load_json(DASHBOARD_DIR / "package-lock.json")
    require(isinstance(lockfile, dict), "package-lock.json must contain an object")
    lock_packages = lockfile.get("packages")
    require(isinstance(lock_packages, dict), "package-lock.json missing packages object")
    root_package = lock_packages.get("")
    require(isinstance(root_package, dict), "package-lock.json missing root package metadata")
    require(
        root_package.get("name") == package.get("name"),
        "package-lock.json root package name does not match package.json",
    )


def check_events() -> int:
    events = load_json(DASHBOARD_DIR / "public" / "events.json")
    require(isinstance(events, list) and events, "public/events.json must contain events")

    for index, event in enumerate(events):
        label = f"event[{index}]"
        require(isinstance(event, dict), f"{label} must be an object")
        require_string(event, "id", label)
        require_string(event, "title", label)
        require_string(event, "source", label)
        source_url = require_string(event, "source_url", label)
        parsed_url = urlparse(source_url)
        require(parsed_url.scheme in {"http", "https"}, f"{label} source_url must be http(s)")

        severity = event.get("severity")
        require(isinstance(severity, int) and 1 <= severity <= 5, f"{label} severity must be 1-5")
        require(isinstance(event.get("mock"), bool), f"{label} mock must be a boolean")

        tags = event.get("tags")
        require(
            isinstance(tags, list) and all(isinstance(tag, str) and tag for tag in tags),
            f"{label} tags must be a non-empty string list",
        )

        geo = event.get("geo")
        if geo is not None:
            require(isinstance(geo, dict), f"{label} geo must be an object or null")
            lat = geo.get("lat")
            lon = geo.get("lon")
            require(isinstance(lat, int | float) and -90 <= lat <= 90, f"{label} geo.lat invalid")
            require(isinstance(lon, int | float) and -180 <= lon <= 180, f"{label} geo.lon invalid")

    return len(events)


def check_tokens() -> int:
    tokens = load_json(DASHBOARD_DIR / "public" / "crypto.json")
    require(isinstance(tokens, list) and tokens, "public/crypto.json must contain tokens")

    for index, token in enumerate(tokens):
        label = f"token[{index}]"
        require(isinstance(token, dict), f"{label} must be an object")
        require_string(token, "id", label)
        require_string(token, "symbol", label)
        require_string(token, "name", label)
        score = token.get("score")
        require(isinstance(score, int | float), f"{label} score must be numeric")
        require(
            isinstance(token.get("feature_importances"), dict),
            f"{label} feature_importances missing",
        )
        risk_flags = token.get("risk_flags")
        require(
            isinstance(risk_flags, list)
            and all(isinstance(flag, str) and flag for flag in risk_flags),
            f"{label} risk_flags must be a string list",
        )

    return len(tokens)


def main() -> int:
    try:
        check_dashboard_files()
        check_public_json_is_tracked()
        check_package_scripts()
        event_count = check_events()
        token_count = check_tokens()
    except SmokeFailure as exc:
        print(f"dashboard-smoke failed: {exc}")
        return 1

    print(f"dashboard-smoke ok: {event_count} events, {token_count} tokens")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
