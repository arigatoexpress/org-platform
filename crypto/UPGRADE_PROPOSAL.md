# Sapphire Alpha Upgrade Proposal

## 1. Trending Token Watchlist

Add a read-only watchlist card fed by `data/crypto/watchlist.json`, showing score, top feature contributions, and risk flags.

```html
<section class="panel">
  <h2>Trending Token Watchlist</h2>
  <ol>
    <li><strong>AAVE</strong> score 72.0 <span>trend + liquidity</span></li>
  </ol>
</section>
```

## 2. Signal Explanation Drawer

For each token, show feature importances: trend rank, market-cap rank, liquidity, news sentiment, and risk penalty. Keep this as explanation, not trading advice.

## 3. Snapshot Delta Digest

Persist hourly/daily snapshots so Sapphire Alpha can show rank changes instead of only current levels.

## 4. Safety Flags

Add GoPlus/Honeypot-derived badges once contract addresses are mapped: proxy risk, mintability, blacklist controls, buy/sell tax, and honeypot status.

## 5. Narrative Tags

Show tags such as `defi`, `l2`, `ai`, `meme`, `rwa`, and `coingecko-trending`, with source badges for where each tag came from.

