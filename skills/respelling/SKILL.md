# Respelling

- id: `respelling`
- family: orthographic transformation
- status: draft
- implementation: complete editorial procedure; independent acceptance pending
- requires: research-required for factual claims
- outputs: pronunciation anchor cards, letter-edit grid, reading-risk ledger, feedback/state delta
- acceptance evidence: mechanical self-review only; independent walkthrough pending

## Operator and nearest neighbors

Change how a supplied lexical or invented form is written while targeting the same intended pronunciation. Freeze phonemes, syllable count and stress before editing letters. Record each replacement, deletion, insertion or doubling. If the desired sound changes, route that step to `phonetic-invention`; if a spoken unit is removed, consider `clipping`. A changed spelling alone does not prove a changed sound, but a stated wish for identical sound does not make an implausible reading acceptable.

SO03 in the [evidence note](../../docs/research/SOUND_ORTHOGRAPHY_EVIDENCE.md) supports the broad definition of spelling anew. The narrower pronunciation-preserving contract is editorial. SO04 supplies practitioner context for some silent-letter and doubled-letter mutations. Neither source proves that any spelling will be read correctly or become commercially successful. Cosmetic changes do not establish legal protection, availability or distinctness for clearance purposes; none is assessed here.

## Use, avoid and inputs

Use when the spoken name or source word already suits the brief and the user wants a different written identity, a more transparent sound mapping, or controlled spelling exploration. Avoid when the spoken form itself is disliked, when exact written retrieval is critical and variants add friction, or when a historic/technical spelling must remain intact. Do not use creative spelling to conceal an unresolved meaning claim.

Required: exact anchor spelling, intended pronunciation with stress, audience assumption and what the spelling change should improve. If missing, infer a broad English target and label it provisional before generating; do not assume ambiguous strings have one true reading. Default: one grapheme edit per candidate, no numerals, no punctuation, preserved capitalization except display title case, and no intended syllable change. Optional: maximum edits, fixed segment, preference for conventional mappings and acceptable spelling explanation burden.

## Reproducible procedure

1. Create anchor A1: supplied spelling, target phonemes, cue, syllable/stress map, provenance and any sense actually claimed. An invented anchor needs no invented etymology. For real lexical meanings retrieve the relevant sense rather than relying on resemblance.
2. Mark candidate edit sites as exact letter spans with positions or unambiguous before/after context. Record kept prefix/suffix and replacement. Deletion must identify the removed letters; “shortened” is insufficient.
3. Fill distinct edit families: consonant grapheme substitution, vowel grapheme substitution, and silent/doubled-letter change. Do not force a family when it changes the intended reading. Produce six private alternatives across at least three anchors or two truly different sites in one anchor.
4. Apply the classification rule below. Keep the frozen target and assess whether the spelling plausibly supports it; write a credible competing reading only when one is established editorially. Do not invent alternatives to fill a field. These are predictions until actual received reading feedback; declaring a target alone never establishes conformance.
5. Ordinarily present 2–3 contrasts with a short anchor/edit explanation and concrete reading risk; keep detailed maps internal. Fixed spoken/written introductions may help editorial comparison, but do not claim a listener test. Invite actual reading feedback when useful; no feedback is required to offer provisional proposals.
6. Refine one site while holding pronunciation fixed. If two repairs need pronunciation coaching, restore a conventional grapheme, use an unchanged anchor, or switch methods. The unchanged anchor is a control, not a respelling candidate.

The six-name default is a navigation pause. Never force increasingly strange spellings to fill a quota. Balance edits across families; distinguish visual novelty from readability and preserve actual user feedback rather than an invented score.

## Editorial classification and counting

Apply mechanics first, then plausible reading, then fit. These are separate axes:

- **Provisional conforming proposal, ordinary target mapping:** edit controls pass and the spelling convention plausibly supports the frozen target. Kove from cove (c→k, /koʊv/) is an editorial example; no decoding result is claimed.
- **Provisional conforming proposal, ambiguous:** edit controls pass and the target remains credible, but a specific competing reading is also credible. Melow permits an anchor-like /ˈmɛ.loʊ/ as well as /ˈmi.loʊ/; fit/risk may justify rejection without calling the map invalid. Fase (/feɪz/ versus /feɪs/) belongs here if the target is judged credible. State that judgment and its uncertainty.
- **Likely target-breaking diagnostic:** the ordinary spelling cue strongly points away from the frozen target and a target reading would require unusual coaching. Cove → Covie cues an extra syllable; cove → Cave (o→a, one site) cues /keɪv/, not target /koʊv/. Do not rescue these by simply restating the target. Riple for /ˈrɪ.pəl/ should conservatively be parked as likely target-breaking because the single-consonant + le pattern cues /ˈraɪ.pəl/; unlike Melow, familiar short-vowel doubled-consonant support has been removed in that pattern. This is a revisable editorial judgment, not listener evidence.
- **Control diagnostic:** the edit limit or other declared constraint fails, irrespective of target plausibility; e.g. Beekon changes two sites under a one-site control.
- **Actual received reading:** record exactly who reported what at which received turn. A reported reading can confirm/fail the target for that respondent and change current selection; it never proves all readers decode alike. Preserve earlier provisional judgments rather than rewriting them as tests.

