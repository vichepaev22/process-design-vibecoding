# Release verification — 1.1.0

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
