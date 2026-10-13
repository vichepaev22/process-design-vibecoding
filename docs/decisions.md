# Decisions

## Decision records

- Use one portable `plugin.json` and inline `extensions.com.openai`, avoiding
  duplicate compatibility manifests whose metadata can diverge.
- Include one skill; add no hosted MCP server, lifecycle hooks, model router or
  automatic delegation. The workflow uses tools available in its host.
- Use an optional change ledger. Existing project documents and naming remain
  authoritative; structural checks do not require adopting package templates.
- Separate public GitHub release from OpenAI directory publication and runtime
  validation. Follow the official October 2026 plugin documentation.
- For 1.2.0, prefer Context7's version-matched official documentation and record
  compatibility findings. A newer documentation version does not authorize a
  dependency upgrade. Keep Context7 host-provided; disclose unavailable lookups
  and use only explicitly identified official fallback evidence.
- For 1.3.0, use the existing primary model for a short diagram-usefulness
  assessment. A separate model/router adds a request and context cost to a small
  decision, so it is not enabled automatically. A supported named model may be
  used if the user explicitly chooses it later; the skill does not change models.
- Keep diagrams optional and tied to a named scenario. Offer a sequence diagram
  for order and integration calls, a flowchart for decisions, and a state diagram
  only when a lifecycle matters. Generate only the useful selected view; do not
  add a diagram approval gate or duplicate the specification.
- Use portable Mermaid Markdown with a plain-language summary and editable
  source when diagrams are requested. Label planned/verified scope and unknown
  integrations explicitly. One generic rendered example validates this release;
  no live project integration or model-compliance benchmark is implied.
