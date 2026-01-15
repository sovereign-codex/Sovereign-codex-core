# systems_registry.yaml
# Canonical System & Repository Registry
# Governed by CODEX_KERNEL.md

registry:
  version: "1.0.0"
  status: canonical
  governing_document: CODEX_KERNEL.md
  last_reviewed: 2026-01-14
  steward: Sovereign Intelligence Council

definitions:
  maturity_levels:
    M0: Concept
    M1: Draft
    M2: Prototype
    M3: Fielded
    M4: Canonical

  covenant_status:
    green: In_Covenant
    yellow: Provisionally_Aligned
    red: Out_of_Covenant
    white: Dormant_Unbound

rules:
  - no_system_may_skip_maturity_levels
  - binding_actions_require_explicit_consent
  - M3_and_above_require_audit_trail
  - M4_requires_kernel_alignment
  - archived_systems_may_not_execute
  - physical_or_planetary_systems_max_maturity: M2

systems:

  # ─────────────────────────────
  # CORE SPINE INFRASTRUCTURE
  # ─────────────────────────────

  codex_kernel:
    type: document
    maturity: M4
    covenant: green
    binding: true
    description: Living core covenant and governance kernel.
    stewards: [Shepherd]
    dependencies: []
    permissions:
      may_execute: false
      may_bind: true
      may_govern: true

  si_core:
    type: repository
    maturity: M3
    covenant: green
    binding: true
    description: Monorepo spine for first-party applications and packages.
    dependencies: [codex_kernel]
    permissions:
      may_execute: true
      may_bind: true
      requires_kernel_reference: true

  sovereign_codex_core:
    type: repository
    maturity: M3
    covenant: green
    binding: true
    description: Knowledge lattice and CodexNet core.
    dependencies: [codex_kernel]
    permissions:
      may_execute: true
      may_publish: true
      requires_maturity_labels: true

  avot_core:
    type: repository
    maturity: M3
    covenant: green
    binding: true
    description: Canonical AVOT registry and guardrails.
    dependencies: [codex_kernel]
    permissions:
      may_spawn_agents: true
      may_bind: true

  avot_engine_core:
    type: repository
    maturity: M3
    covenant: green
    binding: true
    description: Runtime engine for executing AVOTs and scrolls.
    dependencies: [avot_core, codex_kernel]
    permissions:
      may_execute: true
      may_bind: false
      requires_consent_signal: true

  hive_core:
    type: repository
    maturity: M3
    covenant: green
    binding: true
    description: AVOT orchestration, syncing, and lifecycle management.
    dependencies: [avot_core, avot_engine_core]
    permissions:
      may_orchestrate: true
      requires_audit_logs: true

  quantum_intelligence_lattice:
    type: system
    alias: QIL
    maturity: M3
    covenant: green
    binding: true
    description: DAG-based VOT orchestration and metrics engine.
    dependencies: [avot_engine_core]
    permissions:
      may_execute: true
      may_schedule: true

  tyme_lab:
    type: repository
    maturity: M3
    covenant: green
    binding: true
    description: Governance, evaluation, and human-authority enforcement layer.
    dependencies: [codex_kernel]
    permissions:
      may_govern: true
      may_override_agents: true

  sovereign_interface_browser:
    type: repository
    maturity: M3
    covenant: green
    binding: false
    description: Primary user-facing interface shell.
    dependencies: [sovereign_codex_core]
    permissions:
      may_render_status: true
      may_not_bind_without_consent: true

  # ─────────────────────────────
  # ETHICS & CANON
  # ─────────────────────────────

  garden_flame_codex:
    type: codex
    maturity: M4
    covenant: green
    binding: true
    description: Ethical and harmonic law.
    permissions:
      may_govern_all: true

  living_kodex:
    type: system
    maturity: M3
    covenant: green
    binding: true
    description: Ethical Autonomous Intelligence framework.
    dependencies: [garden_flame_codex]
    permissions:
      may_constrain_agents: true

  # ─────────────────────────────
  # ECONOMIC & PLANETARY SYSTEMS
  # ─────────────────────────────

  x_change:
    type: system
    maturity: M1
    covenant: yellow
    binding: false
    description: Resonance-based value exchange system.
    dependencies: [garden_flame_codex]
    permissions:
      may_simulate_only: true

  global_guardian_lattice:
    type: system
    maturity: M1
    covenant: yellow
    binding: false
    description: Planetary coherence and protection concept.
    permissions:
      may_not_execute: true

  plasma_tuning_nodes:
    type: system
    maturity: M2
    covenant: yellow
    binding: false
    description: Experimental plasma-based coherence nodes.
    permissions:
      max_maturity_enforced: M2
      requires_safety_protocol: true

  # ─────────────────────────────
  # CULTURAL & ARCHIVAL
  # ─────────────────────────────

  digital_laboratory:
    type: repository
    maturity: M3
    covenant: green
    binding: false
    description: Public archive of laboratory scrolls.
    permissions:
      may_publish: true

  harmonic_hub:
    type: repository
    maturity: M2
    covenant: green
    binding: false
    description: Scroll and glyph index hub.
    permissions:
      requires_canon_labels: true

  sicc:
    type: repository
    maturity: M2
    covenant: green
    binding: false
    description: Sovereign Intelligence Command Center and living lab.
    permissions:
      experimental_only: true

  dream_console:
    type: repository
    maturity: M1
    covenant: green
    binding: false
    description: Mythic and narrative vessel.
    permissions:
      may_not_execute: true

  # ─────────────────────────────
  # DORMANT / ARCHIVED
  # ─────────────────────────────

  si_ui:
    type: repository
    maturity: M1
    covenant: white
    archived: true
    permissions:
      may_not_execute: true

  tyme_open:
    type: repository
    maturity: M1
    covenant: white
    archived: true

  convergence_gateway:
    type: repository
    maturity: M0
    covenant: white
    archived: true

  aurelius_subnet:
    type: repository
    maturity: M0
    covenant: white
    archived: true

  tyme_launchpad:
    type: repository
    maturity: M0
    covenant: white
    archived: true
