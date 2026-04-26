from __future__ import annotations

import json
import os
from datetime import UTC, datetime
from pathlib import Path

from crypto.feeds.coingecko.client import fetch_trending
from crypto.feeds.defillama.client import fetch_protocol_liquidity
from crypto.score.scoring import score_signals


def main() -> None:
    root = Path(os.getenv("ORG_PLATFORM_OUTPUT_DIR", ".")).resolve()
    offline = os.getenv("ORG_PLATFORM_OFFLINE", "").lower() in {"1", "true", "yes"}
    today = datetime.now(UTC).date().isoformat()

    trending = fetch_trending(limit=10, offline=offline)
    liquidity = fetch_protocol_liquidity(offline=offline)
    watchlist = score_signals(trending, liquidity)

    payload = [signal.model_dump(mode="json") for signal in watchlist]
    data_dir = root / "data" / "crypto"
    data_dir.mkdir(parents=True, exist_ok=True)
    watchlist_path = data_dir / "watchlist.json"
    watchlist_path.write_text(json.dumps(payload, indent=2) + "\n")

    dashboard_path = root / "surface" / "dashboard" / "public" / "crypto.json"
    dashboard_path.parent.mkdir(parents=True, exist_ok=True)
    dashboard_path.write_text(json.dumps(payload, indent=2) + "\n")

    markdown_path = root / "crypto" / f"watchlist-{today}.md"
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.write_text(render_watchlist(payload, today))

    print(f"Wrote {len(watchlist)} token signals to {watchlist_path}")
    print(f"Wrote markdown watchlist to {markdown_path}")
    print(f"Wrote dashboard data to {dashboard_path}")


def render_watchlist(payload: list[dict], today: str) -> str:
    lines = [
        f"# Crypto Signal Watchlist - {today}",
        "",
        "Read-only market intelligence. Not trade execution or financial advice.",
        "",
        "| Rank | Token | Score | Rationale | Risk Flags |",
        "| --- | --- | ---: | --- | --- |",
    ]
    for rank, signal in enumerate(payload, start=1):
        features = signal["feature_importances"]
        rationale = ", ".join(f"{key} {value:+.1f}" for key, value in features.items())
        risk_flags = ", ".join(signal["risk_flags"]) or "none"
        lines.append(
            f"| {rank} | {signal['symbol']} ({signal['name']}) | "
            f"{signal['score']:.2f} | {rationale} | {risk_flags} |"
        )
    lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    main()
