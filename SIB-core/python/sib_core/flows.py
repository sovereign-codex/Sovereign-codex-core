"""Core flow primitives for the Sovereign Intelligence Base."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Dict, Iterable, List, Optional


@dataclass
class FlowContext:
    """Runtime state shared across flow steps."""

    state: Dict[str, object] = field(default_factory=dict)
    log: List[str] = field(default_factory=list)

    def record(self, message: str) -> None:
        """Append a log entry to the context."""

        self.log.append(message)


@dataclass
class FlowStep:
    """A single step in a flow."""

    name: str
    description: str
    action: Callable[[FlowContext], None]

    def run(self, context: FlowContext) -> None:
        """Execute the step and record the outcome."""

        context.record(f"starting:{self.name}")
        self.action(context)
        context.record(f"completed:{self.name}")


@dataclass
class Flow:
    """Composable unit that wires steps together."""

    name: str
    purpose: str
    steps: List[FlowStep]
    guardrails: List[str] = field(default_factory=list)

    def run(self, context: Optional[FlowContext] = None) -> FlowContext:
        """Run each step sequentially."""

        ctx = context or FlowContext()
        for step in self.steps:
            step.run(ctx)
        return ctx


class FlowRegistry:
    """Registry for discovering and reusing flows."""

    def __init__(self) -> None:
        self._flows: Dict[str, Flow] = {}

    def register(self, flow: Flow) -> None:
        if flow.name in self._flows:
            raise ValueError(f"flow already registered: {flow.name}")
        self._flows[flow.name] = flow

    def get(self, name: str) -> Flow:
        try:
            return self._flows[name]
        except KeyError as exc:
            raise KeyError(f"unknown flow: {name}") from exc

    def available(self) -> Iterable[str]:
        return sorted(self._flows.keys())
