# Corpus Contrast

- id: `corpus-contrast`
- family: source discovery and selection
- status: draft
- implementation: editorial procedure; independent acceptance pending
- requires: research-required for factual corpus and lexical claims
- outputs: corpus manifest, term contrast table, concordance/sense ledger, candidate batch, state delta
- acceptance evidence: [actual bounded comparison](../../docs/research/CORPUS_CONTRAST_EVIDENCE.md); self-check only, no independent acceptance or effectiveness evidence

## Operator and boundary

Discover naming ingredients by comparing vocabulary in a bounded domain corpus A with a declared reference corpus B. Relative concentration identifies words worth reading in context; it does not select a brand automatically. The required intermediate operation is a comparison with documented sampling, units, denominators and actual counts, followed by contextual interpretation.

`lexical-research` starts from definitions and follows entry relationships. The discovery-order version starts from a document contrast and only then consults definitions to test discovered ingredients. An explicitly labeled dictionary-informed exploratory version may compare terms already considered or checked; it still requires actual documented counts, but cannot claim contrast-first discovery or a blind pre-dictionary inventory. A glossary may verify a result; opening three favorite glossary entries and calling them a corpus does not implement this operator. Source universes are parameters, not additional methods. Direct use of an observed word, including a verified rare word, is legitimate; spelling adaptation is optional and a separately recorded operation.

## Use, avoid and controls

Use when a source world has a distinctive working vocabulary, when a naming team keeps recycling familiar associations, or when the user wants language grounded in actual texts. Avoid statistical claims with inaccessible corpora, a reference collection of unknown composition, duplicated marketing copy, or unmatched periods/languages/genres whose differences overwhelm the question.

Required: brief, desired property, exclusions, proposed A and B roles, accessible documents or supplied text. Infer English and contemporary public educational prose unless the brief says otherwise. Ask only when the missing choice changes creative direction. Optional controls include era, regional English, document length, minimum document spread, and whether technical opacity is welcome. Default pilot: two documents per set, bounded paragraphs, 10–15 inspected content-word rows, three contrasting candidate options. These are private workload defaults, never user obligations.

B may be general English only if its actual coverage supports that description. A related specialist corpus is valid, but label the question narrowly: “coastal motion versus inland/mixed-water habitats,” not “technical versus ordinary English.” Historical absence never establishes that a word is obsolete.

## Executable procedure

1. Translate the brief into properties and propose contrasting comparison designs. A preview must state both collections and a candidate-flavored hypothesis. Until counted, label vocabulary as leads. For a full universe menu offer 6–12 possibilities, then develop the selected or delegated branch without another permission gate.
2. Declare the version: **contrast-first discovery** or **dictionary-informed exploratory comparison**. Keep a short truthful event sequence (sample/inventory saved → count/contrast → promoted-sense checks for contrast-first). No hashes, preregistration or checkpoint ceremony is required. For exploratory work, record prior dictionary access/term consideration in its actual order and limit the discovery claim. Record the sampling rule before counting. List exact URLs/titles, access dates, inclusion boundaries, exclusions and intended comparison. If documents were chosen after browsing for availability, say so. Do not retrospectively claim random selection or preregistration. Prefer comparable publisher, genre, period and document function; disclose residual mismatch.
3. Freeze a corpus manifest. Remove navigation, captions and repeated transcripts consistently. Fix the unit: here lowercase runs of English letters; punctuation, hyphens and digits separate tokens; no stemming or lemmatization. Count every token for denominators, including function words. Keep singular/plural separate unless an explicitly listed family map is applied identically to both sets.
4. Read A and enumerate potentially name-bearing content words before dictionary lookup. Count each inspected term in every document of A and B, including zeros. Preserve discarded rows and relevant concordance locations. A manual tally with numbered tokens and a second pass is sufficient; a spreadsheet or temporary script is optional. No paid corpus, API or Python dependency is required.
5. Calculate `rate = 1000 × term count / corpus tokens`; compare `delta = rate(A) − rate(B)`. Use no smoothing for this subtraction. Zero means absent from this sample, never absent from English. Do not replace zero by an invented count or interpret a singleton as robust enrichment. Also report document spread: a large difference driven by one document is a localized lead.
6. Read the term's actual contexts. Separate topic labels, portable images, processes and adverse implications. Verify every asserted lexical sense in an opened source and keep exact entry locators. Concentration does not establish meaning, unusualness, positive sentiment or audience recognition. Re-rank by the brief and disclose editorial judgment.
7. Ordinarily present 2–3 contrasting candidates with brief source stories, reading proposals where useful and a concrete drawback. Keep exact source terms, counts/locators, supported senses and selection reasoning in internal records; show the full contrast on request. Include a rejected result only when useful. Preserve `form` separately from `evidence`. Pause for navigation when the useful batch is complete; two inaccessible source routes or repeated contexts are reasons to stop that research branch, not to export automatically.

