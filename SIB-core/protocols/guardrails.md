# SIB Core Guardrails

These guardrails set the minimum safety and provenance bar for any stream or playbook introduced into SIB Core.

## Access
- Maintain a roster of maintainers in `manifest.yaml`; all changes require dual review.
- Prefer read-only mirrors for public distribution; keep write endpoints scoped to signed maintainers.

## Provenance & Moderation
- Require a source URL or hash trail for every stream entry.
- For human-authored content, log author handle and collection time.
- Reject blobs without encoding metadata (charset + format).
- For mirrored bundles, require both checksum and signature verification before merge.
- Heartbeat payloads must include the current manifest version, index hash, and bundle signature reference.

## Validation
- Run linting/format checks for JSON/YAML before merging.
- If a stream emits executable code, sandbox evaluation and log artifacts.
- Enforce schema conformance for all `continuum-*` streams and reject on missing retention or cadence values.
- Cache directories (`streams/cache`, `indices`) must be present before accepting scheduled jobs.

## Publishing
- Tag each release in `manifest.yaml` with a semantic version and timestamp.
- Document any deviations from these guardrails directly inside the associated playbook.
- Publish signed bundles to at least two mirrors and record receipt confirmations.
