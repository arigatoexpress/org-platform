from __future__ import annotations

import json
import os
from datetime import UTC, datetime
from pathlib import Path

import httpx

from normalize.schema import Event, GeoPoint, stable_id

# Windward is a paid product. Do not invent endpoints. This connector only calls an
# operator-provided base URL and token. Product surface: https://insights.windward.ai/
WINDWARD_PRODUCT_URL = "https://insights.windward.ai/"
FIXTURE = Path(__file__).with_name("fixtures").joinpath("windward_alert.json")


def fetch_events(limit: int = 1, offline: bool = False) -> list[Event]:
    base_url = os.getenv("WINDWARD_API_BASE_URL")
    token = os.getenv("WINDWARD_API_TOKEN")
    if offline or not (base_url and token):
        return fixture_events()[:limit]
    response = httpx.get(
        base_url.rstrip("/") + "/alerts",
        headers={"Authorization": f"Bearer {token}"},
        timeout=30,
    )
    response.raise_for_status()
    records = response.json().get("alerts", [])
    return [_event_from_record(record, mock=False) for record in records[:limit]]


def fixture_events() -> list[Event]:
    return [_event_from_record(json.loads(FIXTURE.read_text()), mock=True)]


def _event_from_record(record: dict, mock: bool) -> Event:
    return Event(
        id=stable_id("windward", record.get("vessel_mmsi"), record.get("alert_type")),
        ts=datetime.fromisoformat(record["ts"]).replace(tzinfo=UTC),
        title=record["title"],
        source="Windward",
        source_url=WINDWARD_PRODUCT_URL,
        geo=GeoPoint(lat=record["lat"], lon=record["lon"], label=record.get("area")),
        actors=[str(record.get("vessel_mmsi"))],
        raw=record,
        severity=4,
        tags=["maritime", "sanctions", "windward"],
        mock=mock,
    )

