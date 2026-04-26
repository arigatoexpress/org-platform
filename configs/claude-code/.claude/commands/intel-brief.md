# /intel-brief

Generate a dated intelligence brief from the normalized event store.

Rules:
- Cite every source URL or fixture file.
- Mark fixture-derived records with `[MOCK]`.
- Separate observed facts from analytic judgments.
- Do not send Slack/Discord/Telegram messages unless the matching webhook env var is present and live send is explicitly enabled.
- Save output to `/Intelligence/<topic>-<YYYY-MM-DD>.md`.

Default topic: Iran sanctions evasion shipping watch.

