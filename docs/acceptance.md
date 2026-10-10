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

## Coverage and limitations

Four focused automated tests, not an agent-quality benchmark. The helpers cannot
prove that prose fully captures user intent or that recorded tests actually ran.
Public directory approval and ChatGPT execution must be verified separately.
