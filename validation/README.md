# Validation Evidence

This directory separates structural mapping, semantic claims, execution
receipts, and derived reports for the v0.1.4 release candidate.

- [`component-map/accepted-map.json`](component-map/accepted-map.json) is the
  exact owner-accepted map `component-map-a8bab6017bdc` with SHA-256
  `6272bd254fb4e931d8f09bfda3b9104bbcb288ac4b2a3c5139446d63de802faa`.
- [`release-candidate-test-receipt.json`](release-candidate-test-receipt.json)
  records the full 40-test local suite, package verification, and the official
  skill validator.
- [`managed-workflow-pin-v083-receipt.json`](managed-workflow-pin-v083-receipt.json)
  records the focused local pin checks and their hosted-lifecycle limits.
- [`managed-workflow-pin-v083-final-input.json`](managed-workflow-pin-v083-final-input.json)
  is the reviewed v2 pin claim/evidence/binding input.
- [`history/20260825T044942270679Z-a30a4870.json`](history/20260825T044942270679Z-a30a4870.json)
  is the current append-only semantic authority with canonical digest
  `8bad41397efa9b2513b1af1e030530eddaa7c974a6cf8e279c70d78af26d4a90`.
- [`reports/20260825T044942270679Z-a30a4870.md`](reports/20260825T044942270679Z-a30a4870.md)
  is its deterministic human-readable view.

Earlier release records, inputs, and maps remain immutable historical states.
The current pin record is `PARTIAL`: local exact-SHA consistency and focused
validation do not establish protected environments, hosted canary, agent
execution, draft publication, producer PR/main CI, merge, release, installed
replacement, fresh activation, public issue submission, or scientific validity.
