# Figure, Table, and Slide Clarity

Use this reference when a scholarly display carries a method flow, protocol boundary, evidence comparison, or claim boundary. It extends the method-flow audit to the visible artifact; it does not create new scientific claims or replace a venue's current author instructions.

## Routing and authority

Apply this order:

1. Current official venue/publisher instructions and author kit.
2. The project's executed method, evidence, and canonical terminology contract.
3. Direct official cross-venue display guidance.
4. Cross-source synthesis in this reference.
5. Project-specific visual choices.

Classify every display rule as one of:

- **Direct requirement:** stated by the active venue, publisher, or accessibility standard.
- **Cross-source synthesis:** a conservative practice inferred from multiple authoritative sources.
- **Project-specific choice:** topology, node count, word budget, color, spacing, or typography selected for one artifact.

Never present a project-specific choice as a universal top-tier requirement. Before venue-specific refinement, refresh the live official instructions, record the exact URL and access date, and retain the last verified rule when retrieval fails. A failed request is not evidence of a changed rule.

## Official-source ledger

Access date: **2026-08-20**.

| Source | Retrieval | Directly adopted guidance |
|---|---|---|
| [Nature Research Figure Guide](https://research-figure-guide.nature.com/) | Accessible | Figures should communicate a focused scientific message and be prepared for reliable publication. |
| [Nature figure specifications](https://research-figure-guide.nature.com/figures/preparing-figures-our-specifications/) | Accessible | Use accessible color choices, standard legible fonts, editable/vector artwork where possible, and avoid decorative shadows or effects; judge lettering at final size. Nature's stated 5--7 pt range is venue-specific, not a universal floor. |
| [Nature writing guidance](https://www.nature.com/nature-portfolio/for-authors/write) | Accessible | State the research question early, keep a focused message, make every figure earn its place, and write clear captions. |
| [NeurIPS Paper Checklist](https://neurips.cc/public/guides/PaperChecklist) | Accessible | Make protocol, limitations, reproducibility, and evidence boundaries explicit. This supports the display's scientific contract, not a prescribed visual style. |
| [Elsevier file-preparation guide](https://www.elsevier.support/publishing/answer/how-do-i-prepare-my-files-for-submission-in-editorial-manager) | Accessible; page updated 2026-06-15 | The journal guide controls; double-anonymous title-page separation and journal-specific file roles remain authoritative. |
| [Elsevier new submission experience](https://www.elsevier.support/publishing/answer/author-guide-to-editorial-managers-new-submission-experience) | Accessible; page updated 2026-07-24 | The manuscript can include text, references, figures, and tables; manuscript/declaration roles and journal-specific customization remain relevant to generated-artifact packaging. |
| [C&E: AI Guide for Authors](https://www.sciencedirect.com/journal/computers-and-education-artificial-intelligence/publish/guide-for-authors) | HTTP 403 to automated retrieval | No new rule inferred; retain the last verified journal-specific contract. |
| [AAAI author guide](https://new.aaai.org/Press/Author/authorguide.php) | HTTP 502 to automated retrieval | No new rule inferred; retain the last verified official author kit and track call. |

Nature's initial-submission and formatting-guide pages were not retrievable in this refresh. Do not use that failure to supersede a previously verified venue rule.

## Choose the smallest display that clarifies the claim

- Use a **flow figure** for three or more dependent transformations, optional branches, re-entry, or lifecycle changes.
- Use a **table** for repeated exact mappings, protocol comparisons, metric tradeoffs, or evidence/claim boundaries.
- Use prose for a single fact, a one-step operation, or a comparison that fits in one compact sentence.
- Use a **slide-native workflow** when the presentation must remain editable or when a paper raster would be stretched, illegible, or semantically incomplete at 16:9.

Do not turn evidence analyses into processing stages. A stage transforms an input into an output; an evidence analysis defines an information condition, evaluation, and allowable conclusion. Keep these as separate display surfaces when combining them would confuse topology with evidence.

## Build one semantic display specification

For a display family reused across paper, appendix, slide deck, or response letter, define one machine-readable semantic source containing:

`display id -> terminology-contract version -> nodes/rows -> role -> input -> operation -> output -> edges/relations -> information-access boundary -> medium constraints -> required visible phrases -> notes requirements`

The semantic specification is authoritative for topology and canonical labels. A renderer owns geometry, fonts, and medium-specific copy. Do not make one renderer's private strings the only source of truth.

Validate at least:

- exact node or row identities;
- main path and optional branch/re-entry edges;
- canonical stage/branch terms;
- label/data-access sentences that constrain the claim;
- whether each output changes a prediction, changes a grade, or only ranks cases;
- medium-specific word and font floors.

## Flow-figure contract

Show the main path first:

`named input -> canonical stage/component -> scientific operation -> named output`

Then add optional branches with visually distinct connectors and explicit re-entry when applicable. For every node or branch, a first reader should be able to answer:

- What enters?
- What operation or fitted component acts?
- What leaves?
- Which labels, source rows, or statistics are available?
- Does the branch change the scored output, or only produce a diagnostic?

Keep protocol comparisons in a table or caption when their full exposure logic would crowd the boxes. The image should carry topology and the decisive access boundary; the caption should carry the complete protocol qualifier and nearest unsupported interpretation.

Prefer seven or fewer semantic nodes for a first-read main-paper figure when that is sufficient, but treat this as a project choice, not a venue requirement. Collapse implementation inventory into role-level labels; move checkpoint names, feature widths, seed lists, and exhaustive controls to implementation details or a supplement.

## Table contract

Give each table one question. Recommended protocol/evidence columns are:

`analysis or protocol | data/source and row unit | label/score access | operation/output | metric/aggregation | claim boundary`

For numerical tables:

- put metric direction in the header or note;
- name aggregation (row-level, source mean, fold mean, seed mean);
- pair positive evidence with the same-scope counterevidence;
- distinguish different-protocol context from like-for-like comparison;
- keep units and decimal precision consistent;
- use compact notes for boundaries, not repeated caveats in every cell.

Do not use color alone to encode better/worse, supported/unsupported, or source exposure. Preserve signs, labels, and text cues in grayscale and for color-vision deficiencies.

## Paper-figure profile

- Design at the final column or page width; compute the effective point size after scaling.
- Use a conservative project floor of 7--8 pt unless the active venue specifies otherwise.
- Prefer vector/editable art. When raster is necessary, preserve line-art resolution and exact aspect ratio.
- Keep the main path visually dominant; optional branches should remain subordinate but traceable.
- Use standard fonts, restrained color, solid fills, and sufficient contrast.
- Avoid gradients, shadows, decorative icons, and dense legends when direct labels fit.
- Reopen the staged image, embed it in the generated Word/HTML/PDF artifact, and inspect the final PDF page rather than only the source PNG.

## Slide-deck profile

- Use native editable text boxes, shapes, tables, and connectors for the central workflow.
- Preserve the target 16:9 aspect ratio; never stretch a paper raster to fill the slide.
- Use approximately 18 pt or larger for meaningful body text and 20 pt or larger for primary labels unless the presentation context requires a stricter floor.
- Separate an evidence-map slide from method-stage slides when the audience might confuse analyses with processing stages.
- Put detailed protocol wording in speaker notes only when the decisive access boundary is also visible on the slide.
- Keep equations editable text or native math, not baked into screenshots.
- Give every important shape a stable semantic name so structural validation can count nodes, inspect font sizes, and distinguish pictures from editable objects.

An approximate `python-pptx`/Pillow preview is useful for geometry and gross-overlap checks but is not a native visual proof. Until Microsoft PowerPoint or LibreOffice exports and the slides are inspected, report:

`UNVERIFIED_VISUAL / BLOCKED_NATIVE_RENDER`

Do not call the deck submission-ready while this blocker remains.

## Caption and callout contract

Place a content-based callout near every display: `Figure 1 shows...` or `Table 2 compares...`. Avoid `above`, `below`, or duplicate identifiers in the same lead-in.

A standalone caption should state:

1. the question or object shown;
2. the dataset/protocol and information-access boundary;
3. how to read paths, branches, rows, colors, or symbols;
4. what output or metric is reported;
5. the strongest supported conclusion and nearest unsupported interpretation.

The caption may be denser than the image, but it should not repair a missing main path, unidentified operation, or invisible decisive boundary.

## Generated-artifact gate

Use staged generation:

1. Render to a candidate path.
2. Reopen and structurally validate it.
3. Validate dimensions, aspect ratio, node/row count, fonts, text, and hashes.
4. Promote atomically to the canonical path.
5. Rebuild every affected DOCX, HTML, PDF, PPTX, contact sheet, and upload copy.
6. Compare working/upload hashes and inspect generated ZIP contents when applicable.
7. Scan source and generated artifacts for stale terms, replacement glyphs, private paths, and claim drift.

For rasterized figures, audit the label source and visually inspect both the PNG and its embedded PDF render; text extraction cannot prove image-only labels. For Word, join split runs and inspect document, tables/text boxes, headers/footers, notes, comments, and tracked/deleted text as separate scopes.

## Required report fields

Report:

- display-spec and terminology-contract versions;
- authoritative source URLs and access date;
- direct requirements versus inferred/project-specific choices;
- node/row and edge counts;
- visible-word count where a project budget exists;
- image dimensions, final width, aspect ratio, and effective minimum font size;
- slide count, native-shape count, raster count, and meaningful-text floor;
- renderer identity and visual-verification status;
- working/upload hashes and equality;
- source, structural, terminology, equation, and visual audit results;
- unresolved blockers and the exact recovery action.

Use status labels that distinguish evidence:

- `SOURCE_VALIDATED`
- `STRUCTURALLY_VALIDATED`
- `ARTIFACT_VALIDATED`
- `VISUALLY_VERIFIED_NATIVE`
- `UNVERIFIED_VISUAL / BLOCKED_NATIVE_RENDER`
- `SUPERSEDED`

## Recovery and compatibility

- Preserve legacy filenames and CLI flags when reproducibility depends on them; update public wording and document intentional false positives.
- If a native renderer is unavailable, keep the editable deck and approximate preview, record the blocker, and provide the exact native export/inspection step.
- If an official source cannot be refreshed, retain the last verified venue rule, record the failed retrieval, and do not generalize from another venue.
- If the shared semantic spec changes, rebuild every renderer and rerun terminology, equation, artifact, and visual gates before promotion.
- If a display cannot meet the final-size font floor without losing required meaning, simplify the topology, split the display, or move detail to the caption/table; do not silently shrink text.

## Final checklist

- [ ] The display answers one reader question.
- [ ] Processing stages and evidence analyses are not conflated.
- [ ] Input, operation, output, access, and boundary are locally visible.
- [ ] Canonical terminology matches prose, caption, table, notes, and generated artifacts.
- [ ] The caption is standalone and the callout is nearby.
- [ ] Final-size fonts, aspect ratio, contrast, and non-color cues pass.
- [ ] Paper figures are inspected in the final PDF.
- [ ] Slide workflows are native/editable and structurally validated.
- [ ] Native-render status is reported honestly.
- [ ] Working and upload-facing copies are synchronized by hash.
