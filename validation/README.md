# Validation Evidence

This directory separates structural mapping, semantic claims, execution
receipts, and derived reports for the v0.2.1 release candidate.

- [`component-map/accepted-map.json`](component-map/accepted-map.json) is the
  exact owner-accepted map `component-map-38ac16028770` with SHA-256
  `5f16cda3b1749b96e32ffe1f85b6394ae7fd384d607dae62ed779890a906e852`.
- [`release-candidate-test-receipt.json`](release-candidate-test-receipt.json)
  records the passing full 56-test local suite, package verification, and the
  official skill validator. The earlier focused preacceptance receipt remains
  immutable supporting history.
- [`managed-workflow-pin-v083-receipt.json`](managed-workflow-pin-v083-receipt.json)
  records the focused local pin checks and their hosted-lifecycle limits.
- [`managed-workflow-pin-v083-final-input.json`](managed-workflow-pin-v083-final-input.json)
  is the reviewed v2 pin claim/evidence/binding input.
- [`history/20260828T162203269733Z-5a7a71ab.json`](history/20260828T162203269733Z-5a7a71ab.json)
  is the current final append-only semantic authority with canonical digest
  `8e6e3805d0c43786054a12b402ee4e6f0f57eac02d1bf43d5a5bd01025075a3a`.
- [`reports/20260828T162203269733Z-5a7a71ab.md`](reports/20260828T162203269733Z-5a7a71ab.md)
  is its deterministic human-readable view.

Earlier release records, inputs, and maps remain immutable historical states.
The current v0.2.1 record is `PARTIAL`: the full local suite and package
verification do not establish replacement PR/main CI, protected environments,
hosted canary, agent execution, draft publication, merge, release, installed
replacement, fresh activation, public issue submission, or scientific validity.
