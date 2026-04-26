# Cowork 40-Command Playbook, Sapphire Edition

Source: Khairallah's 40-command article from the session prompt, normalized into Ari's folder layout. Connector-dependent workflows are scaffolded and feature-flagged.

## Slash Commands 01-10

01. `/schedule`: Create or update recurring tasks. Default: daily 7am Gmail + Calendar briefing saved to `/Daily/YYYY-MM-DD-briefing.md`.
02. `/plan`: For tasks touching more than three files, write a numbered plan, success criteria, exit conditions, and rollback before acting.
03. `/review`: Review a diff, document risks first, and save findings beside the target project.
04. `/intel-brief`: Generate a cited OSINT brief from `/Intelligence` and normalized event JSON.
05. `/repo-audit`: Audit repo health, stale branches, CI failures, dependency drift, and missing tests.
06. `/meeting-prep`: Build a meeting prep packet from Calendar, Gmail, Drive, and project docs into `/Meeting-Prep`.
07. `/receipt-sweep`: Move receipts/invoices into `/Receipts/YYYY/MM`, rename with `YYYY-MM-DD-vendor-amount`.
08. `/research-pack`: Create a source-cited research bundle under `/Research/<topic>/`.
09. `/content-draft`: Turn research notes into a draft under `/Content`.
10. `/handoff`: Summarize current work, blockers, verification commands, and next actions.

## File System Power Moves 11-18

11. Downloads triage: move PDFs, images, archives, and installers into predictable folders with dates.
12. Desktop zero: move all Desktop items into dated review folders, preserving names.
13. Duplicate finder: list duplicates by hash, propose deletes, do not delete without review.
14. Archive old projects: compress inactive folders older than 180 days into `/Archives`.
15. Normalize screenshots: move screenshots into `/Research/Screenshots/YYYY-MM`.
16. Rename batches: apply `YYYY-MM-DD-topic-source.ext` naming to research files.
17. Clean node/python artifacts: remove safe generated caches only.
18. Build project index: write a Markdown inventory of active repos and last commit dates.

## Connector Workflows 19-26

19. Gmail to Summary to Drive: summarize important threads into `/Daily` and archive the raw references.
20. Calendar to Prep Brief: generate `/Meeting-Prep/YYYY-MM-DD-<meeting>.md`.
21. Drive research extraction: convert docs to Markdown and store cited summaries in `/Research`.
22. Slack digest: summarize unread/high-signal channels if connector exists.
23. GitHub PR review queue: summarize open PRs, checks, owners, and blocked reviews.
24. Linear/issue triage: group issues by project, priority, and stale state.
25. Receipts to sheet: extract vendor/date/amount into a monthly ledger.
26. Cross-platform search: search Gmail, Calendar, Drive, GitHub, local files, and Notion when connected.

## Document And Content Workflows 27-34

27. Meeting notes to tasks: extract decisions, owners, dates, and open questions.
28. Research memo: synthesize sources into a short cited memo.
29. Competitive brief: compare 3-7 organizations/tools with adoption signals.
30. Technical ADR: turn a decision into `docs/adr/NNNN-topic.md`.
31. SOP/runbook: turn repeated work into a checklist with rollback.
32. Content calendar: propose weekly topics from research and recent wins.
33. Draft cleanup: tighten a draft while preserving Ari's voice.
34. Source audit: check every factual claim has a link or a clear internal-source note.

## Scheduled Automations 35-40

35. Daily inbox zero processor: weekdays, summarize, label, and create follow-ups.
36. Daily research capture: save high-signal links and snippets into `/Research/Inbox`.
37. Monday planning brief: summarize prior week, upcoming calendar, repo state, and top priorities.
38. Friday weekly review: summarize shipped work, stale decisions, and next-week setup.
39. Bi-weekly OSINT scan: check maritime/sanctions/conflict sources and write `/Intelligence/osint-scan-YYYY-MM-DD.md`.
40. End-of-day log: summarize actions, changed files, blockers, and tomorrow's first three moves.

## Pro Tips Baked In

- Batch related tasks into one session.
- Be concrete about source folders, target folders, naming, and retention.
- Schedule heavy compute outside focus hours.
- Force `/plan` mode for multi-file work.
- Keep folder trees predictable.

