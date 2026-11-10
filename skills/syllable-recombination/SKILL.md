# Syllable Recombination

- id: `syllable-recombination`
- family: sound construction
- status: draft
- implementation: complete editorial procedure; independent acceptance pending
- requires: research-optional
- outputs: candidate ledger, method artifact, feedback/state delta

## Mechanism and boundary

Reorder prebuilt spoken syllable units without preserving source-word meaning. Keep each unit's phonemes intact. Unlike `fragment-blending`, chunks carry no claimed lexical lineage; unlike `phonetic-invention`, onset/nucleus/coda are not separately chosen during this operation.

## Use, avoid and inputs

Use for an abstract brand with a repeatable sound family or several future product siblings. Avoid when the brief needs an immediately intelligible meaning or source chunks are secretly fragments of recognizable brands.

Required: tone and syllable count; infer two syllables and first-syllable stress. Default bank: four CV syllables and two CVC syllables with explicit pronunciations. Optional: allowed positions, consonant restrictions and fixed anchor syllable. Never infer etymologies from syllable spellings.

## Procedure

1. Build six syllable cards: label, phonemes, proposed spelling and permitted position. Use one pronunciation per card in a batch.
2. Form a start/end grid; reject self-pairs unless deliberate repetition is desired. Keep units intact. Produce eight combinations spanning at least three starting units.
3. Set stress explicitly. Mark ambiguous spelling and boundaries that accidentally form consonant clusters.
4. Compare a flowing CV+CV palette with a more closed CV+CVC palette. Attribute impressions to editorial hypotheses until the user responds.
5. Return three to six survivors, each with ordered unit IDs. To refine, hold the preferred first unit and swap only the second, or reverse the same pair.

## Selection and recovery

Select for intact units, distinct rhythms and plausible English pronunciation. Assess spoken assembly and written reading separately: intact syllable cards establish a valid construction, not that readers will recover its syllables or stress. If ordinary spelling cues strongly favor a different syllable count, park or reject that spelling for presentation even when the assembly conforms. A credible alternative reading may remain an explicit uncertainty; do not invent a competing reading or claim listener evidence. Recover by swapping a whole unit for a clearer boundary, or declare a separate respelling step while preserving the sound target. Keep the original construction and rejection reason in the ledger. Repeated vowels may create a third syllable; mark that risk rather than assert two. Repair an awkward boundary by swapping a unit, not silently mutating phonemes. If all forms sound interchangeable, add a CVC unit or change stress in a separate comparison.

## Research and evidence

No dictionary needed for invented units: evidence not applicable, no claimed meanings. If the user supplies a real word as a chunk, record it as supplied and separate its meaning claim. A remembered foreign resemblance is an unverified lead; do not retrofit an etymology. Optional research can check a lexical association on request, without clearance claims.

Source basis: S17 only supports constructed forms; narrow procedure is an explicitly experimental editorial technique. See [research bibliography](../../docs/research/BRANDING_METHODS_RESEARCH.md). Steps and worked fixtures below are editorial adaptations, not attributed algorithms or efficacy evidence.

## Candidate record and interaction

Use the [session protocol](../../docs/SESSION_PROTOCOL.md) and [source contract](../../docs/SOURCES_AND_RESEARCH.md). Every internal candidate record has stable branch/candidate IDs; English spelling; proposed pronunciation/stress where uncertain; exact lineage; separate `form` and `evidence`; source IDs or `none`; useful association and main drawback. Ordinary responses show 2–3 contrasts with a brief reason, relevant reading/risk and terse evidence status; IDs and detailed tables stay in the exploration log or session-owned research notes unless requested. Batch/grid sizes are private defaults, not user-facing quotas. Do not put real sessions in this library.

For a sufficiently specified brief, proceed with two or three useful contrasts and a recommendation; no separate preview gate is required. Expand menus when requested or real uncertainty changes direction. Record inferred choices as agent judgments, never as user delegation. Ask which property to preserve, not merely which name is “best.” After feedback record the actual words, changed constraints, rejected/parked paths and next options. Praise does not save a name. Add only explicit selections; repeated selection updates the same candidate. A six-name batch is a pause for navigation, never an automatic export.

## Ordered combinations

`syllable-recombination` → `phonetic-invention` when a syllable's internal sound is deliberately changed. `prefix-attachment` requires an actual stem and explicit new prefix, not arbitrary relabeling of the first syllable. `syllable-recombination` → `intact-word-compounding` can pair a coined form with a familiar noun, preserving both stages.

## Complete synthetic worked trace

All brand briefs, candidate judgments and user turns below are fixtures, not consumer findings. Source facts are separately identified. IDs are local to this trace.

Brief: approachable studio scheduling; abstract, compact, adult. B01 previews: flowing **Nalo**, closed **Nalek**, clipped **Vemlo**. User fixture: “Nalo too soft; keep a firmer ending.” All invented / not applicable; source none.

| Unit | Sound | Spelling | Position |
|---|---|---|---|
| U1 | /nɑ/ | na | start |
| U2 | /loʊ/ | lo | either |
| U3 | /vi/ | vee | start |
| U4 | /su/ | soo | start |
| U5 | /lɛk/ | lek | end |
| U6 | /vɛm/ | vem | either |

Grid samples: U1+U2 **Nalo** /ˈnɑ.loʊ/; U1+U5 **Nalek** /ˈnɑ.lɛk/; U3+U5 **Veelek** /ˈvi.lɛk/; U4+U5 **Soolek** /ˈsu.lɛk/; U6+U2 **Vemlo** /ˈvɛm.loʊ/; U2+U6 **Lovem** /ˈloʊ.vɛm/. B01-C01 Nalo, C02 Nalek, C03 Veelek, C04 Soolek, C05 Vemlo, C06 Lovem. Vemlo creates /ml/ across the boundary and Lovem risks “love 'em”; both rejected for this adult tone, not because they violate the unit rule.

Repair C05 by holding its second unit and replacing first U6 with U1: **Nalo**, existing C01, is valid but conflicts with the user's firmer-ending preference. Better use U1+U5 **Nalek**, existing C02. Do not invent a seventh sound to rescue the grid. User fixture: “Save Nalek, and show other first syllables with lek later.” State: favorites=[B01-C02]; active B01 REFINE; constraint=end U5; rejected=soft endings and /ml/; next_options=new start units, phonetic internal contrast, switch method.
