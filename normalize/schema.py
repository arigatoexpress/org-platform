from __future__ import annotations

from datetime import UTC, datetime
from hashlib import sha1
from typing import Any

from pydantic import BaseModel, Field, HttpUrl


class GeoPoint(BaseModel):
    lat: float = Field(ge=-90, le=90)
    lon: float = Field(ge=-180, le=180)
    label: str | None = None


class Event(BaseModel):
    id: str
    ts: datetime
    title: str
    source: str
    source_url: HttpUrl | str
    geo: GeoPoint | None = None
    actors: list[str] = Field(default_factory=list)
    raw: dict[str, Any] = Field(default_factory=dict)
    severity: int = Field(default=1, ge=1, le=5)
    tags: list[str] = Field(default_factory=list)
    mock: bool = False

    @property
    def source_label(self) -> str:
        return f"[MOCK] {self.source}" if self.mock else self.source


def now_utc() -> datetime:
    return datetime.now(UTC)


def stable_id(source: str, *parts: object) -> str:
    payload = "|".join([source, *(str(part) for part in parts)])
    return sha1(payload.encode("utf-8")).hexdigest()[:16]


def events_to_jsonable(events: list[Event]) -> list[dict[str, Any]]:
    return [event.model_dump(mode="json") for event in events]

