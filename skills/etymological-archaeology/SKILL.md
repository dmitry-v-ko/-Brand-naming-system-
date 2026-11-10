# Etymological Archaeology

- id: `etymological-archaeology`
- family: historical form and meaning tracing
- status: draft
- implementation: new editorial procedure; independent acceptance pending
- requires: research-required for factual claims
- outputs: typed lineage graph, uncertainty ledger, node-based candidates, repair and state delta
- acceptance evidence: actual E01–E03 retrieval in [historical evidence](../../docs/research/HISTORICAL_METHODS_EVIDENCE.md); synthetic trace below; independent acceptance pending

## Operator and boundaries

Trace documented earlier forms and meanings, classify the relationships between them, then choose a useful **node or semantic transition** as naming material. The artifact is a small graph with evidence on every edge. It is not a collection of impressive ancient-looking syllables.

`cross-language-mining` asks what a concept is called elsewhere now. This skill asks how particular forms and senses became connected over time. `historical-lexical-archaeology` can recover an old sense without reconstructing ancestry. Here a documented route is essential; a historical dictionary entry alone does not make a full genealogy. Sound resemblance is a search lead, not an etymological edge.

Use when a transition such as material object → guidance offers a useful story, or when a familiar word can be viewed through an earlier meaning. Avoid when the name needs a falsely certain origin, the user wants an invented word presented as ancient, or the chain contributes only prestige with no useful brand association. A true origin can still be unsuitable. Earlier meaning does not override contemporary meaning; do not commit the etymological fallacy.

Required inputs: desired action/relationship, audience, excluded associations, and acceptable explanation burden. Defaults: two present-day seed concepts, one opened entry per seed, a maximum of three useful historical nodes per chain before reassessment. Optional: language/era, permitted non-Latin source scripts, reconstructed-form tolerance and English-facing sound constraints. If delegated, select a provisional chain and record that as the agent's decision.

## Evidence notation

Give each node exact source spelling, language, dated period when supported, sense, attestation status and reference locator. Use `A` for a form reported in the reference as historical/attested; `R` for a reconstructed form explicitly marked by the source; `U` for unresolved. Asterisks belong in the research graph for reconstructed forms. Removing one from a candidate display does not make the form attested.

Type each edge: **inheritance**, **borrowing**, **spelling revision**, **semantic development**, **morphological formation/derivation**, or **cognate comparison**. Formation covers within-language derivation and source-reported participial relationships; quote/paraphrase only the mechanism the source actually reports, without guessing affixes. If no category is supported, label the edge **unresolved** with source wording, or omit it from the operative graph. This vocabulary is not a requirement to force-fit every link. Cognates share ancestry; one is not thereby borrowed from the other. “Source also of” is not permission to draw a direct parent-child arrow between those languages. Preserve “probably,” “perhaps,” and alternative explanations at the precise edge where the reference uses them. Distinguish dictionary-reported attestation from direct inspection of historical manuscripts.

Candidate form and evidence remain independent. Selecting an unchanged attested node can yield `attested / verified`. Editing a sourced form yields `adapted / verified` for the supported ingredient only. A new assembly is `invented`, never an attested ancient word. An unsupported asserted link makes overall lineage `unverified`; mark the particular failing edge as well.

### Formation example from inspected expansion evidence

