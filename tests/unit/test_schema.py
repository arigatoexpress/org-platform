from datetime import UTC, datetime

import pytest

from normalize.schema import Event, GeoPoint, stable_id


def test_event_schema_accepts_expected_shape() -> None:
    event = Event(
        id=stable_id("test", "one"),
        ts=datetime(2026, 4, 26, tzinfo=UTC),
        title="Test event",
        source="fixture",
        source_url="https://example.com",
        geo=GeoPoint(lat=10, lon=20),
        severity=3,
        tags=["test"],
    )

    assert event.id
    assert event.geo is not None
    assert event.geo.lat == 10


def test_geo_validation_rejects_bad_latitude() -> None:
    with pytest.raises(ValueError):
        GeoPoint(lat=120, lon=20)

