# Clipping

- id: `clipping`
- family: structural construction
- status: draft
- implementation: complete editorial procedure; independent acceptance pending
- requires: research-optional
- outputs: candidate ledger, method artifact, feedback/state delta

## Mechanism and boundary

Remove an uninterrupted beginning or ending from one source word; preserve the remaining contiguous substring. This core procedure uses fore- and back-clipping, not silent letter replacement or added endings. Unlike `fragment-blending`, there is only one source; unlike `suffix-attachment`, nothing is added.

## Use, avoid and inputs

Use when a long evocative term has a strong surviving sound/image. Avoid when a full technical definition must remain apparent or the only pronounceable result requires silently inserting new letters.

Required: 2–4 source words with meanings and desired recognition level. Default: keep 4–7 letters at a plausible spoken boundary; compare a recognizable and an abstract cut. Optional: keep beginning versus ending, syllable cap.

## Procedure

1. Write each source, proposed syllabification and meaning status. Never treat a spelling chunk as a historical morpheme without evidence.
2. Mark two back-clips and one fore-clip per source. Record removed text exactly, including pronunciation changes introduced by the new ending.
3. Place retained forms beside originals. Eliminate cuts that leave only a generic ending or a severe decoding problem.
4. Compare recognition-led, balanced and abstract outputs, at most two per group. Ask how much origin needs to survive.
5. If the user wants polish, change a cut boundary first; adding a letter moves to a declared hybrid branch.

## Selection and recovery

Prefer a useful surviving cue and stable proposed stress. Recovery from an awkward consonant ending: retain one more vowel-bearing segment, if available; otherwise use a different source. Recovery from overfamiliar fragments: keep a longer cut or reverse clipping direction. Stop after two source words fail rather than fabricating a root story.

## Research and evidence

Use `lexical-research` for rare words before cutting. Preserve the exact dictionary sense and note the clipped output is adapted, not attested. Without source access, mark the original unverified or use brief-supplied vocabulary and make no etymological claim.

Source basis: S01/S05; truncation of existing words. See [research bibliography](../../docs/research/BRANDING_METHODS_RESEARCH.md). Steps and worked fixtures below are editorial adaptations, not attributed algorithms or efficacy evidence.

## Candidate record and interaction

Use the [session protocol](../../docs/SESSION_PROTOCOL.md) and [source contract](../../docs/SOURCES_AND_RESEARCH.md). Every displayed batch has stable branch/candidate IDs; English spelling; proposed pronunciation/stress where uncertain; exact lineage; separate `form` and `evidence`; source IDs or `none`; useful association and main drawback. Keep intermediate tables in the exploration log or session-owned research notes. Do not put real sessions in this library.

Show two or three contrasting previews before expanding, unless the user already delegated or specified the operation. Ask which property to preserve, not merely which name is “best.” After feedback record the actual words, changed constraints, rejected/parked paths and next options. Praise does not save a name. Add only explicit selections; repeated selection updates the same candidate. A six-name batch is a pause for navigation, never an automatic export.

## Ordered combinations

`lexical-research` → `clipping` gives a traced short form. `clipping` → `suffix-attachment` declares the new material separately. `clipping` → `intact-word-compounding` treats the clip as a supplied ingredient and preserves its earlier lineage.

## Complete synthetic worked trace

All brand briefs, candidate judgments and user turns below are fixtures, not consumer findings. Source facts are separately identified. IDs are local to this trace.

Brief: a spacious idea journal; abstract but gently connected to learning. B01 previews: **Observ**, **Conserv**, **Orama** from supplied observatory / conservatory / panorama. User fixture: “Spacious, less institutional.” Supplied vocabulary, no dictionary verification claimed.

| ID | Original | Removed | Retained / pronunciation proposal | Decision |
|---|---|---|---|---|
| B01-C01 | observatory | atory (back) | Observ, ob-ZERV | abrupt, verb-like |
| B01-C02 | conservatory | atory (back) | Conserv, kən-ZERV | conservation/institution cue dominates |
| B01-C03 | panorama | pan (fore) | Orama, oh-RAH-muh | spacious cadence, source recognition reduced |
| B01-C04 | panorama | rama (back) | Pano, PAN-oh | compact, broader pronunciation ambiguity |
| B01-C05 | observatory | ory (back) | Observat, ob-ZER-vat | awkward final /t/, reject |

Repair C05 by moving the cut earlier, not adding a vowel: **Observa** (C06) = observa[tory] → Observa, ob-ZER-vuh. The removed segment is tory; the t does not survive. Every cut must be checked against the full spelling. C06 sounds institutional relative to C03. All outputs adapted / not applicable; source none.

User fixture: “Save Orama; park observatory.” State: favorites=[B01-C03 Orama]; B01 REFINE; rejected=institutional source family; untried=other spacious-image source words; source word panorama and exact removal pan retained. No claim that Orama is absent from existing vocabulary or commerce.
