# AGENTS.md — org-platform

## What this repo does

Autonomous intelligence organization platform for Sapphire OS. It collects OSINT signals, normalizes events, scores crypto tokens, and surfaces results through a local dashboard. The current focus is reliable data pipelines and a fast static dashboard fallback.

## Key directories and files

| Path | Role |
|---|---|
| `feeds/` | Source collectors (RSS, APIs, fixtures) |
| `normalize/` | Event deduplication and schema normalization |
| `enrich/` | Scoring, tagging, and entity resolution |
| `store/` | DuckDB persistence and query layer |
| `crypto/` | Token watchlist and market signal logic |
| `surface/dashboard/` | Static dashboard UI build |
| `Intelligence/` | Generated briefs and human-readable output |
| `configs/` | Region, source, and scoring configuration |
| `plans/` | ADRs, runbooks, and migration notes |
| `scripts/bootstrap.sh` | One-time environment setup |
| `Makefile` | Task orchestration (demos, dashboard, tests) |

## How to run tests / dev server

```bash
# Tests
python -m pytest tests/ -q

# Dev dashboard
make dashboard-bg
make dashboard-smoke    # verify without regenerating
```

## Safety boundaries

- **Do NOT** expose secrets, API keys, or credentials in code or logs
- **Do NOT** enable real trading or money movement
- **Do NOT** scrape sources that explicitly forbid it; use official APIs or fixtures
- **Do NOT** modify `Makefile` without testing the affected targets
- Keep every paid or gated connector behind explicit credentials and fixtures

## Current status

- Local demo path stable (`make intel-demo`, `make crypto-demo`)
- Dashboard serves static JSON at `http://127.0.0.1:3000`
- Crypto and intel pipelines are fixture-backed by default
