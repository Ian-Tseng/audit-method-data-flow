# Cross-Section Claim-Chain Clarity

Use this audit when the evidence may be correct but a skeptical first reader must reconstruct the argument across sections.

## Claim-chain contract

Create one row per material claim:

| Link | Reader-facing requirement |
|---|---|
| Problem | State the educational, scientific, or operational consequence, not only the technical gap. |
| Research question | Ask one answerable question with a population/source, information condition, output, and evaluation target. |
| Protocol | Name source exposure, label access, split/batch relationship, fitted versus fixed components, and metric. |
| Operation and output | Say what consumes what and what exact object is produced. |
| Result and counterevidence | Lead with the answer, then the value or comparison; place the strongest same-scope reversal, tradeoff, or null result beside it. |
| Interpretation and boundary | State what action or inference the evidence motivates and the nearest stronger claim it does not establish. |

Record the chain as:

`claim ID -> problem -> RQ -> protocol -> method output -> result -> counterevidence -> boundary -> section locators`

## Audit relations, not word occurrence

A term appearing in every section is not sufficient. Verify that the relations remain stable:

- the same evaluated population or source is in scope;
- the same label and exposure conditions qualify the claim;
- the method output is the object evaluated in Results;
- the metric direction and comparator are unchanged;
- the Discussion conclusion follows the strongest evidence, including direct counterevidence;
- the limitation bounds the claim rather than introducing a different experiment.

Classify a chain as:

- **complete:** every link is explicit and same-scope;
- **delayed qualifier:** a critical protocol or boundary appears only after the reader has interpreted the claim;
- **broken link:** a method output, result, or conclusion changes identity across sections;
- **evidence inversion:** a weaker positive control is foregrounded over a stronger same-scope null, reversal, or adverse result;
- **conclusion drift:** the Discussion or active guidance broadens the result;
- **duplicated boundary:** repeated caveats add length without making the governing limit easier to find.

## Repair pattern

Prefer the smallest repair that closes the broken relation:

1. In the Introduction, state the mechanism together with its information condition and preview the decisive positive and limiting evidence.
2. In Methods, give the branch input, permitted labels, fitted/fixed component, operation, output, and evaluation rows.
3. In Results, answer the research question in the first sentence, then give the metric, comparator, uncertainty, tradeoff, and counterevidence.
4. In Discussion, repeat the answer at the same scope and state the practical implication and unsupported stronger interpretation.
5. Mark stale active-looking plans, check tables, and working drafts as superseded; preserve true archives unchanged.

Do not force identical sentences across artifacts. Preserve semantic identity while adapting density and syntax to the venue format.
