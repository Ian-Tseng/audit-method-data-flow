---
name: audit-method-data-flow
description: Audit and refine scholarly method descriptions, cross-section claim chains, reusable source-backed paper terminology contracts, and reader-facing figures, tables, and slide workflows across data, model objects, phases, transformations, state, metrics, evidence, claims, lifecycle, and provenance. Use for manuscripts, abstracts, introductions, methods, results, discussions, limitations, protocol tables, figures, captions, presentations, supplements, reviewer responses, and generated DOCX/PDF/PPTX artifacts when readers may not know what enters a flow, how a research question connects to its protocol, result, counterevidence, and boundary, where a term belongs, which dataset and model are used, what is produced, whether wording is consistent, or whether a display preserves the same scientific contract at final size; apply concise Nature/Science-style wording, whole-artifact terminology checks, run-aware word/paragraph verification, and honest native-render status reporting.
license: MIT
---

# Audit Method Data Flow

Make each method branch readable as a complete scientific contract:

`input -> dataset/source -> sampled rows and label access -> model/component -> transformation -> output -> evaluation and claim boundary`

## Confirm authorization and create the local evidence contract

Before processing an unpublished manuscript, reviewer material, restricted data
description, or confidential result, confirm that the requester is authorized,
the applicable venue/institution AI and confidentiality policies were checked,
external processing is not being used, a retention decision exists, and a human
verifier remains accountable. Do not paste manuscript text, reviewer text,
private paths, credentials, or unpublished results into web searches or quality
receipts.

Read [references/method-evidence-contract.md](references/method-evidence-contract.md)
completely when a project needs a reusable machine-readable audit artifact.
Create the template locally, replace unresolved fields, then validate:

```text
<python-3> "<skill-root>/scripts/method_evidence_contract.py" template
<python-3> "<skill-root>/scripts/method_evidence_contract.py" validate --contract <local-contract.json>
```

The helper reads one bounded local JSON file and emits IDs, hashes, counts, and
finding codes without echoing claim prose. It performs no network call and
never treats structural `PASS` as proof of scientific validity.

## Build the flow contract

For every supervised, adaptation, external-validation, and diagnostic branch, record:

1. **Input:** Name the fields, artifacts, or observations entering the branch, such as student answer, reference answer, metadata, cached predictions, or a target-statistics batch.
2. **Dataset/source:** Name the benchmark, corpus, institution, source group, or held-out dataset. Do not leave “target data” or “unseen source” undefined.
3. **Partition/batch:** State which split or source supplies the rows, the batch size when material, and whether statistics and evaluation rows are disjoint.
4. **Label access:** State which labels are available for fitting, normalization, selection, and final evaluation.
5. **Model/component:** Name the model, fitted component, or deterministic operation that consumes the input. Distinguish model fitting, neural fine-tuning, weight selection, normalization, and fixed feature extraction.
6. **Transformation:** State the scientific operation applied by that component, not only its local name.
7. **Output:** Name the produced object: score, calibrated score, feature vector, risk value, ranking, representation, or diagnostic.
8. **Evaluation:** State which rows and metric evaluate the output and what baseline or protocol it is compared with.
9. **Boundary:** State the strongest supported claim and the nearest unsupported interpretation.

If any field is unknown, mark it unresolved. Do not infer dataset identity, disjointness, label access, model identity, or output from a nearby experiment.

## Trace the cross-section claim chain

For every material paper claim, trace this reader-facing chain:

`problem -> research question -> information condition/protocol -> operation and output -> result and counterevidence -> interpretation and boundary`

Read [references/claim-chain-clarity.md](references/claim-chain-clarity.md) completely when the user asks to make a paper clearer, when sections pass local method-flow checks but the overall argument remains hard to follow, or when an active planning/check-table claim may restore stale framing.

Require each link to be explicit rather than merely mentioned somewhere in the paper. Put the protocol qualifier before or in the sentence that states the result. State the strongest same-scope counterevidence beside the positive result it limits. Make the Discussion answer the same research question under the same population, exposure, metric, and output definition used in Methods and Results.

