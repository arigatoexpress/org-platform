# Cowork Config

Folder convention:

- `/Daily`
- `/Weekly`
- `/Intelligence`
- `/Meeting-Prep`
- `/Receipts`
- `/Content`
- `/Research`

Every scheduled task should:
- Batch related work into one session.
- Use specific file/folder targets.
- Run heavy compute during evenings/weekends.
- Force `/plan` for changes touching more than three files.
- Gate missing connectors behind feature flags.

Install pattern:
1. Copy `scheduled/*.md` into Cowork scheduled automations.
2. Copy `slash/*.md` into Cowork slash commands.
3. Keep output paths exactly as written unless Ari changes the org folder tree.

