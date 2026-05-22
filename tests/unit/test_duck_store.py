from __future__ import annotations

import builtins
from datetime import UTC, datetime
from pathlib import Path

import pytest

from normalize.schema import Event
from store.duck import write_event_store


def _event() -> Event:
    return Event(
        id="event-1",
        ts=datetime(2026, 5, 22, tzinfo=UTC),
        title="Fixture event",
        source="fixture",
        source_url="https://example.com/source",
        severity=3,
        tags=["fixture"],
        mock=True,
    )


def test_write_event_store_can_skip_missing_duckdb_when_optional(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    real_import = builtins.__import__

    def missing_duckdb(name: str, *args: object, **kwargs: object) -> object:
        if name == "duckdb":
            raise ModuleNotFoundError("No module named 'duckdb'", name="duckdb")
        return real_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", missing_duckdb)

    db_path = tmp_path / "events.duckdb"

    assert write_event_store([_event()], db_path, required=False) is False
    assert not db_path.exists()


def test_write_event_store_requires_duckdb_by_default(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    real_import = builtins.__import__

    def missing_duckdb(name: str, *args: object, **kwargs: object) -> object:
        if name == "duckdb":
            raise ModuleNotFoundError("No module named 'duckdb'", name="duckdb")
        return real_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", missing_duckdb)

    with pytest.raises(ModuleNotFoundError):
        write_event_store([_event()], tmp_path / "events.duckdb")
