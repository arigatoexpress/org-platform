from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path
from xml.etree import ElementTree as ET

import httpx

from normalize.schema import Event, stable_id

BLOG_URL = "https://www.unitedagainstnucleariran.com/blog"
RSS_CANDIDATES = [
    "https://www.unitedagainstnucleariran.com/blog/rss.xml",
    "https://www.unitedagainstnucleariran.com/rss.xml",
]
FIXTURE = Path(__file__).with_name("fixtures").joinpath("uani_blog.xml")


def fetch_events(limit: int = 3, offline: bool = False) -> list[Event]:
    if offline:
        return _events_from_xml(FIXTURE.read_text(), mock=True)[:limit]
    for url in RSS_CANDIDATES:
        try:
            response = httpx.get(url, timeout=20, follow_redirects=True)
            response.raise_for_status()
            return _events_from_xml(response.text, mock=False)[:limit]
        except Exception:
            continue
    return _events_from_xml(FIXTURE.read_text(), mock=True)[:limit]


def _events_from_xml(xml_text: str, mock: bool) -> list[Event]:
    root = ET.fromstring(xml_text)
    events: list[Event] = []
    for item in root.findall(".//item"):
        title = item.findtext("title", "UANI item").strip()
        link = item.findtext("link", BLOG_URL).strip()
        pub_date = item.findtext("pubDate")
        ts = _parse_rss_date(pub_date)
        events.append(
            Event(
                id=stable_id("uani", title, link),
                ts=ts,
                title=title,
                source="UANI blog",
                source_url=link,
                actors=["Iran"],
                raw={"pubDate": pub_date, "fixture": mock},
                severity=3,
                tags=["sanctions", "iran", "uani", "shipping"],
                mock=mock,
            )
        )
    return events


def _parse_rss_date(value: str | None) -> datetime:
    if not value:
        return datetime.now(UTC)
    try:
        from email.utils import parsedate_to_datetime

        parsed = parsedate_to_datetime(value)
        return parsed if parsed.tzinfo else parsed.replace(tzinfo=UTC)
    except Exception:
        return datetime.now(UTC)

