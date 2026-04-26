# Daily Inbox Zero Processor

Schedule: `0 16 * * 1-5`

Feature flags: `GMAIL_CONNECTOR`

Prompt:
Process unread inbox items into archive, needs-reply, waiting, read-later, and receipt categories. Write `/Daily/YYYY-MM-DD-inbox-zero.md` with counts and drafts to review. Do not send email.

