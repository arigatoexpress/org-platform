from __future__ import annotations

import json
import os
from datetime import UTC, datetime
from pathlib import Path

from normalize.schema import Event, GeoPoint, stable_id

# Official AISStream WebSocket documentation:
# https://aisstream.io/documentation.html
AISSTREAM_DOCS = "https://aisstream.io/documentation.html"
FIXTURE = Path(__file__).with_name("fixtures").joinpath("position_report.json")


def fetch_events(limit: int = 1, offline: bool = False) -> list[Event]:
    if offline or not os.getenv("AISSTREAM_API_KEY"):
        return fixture_events()[:limit]
    # Live websocket collection is intentionally not started in a demo command because it can run
    # indefinitely. Production worker should subscribe server-side using AISSTREAM_API_KEY.
    return fixture_events()[:limit]


def fixture_events() -> list[Event]:
    payload = json.loads(FIXTURE.read_text())
    report = payload["Message"]["PositionReport"]
    return [
        Event(
            id=stable_id("ais-fixture", report["UserID"], report["Latitude"], report["Longitude"]),
            ts=datetime(2026, 4, 26, tzinfo=UTC),
            title=f"AIS fixture position report for MMSI {report['UserID']}",
            source="AISStream",
            source_url=AISSTREAM_DOCS,
            geo=GeoPoint(lat=report["Latitude"], lon=report["Longitude"], label="Fixture vessel"),
            actors=[str(report["UserID"])],
            raw=payload,
            severity=2,
            tags=["ais", "maritime", "shipping"],
            mock=True,
        )
    ]

