# Release acceptance

## Scenarios

AC-001: the written procedure requires canonical-spec-first updates and a final
request reconciliation, including explicit proposal/deferral states.

AC-002: offline helper regressions cover PRD preservation, an auxiliary-only
accepted change, a missing current-task request and valid/invalid verification
records. These checks evaluate document structure and traceability.

AC-003–AC-005: validate the package, inspect exported archives, compare installed
file hashes, and inspect public GitHub repository/release metadata.

AC-006: installation instructions explicitly distinguish a GitHub package from
an approved listing, and do not claim ChatGPT runtime tests were performed.

AC-007: inspect three instruction scenarios: a new slice using an installed
library version, a possibly API-related bug, and unavailable Context7/docs.
The required outcomes are version-aware lookup, official API verification,
and an honest limitation with no guessed contract. Verify the new reference
is present in both ZIPs and every installed skill file matches the source.
This is instruction/package inspection, not an LLM compliance benchmark.

AC-008: manually walk through the simple-change, useful-integration and
explicit-request/change scenarios. Check that the current model makes a short
usefulness assessment, any offer is optional, a decline is remembered, and the
diagram remains tied to current requirements. Parse and render the generic
sequence example; inspect its action, integration call, successful response,
failure branch and visible user result. Rendering proves syntax/display, not
the integration's behavior or future agent compliance. Check package inclusion
and source/installed version/hash equality.

## Coverage and limitations

Four focused automated tests, not an agent-quality benchmark. The helpers cannot
prove that prose fully captures user intent or that recorded tests actually ran.
Public directory approval and ChatGPT execution must be verified separately.
