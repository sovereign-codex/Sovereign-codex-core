# Continuum expansion: extend a Sovereign Intelligence Base across peers

## Goal
Expand a running SIB node so it continuously exchanges signals, artifacts, and guardrail updates with trusted peers while keeping offline resilience.

## Steps
1. **Snapshot current state** — export the active `manifest.yaml`, `streams/`, and `protocols/` to `mirrors/` and sign the bundle (GPG or Sigstore). Record the signature location.
2. **Enable heartbeats** — configure a scheduled job to emit a JSON heartbeat from `streams/continuum-heartbeat.json` to peers every 15 minutes; include version, checksum, and index hash.
3. **Provision caches** — ensure `streams/cache/` and `indices/` exist; pre-create empty files for streams declared in `continuum-*` descriptors to keep paths stable.
4. **Guardrail sync** — pull the latest `protocols/` from upstream peer(s). Diff against local guardrails and capture exceptions directly in this playbook.
5. **Mirror ingestion** — register `streams/continuum-mirror.json` in your intake scheduler. Validate checksums before writing to `streams/cache/`.
6. **Rebuild index** — run `python scripts/build_rag_index.py` from repo root. Store the resulting hash in the heartbeat payload.
7. **Publish and tag** — bump `manifest.yaml` version and `last_updated`, then push signed bundles to configured mirrors and IPFS if available.

## Success criteria
- Heartbeat artifacts are present in `streams/cache/` with current timestamps and hashes.
- Guardrail deviations are documented and reconciled or explicitly deferred.
- Index rebuild completes without validation errors and the hash is echoed in the latest heartbeat.
- Mirrors receive the signed bundle and acknowledge integrity checks.
