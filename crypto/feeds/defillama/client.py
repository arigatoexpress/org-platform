from __future__ import annotations

import httpx

# Official DefiLlama API docs:
# https://defillama.com/docs/api
PROTOCOLS_URL = "https://api.llama.fi/protocols"


def fetch_protocol_liquidity(limit: int = 250, offline: bool = False) -> dict[str, float]:
    if offline:
        return {"AAVE": 12_000_000_000.0, "BTC": 0.0}
    try:
        response = httpx.get(PROTOCOLS_URL, timeout=30)
        response.raise_for_status()
        protocols = response.json()[:limit]
        liquidity: dict[str, float] = {}
        for protocol in protocols:
            symbol = (protocol.get("symbol") or protocol.get("name") or "").upper()
            if symbol:
                tvl = float(protocol.get("tvl") or 0.0)
                liquidity[symbol] = max(liquidity.get(symbol, 0.0), tvl)
        return liquidity
    except Exception:
        return {"AAVE": 12_000_000_000.0, "BTC": 0.0}
