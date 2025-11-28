"""Canonical flows that mirror the SIB playbooks."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

from .flows import Flow, FlowContext, FlowStep


def _ensure_path_exists(path: Path, ctx: FlowContext) -> None:
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
        ctx.record(f"created:{path}")
    else:
        ctx.record(f"exists:{path}")


def _echo_guardrails(guardrails: Iterable[str], ctx: FlowContext) -> None:
    for guardrail in guardrails:
        ctx.record(f"guardrail:{guardrail}")


def bootstrap_flow(base_dir: Path = Path(".")) -> Flow:
    """Bring a node online by creating the expected directories."""

    flow_guardrails = ["offline-ready", "idempotent"]

    def record_guardrails(ctx: FlowContext) -> None:
        _echo_guardrails(flow_guardrails, ctx)

    def create_playbook_dir(ctx: FlowContext) -> None:
        _ensure_path_exists(base_dir / "playbooks", ctx)

    def create_protocol_dir(ctx: FlowContext) -> None:
        _ensure_path_exists(base_dir / "protocols", ctx)

    def create_stream_dir(ctx: FlowContext) -> None:
        _ensure_path_exists(base_dir / "streams", ctx)

    steps = [
        FlowStep(
            name="record-guardrails",
            description="Capture bootstrap guardrails",
            action=record_guardrails,
        ),
        FlowStep(
            name="create-playbook-dir",
            description="Ensure playbook folder exists",
            action=create_playbook_dir,
        ),
        FlowStep(
            name="create-protocol-dir",
            description="Ensure protocol folder exists",
            action=create_protocol_dir,
        ),
        FlowStep(
            name="create-stream-dir",
            description="Ensure stream folder exists",
            action=create_stream_dir,
        ),
    ]

    return Flow(
        name="bootstrap",
        purpose="Prepare the SIB folders on disk",
        steps=steps,
        guardrails=flow_guardrails,
    )


def stream_intake_flow(stream_name: str, guardrails: Iterable[str] | None = None) -> Flow:
    """Represent the critical path for receiving a new stream payload."""

    flow_guardrails = ["reproducible"]
    if guardrails:
        flow_guardrails.extend(guardrails)

    def validate(ctx: FlowContext) -> None:
        ctx.state.setdefault("validated_streams", []).append(stream_name)
        ctx.record(f"validated:{stream_name}")

    def persist(ctx: FlowContext) -> None:
        ctx.state.setdefault("persisted_streams", []).append(stream_name)
        ctx.record(f"persisted:{stream_name}")

    def publish(ctx: FlowContext) -> None:
        ctx.state.setdefault("published_streams", []).append(stream_name)
        ctx.record(f"published:{stream_name}")

    steps = [
        FlowStep(
            name="record-guardrails",
            description="Document guardrails in the context log",
            action=lambda ctx: _echo_guardrails(flow_guardrails, ctx),
        ),
        FlowStep(
            name="validate-stream",
            description="Apply schema and safety checks",
            action=validate,
        ),
        FlowStep(
            name="persist-stream",
            description="Store the incoming stream artifact",
            action=persist,
        ),
        FlowStep(
            name="publish-stream",
            description="Expose the stream to downstream consumers",
            action=publish,
        ),
    ]

    return Flow(
        name=f"stream-intake:{stream_name}",
        purpose="Validate, persist, and publish a stream payload",
        steps=steps,
        guardrails=flow_guardrails,
    )


def continuum_expansion_flow(
    base_dir: Path = Path("."), streams: Iterable[str] | None = None
) -> Flow:
    """Prepare cache, index, and mirror scaffolding for continuum expansion."""

    flow_guardrails = ["signed-bundles", "redundant-mirrors", "heartbeat-visible"]
    stream_names = list(streams) if streams else []

    def record_guardrails(ctx: FlowContext) -> None:
        _echo_guardrails(flow_guardrails, ctx)

    def ensure_cache(ctx: FlowContext) -> None:
        _ensure_path_exists(base_dir / "streams" / "cache", ctx)

    def ensure_indices(ctx: FlowContext) -> None:
        _ensure_path_exists(base_dir / "indices", ctx)

    def ensure_mirrors(ctx: FlowContext) -> None:
        _ensure_path_exists(base_dir / "mirrors", ctx)

    def provision_stream_placeholders(ctx: FlowContext) -> None:
        cache_dir = base_dir / "streams" / "cache"
        for stream_name in stream_names:
            placeholder = cache_dir / f"{stream_name}.placeholder"
            if not placeholder.exists():
                placeholder.touch()
                ctx.record(f"provisioned:{placeholder}")
            else:
                ctx.record(f"exists:{placeholder}")

    def mark_ready(ctx: FlowContext) -> None:
        ctx.record("continuum-ready")

    steps = [
        FlowStep(
            name="record-guardrails",
            description="Document guardrails in the context log",
            action=record_guardrails,
        ),
        FlowStep(
            name="ensure-cache",
            description="Create stream cache directory",
            action=ensure_cache,
        ),
        FlowStep(
            name="ensure-indices",
            description="Create index directory",
            action=ensure_indices,
        ),
        FlowStep(
            name="ensure-mirrors",
            description="Create mirror directory",
            action=ensure_mirrors,
        ),
        FlowStep(
            name="provision-streams",
            description="Pre-create placeholders for continuum streams",
            action=provision_stream_placeholders,
        ),
        FlowStep(
            name="mark-ready",
            description="Signal readiness for continuum expansion",
            action=mark_ready,
        ),
    ]

    return Flow(
        name="continuum-expansion",
        purpose="Provision directories and placeholders for cross-peer expansion",
        steps=steps,
        guardrails=flow_guardrails,
    )
