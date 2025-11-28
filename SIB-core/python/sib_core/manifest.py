"""Manifest helpers for SIB Core."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass
class Manifest:
    name: str
    version: str
    status: str
    description: str
    last_updated: str
    stewards: List[dict]
    compatibility: dict
    artifacts: dict


def load_manifest(path: Path | str) -> Manifest:
    """Load a manifest from disk.

    The function prefers PyYAML if installed but will raise a clear error if the
    dependency is missing.
    """

    manifest_path = Path(path)
    if not manifest_path.exists():
        raise FileNotFoundError(manifest_path)

    try:
        import yaml  # type: ignore
    except ImportError as exc:  # pragma: no cover - runtime environment dependent
        raise ImportError(
            "PyYAML is required to parse manifest files. Install sib-core[extras]"
        ) from exc

    with manifest_path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)

    return Manifest(
        name=data.get("name", ""),
        version=data.get("version", ""),
        status=data.get("status", ""),
        description=data.get("description", ""),
        last_updated=data.get("last_updated", ""),
        stewards=data.get("stewards", []),
        compatibility=data.get("compatibility", {}),
        artifacts=data.get("artifacts", {}),
    )
