# Audit Method Data Flow

Audit Method Data Flow helps authors make scholarly methods and claims readable
as connected scientific contracts. It traces data and label access through
models, operations, outputs, evaluation, counterevidence, and claim boundaries;
maintains source-backed terminology; and checks that figures, tables, slides,
DOCX, PDF, and prose preserve the same meaning.

The skill keeps four surfaces distinct:

- method branches and their inputs, operations, outputs, and evaluation;
- cross-section claim chains from problem through boundary;
- a versioned paper terminology contract;
- reader-facing displays and generated-artifact evidence.

## Install

Install for Codex:

    gh skill install Ian-Tseng/audit-method-data-flow skills/audit-method-data-flow/SKILL.md --agent codex --scope user

Install the same package for Claude Code:

    gh skill install Ian-Tseng/audit-method-data-flow skills/audit-method-data-flow/SKILL.md --agent claude-code --scope user

Start a fresh client session after installation. In Codex, invoke:

    $audit-method-data-flow audit this manuscript's method flow, claim chain,
    terminology contract, and generated displays

In Claude Code, confirm the package appears in `/skills`, then invoke
`/audit-method-data-flow` with the same target artifacts.

Installation proves managed distribution. It does not by itself prove client
discovery, a real invocation, native rendering, or scientific validity.

## Update

Updates remain user-controlled. The installed skill asks once before enabling
notification or automatic replacement, verifies one clean GitHub-managed
user installation, and checks through a 24-hour lease after substantive use:

    gh skill update audit-method-data-flow --dry-run
    gh skill update audit-method-data-flow

Pin a reproducible installation when needed:

    gh skill install Ian-Tseng/audit-method-data-flow skills/audit-method-data-flow/SKILL.md --agent codex --scope user --pin v0.1.5

This release has a consent-gated managed updater and a content-free quality
receipt. Both run after the substantive result and never authorize telemetry,
issue submission, file upload, or feedback transport. A compatible
`analyze-project-claims` adapter may create one local proposal; any public
issue requires separate exact approval. The workflow also instructs the active
agent to refresh time-sensitive first-party scholarly guidance when relevant.

When a user explicitly asks for a recommended reusable skill update, the skill
defaults the local contribution preview to
`Ian-Tseng/audit-method-data-flow`. Nothing is sent by default. Public issue
submission still requires approval of the exact draft and a separate
public-visibility confirmation.

## Evidence boundary

The package is guidance plus deterministic package-integrity verification. It
does not parse manuscripts by itself, submit artifacts, mutate files without
authorization, or claim that structural consistency proves scientific
correctness. DOCX/PDF/PPTX and visual claims require the stated artifact and
native-render checks.

The source ledger in
[`figure-table-clarity.md`](skills/audit-method-data-flow/references/figure-table-clarity.md)
separates direct venue requirements, cross-source synthesis, project choices,
and retrieval limitations.

The [validation evidence index](validation/README.md) links the accepted
component map, local execution receipt, evidence-bound JSON record, and
derived report. Its `PARTIAL` status keeps local structural evidence separate
from public release, client activation, and scientific-validity claims.

## GitHub-managed repair boundary

This repository carries one closed policy and one thin caller pinned to analyzer
workflow commit `0fb28f50d9ed84ba47fdbdf2b7d0001f8b4e05b4`. It copies no central repair implementation. A
label is triage eligibility only; protected environments gate the agent and
draft publication separately. Method is the first live-canary candidate; hosted readiness is still unobserved.

See the immutable [managed fleet quickstart](https://github.com/Ian-Tseng/analyze-project-claims/blob/0fb28f50d9ed84ba47fdbdf2b7d0001f8b4e05b4/docs/MANAGED_FLEET_QUICKSTART.md)
and [operations runbook](https://github.com/Ian-Tseng/analyze-project-claims/blob/0fb28f50d9ed84ba47fdbdf2b7d0001f8b4e05b4/docs/MANAGED_FLEET_OPERATIONS.md).

## Development

    py -3 -X utf8 -m unittest discover -s tests -v
    py -3 -X utf8 skills\audit-method-data-flow\scripts\package_integrity.py verify

See [SOURCE.md](SOURCE.md) for ownership and transformation provenance,
[PUBLISHING.md](PUBLISHING.md) for release gates, and
[SECURITY.md](SECURITY.md) for trust boundaries.

## Citation and license

See [CITATION.cff](CITATION.cff) and the [MIT License](LICENSE). Identical
copies are included in the installed package and tested against the
repository-root authorities.
