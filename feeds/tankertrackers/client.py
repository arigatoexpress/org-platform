from __future__ import annotations

import os
from datetime import UTC, datetime

from normalize.schema import Event, stable_id

TANKERTRACKERS_URL = "https://x.com/TankerTrackers"


def fetch_events(limit: int = 1, offline: bool = False) -> list[Event]:
    if offline or not os.getenv("X_BEARER_TOKEN"):
        return fixture_events()[:limit]
    # Official X API integration belongs here once X_BEARER_TOKEN is provisioned.
    return fixture_events()[:limit]


def fixture_events() -> list[Event]:
    return [
        Event(
            id=stable_id("tankertrackers-fixture", "iran-export-watch"),
            ts=datetime(2026, 4, 26, tzinfo=UTC),
            title="Fixture: TankerTrackers-style Iran export watch item",
            source="TankerTrackers",
            source_url=TANKERTRACKERS_URL,
            actors=["Iran-linked tanker"],
            raw={"fixture": True},
            severity=3,
            tags=["maritime", "iran", "oil", "shipping"],
            mock=True,
        )
    ]

