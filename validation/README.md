# Validation Evidence

This directory separates structural mapping, semantic claims, execution
receipts, and derived reports for the v0.1.5 release candidate.

- [`component-map/accepted-map.json`](component-map/accepted-map.json) is the
  exact owner-accepted map `component-map-72111294987f` with SHA-256
  `1877c51f0e2919bde6c7f79dd91fdae3ef6b62de5b322551bab86f1f4466b1b3`.
- [`release-candidate-test-receipt.json`](release-candidate-test-receipt.json)
  records the passing full 41-test local suite, package verification, and the
  official skill validator.
- [`managed-workflow-pin-v083-receipt.json`](managed-workflow-pin-v083-receipt.json)
  records the focused local pin checks and their hosted-lifecycle limits.
- [`managed-workflow-pin-v083-final-input.json`](managed-workflow-pin-v083-final-input.json)
  is the reviewed v2 pin claim/evidence/binding input.
- [`history/20260826T170245964364Z-9e9090ff.json`](history/20260826T170245964364Z-9e9090ff.json)
  is the current final append-only semantic authority with canonical digest
  `fdc550991b69c919cf6dda467993f5dc7b8361bcd94192f34a8d98c8f081013a`.
- [`reports/20260826T170245964364Z-9e9090ff.md`](reports/20260826T170245964364Z-9e9090ff.md)
  is its deterministic human-readable view.

Earlier release records, inputs, and maps remain immutable historical states.
The current v0.1.5 record is `PARTIAL`: the full local suite and package
verification do not establish replacement PR/main CI, protected environments,
hosted canary, agent execution, draft publication, merge, release, installed
replacement, fresh activation, public issue submission, or scientific validity.
