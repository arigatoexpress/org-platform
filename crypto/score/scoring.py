from __future__ import annotations

from crypto.schema import TokenSignal


def score_signals(
    signals: list[TokenSignal], liquidity_by_symbol: dict[str, float]
) -> list[TokenSignal]:
    scored: list[TokenSignal] = []
    for signal in signals:
        trend_component = _trend_component(signal.trending_rank)
        rank_component = _market_cap_component(signal.market_cap_rank)
        liquidity_component = _liquidity_component(
            liquidity_by_symbol.get(signal.symbol.upper(), 0.0)
        )
        risk_penalty = min(len(signal.risk_flags) * 10.0, 30.0)
        score = max(
            trend_component
            + rank_component
            + liquidity_component
            + signal.news_sentiment
            - risk_penalty,
            0.0,
        )
        signal.liquidity_score = liquidity_component
        signal.score = round(score, 2)
        signal.feature_importances = {
            "trend": round(trend_component, 2),
            "market_cap_rank": round(rank_component, 2),
            "liquidity": round(liquidity_component, 2),
            "news_sentiment": round(signal.news_sentiment, 2),
            "risk_penalty": round(-risk_penalty, 2),
        }
        scored.append(signal)
    return sorted(scored, key=lambda item: item.score, reverse=True)


def _trend_component(rank: int | None) -> float:
    if rank is None:
        return 0.0
    return max(35.0 - (rank - 1) * 3.0, 5.0)


def _market_cap_component(rank: int | None) -> float:
    if rank is None:
        return 5.0
    if rank <= 10:
        return 25.0
    if rank <= 100:
        return 18.0
    if rank <= 300:
        return 10.0
    return 4.0


def _liquidity_component(tvl: float) -> float:
    if tvl >= 10_000_000_000:
        return 20.0
    if tvl >= 1_000_000_000:
        return 14.0
    if tvl >= 100_000_000:
        return 8.0
    return 2.0
