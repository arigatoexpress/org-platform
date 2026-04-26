from __future__ import annotations

from datetime import UTC, datetime

import httpx

from crypto.schema import TokenSignal

# Official CoinGecko API docs:
# https://docs.coingecko.com/reference/introduction
BASE_URL = "https://api.coingecko.com/api/v3"


def fetch_trending(limit: int = 10, offline: bool = False) -> list[TokenSignal]:
    if offline:
        return fixture_trending()[:limit]
    try:
        response = httpx.get(f"{BASE_URL}/search/trending", timeout=20)
        response.raise_for_status()
        coins = response.json().get("coins", [])
        signals: list[TokenSignal] = []
        for index, wrapper in enumerate(coins[:limit], start=1):
            item = wrapper["item"]
            signals.append(
                TokenSignal(
                    id=item.get("id") or item.get("coin_id") or item["symbol"].lower(),
                    symbol=item["symbol"].upper(),
                    name=item["name"],
                    ts=datetime.now(UTC),
                    trending_rank=index,
                    market_cap_rank=item.get("market_cap_rank"),
                    narrative_tags=["coingecko-trending"],
                    raw=item,
                )
            )
        return signals or fixture_trending()[:limit]
    except Exception as exc:
        signals = fixture_trending()[:limit]
        for signal in signals:
            signal.raw["fallback_reason"] = str(exc)
        return signals


def fixture_trending() -> list[TokenSignal]:
    now = datetime(2026, 4, 26, tzinfo=UTC)
    return [
        TokenSignal(
            id="bitcoin",
            symbol="BTC",
            name="Bitcoin",
            ts=now,
            trending_rank=1,
            market_cap_rank=1,
            narrative_tags=["fixture", "store-of-value"],
            raw={"fixture": True},
        ),
        TokenSignal(
            id="aave",
            symbol="AAVE",
            name="Aave",
            ts=now,
            trending_rank=2,
            market_cap_rank=54,
            narrative_tags=["fixture", "defi"],
            raw={"fixture": True},
        ),
    ]

