# Workstream A Plan: Tooling & Environment

## Goal

Make `org-platform` bootstrap a standard dev surface for macOS, Linux, and a small cloud worker.

## Plan

1. Add Claude Code project memory, slash commands, hooks, and MCP registration examples.
2. Add Cowork folders, scheduled task specs, slash command specs, and a normalized 40-command playbook.
3. Add Codex AGENTS, sandbox recommendations, allowlists, and `codex.toml`.
4. Add local setup files: Brewfile, mise, VS Code/Cursor settings, extensions, and direnv pattern.
5. Add cloud worker stubs: Dockerfile, Compose, Fly.io, Cloudflare Workers, and Modal GPU reference.
6. Add idempotent `scripts/bootstrap.sh`.

## Definition Of Done

- [x] `scripts/bootstrap.sh` is executable and green locally.
- [x] Claude commands `/review`, `/plan`, `/intel-brief`, `/repo-audit` exist.
- [x] At least 8 Cowork scheduled task specs exist.
- [x] `docs/adr/0001-tooling-stack.md` ranks candidate repos from stars/trending.
