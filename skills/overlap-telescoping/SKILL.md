# Overlap Telescoping

- id: `overlap-telescoping`
- family: structural construction
- status: draft
- implementation: complete editorial procedure; independent acceptance pending
- requires: research-optional
- outputs: candidate ledger, method artifact, feedback/state delta

## Mechanism and boundary

Merge two words by writing an identical suffix of A and prefix of B once. Default mode is exact letters, at least two; phonetic overlaps need a separate sound map. Unlike `fragment-blending`, both source strings must be reconstructible through the shared join.

## Use, avoid and inputs

Use for a compact name whose two concepts can share a natural junction. Avoid forcing unrelated words merely because letters match, single-letter accidental joins, or calling a head-tail truncation an overlap.

Required: two concept banks and acceptable length. Default: exact-letter suffix/prefix overlap of 2–4 letters, case ignored; 3 terms per bank. Optional: phonetic overlap, declared explicitly and shown in IPA or clear sound units. Do not mix modes in one ledger.

## Procedure

1. List anchor endings of length 2, 3 and 4. List partner beginnings of the same lengths. Match equal sequences manually.
2. Write A = prefix + overlap; B = overlap + suffix. Output = prefix + overlap + suffix. Reconstruct both originals as a mechanical check.
3. Reject pairs that satisfy letters but lack a positioning relationship. Keep a no-match row so empty banks are visible.
4. Compare a readable short overlap with a denser longer overlap; propose pronunciation because shared spelling may change source sounds.
5. Show up to six valid outputs from at least two semantic pairings. If only one pair works, show it as a narrow result and offer new partners rather than padding.

## Selection and recovery

A valid join is necessary, not sufficient. Check recovered source strings, semantic balance and intended pronunciation separately. If the match is technically valid but awkward, replace partner with another word starting in the same sequence. If no two-letter match survives, park the branch and offer fragment blending; never fabricate an overlap.

## Research and evidence

Use supplied words without external etymology. When a rare ingredient drives the idea, verify its exact spelling and sense using `lexical-research`. Search exact word, not a convenient guessed variant; unavailable evidence remains unverified. Phonetic equivalence is an analysis proposal unless a pronunciation reference was actually consulted.

Source basis: S04; explicit overlap contrasted with fragments. See [research bibliography](../../docs/research/BRANDING_METHODS_RESEARCH.md). Steps and worked fixtures below are editorial adaptations, not attributed algorithms or efficacy evidence.

## Candidate record and interaction

Use the [session protocol](../../docs/SESSION_PROTOCOL.md) and [source contract](../../docs/SOURCES_AND_RESEARCH.md). Every displayed batch has stable branch/candidate IDs; English spelling; proposed pronunciation/stress where uncertain; exact lineage; separate `form` and `evidence`; source IDs or `none`; useful association and main drawback. Keep intermediate tables in the exploration log or session-owned research notes. Do not put real sessions in this library.

Show two or three contrasting previews before expanding, unless the user already delegated or specified the operation. Ask which property to preserve, not merely which name is “best.” After feedback record the actual words, changed constraints, rejected/parked paths and next options. Praise does not save a name. Add only explicit selections; repeated selection updates the same candidate. A six-name batch is a pause for navigation, never an automatic export.

## Ordered combinations

`lexical-research` → `overlap-telescoping`: use attested spelling. `overlap-telescoping` → `phonetic-invention` is a hybrid if the join is altered; preserve the original overlap step before sound repair. `fragment-blending` is the explicit fallback, not an interchangeable label.

## Complete synthetic worked trace

All brand briefs, candidate judgments and user turns below are fixtures, not consumer findings. Source facts are separately identified. IDs are local to this trace.

Brief: bright ideas developed together, warm rather than corporate. B01 previews: warm-light **Gleamber**, community **Teamity**, wandering-thought **Dreamble**. All satisfy the default two-letter overlap. User fixture: “Explore warmth, but do not make it childish.” Supplied words, sources none.

| ID / name | A decomposition | B decomposition | Output reconstruction | Assessment |
|---|---|---|---|---|
| B01-C01 Gleamber | gle + am (gleam) | am + ber (amber) | gle + am + ber | GLEEM-ber proposed; amber sound not preserved |
| B01-C02 Teamity | te + am (team) | am + ity (amity) | te + am + ity | tee-AM-i-tee proposed; teamwork/friendship, bouncy |
| B01-C03 Dreamble | dre + am (dream) | am + ble (amble) | dre + am + ble | DREEM-bəl proposed; exploratory, collaboration less legible |
| diagnostic only: Gloworks | glo + w (glow) | w + orks (works) | glo + w + orks | reject: one-letter join below default |

All candidates invented / not applicable. Spelling overlap is mechanically demonstrated; it is not lexical evidence or evidence that source pronunciations survive. Gloworks is a boundary diagnostic, not a valid default preview. Contained-word pair spark + ark also fails usefulness: spark already contains all of ark and no new material is added.

Weak valid output C02 is too bouncy for the selected brief. Repair by keeping team and replacing partner amity with amber, preserving shared am: **Teamber** (C04) = te[am] + [am]ber → te + am + ber, TEEM-ber proposed. This is shorter, warm, but has a possible “timber” resemblance. C01 emphasizes light, C03 exploratory thought, C04 collective warmth; do not claim a single semantic family covers all equally well.

User fixture: “Keep Gleamber as a direction, no save; Teamber still sounds playful.” State: active B01 REFINE; favorites=[]; rejected=bouncy team family; preferred=warm light; next=research amber sense in a child `lexical-research` branch or compare intact compounds. All trials remain visible.
