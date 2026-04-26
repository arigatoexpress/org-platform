# sapphirealpha.xyz Current State

Status: first-pass public and local discovery completed on 2026-04-26.

Verified public surface:
- `https://sapphirealpha.xyz/` currently renders "Sapphire Analytics".
- The public page says it reads BigQuery dataset `tho-ai-agent.sapphire` and refreshes every 60 seconds.
- Visible tables: latest regime snapshots, recent signals, daily performance, predictions, and threat severity.
- Browser HTML references API routes such as `/api/summary`, `/api/regime`, `/api/performance`, `/api/predictions`, `/api/threats`, and `/api/signals/recent`.

Verified local candidate:
- Candidate codebase exists at `/Users/aribs/Code/SapphireAlpha`.
- It is a Vite/React app on local branch `master`.
- Local source appears to be a portfolio/showcase frontend, while `dist/`/public deployment is the BigQuery analytics page. This needs reconciliation before editing the live site repo.

Assumptions to verify next:
- Public site surfaces read-only analytics rather than executing trades.
- The deployed BigQuery analytics surface is produced from the local `dist/` artifact, a Cloud Run service, or another repo not yet identified.
- The upgrade path should add a read-only `/api/token-watchlist` endpoint or BigQuery table rather than front-end-only static JSON.
- Existing Sapphire Alpha risk controls should remain read-only; no order placement is in scope.

Planned integration artifact:
- `data/crypto/watchlist.json` as the stable local contract for a first read-only upgrade.
- Later: BigQuery table `tho-ai-agent.sapphire.token_signals` with fields matching `crypto.schema.TokenSignal`.
