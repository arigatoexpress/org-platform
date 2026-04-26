# ADR 0001: Tooling Stack

Date: 2026-04-26

## Status

Accepted for first vertical slice.

## Context

The platform needs agent tooling, local/cloud reproducibility, OSINT mapping/data engineering, and crypto/finance signal generation. Candidate repositories were seeded from Ari's GitHub stars via `gh api users/arigatoexpress/starred --paginate`, current GitHub trending pages, and the starter shortlist.

## Decision

Use a small core stack first: Python, TypeScript, DuckDB, Pydantic, pytest, ruff, Next.js, Foundry transform conventions, and small source adapters. Avoid heavyweight agent/data frameworks until a vertical slice proves where orchestration complexity is real.

## Candidate Ranking

| Rank | Repo | Pick/Pass | Why |
| --- | --- | --- | --- |
| 1 | `open-metadata/OpenMetadata` | Pick later | Strong governance/lineage reference; too heavy for first slice. |
| 2 | `microsoft/markitdown` | Pick | Useful for document-to-Markdown ingestion in Cowork/OSINT workflows. |
| 3 | `zilliztech/claude-context` | Pick later | Good codebase context MCP pattern; not needed for bootstrap. |
| 4 | `openai/openai-agents-python` | Pick later | Useful agent SDK reference for orchestration after adapters stabilize. |
| 5 | `langchain-ai/langgraph` | Pick later | Durable graph orchestration if jobs become multi-agent/stateful. |
| 6 | `stanfordnlp/dspy` | Pick later | Candidate for scoring/rationale optimization, not first slice. |
| 7 | `marimo-team/marimo` | Pick later | Better notebooks for analyst exploration than static `.ipynb`. |
| 8 | `OpenBB-finance/OpenBB` | Pick later | Strong finance data terminal; keep separate from crypto minimum. |
| 9 | `ccxt/ccxt` | Pass now | Trading/exchange surface increases risk; no trade execution needed. |
| 10 | `freqtrade/freqtrade` | Pass | Live/paper trading bot is outside this no-trading layer. |
| 11 | `defillama/defillama-sdk` | Pick later | Useful if direct API calls become noisy; keyless HTTP is enough now. |
| 12 | `duneanalytics/dune-client` | Pick later | Needs key and saved queries; scaffold only. |
| 13 | `pyais/pyais` | Pick later | Needed when AIS raw NMEA ingestion starts; fixture/demo does not need it. |
| 14 | `aisstream/aisstream-example` | Pick | Official AISStream WebSocket patterns inform the gated connector. |
| 15 | `cyterat/deepstate-map-data` | Pick | Keyless GeoJSON source for conflict-map vertical slice. |
| 16 | `acled-data` ecosystem clients | Pick later | ACLED API needs credentials; client comes after account wiring. |
| 17 | `osmnx/osmnx` | Pick later | Useful OSM enrichment, too large for first demo. |
| 18 | `visgl/deck.gl` | Pick later | Strong map rendering for serious dashboard; Next static view starts simpler. |
| 19 | `keplergl/kepler.gl` | Pick later | Analyst map exploration candidate; heavy for first slice. |
| 20 | `mapbox/mapbox-gl-js` | Pass now | Token/licensing/tiles add friction; use simple local map first. |
| 21 | `palantir/transforms-python` examples | Pick | Foundry transform style anchor. |
| 22 | `duckdb/duckdb` | Pick | Local analytics store with simple deployment and parquet path later. |
| 23 | `pydantic/pydantic` | Pick | Schema enforcement for source adapters and scoring objects. |
| 24 | `astral-sh/ruff` | Pick | Fast Python linting and formatting guardrail. |
| 25 | `biomejs/biome` | Pick later | TS formatting/linting once dashboard grows. |
| 26 | `openhands/openhands` | Pass now | Agent framework is broader than needed for controlled configs. |
| 27 | `aider-ai/aider` | Pass now | Useful external tool, but Codex/Claude configs are canonical here. |
| 28 | `continuedev/continue` | Pick later | IDE agent config candidate for local dev pack. |
| 29 | `crewAIInc/crewAI` | Pass now | Multi-agent framework before source reliability would add indirection. |
| 30 | `sherlock-project/sherlock` | Pass | OSINT social username scope does not map to flagship maritime/conflict need. |

## Consequences

The first slice is boring on purpose: fewer moving parts, clear fixtures, easy tests, and a dashboard that can be replaced by deck.gl/Kepler once the event model stabilizes.