The [preserved operator trial](../../docs/reviews/EXPANSION_OPERATOR_TRIAL.md), S03/S04, reports opened Etymonline [text](https://www.etymonline.com/word/text), noun L11–15, and [texture](https://www.etymonline.com/word/texture), noun L11–15, on 2026-11-10. This is inherited access evidence, not a new opening here. Latin `texere → textus` has a source-reported past-participle relationship: use **morphological formation/derivation**, retain that report, and do not invent a suffix analysis. `texere → textura` is reported stem-based formation, likewise not borrowing. Distinguish `textus` material sense → written-account sense (**semantic development**) from Latin/French/English `textus → texte → text` (**borrowing**, within the reference's reported scope). Preserve separate form/sense nodes and source locators. Deeper `*teks-` remains reconstructed; tentative comparisons do not become donor arrows. If the reference merely says “related to,” keep an unresolved comparison rather than declaring a derivation. The old raw02 notation gap remains historical evidence, not a retroactively repaired execution.

## Procedure

1. Convert the brief into two seed relationships, not just synonyms: “thread through complexity,” “movement without struggle.” Offer contrasting previews with factual claims marked as unverified until opened.
2. Search exact seed + etymology and open the relevant noun/verb entry. Record publisher, URL, section, retrieval date and access result. Follow one useful linked entry; inspect it rather than treating link text as verification.
3. Transcribe a bounded graph. Separate form history from meaning history, since spelling and sense dates can differ. A dated spelling is not automatically evidence for every meaning now associated with it.
4. Audit every arrow. Ask which source wording supports this relationship; whether a comparison has been misread as descent; whether a reconstruction or uncertainty marker disappeared; and whether different grammatical entries were merged. Remove unsupported edges rather than decorating them with confidence scores.
5. Make an opportunity matrix: historical node/transition, positive image, negative implication, modern-reading burden, factual limit. Select two contrasting nodes or transitions; do not generate ten near-identical pseudo-roots from one speculative ancestor.
6. Produce direct forms before adaptations. For each changed candidate, preserve exact retained/deleted/added letters and the additional operator. A private working batch of four to six candidates can include a valid rejected result; fewer are acceptable when evidence is thin.
7. Read each candidate in an ordinary introduction without its origin story. Judge present meaning, ease of explanation, sound ambiguity and fidelity of the optional story. Pause for feedback after meaningful contrast, when chains converge, or after two failed source routes. Offer another seed, historical sense recovery, construction or stopping; do not auto-export.

If access fails, record the failure and attempt one accessible reference or relevant entry section. Search snippets and agent memory remain leads. With no inspected chain, park factual etymology and offer meaning-free `phonetic-invention` with `source IDs=none`, or ask the user to supply a reference passage. Never invent an origin to keep a batch full.

## Complete synthetic trace

This fixture illustrates agent choices, not consumer research. Actual evidence was opened on 2026-11-10. E01's `clue (n.)` and linked clew summary are the consulted surface: the dedicated clew URL failed; no claim of opening that separate entry is made.

T01: “Name a tool that helps small teams navigate complex projects. Warm, practical; no heroic or painful journey story.” Previews: **Clew**, thread becoming guidance; **Trauel**, a movement-history lead; **Clue**, familiar guidance. T02: “Try the thread history; compare one journey option.” B01 thread active; B02 journey comparison authorized.

| Graph row | Evidence-bearing relationship | Naming implication and limit |
|---|---|---|
| E01, A: Old English `cliewen` → Middle English `clewe`, `cleue` → `clue` | E01 reports historical forms and later spelling revision; guidance sense 1590s, broader figurative sense 1620s | a material-to-guidance story; Greek narrative reference does not make the word a Greek borrowing |
| E01, R: `*kleuwin`, `*kliwjo-`, possible `*gleu-` | deeper ancestry is qualified; related Dutch `kluwen` is comparison, not the English word's donor | parked; no certainty upgrade or invented “ancient clarity” gloss |
| E02/E03, A: Old French `travailler` → English `travailen` → `trauel`, `travell` | borrowing and later variant development; explanation of the semantic route remains tentative | effort/journey imagery conflicts with T01; never call it an ancient word for effortless progress |

Dates and qualifications are reference reports. The trace does not independently date manuscripts or establish the first use. Current-source summaries support a bounded graph, not every hypothetical intermediate.

| ID | Candidate / proposed reading | Form / evidence | Exact lineage / current decision |
|---|---|---|---|
| B01-C01 | Clew / KLOO | attested / verified | unchanged E01 historical node; useful thread image, spelling explanation needed |
| B01-C02 | Clue / KLOO | attested / verified | unchanged E01 present node; accessible, may suggest puzzles or detectives |
| B01-C03 | Clew Path / KLOO PATH | invented / verified for Clew; Path supplied | child `intact-word-compounding`: Clew + space + Path, no deletions; added guidance is more explicit |
| B02-C01 | Trauel / proposed TRAV-el | attested / verified | unchanged E02 historical spelling; reading friction and painful-history mismatch |
| B01-C04 | Gleura / proposed GLOOR-uh | adapted / unverified | diagnostic: remove `*` and final hyphen from speculative `*gleu-`, append `ra`; false “ancient clarity” gloss has no support |

C04 is an out-of-operator diagnostic because its claimed genealogy is unsupported. Repair changes the decision: drop the speculative gloss and return to the attested Clew node, producing C03 through a separately recorded construction. C01–C03 and B02-C01 are four conforming outputs; three retained, one rejected for this brief. C04 stays in the audit as a rejected diagnostic, not a fifth successful etymological candidate.

T03: “Save Clew Path, keep Clue for comparison. Park the journey words.” Record exact comment and explicit consent only for B01-C03. State: `received_through=T03`; favorites `[B01-C03]`; B01 REFINE, B02 parked; C02 comparison only; deep reconstructed branch untried/parked. Preserve E01 access success and dedicated-entry failure together. On resume, no implied consent for C02.

Optional combinations: `etymological-archaeology` → `clipping` must retain the selected node and deletion map; `etymological-archaeology` → `metaphor-mining` separates documented historical meaning from the new brand analogy. No transformation is required: Clew unchanged can be the outcome. Follow [session protocol](../../docs/SESSION_PROTOCOL.md) for persistence and explicit-only export; unresolved origin edges remain visible in any requested export.
