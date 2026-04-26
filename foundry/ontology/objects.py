from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class Vessel(BaseModel):
    mmsi: str
    imo: str | None = None
    name: str | None = None
    flag: str | None = None
    risk_tags: list[str] = Field(default_factory=list)


class Voyage(BaseModel):
    id: str
    vessel_mmsi: str
    origin: str | None = None
    destination: str | None = None
    started_at: datetime | None = None
    ended_at: datetime | None = None


class Sanction(BaseModel):
    id: str
    authority: str
    program: str
    target_name: str
    target_type: str | None = None
    listed_at: datetime | None = None


class ConflictEvent(BaseModel):
    id: str
    ts: datetime
    lat: float | None = None
    lon: float | None = None
    actors: list[str] = Field(default_factory=list)
    severity: int = 1
    source: str


class Region(BaseModel):
    id: str
    name: str
    geometry: dict[str, Any] | None = None


class Actor(BaseModel):
    id: str
    name: str
    actor_type: str
    aliases: list[str] = Field(default_factory=list)


class IntelReport(BaseModel):
    id: str
    title: str
    created_at: datetime
    body_markdown: str
    source_event_ids: list[str] = Field(default_factory=list)


class CryptoToken(BaseModel):
    id: str
    symbol: str
    name: str
    chain: str | None = None
    contract_address: str | None = None


class MarketSignal(BaseModel):
    id: str
    token_id: str
    ts: datetime
    score: float
    feature_importances: dict[str, float] = Field(default_factory=dict)
    risk_flags: list[str] = Field(default_factory=list)

