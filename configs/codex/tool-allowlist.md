# Tool Allowlist

Recommended local command families:
- `git status`, `git diff`, `git log`, `git show`, `git worktree`
- `rg`, `sed`, `find`, `ls`, `wc`
- `uv venv`, `uv pip install`, `python -m pytest`, `python -m ruff`
- `npm install`, `npm run dev`, `npm run build`
- `gh api`, `gh repo view`, `gh pr list`, `gh pr create`
- `curl` for public documentation and keyless public APIs

Requires explicit dry-run or fixture mode:
- Any Telegram send.
- Any trading or token-transfer action.
- Any webhook post.
- Any paid API connector.

Never allow:
- Printing secret-manager payloads.
- Committing `.env` or credential files.
- Enabling live trading or real Telegram test messages.

