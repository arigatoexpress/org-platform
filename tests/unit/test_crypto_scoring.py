from crypto.feeds.coingecko.client import fixture_trending
from crypto.score.scoring import score_signals


def test_score_signals_orders_by_score() -> None:
    scored = score_signals(fixture_trending(), {"AAVE": 12_000_000_000.0, "BTC": 0.0})

    assert scored[0].score >= scored[-1].score
    assert "trend" in scored[0].feature_importances

