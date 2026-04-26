from __future__ import annotations

import gzip
from datetime import UTC, datetime
from typing import Any

import httpx

from normalize.schema import Event, GeoPoint, stable_id

# Source contract: public GitHub mirror documented at
# https://github.com/cyterat/deepstate-map-data
GEOJSON_GZ_URL = (
    "https://raw.githubusercontent.com/cyterat/deepstate-map-data/main/"
    "deepstate-map-data.geojson.gz"
)


def _centroid_from_geometry(geometry: dict[str, Any]) -> GeoPoint | None:
    coords = geometry.get("coordinates")
    if not coords:
        return None
    points: list[tuple[float, float]] = []

    def walk(value: Any) -> None:
        if (
            isinstance(value, list)
            and len(value) >= 2
            and all(isinstance(item, int | float) for item in value[:2])
        ):
            points.append((float(value[1]), float(value[0])))
            return
        if isinstance(value, list):
            for item in value:
                walk(item)

    walk(coords)
    if not points:
        return None
    sample = points[:200]
    lat = sum(point[0] for point in sample) / len(sample)
    lon = sum(point[1] for point in sample) / len(sample)
    return GeoPoint(lat=lat, lon=lon, label="DeepStateMap occupied-area centroid")


def fetch_events(limit: int = 3, offline: bool = False) -> list[Event]:
    if offline:
        return fixture_events()
    try:
        response = httpx.get(GEOJSON_GZ_URL, timeout=30, follow_redirects=True)
        response.raise_for_status()
        payload = gzip.decompress(response.content)
        geojson = httpx.Response(200, content=payload).json()
        events: list[Event] = []
        for index, feature in enumerate(geojson.get("features", [])[:limit]):
            props = feature.get("properties", {})
            geo = _centroid_from_geometry(feature.get("geometry", {}))
            events.append(
                Event(
                    id=stable_id("deepstatemap", index, props),
                    ts=datetime.now(UTC),
                    title=f"DeepStateMap occupied territory feature {index + 1}",
                    source="DeepStateMap mirror",
                    source_url=GEOJSON_GZ_URL,
                    geo=geo,
                    actors=["Russia", "Ukraine"],
                    raw={"properties": props},
                    severity=3,
                    tags=["conflict", "ukraine", "map"],
                )
            )
        return events or fixture_events()
    except Exception as exc:
        events = fixture_events()
        for event in events:
            event.raw["fallback_reason"] = str(exc)
        return events


def fixture_events() -> list[Event]:
    return [
        Event(
            id=stable_id("deepstatemap-fixture", "donetsk"),
            ts=datetime(2026, 4, 26, tzinfo=UTC),
            title="DeepStateMap fixture: front-line activity in eastern Ukraine",
            source="DeepStateMap mirror",
            source_url=GEOJSON_GZ_URL,
            geo=GeoPoint(lat=48.0159, lon=37.8029, label="Donetsk region"),
            actors=["Russia", "Ukraine"],
            raw={"fixture": True},
            severity=3,
            tags=["conflict", "ukraine", "map"],
            mock=True,
        )
    ]

