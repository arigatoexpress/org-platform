# Workstream C Plan: Foundry Flagship

## Goal

Make Foundry the canonical target while keeping the local DuckDB/dashboard fallback demonstrable today.

## Plan

1. Define ontology objects for vessels, voyages, sanctions, conflict events, regions, actors, intel reports, crypto tokens, and market signals.
2. Add `@transform_df` style transform stubs for each source.
3. Add `unify_events.py` to merge source transforms into a canonical event table.
4. Specify the Workshop app: global map, vessel detail, sanctions queue, alerts stream.
5. Add analyst notebook/quiver stubs.
6. Document import steps and mocked wiring.

## Definition Of Done

- [x] Foundry README names every file to edit for a real workspace.
- [x] Transform stubs follow Foundry conventions.
- [x] Local dashboard reads the same normalized event shape.
