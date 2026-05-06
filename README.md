# org-platform

Autonomous intelligence organization platform for Sapphire OS: agent tooling, OSINT fan-in, Foundry-ready transforms, a local dashboard fallback, and a crypto signal layer.

## Quick Start

```bash
./scripts/bootstrap.sh
make intel-demo
make crypto-demo
make dashboard-bg
```

Then open `http://127.0.0.1:3000`. Use `make dashboard-stop` to stop the background server.
Use `make dashboard-smoke` to verify the committed dashboard JSON and build prerequisites without regenerating demo artifacts.

## Demos

- `make intel-demo` writes a dated Iran shipping watch brief to `Intelligence/`, normalized events to `data/intel/events.json`, and dashboard data to `surface/dashboard/public/events.json`.
- `make crypto-demo` writes a ranked token watchlist to `data/crypto/watchlist.json`, `crypto/watchlist-<date>.md`, and `surface/dashboard/public/crypto.json`.

Paid/gated sources are fixture-backed and visibly marked `[MOCK]` until credentials are configured through `.env` or a secret manager.
