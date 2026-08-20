# Validation Evidence

This directory separates structural mapping, semantic claims, execution
receipts, and derived reports.

- [`component-map/accepted-map.json`](component-map/accepted-map.json) is the
  accepted component-to-evidence structure for the v0.1.0 candidate.
- [`release-candidate-test-receipt.json`](release-candidate-test-receipt.json)
  records the local 27-test, package-manifest, and official-validator results
  and their explicit boundaries.
- [`release-scan-v010-input.json`](release-scan-v010-input.json) is the reviewed
  claim/evidence/binding input.
- [`history/20260820T082347373282Z-206f1163.json`](history/20260820T082347373282Z-206f1163.json)
  is the append-only semantic audit authority for that evidence state.
- [`reports/20260820T082347373282Z-206f1163.md`](reports/20260820T082347373282Z-206f1163.md)
  is its deterministic human-readable view.

Earlier records and maps are immutable historical states. They may contain
wording or source identities superseded by the linked current record and must
not be used as the current release verdict.

The recorded status is `PARTIAL`: local release identity, package integrity,
and structural scholarly-audit contracts are supported. Public CI, immutable
publication, managed client installation, client discovery/invocation, and
scientific validity remain outside that record's evidence.
