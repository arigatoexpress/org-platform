# HANDOFF

This file is updated at the end of each work slice. Current status: first vertical slice is scaffolded, working locally, and tested.

## Status Matrix

| Workstream | Scoped | Scaffolded | Working | Tested | Deployed |
| --- | --- | --- | --- | --- | --- |
| A. Tooling & Environment | Yes | Yes | Yes | Yes | No |
| B. OSINT Pipeline | Yes | Yes | Yes | Yes | Local |
| C. Foundry Flagship | Yes | Yes | Importable skeleton | N/A | No |
| D. Crypto Signal Layer | Yes | Yes | Yes | Yes | Local |
| E. Cowork Automations | Yes | Yes | Specs only | N/A | No |

## What Changed

Tooling:
- Added `AGENTS.md`, `CLAUDE.md`, `README.md`, `.env.example`, `Makefile`, `pyproject.toml`, `mise.toml`.
- Added Claude Code commands for `/review`, `/plan`, `/intel-brief`, `/repo-audit`.
- Added Codex config, local Brewfile/VS Code settings, cloud Docker/Compose/Fly/Cloudflare/Modal stubs.
- Added `scripts/bootstrap.sh`.

Cowork:
- Added normalized `configs/cowork/playbook.md`.
- Added 9 scheduled specs, including daily briefing, Gmail summary, calendar prep, inbox zero, Monday planning, bi-weekly OSINT scan, and EOD log.
- Added slash specs for cross-platform search, intel brief, repo audit, and plan.

OSINT:
- Added adapters for DeepStateMap, OFAC, UANI, AISStream, ACLED, Windward, and TankerTrackers.
- Added common `normalize.schema.Event`.
- Added DuckDB writer and generated demo outputs.
- Produced `Intelligence/iran-shipping-2026-04-26.md`.

Foundry:
- Added ontology models for `Vessel`, `Voyage`, `Sanction`, `ConflictEvent`, `Region`, `Actor`, `IntelReport`, `CryptoToken`, and `MarketSignal`.
- Added `@transform_df`-style transform stubs and Workshop dashboard spec.

Crypto:
- Added CoinGecko and DefiLlama live adapters.
- Added Dune, GoPlus/Honeypot, and CryptoPanic scaffold docs.
- Added explainable scoring and generated `crypto/watchlist-2026-04-26.md`.
- Updated `crypto/CURRENT_STATE.md` from public `sapphirealpha.xyz` and local repo discovery.

Dashboard:
- Added Next.js fallback dashboard under `surface/dashboard`.
- Dashboard reads generated `public/events.json` and `public/crypto.json`.

## Source Status

`make intel-demo` produced 12 events:
- Live: OFAC SDN (4), DeepStateMap mirror (2), UANI blog (2).
- Fixture-tagged: AISStream (1), ACLED (1), Windward (1), TankerTrackers (1).

`make crypto-demo` produced 10 token signals:
- Live: CoinGecko trending and DefiLlama protocol liquidity.
- Gated/scaffolded: Dune, GoPlus/Honeypot, CryptoPanic.

## Verify

```bash
./scripts/bootstrap.sh
make test
make lint
make intel-demo
make crypto-demo
npm audit --prefix surface/dashboard --audit-level=moderate
npm run build --prefix surface/dashboard
make dashboard
```

Verified in this slice:
- `./scripts/bootstrap.sh` passed.
- `make test` passed: 5 tests.
- `make lint` passed.
- `make intel-demo` passed.
- `make crypto-demo` passed.
- `npm audit --prefix surface/dashboard --audit-level=moderate` passed.
- `npm run build --prefix surface/dashboard` passed.

## Top 5 Next Actions

1. Identify the repo/service that owns the deployed BigQuery-backed `sapphirealpha.xyz` API routes.
2. Create BigQuery or API contract for `TokenSignal` ingestion into Sapphire Alpha.
3. Provision bounded credentials for AISStream and ACLED, then replace two fixture sources.
4. Add a real entity-resolution enrichment pass joining AIS MMSI/IMO to OFAC maritime entities.
5. Push this repo to a private GitHub remote and split follow-up branches/PRs by workstream.

## Top 5 Questions

1. Should `org-platform` live as `arigatoexpress/org-platform`, inside Sapphire, or in a new GitHub org?
2. What Foundry workspace/repo conventions should the skeleton target?
3. Which source should be canonical for current `sapphirealpha.xyz` deployment: local `SapphireAlpha`, Cloud Run, or another repo?
4. Which paid connector should be provisioned first: Windward, AISStream, ACLED, X, Dune, or CryptoPanic?
5. Should Cowork automations write to local folders first or directly into Drive/Notion once connectors exist?
