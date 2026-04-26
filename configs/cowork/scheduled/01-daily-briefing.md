# Daily Briefing

Schedule: `0 7 * * 1-5`

Feature flags: `GMAIL_CONNECTOR`, `CALENDAR_CONNECTOR`

Prompt:
At 7am, scan today's Calendar, unread/high-priority Gmail, and yesterday's unresolved follow-ups. Write `/Daily/YYYY-MM-DD-briefing.md` with agenda, time blocks, prep needs, decisions due, and top three actions. Do not send messages.

