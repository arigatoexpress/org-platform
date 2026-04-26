from feeds.uani.client import fetch_events


def test_uani_fixture_parses_events() -> None:
    events = fetch_events(offline=True)

    assert events
    assert events[0].mock is True
    assert "uani" in events[0].tags

