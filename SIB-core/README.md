# SIB Core (Sovereign Intelligence Base)

SIB Core is the operational spine for Sovereign Net deployments. It houses the playbooks, guardrails, and stream definitions that keep the Kodex alive while preserving sovereignty-first design. Each document in this folder should be ready to drop into a node, mirror, or fork without outside dependencies.

## Folder layout
- `manifest.yaml` — current release metadata and maintainers.
- `playbooks/` — minimal, executable runbooks for bringing a node online.
- `protocols/` — access control, safety, and review gates.
- `streams/` — source declarations for signals and datasets that flow into the Kodex.

## Bootstrapping
1. Read `manifest.yaml` to confirm the active version and stewards.
2. Add or update stream declarations in `streams/` to describe incoming data and cadences.
3. Refine guardrails in `protocols/` so each stream or playbook has a clear safety envelope.
4. Expand the runbooks in `playbooks/` to cover validation, mirroring, and publishing steps.
5. Run `python scripts/build_rag_index.py` to fold the new SIB documents into the on-disk index.

## Operating principles
- **Sovereign-first:** every file must assume offline resilience and forkability.
- **Transparent trails:** capture decisions and handoffs directly in the playbooks.
- **Composable:** streams and guardrails should be small, declarative, and easy to remix across nodes.
