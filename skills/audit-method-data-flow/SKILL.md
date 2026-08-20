---
name: audit-method-data-flow
description: Audit and refine scholarly method descriptions, cross-section claim chains, reusable source-backed paper terminology contracts, and reader-facing figures, tables, and slide workflows across data, model objects, phases, transformations, state, metrics, evidence, claims, lifecycle, and provenance. Use for manuscripts, abstracts, introductions, methods, results, discussions, limitations, protocol tables, figures, captions, presentations, supplements, reviewer responses, and generated DOCX/PDF/PPTX artifacts when readers may not know what enters a flow, how a research question connects to its protocol, result, counterevidence, and boundary, where a term belongs, which dataset and model are used, what is produced, whether wording is consistent, or whether a display preserves the same scientific contract at final size; apply concise Nature/Science-style wording, whole-artifact terminology checks, run-aware word/paragraph verification, and honest native-render status reporting.
license: MIT
---

# Audit Method Data Flow

Make each method branch readable as a complete scientific contract:

`input -> dataset/source -> sampled rows and label access -> model/component -> transformation -> output -> evaluation and claim boundary`

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

`canonical term -> definition -> symbol -> role -> parent stage/branch -> input -> output -> changed/fixed conditions -> lifecycle/reset scope -> allowed aliases -> forbidden aliases -> source -> project mapping -> contract version`

Keep one versioned project contract as the active authority. Increment its
version when a definition changes. Preserve immutable historical wording as
provenance and map it to the current term instead of silently rewriting it.
When browsing is unavailable, retain the last verified source ledger and mark
the refresh pending. If writes are unauthorized, return a candidate contract
and drift report without implying they were persisted.

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
mapping is presented as a quotation rather than an inference, or an active
artifact uses a forbidden alias. Report terminology-contract version and
source-verification date in the handoff.
