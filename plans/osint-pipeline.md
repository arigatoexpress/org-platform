# Workstream B Plan: OSINT Pipeline

## Goal

Create `feeds -> normalize -> enrich -> store -> surface` with a first Iran sanctions evasion shipping watch brief.

## Plan

1. Define a common `Event` schema with source, timestamp, geo, actors, severity, tags, raw payload, and mock marker.
2. Build small source adapters for DeepStateMap, OFAC, UANI, AIS, ACLED, TankerTrackers, and Windward.
3. Gate paid/gated sources behind credentials and fixtures.
4. Write normalized events to JSON and DuckDB.
5. Generate a dated Markdown brief citing every source.
6. Copy dashboard-ready JSON into `surface/dashboard/public/`.

## Definition Of Done

- [x] At least one live source and three total sources flow into a brief.
- [x] Mocked sources are visibly tagged `[MOCK]`.
- [x] Unit tests cover fixture parsing and schema validation.
- [x] Integration test covers offline demo generation.
