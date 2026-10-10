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
