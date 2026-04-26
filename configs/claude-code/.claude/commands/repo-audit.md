# /repo-audit

Audit the repo for production-autonomy readiness.

Checklist:
- Bootstrap works from a clean checkout.
- Tests cover parser fixtures and demo pipelines.
- Secrets are only referenced via env vars and `.env.example`.
- Paid/gated connectors fail closed.
- Dashboard loads current demo JSON.
- `RUNNING_LOG.md`, `BLOCKERS.md`, `HANDOFF.md`, and `RESUME.md` are current.

Write concise findings and proposed next actions.

