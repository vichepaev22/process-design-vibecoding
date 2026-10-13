# Release verification — 1.3.0

Checks performed on 2026-10-13 for optional project-logic visualization:

- Four unchanged offline helper regressions passed on Python 3.12. Skill
  frontmatter and the existing portable manifest/OpenAI metadata checks passed.
- Three instruction scenarios were manually reviewed: a simple local change,
  a useful integration sequence, and an explicit request/decline/material change.
  The written outcomes keep the assessment with the current model, make
  generation optional, respect declines and preserve canonical-spec authority.
  This is instruction review, not a model-compliance benchmark.
- Context7 supplied official Mermaid sequence and public API documentation,
  including the v11.0.0 syntax reference. The generic example was parsed and
  rendered using Mermaid 11.0.0 in headless Edge; the user action, integration
  request, successful result and failure result labels were present, with no
  page errors. The rendered image was inspected for readable labels and arrows.
  Package integrity was verified against the official npm registry metadata.
- The installed skill matches all 17 source files; the preceding 1.2.0 files
  were saved for rollback, and global instructions were preserved.
- The release allowlist includes the new visualization reference in both
  package types. ZIP contents/privacy, GitHub state and downloaded asset hashes
  are checked separately before a final publication claim.

REL-008 / AC-008 is implemented in the specification phase, change control,
project-rule/spec templates, evaluation scenarios and focused reference.
Rendering validates syntax/display, not a real integration or system behavior.
No model routing or delegated agents were used. OpenAI listing and ChatGPT
runtime validation remain separate checks.

## Previous release — 1.2.0

Checks performed on 2026-10-11 for the Context7 instruction update:

- Four existing offline helper regressions passed on Python 3.12; helper behavior
  was preserved. No new tests were added for this documentation-only policy.
- The updated skill passed `quick_validate.py`. The 1.2.0 portable manifest passed
  the official JSON schema and the existing OpenAI metadata/asset checks.
- Three instruction scenarios were manually inspected: implementation with an
  installed version, a possibly API-related bug, and unavailable Context7/docs.
  Their outcomes require version-compatible lookup, official API documentation
  before the fix, and honest limits with no guessed API, respectively.
- The installed skill matches all 16 reviewed source files. Version 1.1.0 was
  saved as a rollback copy, and global instructions were preserved.
- The release allowlist includes `references/context7-documentation.md` in both
  package types. Archive integrity and privacy checks are performed on the
  versioned ZIPs before upload; published assets are downloaded and compared.

REL-007 / AC-007 is implemented across the workflow, reduced path, project
template, delivery-plan template, quality gates and supporting reference.

Context7 MCP tools were not exposed in the editing session. No live resolve or
documentation query was performed; this is instruction and package verification,
not a Context7 connection test or an LLM compliance benchmark.

## Previous release — 1.1.0

Checks performed on 2026-10-10 before GitHub publication.

## Completed checks

- Four offline tests passed on Python 3.12: PRD preservation/ambiguous selection,
  auxiliary-only specification link rejection, missing request detection with
  explicit proposal/deferral states, valid traceability and verification evidence.
- Skill frontmatter passed the Codex skill creator's `quick_validate.py`.
- The portable manifest passed the official Agent Plugins 1.0.0 JSON schema
  using jsonschema 4.26.0. OpenAI listing text limits, prompts, relative asset
  paths, square SVG icon and root marketplace reference were checked separately.
- Release project documents passed the optional structural helper.
- The 34 public files and both allowlisted ZIPs were inspected for private
  machine paths, credential patterns and missing skill references; none found.
  Archive integrity passed. Export contents are 26 plugin files and 16 standalone
  skill files, including its license.
- The local installed skill was updated after checking original hashes against
  a saved rollback copy: all 15 reviewed files match; global instructions were
  preserved. This verifies files, not future activation or model compliance.

Commands for the portable offline tests and release build:

```bash
python -m unittest discover -s tests -v
python scripts/build_release.py
```

The initial test attempt under the restricted Windows Python 3.14 environment
could not access its temporary directories. The same unchanged four tests then
passed on installed Python 3.12. No product behavior was changed to bypass a test.

## Request reconciliation

| Requirement | Result |
| --- | --- |
| REL-001 | Canonical-spec-first updates and final request reconciliation in workflow, gates and templates |
| REL-002 | Existing PRD preservation and optional traceability helper; four offline regressions |
| REL-003 | Portable manifest, GitHub marketplace, allowlisted plugin/skill ZIP builder, MIT license and public release links |
| REL-004 | ChatGPT document workflow and installation guide, including honest handling of unavailable file edits |
| REL-005 | Bounded offline verification and local installation hash check with rollback |
| REL-006 | Explicit external dependency: verified developer identity, OpenAI review and publication |

## Not established by these checks

- That an assistant will consistently capture every natural-language requirement.
- Actual installation or workflow execution inside ChatGPT.
- Submission, approval or public listing in the OpenAI plugin directory.
- Access to upload/import for any particular user's account or workspace.

Public GitHub repository/release metadata is checked separately after upload.
No hosted service, automatic model routing or delegated agents were used in this
release verification.
