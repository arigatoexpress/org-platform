# 00 Session Plan

## Objective

Stand up the next iteration of Ari's autonomous intelligence organization as a durable `org-platform` repo with a working first vertical slice across tooling, OSINT, Foundry scaffolding, crypto signals, and Cowork automations.

## Numbered Plan

1. Verify current state: Sapphire cleanliness, GitHub identity, toolchain, and existing codebase hints.
2. Create `org-platform/` with logs, blockers, handoff, AGENTS/Claude memory, bootstrap, Make targets, and reproducible dependency files.
3. Build Workstream A first: Claude Code commands, Codex config, Cowork playbook/schedules, local machine config, cloud worker stubs, and ADR.
4. Build a narrow OSINT vertical slice: source adapters with fixtures, common `Event` schema, DuckDB store, dated Iran shipping watch brief, and dashboard JSON.
5. Build a narrow crypto vertical slice: CoinGecko + DefiLlama live adapters, scoring module, JSON/Markdown watchlist, and dashboard JSON.
6. Scaffold Foundry ontology/transforms/workshop specs that paste cleanly into a real workspace.
7. Add focused tests and run `make test`, `make intel-demo`, and `make crypto-demo`.
8. Commit the baseline locally, then create/push a remote branch and draft PR if a safe GitHub remote exists or can be created privately.

## Success Criteria

- `./scripts/bootstrap.sh` prints a green checklist.
- `make intel-demo` produces `Intelligence/iran-shipping-<date>.md` and dashboard event data.
- `make crypto-demo` produces a fresh token watchlist with scoring rationale.
- `surface/dashboard` can show unified events and crypto signals.
- `foundry/README.md` explains how to lift the skeleton into Foundry.
- At least 8 Cowork scheduled task specs exist.
- `HANDOFF.md` clearly states what is real, mocked, blocked, and next.

## Exit Conditions

- Tests pass or known failures are documented with exact remediation.
- Demo commands run or blockers are documented with fixtures.
- No secrets are committed.
- Local repo has a clean committed baseline or a documented dirty state.

## Definition Of Done

- [x] Tooling configs scaffolded and documented.
- [x] OSINT demo produces normalized events, a store, and a brief.
- [x] Crypto demo produces a scored watchlist.
- [x] Foundry skeleton present.
- [x] Cowork playbook + scheduled specs present.
- [x] Tests and lint run.
- [x] Handoff and resume notes updated.
