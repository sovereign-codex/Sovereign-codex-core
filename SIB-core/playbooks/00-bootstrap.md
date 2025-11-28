# Bootstrap: Bring a Sovereign Intelligence Base online

## Goal
Stand up a minimal Sovereign Intelligence Base (SIB) node that can ingest curated streams, enforce guardrails, and publish updates back into the Kodex network.

## Steps
1. **Inventory streams** — confirm `streams/` contains the sources you plan to ingest, with cadence and transport documented.
2. **Review guardrails** — update `protocols/guardrails.md` to reflect current moderation, provenance, and access controls.
3. **Seed content** — ingest at least one scroll or KO sample into local storage to validate indexing.
4. **Index locally** — run `python scripts/build_rag_index.py` from repo root to produce `indices/kodex.index.json` for offline search.
5. **Publish snapshot** — commit new streams, guardrails, and scrolls to your fork; optionally mirror to IPFS.
6. **Signal readiness** — update `manifest.yaml` with a new `last_updated` timestamp and bump the version.

## Success criteria
- All declared streams have owners and update cadences.
- Guardrails map each stream to a review path.
- Index builds cleanly with the added artifacts.
