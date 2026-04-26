from __future__ import annotations

import xml.etree.ElementTree as ET
from datetime import UTC, datetime

import httpx

from normalize.schema import Event, stable_id

# Official OFAC Sanctions List Service documentation:
# https://ofac.treasury.gov/sanctions-list-service
SDN_XML_URL = "https://sanctionslistservice.ofac.treas.gov/api/PublicationPreview/exports/SDN.XML"


def fetch_events(query: str = "IRAN", limit: int = 5, offline: bool = False) -> list[Event]:
    if offline:
        return fixture_events()
    try:
        response = httpx.get(SDN_XML_URL, timeout=30, follow_redirects=True)
        response.raise_for_status()
        root = ET.fromstring(response.content)
        events: list[Event] = []
        for entry in root.iter():
            if not entry.tag.lower().endswith("sdnentry"):
                continue
            text = " ".join(entry.itertext())
            if query.lower() not in text.lower():
                continue
            name = _first_child_text(entry, "lastName") or _first_child_text(entry, "sdnName")
            sdn_type = _first_child_text(entry, "sdnType") or "unknown"
            program = _first_child_text(entry, "program") or query
            events.append(
                Event(
                    id=stable_id("ofac", name, program, len(events)),
                    ts=datetime.now(UTC),
                    title=f"OFAC SDN match: {name or 'unnamed target'}",
                    source="OFAC SDN",
                    source_url=SDN_XML_URL,
                    actors=[name] if name else [],
                    raw={"sdn_type": sdn_type, "program": program},
                    severity=4,
                    tags=["sanctions", "iran", "ofac"],
                )
            )
            if len(events) >= limit:
                break
        return events or fixture_events()
    except Exception as exc:
        events = fixture_events()
        for event in events:
            event.raw["fallback_reason"] = str(exc)
        return events


def _first_child_text(entry: ET.Element, suffix: str) -> str | None:
    for child in entry.iter():
        if child.tag.lower().endswith(suffix.lower()) and child.text:
            return child.text.strip()
    return None


def fixture_events() -> list[Event]:
    return [
        Event(
            id=stable_id("ofac-fixture", "iran-shipping"),
            ts=datetime(2026, 4, 26, tzinfo=UTC),
            title="OFAC fixture: Iran-linked shipping sanctions target",
            source="OFAC SDN",
            source_url=SDN_XML_URL,
            actors=["Fixture Shipping Co."],
            raw={"fixture": True, "program": "IRAN"},
            severity=4,
            tags=["sanctions", "iran", "ofac"],
            mock=True,
        )
    ]

