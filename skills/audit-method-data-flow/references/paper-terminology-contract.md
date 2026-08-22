# Paper Terminology Contract Reference

Use this reference to create or update a reusable project-wide terminology
contract. Keep specialist project terms in the project contract, not in the
generic skill.

## Authority order

1. Executed implementation, resolved configuration, and validated artifacts
   determine what the project did.
2. Venue and reporting standards determine distinctions that must be reported.
3. Original authoritative papers define specialist concepts.
4. The project contract selects one stable reader-facing expression.

Do not let published terminology override a conflicting implementation.
Label a source-to-project mapping as an inference unless the objects and
operations are the same.

## Required contract header

```text
contract_id: <stable-name>
contract_version: <integer-or-semver>
last_source_verification: <YYYY-MM-DD>
scope: <active manuscript/artifact set>
historical_policy: preserve-and-map
```

## Required source ledger

| Source | Authority type | Venue/year | URL/DOI | Adopted distinction | Project mapping | Mapping status | Verified |
|---|---|---|---|---|---|---|---|
| ... | reporting standard/original paper | ... | ... | ... | ... | direct/inferred | YYYY-MM-DD |

Use primary sources. Prefer official venue, publisher, standards body,
proceedings, or authoritative paper-PDF pages.

## Required term record

| Field | Requirement |
|---|---|
| Canonical term | One reader-facing name |
| Definition | Exact project meaning |
| Symbol | Mathematical notation, if any |
| Role | Dataset, parameter, state, transformation, output, metric, evidence, claim, lifecycle, or provenance |
| Parent | Named stage or branch |
| Input/output | Objects consumed and produced |
| Changed/fixed conditions | What varies and remains controlled |
| Scope | Batch, epoch, run, dataset, checkpoint, artifact, or paper |
| Allowed aliases | Safe shortened forms |
| Forbidden aliases | Ambiguous or superseded forms |
| Source mapping | Source-ledger identifier and direct/inferred status |
| Version | Contract version introducing the meaning |

## Required coverage

Audit at least:

- data sources, partitions, sampling, labels, exposure, and leakage;
- model objects, parameters, hyperparameters, buffers, state, and outputs;
- initialization, training, validation, selection, calibration, testing,
  inference, deployment, and adaptation;
- transformations and reset/carry/freeze/detach behavior;
- latest, best, final, aggregate, uncertainty, and checkpoint-linked metrics;
- implementation, execution, validation, completion, scientific evaluation,
  acceptance, and provenance states;
- claim strength, evidence scope, counterevidence, and boundaries.

## First-reader inference gate

Maintain a compact definition inventory in reading order:

| Term | First abstract use | First body use | Local definition locator | Required relation | Verdict |
|---|---|---|---|---|---|
| ... | paragraph/sentence or absent | section/paragraph | same sentence or nearby sentence | The distinction a reader must know before interpreting the claim | defined locally / timely body definition / unresolved inference |

A contract entry does not repair an undefined first use by itself. Check whether
the reader-facing body gives a local definition before the term structures a
research question, result, or interpretation. The local definition must state
the required relation that changes the claim, such as label access, source
exposure, fitted versus fixed state, input/output role, or evaluation boundary.
If the abstract must stay compact, require a self-explanatory abstract label and
define it no later than its first substantive body use.

For deterministic checks, assert the semantic relation and its order before the
dependent claim. Do not require one preferred sentence when equivalent wording
preserves the same definition.

## Drift and update rules

1. Read the existing contract before editing any central term.
2. Refresh primary sources before adding or materially changing terminology.
3. Compare active prose, equations, figures, captions, tables, configuration
   labels, schemas, logs, DOCX/PDF derivatives, and reviewer responses.
4. Classify each difference as a compatible alias, forbidden ambiguity,
   definition drift, phase/role conflict, or immutable historical provenance.
5. Increment the contract version for definition changes. Keep wording-only
   repairs in the current version when meaning is unchanged.
6. Preserve historical evidence and add an explicit old-to-current mapping.
7. Rebuild and re-audit generated artifacts after active-source changes.

## Completion gate

Pass only when every central active term has one role and parent, every source
mapping is identified as direct or inferred, forbidden aliases are absent from
active artifacts, historical aliases are classified as provenance, and the
contract version and source-verification date are reported.
