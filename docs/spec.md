# Release specification — Process Design Vibecoding 1.1.0

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

## Assumptions and open questions

Public GitHub publication is explicitly authorized. The package is instruction
based and requires no hosted MCP service or authentication. Access to workspace
uploads and public-directory submission depends on the recipient's account and
workspace. Catalog submission is not part of a confirmed published result.