Fail the clarity audit when:

- an Introduction names a mechanism without saying which data or labels make it possible;
- a reader must combine distant paragraphs to distinguish a positive control from the authoritative stress test;
- Results state a number before naming its protocol, metric direction, or comparator;
- Discussion broadens a diagnostic, retrospective, represented-source, or source-exposed result into an automatic, prospective, source-exclusive, or deployment claim;
- an active check table or working draft presents superseded framing as “current,” even when the main manuscript is correct; or
- repeated caveats obscure the one boundary that should sit beside the claim.

When a repository has deterministic manuscript checks, add a semantic chain gate across the relevant sections and active guidance files. Test the presence of the required concepts in their required roles or sections, not a preferred sentence style.

## Build and maintain a paper terminology contract

Treat a project terminology contract as a default paper artifact, not an
optional glossary. Read
[references/paper-terminology-contract.md](references/paper-terminology-contract.md)
completely whenever central terminology is new, ambiguous, contested,
inconsistent, or being materially revised.

Before establishing or materially changing a central term:

1. Inspect the implementation, resolved configuration, artifacts, equations,
   and active paper text to determine the project's executed meaning.
2. Search current primary official reporting guidance and original
   authoritative top-tier papers by default. Prefer venue, publisher, standards
   body, official proceedings, and authoritative paper-PDF pages. Use reviews
   only to locate originals.
3. Record the source, venue/year, stable URL or DOI, adopted concept,
   project-specific mapping, whether that mapping is inferred, and the
   verification date.
4. Select one reader-facing canonical term without copying source jargon that
   changes the implemented meaning.

Apply a **semantic universality gate** before treating a term as ordinary field
language. Classify it as `field-standard`, `project-specific`, or better stated
by a `plain protocol description`. A field-standard term must preserve the same
operation and claim boundary in authoritative sources. A project-specific term
must be identified as local and defined before it carries a research question or
result. Prefer a plain protocol description when a coined label merely compresses
data access, split membership, fitting, selection, or evaluation conditions that
can be stated directly. Search across the relevant standards and adjacent
literatures. If a proposed term is absent, report that it was not located in the checked sources; do not claim that no literature uses it.

Cover the whole paper vocabulary:

- datasets, partitions, sampling units, label access, exposure, and leakage;
- learned parameters, hyperparameters, generated values, buffers, state,
  anchors, representations, predictions, and other model objects;
- initialization, fitting, training, validation, selection, calibration,
  testing, inference, deployment, and adaptation phases;
- transformations, reset/carry/freeze/detach behavior, inputs, and outputs;
- latest, best, final, aggregate, uncertainty, and checkpoint-matched metrics;
- planned, implemented, executed, structurally validated, artifact-validated,
  scientifically evaluated, paper-eligible, and historical lifecycle states;
- supported, partially supported, contradicted, untested, and bounded claims;
- configuration identity, run grouping, checkpoints, hashes, sources, and
  provenance.

For every central term, record:

`canonical term -> definition -> symbol -> role -> parent stage/branch -> input -> output -> changed/fixed conditions -> lifecycle/reset scope -> allowed aliases -> forbidden aliases -> source -> project mapping -> universality status -> citation class -> reader-facing citation -> contract version`

Apply citation closure to the reader-facing chain separately from the terminology-source
ledger. Inventory named datasets, benchmarks, methods, algorithms, model
families, architectures, metrics, specialized terms, and exact software or
checkpoint identifiers in reading order. Classify each as requiring an
authoritative scholarly citation, requiring software/model-card provenance,
project-defined and requiring a local definition, or an ordinary operation
that is citation-exempt unless its lineage changes the claim. For every item
that requires scholarly support, verify:

`first substantive use -> nearby unambiguous citation -> matching citation key or reference-list entry -> visible citation in each regenerated reader-facing artifact`

A terminology source ledger does not replace the manuscript citation. When an
implementation is inspired by or simplifies a named method, cite the original
source and state that the project mapping is inspired or inferred rather than
claiming an exact implementation. If one sentence names several methods, make
clear which source supports each term instead of relying on an ambiguous bundled
citation block. Do not add citation clutter for ordinary operations such as a
mean, minimum, maximum, generic matrix multiplication, or cosine distance unless
the paper invokes a specific scholarly lineage.

