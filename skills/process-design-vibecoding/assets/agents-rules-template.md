# Project agent instructions

<!-- Local supplement derived from the supplied SKILL.md, 2026-10-05. Only create after adapting to the project; do not replace existing instructions. -->

- Read applicable instructions and the relevant current specification and plan.
- Inspect existing implementation before proposing architecture.
- Preserve user changes, accepted decisions and project conventions.
- Prefer process-design-vibecoding for substantial software changes.
- Use the reduced workflow for bounded fixes; handle trivial edits directly.
- Before software implementation, identify affected technologies and versions,
  obtain current documentation through Context7, verify API compatibility and
  use documented methods/examples. For possibly API-related bugs, check the
  technology's official documentation through Context7 before choosing the fix.
  Disclose unavailable tools/docs; label any official-source fallback and never
  invent an API or claim an unperformed lookup.
- Ask only about uncertainty that materially changes behavior, risk or scope.
- Record the exact canonical-spec path in the project map below. Feature plans do not replace it.
- Capture material proposals and deferred work; update accepted requirements in the canonical spec before code.
- Keep intentional requirement changes, acceptance criteria, plan and tests synchronized.
- Before completion reconcile every material current-task request with its recorded status and actual delivery evidence.
- Run relevant project verification commands and report actual outcomes.
- Do not treat document presence or a smoke test as end-to-end verification.

## Project commands and conventions

- Canonical specification: choose the existing primary PRD/spec.
- Plan, acceptance and decisions: use the established project paths.
- Verification commands: record only commands appropriate to this project.

Fill in these paths and commands after inspecting the repository; do not leave this template as an active instruction file.