## Failure, selection and recovery

Keep an attractive word when its supported sense fits, even if its delta is modest; explain that decision. Conversely, reject a high-scoring word that contradicts the promise. Do not enlarge A selectively until a favorite appears strong. A second comparison needs a new manifest/version and its own denominator. For a larger claim, expand both sets with the same declared sampling rule and inspect document dispersion; never silently pool incompatible samples.

If counts cannot be reproduced, switch explicitly to **qualitative manual comparison**, not statistical corpus frequency. List the opened passages, observed terms and contextual contrasts; provide no rates, invented ranks or artificial numbers. If neither corpus is accessible, retain the source plan as unverified, offer accessible adjacent material or switch methods. Dictionary verification alone cannot repair missing corpus evidence.

## Complete synthetic trace

All brief decisions, judgments and turns here are fixtures. Actual observations are in the linked evidence report; no consumer study is implied.

T01: “Name a calm planning workspace for independent designers. Give me real English words, without danger or hustle.” Provisional properties: visibility, room to think, gentle progress.

B01 previews: coastal-motion A versus watershed/estuary B, **Crest / Horizon / Surface** as unverified leads; a second possible comparison, weaving instructions versus general craft prose, **Selvedge / Shuttle**, unverified leads; a third, optics explanations versus mechanics prose, **Aperture / Focus**, unverified leads. The latter two are unexecuted designs, not findings. T02: “Choose the coastal comparison and show different kinds of calm.” Record delegated choice; proceed to DEEP_EXPLORE.

B01 manifest v1 uses NOAA D1–D2 against R1–R2, totaling 180 versus 95 tokens. The evidence table retains 13 inspected rows. `waves` has delta +44.44 per thousand; `surface` +16.67; `crest`, `horizon`, and `friction` each +5.56; `basin` −4.97. Every positive row occurs in only one of two A documents; none establishes concentration across the whole source world. These are bounded topic contrasts, not a rarity ranking.

| ID / candidate | Exact lineage / sources | Form / evidence | Editorial direction and limitation |
|---|---|---|---|
| B01-C01 **Crest**, KREST | `crest` in D1 → initial capital only; S05 sense 1 | attested / verified | A distinct high point; may feel achievement-driven rather than calm. |
| B01-C02 **Horizon**, huh-RYE-zun | `horizon` in D1 → initial capital only; S06 sense 1 | attested / verified | Spatial perspective; does not literally mean future planning. |
| B01-C03 **Surface**, SUR-fis | `surface` in D1 → initial capital only; S07 sense 1 | attested / verified | A visible working plane; can suggest superficiality. |
| B01-C04 **Friction**, FRIK-shun | `friction` in D1 → initial capital only; S01 context | attested / verified for occurrence/context only | Mechanically valid discovery but rejected: source context concerns wave generation; “effortless” is unsupported. |

Weak decision: promoting C04 merely because B contains zero occurrences would violate the brief. Recovery: retain its row as a rejected conforming result, then elevate C03's visible-plane direction after checking its sense. The corpus stays unchanged. No forced suffix is needed to disguise the problem.

T03: “Save Horizon. Crest feels too competitive. Keep Surface for discussion.” Result: favorites=[B01-C02], consent/comment linked to T03; C01 rejected for this brief, C03 pending, C04 rejected. Praise/pending discussion is not shortlist consent. Four unique conforming records = two retained + two rejected; zero out-of-operator diagnostics; one shortlisted subset.

B01 remains REFINE; weaving and optics designs are parked/unexecuted opportunities. Offer deeper coastal sampling, another universe, another method, or an explicitly ordered combination such as `corpus-contrast` → `clipping` with a retained/deleted letter map. Do not invent a clipped favorite before a received instruction. Resume from these exact IDs and actual feedback; export only on request.

## State and provenance

Follow [session protocol](../../docs/SESSION_PROTOCOL.md) and [source contract](../../docs/SOURCES_AND_RESEARCH.md). Copy bibliography IDs into session-scoped sources explicitly; S01 here means the worked fixture, not the research bibliography. Store manifest, counts, source status, sense locators, transformation maps, actual turn IDs and received-through boundary in session-owned notes outside this repository. Reconcile log and shortlist after T03; if a write fails, say which record remains incomplete. With no write tools, provide equivalent in-chat state and say no file was saved. Procedures, ranking and branding associations are editorial adaptations; sources verify their stated observations only. No availability, legal clearance or efficacy claim follows.