Keep one versioned project contract as the active authority. Increment its
version when a definition changes. Preserve immutable historical wording as
provenance and map it to the current term instead of silently rewriting it.
When browsing is unavailable, retain the last verified source ledger and mark
the refresh pending. If writes are unauthorized, return a candidate contract
and drift report without implying they were persisted.

## Eliminate first-reader inference

Build a definition inventory for central protocol, component, representation,
metric, and claim terms:

`term -> first abstract use -> first substantive use -> plain-language definition -> semantic relation -> parent stage/branch -> unresolved inference`

1. Scan the abstract and then the body in reading order. Record the first use,
   even when the same term has a complete entry in a later table or contract.
2. When abstract space is constrained, permit a compact self-explanatory label,
   but provide a local plain-language definition no later than the first
   substantive body use. Place it before the term structures a research
   question, result, or interpretation.
3. Count a term as defined only when the local sentence states the distinction
   that changes the claim, such as source or label access, fitted versus fixed
   state, input/output role, or evaluation boundary. Repeating the term,
   expanding an acronym, or naming its parent stage is not enough.
4. Do not require readers to combine a later protocol table, caption, glossary,
   or supplement to recover the meaning of an earlier claim.
5. When deterministic checks exist, test the required semantic relation and its
   position before the dependent claim. Avoid locking the paper to one exact
   sentence when equivalent concise wording is valid.
6. Treat counted or collective component labels as definition obligations. At
   first substantive use, name every stable member and state its role. If
   membership varies by protocol, name the invariant members and state the
   eligibility or selection rule for the rest. A phrase such as `two shared
   scorers` remains unresolved until the reader is told which two scorers it
   denotes.

Classify each item as `defined locally`, `self-explanatory with timely body
definition`, or `unresolved inference`. Fail when a central term remains an
unresolved inference at the point where a first-time reader must interpret a
research question, result, or claim boundary.

## Link every term to a named stage or branch

Treat stage-linked terminology as the default, not an optional refinement.

1. Define the reader-facing flow with a small set of canonical stage or branch names before introducing specialist components, controls, ablations, or baselines.
2. Assign every central term one parent stage or branch. On first use, state the exact parent label and whether the term names an operation, model, representation, exposure condition, ablation, baseline family, or output.
3. Prefer a stage-bearing canonical term when the relationship would otherwise be ambiguous, such as `source-exposed base-scoring control`. Do not rely on relative words such as `upstream`, `downstream`, `initial`, `post-hoc`, `upper`, or `lower` without also naming the exact stage or branch.
4. For an exposure control, distinguish where the evaluated source was seen from where the tested operation begins. For an ablation or baseline, state the parent protocol, the input that changes, and the batch, labels, models, and evaluation conditions that remain fixed.
5. Use the same canonical term in the abstract, Introduction, Methods, Results, Discussion, Limitations, headings, figure labels, captions, callouts, table titles and notes, reviewer responses, supplements, and generated DOCX/PDF artifacts. Record old or ambiguous aliases as forbidden variants in the project terminology contract.

Use a compact mapping during the audit:

`canonical term -> parent stage/branch -> role -> input -> output -> changed/fixed conditions`

Fail the audit when a first reader must infer a term location from document order, layout, or a relation-only synonym.

## Write in top-paper form

Lead with the dataset and experimental unit, then follow the data through the responsible model or component to its output. Use direct sentences, one logical move per sentence, and place the limitation beside the result it constrains. Render every mathematical variable or short expression as inline mathematics rather than prose text: for example, use `\(b(x)^2\)`, `\(\phi(x)\)`, and `\(p_i(x)\)`, not `b(x)^2`, `phi(x)`, or `p1(x)`.

Prefer this pattern:

