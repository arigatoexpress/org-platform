from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class TokenSignal(BaseModel):
    id: str
    symbol: str
    name: str
    ts: datetime
    trending_rank: int | None = None
    market_cap_rank: int | None = None
    liquidity_score: float = 0.0
    narrative_tags: list[str] = Field(default_factory=list)
    news_sentiment: float = 0.0
    risk_flags: list[str] = Field(default_factory=list)
    score: float = 0.0
    feature_importances: dict[str, float] = Field(default_factory=dict)
    raw: dict[str, Any] = Field(default_factory=dict)

