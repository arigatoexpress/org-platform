# BLOCKERS

| Item | Status | Route Around |
| --- | --- | --- |
| Foundry workspace URL/token | Not provisioned | Build importable `foundry/` skeleton and use DuckDB/dashboard locally. |
| Windward API contract/token | Not provisioned; public API docs not verified in this session | Fixture-backed connector that fails closed unless `WINDWARD_API_BASE_URL` and `WINDWARD_API_TOKEN` are set. |
| X API token for TankerTrackers | Not provisioned | Fixture/RSS-style adapter only; no brittle scraping of X pages. |
| UANI direct fetch | Cloudflare challenge returned HTTP 403 on 2026-04-26 | Fixture-backed adapter with source URL retained and `[MOCK]` tag. |
| AISStream API key | Not provisioned | Fixture-backed AIS event; official WebSocket subscription shape documented. |
| ACLED credentials | Not provisioned | Fixture-backed conflict event; official API docs linked. |
| Dune/CryptoPanic keys | Not provisioned | CoinGecko + DefiLlama live, Dune/CryptoPanic fixture/disabled. |

