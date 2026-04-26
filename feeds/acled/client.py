from __future__ import annotations

import json
import os
from datetime import UTC, datetime
from pathlib import Path

import httpx

from normalize.schema import Event, GeoPoint, stable_id

# Official ACLED API docs:
# https://acleddata.com/acled-api-documentation
ACLED_DOCS = "https://acleddata.com/acled-api-documentation"
FIXTURE = Path(__file__).with_name("fixtures").joinpath("acled_events.json")


def fetch_events(limit: int = 3, offline: bool = False) -> list[Event]:
    if offline or not (os.getenv("ACLED_API_KEY") and os.getenv("ACLED_EMAIL")):
        return fixture_events()[:limit]
    params = {
        "key": os.environ["ACLED_API_KEY"],
        "email": os.environ["ACLED_EMAIL"],
        "limit": limit,
        "country": "Yemen",
        "event_date_where": ">=",
        "event_date": "2026-01-01",
    }
    try:
        response = httpx.get("https://api.acleddata.com/acled/read", params=params, timeout=30)
        response.raise_for_status()
        data = response.json().get("data", [])
        return [_event_from_record(record, mock=False) for record in data[:limit]]
    except Exception:
        return fixture_events()[:limit]


def fixture_events() -> list[Event]:
    return [
        _event_from_record(record, mock=True)
        for record in json.loads(FIXTURE.read_text()).get("data", [])
    ]


def _event_from_record(record: dict, mock: bool) -> Event:
    lat = float(record.get("latitude") or 15.3694)
    lon = float(record.get("longitude") or 44.191)
    event_date = record.get("event_date") or "2026-04-26"
    ts = datetime.fromisoformat(event_date).replace(tzinfo=UTC)
    actors = [value for value in [record.get("actor1"), record.get("actor2")] if value]
    return Event(
        id=stable_id("acled", record.get("event_id_cnty"), record.get("event_date")),
        ts=ts,
        title=record.get("notes") or "ACLED conflict event",
        source="ACLED",
        source_url=ACLED_DOCS,
        geo=GeoPoint(lat=lat, lon=lon, label=record.get("location")),
        actors=actors,
        raw=record,
        severity=3,
        tags=["conflict", "acled", "red-sea"],
        mock=mock,
    )

