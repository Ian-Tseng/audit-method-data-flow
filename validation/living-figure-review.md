# Evidence-map review and owner acceptance (v0.2.2)

The candidate below was reviewed and accepted on November 27, 2026 under the
owner's delegation of the v0.2.2 release. Previous maps and audit records remain
immutable history.

- Candidate: [component-map-6f7f031a4fc8](component-map/candidates/20261127T075102927595Z-15d2c900-component-map-6f7f031a4fc8.json)
- Candidate file SHA-256: `9b1eff46de6187a1447e7cfc079c730c5cf5149f4bd7b65043744e02d8a66dc8`
- Previous accepted map: `component-map-cbb849faebee`
- [Observation](component-map-observation-v022.json)
- [Exact delta](component-map/deltas/20261127T075102927595Z-15d2c900.json)

The candidate adds one element, `scholarly-audit-contract / living-architecture-figure`,
and refreshes the source hashes of the files changed for v0.2.2. It also records the
current analyzer identity. No component or element is removed.

[Owner acceptance](living-figure-owner-acceptance.json) records the exact candidate
hash. After acceptance the reconciler reported `checked_unchanged`, and evidence
preflight returned `ready`. The scoped [audit record](history/20261127T075518264661Z-729b7760.json)
and [derived report](reports/20261127T075518264661Z-729b7760.md) are `PARTIAL`:
source presence is supported; display clarity, publication and fresh activation are
unobserved. Structural acceptance does not imply passing CI, merge or publication.

A second candidate, [component-map-e8e74937de2f](component-map/candidates/20261127T075349677625Z-ce5aac4e-component-map-e8e74937de2f.json) (SHA-256 `fbc6bc18d351bddf002f2ad201306b8ec5b08eadb9bc42767dd9ff31a2ab47d9`),
was accepted after the release pins moved to 0.2.2. Its delta only refreshes the hashes of the package
manifest, `package_integrity.py` and two tests. The current record above is bound to it; the first v0.2.2
record is kept as superseded history.

The test file `tests/test_package_contract.py` then had its release-date pins moved to 2026-11-27,
which needed two more hash-only candidates. The final accepted map is `component-map-556341431902` (file SHA-256 `bc235a6290a97fdd3ef17e81c603dbf21835fc4c02efa7415ba313f4aafc3a9f`);
every acceptance is listed in the owner acceptance record. The current record is bound to the final map.
