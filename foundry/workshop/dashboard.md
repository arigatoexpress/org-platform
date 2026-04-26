# Workshop Dashboard Spec

## Global Map

- Dataset: `unified_events`
- Layers:
  - Maritime/AIS points.
  - Sanctions targets without geo as queue counts.
  - Conflict events as severity-colored points or polygons.
- Filters: source, severity, mock/live, tag, actor, time range.

## Vessel Detail Page

- Object: `Vessel`
- Panels: latest AIS position, voyage history, sanctions joins, risk tags, related reports.

## Sanctions Watchlist Queue

- Object: `Sanction`
- Columns: authority, program, target, target type, related vessel/entity, last seen, confidence.
- Actions: mark reviewed, open entity resolution task, generate report section.

## Alerts Stream

- Dataset: high-severity `unified_events`
- Cards: title, source, severity, why it matters, recommended next collection action.

