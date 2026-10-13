# Release specification — Process Design Vibecoding 1.3.0

This file is the canonical specification for this skill release. Auxiliary
installation and submission guides do not replace it.

## Context and problem

Accepted changes can be lost when an assistant updates an auxiliary plan but
leaves the main specification unchanged. The package also needs a public,
shareable distribution and a portable plugin for ChatGPT and Codex.

## Requirements and domain rules

- REL-001 / accepted: name the canonical specification; record each material
  request with an explicit decision status; update accepted requirements in
  that document before implementation; reconcile current-task requests before
  completion. Keep acceptance, implementation and verification separate.
- REL-002 / accepted: preserve existing specifications and project conventions;
  support optional traceability checks without forcing new document formats.
- REL-003 / accepted: publish a public GitHub repository and downloadable plugin
  and standalone skill packages. Include installation guidance and MIT license.
- REL-004 / accepted: support ChatGPT document workflows honestly when there is
  no file-editing tool. Provide current guidance for the ordinary ChatGPT plugin
  directory, workspace upload and GitHub import.
- REL-005 / accepted: use bounded offline tests and package validation; preserve
  the local installed skill, with a rollback copy, while applying this update.
- REL-006 / external dependency: public directory publication requires a
  verified developer identity and OpenAI review. Package preparation and GitHub
  publication do not establish directory listing or actual ChatGPT execution.
- REL-007 / accepted: before software implementation, identify relevant
  technologies and installed or explicitly targeted versions, obtain current
  documentation through Context7, check API compatibility with those versions,
  and use documented methods/examples. For a bug that may involve a technology's
  API, check its official documentation through Context7 before choosing the
  fix. If documentation or the Context7 tool is unavailable, state the precise
  limitation; never invent an API or claim a lookup occurred. An explicitly
  disclosed official-source fallback may resolve the contract; unresolved API
  work stays pending while independent authorized work continues.
- REL-008 / accepted: offer lightweight project-logic visualization as an
  optional aid after requirements are understood or a material change affects
  a scenario. The current primary model assesses whether a diagram clarifies
  ordering, cross-system calls, branching or results; no additional model call
  or router is required. Recommend a concrete scenario and diagram type once,
  respect a decline, and continue independent work while an optional answer is
  pending. When requested, prefer a sequence diagram from the user's action
  through the system and named integrations to the visible result, including
  relevant failure behavior. Link it to the canonical requirements/acceptance,
  label planned versus verified behavior, and update accepted diagrams with the
  corresponding requirements. Diagrams never replace the canonical spec or
  become an additional implementation gate by default.

## Acceptance criteria

- AC-001: instructions explicitly prevent an auxiliary-only update; completion
  reconciles all material current-task requests and records actual evidence.
- AC-002: an existing PRD remains unchanged during bootstrap; optional validation
  rejects accepted changes linked only to an auxiliary document, missing request
  IDs and unsupported verification claims; valid traceability passes.
- AC-003: the manifest follows the portable schema, a skills-only ZIP has its
  manifest at the root, and the GitHub marketplace points to the root package.
- AC-004: public files and archive contents exclude machine paths, credentials,
  chat transcripts and private project data; public repository/release verified.
- AC-005: local installation matches the reviewed package; Astra remains paused.
- AC-006: documentation distinguishes package checks from ChatGPT execution and
  public directory approval; no automatic listing or universal plan access claim.
- AC-007: the main workflow, reduced workflow, implementation gate, project-rule
  template and quality gates enforce REL-007. Supporting guidance explains
  resolve-library-id then query-docs, version-specific selection, focused
  queries, evidence, API-related bug fixes and unavailable-documentation handling.
  The new reference is included in plugin and standalone skill archives. Package
  and installed skill versions identify the current release.
- AC-008: inspect three bounded scenarios: a simple local change that needs no
  offer, an integration scenario where a sequence diagram is useful, and an
  explicit request or later requirement change. The optional offer must not
  block delivery, invoke a second model automatically, repeat after refusal,
  invent integrations, or imply that a planned flow has been verified. Validate
  and render one generic sequence example containing both a successful result
  and an integration failure. Include the reference in both packages; the
  source and installed skill must match version 1.3.0.

## Assumptions and open questions

Public GitHub publication is explicitly authorized. The package is instruction
based and requires no hosted MCP service or authentication. Access to workspace
uploads and public-directory submission depends on the recipient's account and
workspace. Catalog submission is not part of a confirmed published result.
Context7 is supplied by the host environment and is not bundled or configured
by this instruction-based plugin. This release changes workflow instructions;
it does not establish live Context7 availability or execution.
