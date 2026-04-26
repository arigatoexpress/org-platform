# AGENTS.md

Codex is Ari's primary operator for Sapphire OS production-autonomy work.

Default stance:
- Lead from current-state verification, not stale audit notes.
- Keep `/Users/aribs/Code/Sapphire` clean on `origin/main` whenever possible.
- Use `/Users/aribs/Code/_worktrees/` for Sapphire PR work and remove clean worktrees after merge or abandonment.
- Preserve local WIP before cleanup with a backup branch, patch, and stash.
- Keep Claude as a constrained reviewer/helper unless Ari explicitly gives it ownership of a task.
- Never expose secrets, enable real trading, or send real Telegram test messages.

Project rules for this repo:
- Build the smallest end-to-end slice first, then widen the fan-in.
- Keep every paid or gated connector behind explicit credentials and fixtures.
- Use TypeScript for browser/edge surfaces and Python for data, scoring, and Foundry transforms.
- Respect source terms. Do not scrape sources that forbid it; use official APIs or document why a fixture is used.
- Prefer durable artifacts over chat output: plans, tests, dashboards, configs, ADRs, and handoffs.

