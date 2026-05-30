# org-platform

Autonomous intelligence organization platform for Sapphire OS: agent tooling, OSINT fan-in, knowledge graph transforms, a local dashboard, and a crypto signal layer.

## What this does

A local-first compute mesh that collects open-source intelligence, normalizes events, scores crypto tokens, and surfaces everything through a lightweight dashboard. Paid or gated sources fall back to mock fixtures until real credentials are configured.

## Quick start

```bash
# Bootstrap dependencies and data directories
./scripts/bootstrap.sh

# Run demos
make intel-demo      # Iran shipping watch brief + normalized events
make crypto-demo     # Ranked token watchlist
make dashboard-bg    # Start background dashboard server

# Verify without regenerating artifacts
make dashboard-smoke
```

Open `http://127.0.0.1:3000`. Stop with `make dashboard-stop`.

## Architecture

```
Public sources / APIs / fixtures
        │
        ▼
┌──────────────┐    ┌──────────┐    ┌─────────────┐
│   feeds/     │───▶│ normalize│───▶│   store/    │
│   crypto/    │    │  enrich/ │    │  (DuckDB)   │
└──────────────┘    └──────────┘    └──────┬──────┘
                                           │
                     ┌─────────────────────┼─────────────────────┐
                     ▼                     ▼                     ▼
               ┌──────────┐         ┌──────────┐          ┌──────────┐
               │ surface/ │         │ Intelligence/│      │  plans/  │
               │dashboard │         │  briefs      │      │  configs │
               └──────────┘         └──────────┘          └──────────┘
```

## Key features

- **OSINT fan-in** — RSS, public APIs, and fixture-backed gated sources
- **Event normalization** — Deduplicated, scored, and timestamped events
- **Crypto scoring** — Token watchlists with risk ranking and market signals
- **Local dashboard** — Fast, static JSON-backed fallback UI
- **Foundry-ready transforms** — Export pipelines for downstream analytics

## Tech stack

![Python](https://img.shields.io/badge/python-3.11%2B-3776AB)
![DuckDB](https://img.shields.io/badge/DuckDB-1.2%2B-fff000)
![pytest](https://img.shields.io/badge/pytest-8%2B-0A9EDC)

- Python 3.11+, Pydantic v2, DuckDB
- TypeScript dashboard (Next.js-style static build)
- `make` for task orchestration

## Data sources

All signals are public-source or fixture-backed:
- RSS feeds, OSM, public registries
- Crypto market data (fixture-backed until API keys configured)
- Mock/gated sources marked `[MOCK]` in output

## Governance notes

- No real trading or money movement
- No secret exposure in logs or commits
- Paid sources require explicit credential configuration

## Agent collaborators

See [AGENTS.md](AGENTS.md) for build commands, safety boundaries, and repo conventions.