> For each [fold/protocol], [input rows or batch] are drawn from [named dataset/source]. [Labels] remain [available/withheld] during [stages]. [Model/component] applies [operation] and outputs [object] for [evaluation rows]. We evaluate this output using [metric/comparison]. This protocol supports [claim] but does not establish [boundary].

Avoid:

- implementation inventories before the reader knows the data path;
- “the dataset,” “target batch,” “external data,” or “unseen source” without a local referent;
- passive sequences that hide which data fit a model or compute statistics;
- naming a model without stating which input it consumes and what output it produces;
- output-free component descriptions such as “features are processed”;
- treating different operations as equivalent, such as calling Ridge fitting, neural fine-tuning, blend-weight selection, and normalization all “training”;
- distant or repeated caveats that force the reader to reconstruct the protocol;
- promotional wording, generic leaderboard claims, or claims broader than the evaluation.

Keep central prose compact. Put checkpoint identifiers, exhaustive feature widths, per-source rows, prompts, and audit inventories in a table, appendix, or release artifact.

## Audit figures, tables, slides, and derivatives

Read [references/figure-table-clarity.md](references/figure-table-clarity.md) completely whenever the user asks to create, simplify, repair, compare, or validate a scholarly figure, table, diagram, presentation workflow, caption/callout, or generated visual artifact. The reference separates direct venue requirements from cross-source synthesis and project-specific visual choices; it also defines paper-figure, table, slide-deck, staging, and native-render gates.

Require every figure branch to show, in reading order:

`named source -> sampled input -> model/component -> operation -> output`

Show label access or disjointness where it changes the claim. A standalone caption must identify the dataset/protocol, explain which model or component operates on each input, state what each branch produces, and give the evaluation boundary. Align the same terms and mathematical typography across prose, headings, boxes, arrows, captions, table headers, supplements, DOCX, PDF, and peer-review copies. Require native inline OMML in Word and inline MathML or equivalent mathematical rendering in HTML/PDF; reject replacement/question-mark glyphs within math runs; display equations alone do not satisfy this gate.

## Run a word- and paragraph-level artifact check

Do not treat a raw XML substring search as a Word audit. DOCX may split one visible phrase across several `w:t` runs.

1. Reconstruct each displayed paragraph by joining prose `w:t` and Office Math `m:t` runs in reading order. Inspect the main document, tables, text boxes, headers, footers, footnotes, and endnotes.
2. Inspect reviewer comments, author replies, tracked insertions, and deleted text as separate scopes. Do not rewrite immutable reviewer wording merely because it quotes a superseded term; require the active visible body and author replies to use the canonical wording.
3. Compare active headings as complete normalized paragraphs. For cross-format prose, normalize only Unicode, soft hyphens, line-wrap hyphenation, and whitespace; do not normalize away meaningful words, numbers, signs, or protocol qualifiers.
4. Separate active upload/review derivatives from received-review evidence and archived drafts. A stale phrase in an active visible body is a failure; the same phrase in a clearly classified immutable source is provenance, not an upload failure.
5. When DOCX is in scope and the separately installed `audit-venue-submission` skill is available, use its `scripts/audit_docx_text_parts.py` helper. That helper is not bundled here; otherwise use an equivalent run-aware extractor. Recheck the copied Downloads/upload file itself, not only its workspace source.

Fail the audit if exact headings drift, an active body contains a forbidden alias, a supposedly synchronized copy differs, or the scan silently ignores non-body Word parts.

## Validate

Use a convergent repair loop for every audit that permits edits:

1. Run the complete applicable audit and record every in-scope finding.
2. Repair the findings, then rebuild and reload every affected reader-facing
   artifact from disk.
3. Treat any repair as invalidating the preceding pass. Restart every
   applicable source, contract, generated-artifact, and visual check from the
   beginning; do not resume only at the repaired item.
4. Repeat until one complete pass makes no further repair and reports zero
   unresolved in-scope failures.
5. Stop after at most three repair-and-recheck cycles. If an external
   dependency, missing authority, repeated finding set, or the cycle bound
   prevents convergence, report the artifact as blocked or partially verified
   rather than clean.

A complete clean pass closes the audit. The three-cycle bound is a safety stop,
not permission to call a still-changing artifact complete.

