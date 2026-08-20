# Validation Evidence

This directory separates structural mapping, semantic claims, execution
receipts, and derived reports for the v0.1.1 release candidate.

- [`component-map/accepted-map.json`](component-map/accepted-map.json) is the
  exact owner-accepted map `component-map-33bfa8598c17`.
- [`release-candidate-test-receipt.json`](release-candidate-test-receipt.json)
  records 34 passing local tests, package verification, the official skill
  validator, and explicit lifecycle limits.
- [`release-scan-v011-input.json`](release-scan-v011-input.json) is the
  reviewed v2 claim/evidence/binding input.
- [`history/20260820T161658306132Z-59d523a0.json`](history/20260820T161658306132Z-59d523a0.json)
  is the current append-only semantic authority.
- [`reports/20260820T161658306132Z-59d523a0.md`](reports/20260820T161658306132Z-59d523a0.md)
  is its deterministic human-readable view.

Earlier records and maps remain immutable historical states and are not the
current release verdict. The current record is `PARTIAL`: local release,
package, scholarly-contract, update/receipt, and thin managed-caller evidence
does not establish protected environments, hosted canary, agent execution,
draft publication, PR/main CI, release, public installation, client activation,
or scientific validity.