Use unique candidate IDs internally. Counts labeled “conforming” here mean **provisional target-plausible, edit-conforming proposals**, split into retained/rejected for fit or risk, plus separately counted diagnostics. They do not count established decoding successes. If target plausibility is unresolved, park the row outside the conforming total pending a clearer mapping or feedback. Never silently change phonemes to make a row pass.

## Candidate and research contract

Follow the [session protocol](../../docs/SESSION_PROTOCOL.md) and [source contract](../../docs/SOURCES_AND_RESEARCH.md). Every record needs stable branch/candidate ID, spelling, anchor ID/exact source spelling, target sound/stress, exact kept/deleted/added letters, intended benefit, competing reading/risk, form, evidence, and session source IDs or `none`. A changed single-source lexical form is `adapted`; a changed already-invented anchor remains `invented` with both stages retained. Evidence describes lineage, not the certainty of pronunciation.

Supplied ordinary fixture words may use `not applicable` without asserting researched senses. If a name depends on a lexical sense or an attested pronunciation, search exact headword plus dictionary, open the relevant entry, and record publisher/date/locator and supported scope. Bibliography IDs are not session ingredient IDs. Two failed routes mean an unverified claim or a supplied invented anchor, never a fabricated dictionary entry. Real session records stay outside this library. Do not claim a minor edit resolves a conflict or makes a name ownable.

## Complete synthetic worked trace

All source ingredients, judgments and received turns below are fixtures. T01: “For a studio lamp line, retain familiar spoken words but explore new spellings. Use cove, gleam and mellow. Keep ordinary English readings; no numbers.” B01 is delegated respelling; anchors are supplied, no etymology or externally verified sense asserted.

Anchor grid: A1 cove, /koʊv/, one syllable; A2 gleam, /ɡlim/, one syllable; A3 mellow, /ˈmɛ.loʊ/, two syllables with initial stress. Preview consonant substitution **Kove**, vowel substitution **Gleem**, deletion **Melow**. All are `adapted / not applicable`, source IDs `none`.

| ID / spelling | Exact edit map | Frozen target / plausible risk | Assessment |
|---|---|---|---|
| B01-C01 Kove | A1 c→k at position 1; retain ove | /koʊv/; target plausible, but requires learning k spelling | conspicuous initial edit |
| B01-C02 Covie | A1 retain cov, replace final e→ie | target /koʊv/; /ˈkoʊ.vi/ likely | diagnostic: added-syllable risk defeats ordinary-reading brief |
| B01-C03 Gleem | A2 retain gl,m; ea→ee | /ɡlim/; target plausible, but familiar spelling lost | long-vowel alternative |
| B01-C04 Gleame | A2 retain gleam; insert final e | /ɡlim/ plausible; no specific alternative established, extra final e may cause spelling hesitation | silent-ending hypothesis; extra letter without clear benefit |
| B01-C05 Melow | A3 retain me and ow; ll→l | /ˈmɛ.loʊ/; /ˈmi.loʊ/ possible | compact but vowel reading less stable |
| B01-C06 Melloh | A3 retain mell; ow→oh | /ˈmɛ.loʊ/; final /ɒ/ or spelling hesitation possible | explicit vowel cue; appearance may feel mannered |

C01, C03–C06 are provisional target-plausible, edit-conforming proposals with flagged fit/reading risk; C02 is an out-of-operator diagnostic for this brief, not a successful respelling. No dictionary attestation of the altered strings is claimed. A risk is not proof that every reader uses the competing pronunciation.

T02: “Kove reads correctly to me. Melow makes me say mee-low. I like a shorter mellow spelling, but keep the short e.” C05 is the weak case with actual fixture reading failure. Repair its decision: restore ll to cue the anchor's short vowel, then change final ow→o. B01-C07 **Mello**, /ˈmɛ.loʊ/: from A3 retain mell, delete w from final ow. The repair is one anchor deletion, not a hidden sound change; compared with C05, restore l and remove w. Drawback: still departs from the familiar word spelling. Classification adapted/not applicable, source none.

T03: “Save Kove and Mello. Note on Mello: ‘short e matters’. Leave Gleem for later.” Final state: received_through=T03; favorites=[B01-C01,B01-C07]; C07 exact comment from T03; active=B01/REFINE/A3; parked=A2; rejected=C05 reading and C02 diagnostic. Seven records = six provisional target/edit-conforming proposals (C05 rejected after received fixture reading failure) plus one diagnostic; shortlisted two. This is not six confirmed decoding successes; only T02 supplies a respondent reading for C01/C05, and it is synthetic. Reconcile both session records; no save was inferred from “like” at T02. Resume with /ˈmɛ.loʊ/ and retained ll, preserve other variants in history. Next options: another final-vowel mapping, revisit Gleem, change spoken form in a child, or explicit export.

## Ordered combinations

`fragment-blending` → `respelling` freezes the blend's sound and preserves its cut map before letter edits. `onomatopoeic-naming` → `respelling` preserves the sound-event mapping. `respelling` → `phonetic-invention` begins a child when the user deliberately changes a sound; retain the rejected reading as feedback, not a retroactive pronunciation target. A changed pronunciation must never silently pass as successful respelling.
