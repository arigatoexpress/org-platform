# Foundry Import Skeleton

This directory is designed to paste into a Foundry repository with minimal edits.

## What To Wire

1. Replace placeholder dataset paths in `foundry/transforms/*.py` with real Foundry dataset RIDs or path objects.
2. Paste ontology models from `foundry/ontology/objects.py` into your ontology/modeling workflow.
3. Register each connector transform in Foundry Code Repositories.
4. Point `unify_events.py` at the source transform outputs.
5. Build the Workshop app from `foundry/workshop/dashboard.md`.

## Current Mocking

- Windward, AISStream, ACLED, X/TankerTrackers, Dune, and CryptoPanic are mocked unless credentials are configured.
- Local demo truth is `data/intel/events.json` and `data/store/events.duckdb`.
- The dashboard fallback reads `surface/dashboard/public/events.json` and `crypto.json`.

## Local To Foundry Mapping

| Local | Foundry |
| --- | --- |
| `normalize.schema.Event` | `Event` object/table |
| `data/intel/events.json` | Raw/source datasets |
| `data/store/events.duckdb` | Curated event table |
| `crypto.schema.TokenSignal` | `MarketSignal` object/table |
| `Intelligence/*.md` | `IntelReport` object |

