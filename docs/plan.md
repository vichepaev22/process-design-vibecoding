# Release plan

## Objective and scope

Deliver REL-001 through REL-005 and REL-007 from the canonical `docs/spec.md`; document the
external dependency in REL-006.

## Vertical slices

1. Canonical-spec change control, request reconciliation and document templates.
2. Optional preservation and traceability helpers with four offline regressions.
3. Portable plugin, public marketplace, reproducible ZIP builder and guides.
4. Validate, install locally with rollback, publish GitHub repository and release.
5. For 1.2.0, add the Context7 documentation checkpoint and API-related bug-fix
   rule across the main workflow, templates and gates; preserve prior requirements.
6. Validate the updated skill, archive reference and version consistency, sync
   the installed files with rollback, and publish a new release.

## Verification commands

```bash
python -m unittest discover -s tests -v
python scripts/build_release.py
```

Also validate skill frontmatter and the portable manifest against its official
schema. Audit public files/ZIP contents and verify repository/release API state.

## Progress and remaining work

Implementation and validation results are recorded in `docs/verification.md`.
The 1.1.0 distribution is complete. The 1.2.0 Context7 instruction update and
local installation are complete; versioned distribution uses the GitHub release.
OpenAI review and a ChatGPT runtime test remain separate external checks.
