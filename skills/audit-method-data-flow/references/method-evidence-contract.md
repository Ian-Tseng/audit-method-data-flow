# Local Method Evidence Contract

Use this contract when the method-flow and claim-chain audit must be repeatable
without placing manuscript prose in logs, issue drafts, or external services.
The contract is a local project artifact; do not add a confidential instance to
the reusable skill repository.

## Authorization gate

Set all authorization fields deliberately. Processing is blocked unless the
requester is authorized, the applicable confidentiality policy was checked,
external services are disabled, a retention decision is recorded, and a human
verifier is named. Confirm venue and institutional AI rules separately when
they apply. The helper does not grant permission.

## Stable relations

Represent every method branch with a stable ID and all nine fields:

`input -> dataset_source -> partition_or_batch -> label_access -> model_component -> transformation -> output -> evaluation -> boundary`

Represent every material claim with a stable ID, its branch ID, the complete
problem-to-boundary chain, and section locators. Use `unresolved` instead of
guessing. Bind evidence to a claim with a SHA-256 digest, evidence kind,
content-minimized stable `locator_id`, locator-verification state, verifier,
and verification time. The all-zero template digest and `unresolved` locator
are placeholders; they never count as verified evidence or permit `PASS`.
Hashes bind bytes; they do not establish that an interpretation is
scientifically correct.

## Commands

```text
<python-3> "<skill-root>/scripts/method_evidence_contract.py" template
<python-3> "<skill-root>/scripts/method_evidence_contract.py" validate --contract <local-contract.json>
```

`PASS` means the declared structural fields and verified evidence bindings are
complete. `PARTIAL` identifies unresolved relations or evidence gaps by ID.
`BLOCKED` means the authorization/confidentiality boundary is not satisfied.
The report never echoes branch or claim prose and never uploads content.

The input must be ordinary UTF-8 JSON, at most 256 KiB, and not a symlink or
reparse point. Keep it inside the authorized project boundary and apply the
recorded retention decision after the audit.
