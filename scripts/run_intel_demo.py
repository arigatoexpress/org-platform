from __future__ import annotations

import json
import os
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from normalize.schema import Event


def _ensure_repo_root_on_path() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    repo_root_str = str(repo_root)
    if repo_root_str not in sys.path:
        sys.path.insert(0, repo_root_str)


_ensure_repo_root_on_path()


def main() -> None:
    from feeds.acled.client import fetch_events as fetch_acled
    from feeds.ais.client import fetch_events as fetch_ais
    from feeds.deepstatemap.client import fetch_events as fetch_deepstate
    from feeds.ofac.client import fetch_events as fetch_ofac
    from feeds.tankertrackers.client import fetch_events as fetch_tankertrackers
    from feeds.uani.client import fetch_events as fetch_uani
    from feeds.windward.client import fetch_events as fetch_windward
    from normalize.schema import events_to_jsonable
    from store.duck import write_event_store

    root = Path(os.getenv("ORG_PLATFORM_OUTPUT_DIR", ".")).resolve()
    offline = os.getenv("ORG_PLATFORM_OFFLINE", "").lower() in {"1", "true", "yes"}
    today = datetime.now(UTC).date().isoformat()

    events = []
    events.extend(fetch_deepstate(limit=2, offline=offline))
    events.extend(fetch_ofac(query="IRAN", limit=4, offline=offline))
    events.extend(fetch_uani(limit=2, offline=offline))
    events.extend(fetch_ais(limit=1, offline=offline))
    events.extend(fetch_acled(limit=2, offline=offline))
    events.extend(fetch_windward(limit=1, offline=offline))
    events.extend(fetch_tankertrackers(limit=1, offline=offline))

    data_dir = root / "data" / "intel"
    data_dir.mkdir(parents=True, exist_ok=True)
    events_path = data_dir / "events.json"
    events_path.write_text(json.dumps(events_to_jsonable(events), indent=2) + "\n")

    dashboard_path = root / "surface" / "dashboard" / "public" / "events.json"
    dashboard_path.parent.mkdir(parents=True, exist_ok=True)
    dashboard_path.write_text(json.dumps(events_to_jsonable(events), indent=2) + "\n")

    store_written = write_event_store(
        events,
        root / "data" / "store" / "events.duckdb",
        required=not offline,
    )

    brief_path = root / "Intelligence" / f"iran-shipping-{today}.md"
    brief_path.parent.mkdir(parents=True, exist_ok=True)
    brief_path.write_text(render_brief(events, today))

    print(f"Wrote {len(events)} events to {events_path}")
    if not store_written:
        print("Skipped DuckDB event store because duckdb is not installed in offline mode")
    print(f"Wrote brief to {brief_path}")
    print(f"Wrote dashboard data to {dashboard_path}")


def render_brief(events: list[Event], today: str) -> str:
    live_count = sum(not event.mock for event in events)
    mock_count = sum(event.mock for event in events)
    lines = [
        f"# Iran Sanctions Evasion Shipping Watch - {today}",
        "",
        f"Source status: {live_count} live-derived events, {mock_count} fixture-derived events.",
        "",
        "## Executive Read",
        "",
        (
            "This first vertical slice fuses sanctions, maritime, and conflict indicators into a "
            "single normalized event stream. Treat `[MOCK]` items as connector-shape proof, not "
            "intelligence claims."
        ),
        "",
        "## Events",
        "",
    ]
    for event in sorted(events, key=lambda item: item.severity, reverse=True):
        mock = " [MOCK]" if event.mock else ""
        geo = f" ({event.geo.lat:.3f}, {event.geo.lon:.3f})" if event.geo else ""
        actors = ", ".join(event.actors) if event.actors else "n/a"
        tags = ", ".join(event.tags)
        lines.extend(
            [
                f"### {event.title}{mock}",
                "",
                f"- Source: {event.source} - {event.source_url}",
                f"- Timestamp: {event.ts.isoformat()}",
                f"- Severity: {event.severity}",
                f"- Actors: {actors}",
                f"- Geo: {event.geo.label if event.geo else 'n/a'}{geo}",
                f"- Tags: {tags}",
                "",
            ]
        )
    lines.extend(
        [
            "## Next Collection Tasks",
            "",
            "- Provision Windward credentials and replace fixture alert with official API output.",
            "- Provision AISStream key and run a bounded server-side Persian Gulf sample.",
            "- Provision ACLED credentials and add Yemen/Red Sea filters.",
            "- Decide whether TankerTrackers uses official X API or a licensed archive.",
            "",
        ]
    )
    return "\n".join(lines)


if __name__ == "__main__":
    main()
