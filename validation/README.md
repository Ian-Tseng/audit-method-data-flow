# Validation Evidence

This directory separates structural mapping, semantic claims, execution
receipts, and derived reports for the v0.2.0 release candidate.

- [`component-map/accepted-map.json`](component-map/accepted-map.json) is the
  exact owner-accepted map `component-map-e1c145536297` with SHA-256
  `35b3d97c3c5a64fd1270fe3540ad54171f93f9ac76a7f4666a28eeaa9fb5cc05`.
- [`release-candidate-test-receipt.json`](release-candidate-test-receipt.json)
  records the passing full 55-test local suite, package verification, and the
  official skill validator.
- [`managed-workflow-pin-v083-receipt.json`](managed-workflow-pin-v083-receipt.json)
  records the focused local pin checks and their hosted-lifecycle limits.
- [`managed-workflow-pin-v083-final-input.json`](managed-workflow-pin-v083-final-input.json)
  is the reviewed v2 pin claim/evidence/binding input.
- [`history/20260827T052007359636Z-af37b0d4.json`](history/20260827T052007359636Z-af37b0d4.json)
  is the current final append-only semantic authority with canonical digest
  `32fb4eb2ce62ab2747b17af41b6496eb3be5c273b1117553a21c8f45d008f68d`.
- [`reports/20260827T052007359636Z-af37b0d4.md`](reports/20260827T052007359636Z-af37b0d4.md)
  is its deterministic human-readable view.

Earlier release records, inputs, and maps remain immutable historical states.
The current v0.2.0 record is `PARTIAL`: the full local suite and package
verification do not establish replacement PR/main CI, protected environments,
hosted canary, agent execution, draft publication, merge, release, installed
replacement, fresh activation, public issue submission, or scientific validity.
