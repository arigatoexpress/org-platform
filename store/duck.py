from __future__ import annotations

import json
from pathlib import Path

from normalize.schema import Event


def write_event_store(events: list[Event], db_path: Path) -> None:
    import duckdb

    db_path.parent.mkdir(parents=True, exist_ok=True)
    rows = [
        (
            event.id,
            event.ts.isoformat(),
            event.title,
            event.source,
            str(event.source_url),
            event.geo.lat if event.geo else None,
            event.geo.lon if event.geo else None,
            json.dumps(event.actors),
            event.severity,
            json.dumps(event.tags),
            event.mock,
            json.dumps(event.raw, sort_keys=True),
        )
        for event in events
    ]
    with duckdb.connect(str(db_path)) as con:
        con.execute(
            """
            create or replace table events (
              id varchar,
              ts varchar,
              title varchar,
              source varchar,
              source_url varchar,
              lat double,
              lon double,
              actors json,
              severity integer,
              tags json,
              mock boolean,
              raw json
            )
            """
        )
        if rows:
            con.executemany(
                """
                insert into events
                values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                rows,
            )
