# Phonetic Invention

- id: `phonetic-invention`
- family: sound construction
- status: draft
- implementation: complete editorial procedure; independent acceptance pending
- requires: research-optional
- outputs: candidate ledger, method artifact, feedback/state delta

## Mechanism and boundary

Construct spoken forms from onset, nucleus and coda constraints, then choose spelling. There are no semantic roots. Unlike `syllable-recombination`, components inside each syllable are generated; unlike sound-symbolic claims, no universal personality is assigned to letters.

## Use, avoid and inputs

Use for meaning-free names with deliberate rhythm and an audience pronunciation target. Avoid when the brand requires an origin story based on real vocabulary, or the user needs validated consumer impressions rather than exploratory sound hypotheses.

Required: audience pronunciation assumptions, desired syllable count and exclusions. Default: broad English-compatible two syllables, initial stress, no three-consonant clusters. Optional: a preferred spoken candidate, spelling simplicity or one sound contrast to test. IPA may be supplemented by plain cues; pronunciations are proposals.

## Procedure

1. Set C1/V1/C2/V2 constraints, optional final coda, stress and forbidden sequences. Write permitted phonemes before letters.
2. Build two contrasting palettes: e.g. nasal/liquid onsets versus stop-led onsets. Change one feature in matched examples where possible; do not change vowels, stress and length simultaneously then attribute the effect to one sound.
3. Fill a small component grid manually, creating eight spoken forms by default. For the conductor’s [independent sound control](../../docs/SESSION_PROTOCOL.md#independent-sound-control), use its smaller declared budget (at most two controls) for both spoken generation and spellings; do not generate a hidden larger pool. Reject violations, accidental clusters and ambiguous syllable counts.
4. Spell up to six survivors, or the smaller remaining conductor budget, using a consistent sound-to-letter mapping. Compare predicted readings; keep spelling variants attached to the same spoken-form record until selected.
5. Ask for actual user impressions in identical product introductions. Retain the preferred contrast and generate four near-neighbors, changing one component at a time.

## Selection and recovery

Check compliance before aesthetic ranking. Compare pronounceability proposals, family diversity and fit to actual feedback. An association such as “lighter” is a hypothesis, not a test result. If spelling is unstable, choose a clearer mapping or ask one pronunciation preference. If the palette is bland, alter a single dimension (coda or stress), not random extra letters.

## Research and evidence

No lexical research is required: form invented, evidence not applicable, sources none. Source S11 is not a table of universal vowel meanings. If a candidate resembles a real word, record the observation as an unverified lead and research only the specific lexical claim. Do not imply an exhaustive language or conflict screen.

Source basis: S19–S20 support sound-direction practice, not a disclosed proprietary algorithm; S11 supports context-dependent sound comparisons only. See [research bibliography](../../docs/research/BRANDING_METHODS_RESEARCH.md). Steps and worked fixtures below are editorial adaptations, not attributed algorithms or efficacy evidence.

## Candidate record and interaction

Use the [session protocol](../../docs/SESSION_PROTOCOL.md) and [source contract](../../docs/SOURCES_AND_RESEARCH.md). Every internal candidate record has stable branch/candidate IDs; English spelling; proposed pronunciation/stress where uncertain; exact lineage; separate `form` and `evidence`; source IDs or `none`; useful association and main drawback. Ordinary responses show 2–3 contrasts with a brief reason, relevant reading/risk and terse evidence status; IDs and detailed tables stay in the exploration log or session-owned research notes unless requested. Batch/grid sizes are private defaults, not user-facing quotas. Do not put real sessions in this library.

For a sufficiently specified brief, proceed with two or three useful contrasts and a recommendation; no separate preview gate is required. Expand menus when requested or real uncertainty changes direction. Record inferred choices as agent judgments, never as user delegation. Ask which property to preserve, not merely which name is “best.” After feedback record the actual words, changed constraints, rejected/parked paths and next options. Praise does not save a name. Add only explicit selections; repeated selection updates the same candidate. A six-name batch is a pause for navigation, never an automatic export.

## Ordered combinations

`phonetic-invention` → `syllable-recombination`: freeze accepted syllables as new units for future family generation. `fragment-blending` → `phonetic-invention`: repair an awkward blend sound with retained source map and an explicit added/deleted phoneme. `phonetic-invention` → `intact-word-compounding`: attach a familiar descriptor as another operation.

## Complete synthetic worked trace

All brand briefs, candidate judgments and user turns below are fixtures, not consumer findings. Source facts are separately identified. IDs are local to this trace.

Brief: precise, welcoming inventory tool; no invented etymology. B01 previews: fluid **Nelo**, stop-led **Telo**, closed **Telok**. User fixture: “Telo feels more precise; avoid a harsh last stop.”

Constraint artifact: two syllables; /ˈCɛ.Coʊ/ where the second nucleus is /oʊ/; first onset ∈ {/n/,/t/}, second onset ∈ {/l/,/m/}; optional final /k/ only in the closed contrast. Stress first. Map /ɛ/→e, /oʊ/→o. There is no claim that n or t inherently means anything.

| ID | Assembly | Output / proposed sound | Assessment |
|---|---|---|---|
| B01-C01 | n + ɛ; l + oʊ | Nelo /ˈnɛ.loʊ/ | fluid baseline |
| B01-C02 | t + ɛ; l + oʊ | Telo /ˈtɛ.loʊ/ | matched initial-onset contrast |
| B01-C03 | n + ɛ; m + oʊ | Nemo /ˈnɛ.moʊ/ | recognizable fictional resemblance; park, no clearance inference |
| B01-C04 | t + ɛ; m + oʊ | Temo /ˈtɛ.moʊ/ | useful second-onset contrast |
| B01-C05 | t + ɛ; l + oʊ + k | Telok /ˈtɛ.loʊk/ | final stop rejected by user |
| B01-C06 | t + ɛ; l + oʊ + sk | Telosk | reject before presentation: /sk/ coda not permitted |

Repair C06 by removing unauthorized /s/ gives Telok (C05), still disfavored. Remove optional /k/ gives Telo (C02), favored. Refine C02 by changing only second onset /l/→/m/ gives Temo (C04), rather than generating an unrelated name. All invented / not applicable, source none. User fixture: “Save Telo; Temo is less clear to me.” State: favorites=[B01-C02]; constraint=no final stop; rejection=C04 is an actual fixture response, not universal clarity evidence; active B01 REFINE; next=single-vowel contrasts or semantic method. No automatic export.
