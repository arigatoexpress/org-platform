# Claude Code Config

Claude Code should act as a constrained reviewer/helper for this repo.

Default behaviors:
- Start with `/plan` for changes touching more than three files.
- Use `/review` before merge or handoff.
- Use `/intel-brief` only in dry-run unless webhook env vars are present and explicitly enabled.
- Never expose secrets, raw webhook payloads, or secret-manager values.

Recommended MCP servers:
- GitHub for PR/issue context.
- Filesystem scoped to this repo.
- Browser only for local dashboard verification and public documentation.
- No Telegram/trading MCP server in live-send mode.

