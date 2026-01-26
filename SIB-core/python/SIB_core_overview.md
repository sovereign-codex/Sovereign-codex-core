# SIB Core Python package

This package exposes Python helpers for the Sovereign Intelligence Base. It bundles
lightweight utilities for reading the SIB manifest and defining core flows used by
nodes to orchestrate bootstrap and stream handling steps.

## Features
- `sib_core.manifest` to load `SIB-core/manifest.yaml` data into structured objects.
- `sib_core.flows` primitives for defining, validating, and running SIB flows.
- Pre-baked flows in `sib_core.core_flows` that mirror the playbooks shipped in this repository.
- `continuum_expansion_flow` to scaffold cache, index, and mirror directories for cross-peer distribution.

## Development
Install the package in editable mode:

```bash
pip install -e .
```

Optional YAML support can be enabled with:

```bash
pip install -e .[extras]
```

When adding new flow definitions, keep them small and composable so they can be reused
by downstream nodes.