Ask whether a skeptical reader can answer, without searching elsewhere:

- What dataset or source supplies this branch?
- What input fields, artifacts, or observations enter it?
- Which rows enter it, and are they separate from evaluation rows?
- Which labels are available at each stage?
- Which model or component consumes each input?
- What operation does that model or component perform?
- What exact output is produced?
- Where is that output applied?
- How and against what is the output evaluated?
- What conclusion is and is not supported?

When a repository has deterministic manuscript checks, use red-green-refactor: first add a failing dataset-to-output contract assertion, then revise the canonical source, and finally rebuild and audit every affected generated artifact. Do not call the flow clear merely because the source text passes; inspect the rendered figure and final PDF. For slide decks, require native editable workflow shapes and report `UNVERIFIED_VISUAL / BLOCKED_NATIVE_RENDER` until a PowerPoint or LibreOffice export has been visually inspected.

Also fail when an active central term lacks a contract entry, one term denotes
multiple roles, aliases cross phase or lifecycle boundaries, a source-backed
mapping is presented as a quotation rather than an inference, a project-specific
term is presented as field-standard, a plain protocol description would remove
avoidable first-reader inference, an active artifact uses a forbidden alias, or
a term that requires scholarly support lacks an unambiguous nearby citation, a
matching reference entry, or a visible citation in a regenerated reader-facing
artifact.
Report terminology-contract version and source-verification date in the handoff.

## Route explicit recommended updates to the owner

When the user asks for a `recommended update`, `recommend this update`, or an
owner update and clearly means a reusable improvement to this skill, default the
destination to `Ian-Tseng/audit-method-data-flow`. Finish the substantive audit
first. If it reveals a reusable skill-level gap, select the closest non-`no_issue`
quality signal, emit one content-free receipt, and use an installed
`analyze-project-claims` consumer to create one local contribution preview
bound to that derived destination. Preview sends nothing and must not contain
manuscript text, project findings, paths, prompts, logs, patches, attachments,
or credentials.

If the analyzer is unavailable, return the exact marker and its portable
consumer prompt; do not install a transport or send anything silently. A
recommendation request authorizes only the local proposal and preview. Public
submission still requires exact approval of the draft plus a separate
public-visibility confirmation. It does not authorize an installed update,
merge, release, or publication. When no reusable skill-level improvement
exists, use `no_issue` and do not manufacture a proposal or issue.

## Finish with managed maintenance and one quality receipt

After completing the substantive audit and immediately before the final
response, run:

```text
<python-3> <skill-root>/scripts/update_policy.py --format json maintain
```

Maintenance is consent-gated, leased, and restricted to one clean, unpinned,
user-scope GitHub CLI installation from `Ian-Tseng/audit-method-data-flow`.
It must not replace or shorten the audit. Append its `message` and `action`
only when `emit` is true; a verified replacement activates on the next
invocation.

Then emit exactly one content-free outcome receipt:

```text
<python-3> <skill-root>/scripts/skill_outcome.py --format json emit \
  --outcome <completed|completed_with_limitations|failed> \
  --quality-signal <claim_evidence_gap|lifecycle_inconsistency|documentation_mismatch|internal_failure|no_issue>
```

Append only the returned `SKILL_OUTCOME_RECEIPT_V1:` marker as the final line.
Use `no_issue` when no reusable skill-quality follow-up is warranted. The
marker contains no manuscript, finding, path, prompt, log, or patch. It permits
an installed `analyze-project-claims` adapter to create one local proposal;
it never authorizes an issue, edit, update, merge, release, or upload. Any
public issue remains a separate, twice-confirmed action restricted to the
`Ian-Tseng` owner boundary.

Repository-side repair is separate from this invocation. An owner-reviewed
`managed-repair-ready` issue may enter the full-SHA-pinned central workflow,
but the label is eligibility only: protected environments separately approve
credential-free candidate work and draft publication. The workflow cannot
accept evidence, merge, release, publish, update this installation, or prove
fresh activation. Never bypass the native updater or send project content as
feedback.
