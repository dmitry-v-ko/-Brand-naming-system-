# Historical Lexical Archaeology

- id: `historical-lexical-archaeology`
- family: historical source discovery and sense recovery
- status: draft
- implementation: new editorial procedure; independent acceptance pending
- requires: research-required for factual claims
- outputs: variant-search plan, dated sense ledger, candidate comparisons, feedback/state delta
- acceptance evidence: inspected reference entries in [historical evidence](../../docs/research/HISTORICAL_METHODS_EVIDENCE.md); synthetic walkthrough below; no independent acceptance yet

## Operator and decisions

Recover older or regional vocabulary by searching spelling variants and reading dated attestations in context. Select a particular historical sense, then test whether its accompanying implications fit a present brief. The working unit is **form + sense + period/register + attestation**, not an evocative-looking old string.

`lexical-research` selects vocabulary by definitions; this operator adds variant retrieval, chronology and historical sense discrimination. `etymological-archaeology` follows descent and borrowing between forms; this skill can stop with one well-supported historical usage without proposing its origin. Scots material is identified as Scots, not casually described as obsolete English. Another language or regional variety is an optional source, not the defining operation.

Use when an overlooked craft action, atmospheric condition or social practice could offer a concrete image, and when a source story deserves investigation. Avoid when the audience needs instant literal comprehension, when antiquity itself is the only attraction, or when the brief would romanticize a harmful historical practice. A pronunciation requiring explanation can be acceptable for exploration; it is a recorded tradeoff.

Required inputs: offer, desired behavior, excluded implication and tolerance for unfamiliar English-facing spelling. Defaults: one distant world, two concepts and three initial queries. Optional controls: region, date range, contemporary readability, permission to adapt. If delegated, select a provisional world and proceed; historical research does not require repeated permission.

## Reproducible procedure

1. Translate the promise into actions and scenes. For a quiet evening workspace: ending a day, sheltering embers, twilight, closing shutters. Propose contrasting **recovery operations**: old hearth verbs, regional light words, forgotten senses of ordinary words. An unopened preview is an unverified lead, never a discovered meaning.
2. Choose an accessible historical dictionary or archive. Search concept + reference, then headword and listed variants. Record the exact query, source scope and whether it exposes quotations. A modern dictionary can corroborate contemporary use but cannot substitute for the historical evidence requested.
3. Make a variant sheet before producing names: displayed headword; exact alternative spellings; query attempted; successful entry locator; variant relationships explicitly stated or merely suspected. Do not infer a common lemma from resemblance. OCR strings remain uncertain until checked against a reliable transcription or scan.
4. Read the target sense and at least one dated quotation; inspect neighboring senses and entry warnings. Record quotation date as printed, including `c`, `a` or ranges; identify author/work/page or section. A dictionary quotation verifies the dictionary's documented witness, not a first occurrence independently established by this agent.
5. Build a sense ledger with columns: form, dated witness, usable action, adverse implication, contemporary-status evidence, confidence. Keep “not found in this search” separate from “obsolete.” Use the latter only for the exact form/sense a source labels so; an old quotation, missing modern hit or old dictionary publication does not establish extinction.
6. Compare at least two sense families before settling. A private target is four to eight ingredient rows, not a user-facing quota. Generate direct exact forms first; historical variation can supply contrasting candidates without manufacturing spelling. Additional clipping or compounding is a declared child operation.
7. Present three to six options with a short source story and an equally concrete objection. Judge historical fidelity, reading burden, useful image, negative senses and dependence on explanation. Pause when new variants repeat the same decision, two access routes fail, or the user has enough contrast. Offer deeper era research, a new world, another method or a shortlist decision.

Keep queries, rejected senses and unexplored variants in session research notes outside this repository. Follow the [source contract](../../docs/SOURCES_AND_RESEARCH.md) and [session protocol](../../docs/SESSION_PROTOCOL.md). Candidate form is `attested`, `adapted` or `invented`; evidence is independently `verified`, `unverified` or `not applicable`. Capitalization alone does not invent a new lexical spelling. Verification covers the inspected sense, not a name's suitability.

## Retrieval and access boundary

Actual source records H01–H04 are library bibliography IDs, copied into session source IDs when used. Search `site.dsl.ac.uk smuir fire`; open the SND entry, locate I.3.(1), then inspect I.1 and the Smore cross-reference. For a separate light branch search `site.dsl.ac.uk gloming`, open DOST and SND entries. These pages were read on 2026-11-10. Their quotations are dictionary-mediated evidence; the original works were not opened. Source facts support ingredients; the search budget, comparison grid and naming judgments are this library's editorial process.

If a page supplies only a title, snippet or login prompt, retain the query as a lead. After two failed routes, park verified historical claims and offer accessible adjacent vocabulary through `lexical-research`, or an explicitly invented branch. Do not backfill dates or definitions from memory.

## Complete synthetic trace

All turns and preferences here are fixtures. Sources were actually consulted; no audience test occurred.

T01: “Name a quiet evening writing room. Warm and unhurried; avoid anything suggesting suffocation.” Assumed English-facing audience. B01 previews: **Smoor**, a hearth-action lead; **Gloming**, a twilight-form lead; **Gloamin**, a regional-spelling lead. T02: “Explore the hearth idea first, but compare twilight.” This authorizes B01 hearth and sibling B02 light research, without shortlist consent.

| Source / branch | Retained intermediate | Supported implication / exclusion |
|---|---|---|
| H01 / B01 | `smuir; smure; smoor(e); smour`; I.3.(1); 1929 F. M. McNeill, *Sc. Kitchen*, p.57 | banked overnight fire; entry also contains choking senses, so do not claim uncomplicated safety |
| H02 / B01 | `smore; smoar; smoor`; separate cross-reference | adjacent suffocation senses reinforce the brief conflict; spelling cannot remove it |
| H03 / B02 | `Gloming`, variants including `gloaming`; c1420 Wynt. iv.827 | twilight; approximate witness date retained; not evidence of morning brightness |
| H04 / B02 | `Gloamin`, variant `gloaming`; sense 1; 1814 Scott, *Waverley*, iii | evening light; later literary use prevents an unsupported “lost forever” story |

| ID | Candidate / proposed English reading | Form / evidence | Exact lineage and decision |
|---|---|---|---|
| B01-C01 | Smoor / SMOOR | attested / verified | unchanged H01 variant; hearth connection fits, choking implication fails T01 |
| B01-C02 | Smuir / SMOOR, uncertain English decoding | attested / verified | unchanged H01 headword; spelling change does not repair the sense problem |
| B02-C01 | Gloming / GLOH-ming | attested / verified | unchanged H03 headword; historical texture, possible “gloom” association |
| B02-C02 | Gloamin / GLOH-min | attested / verified | unchanged H04 headword; oral warmth, unfamiliar ending |
| B02-C03 | Gloaming / GLOH-ming | attested / verified | unchanged listed H03/H04 variant; clearest complete evening image |

Weak result: C01 is historically valid but unsuitable. Repair changes the selected sense family to twilight; it does not sanitize Smoor as “gentle breath.” All five records conform to the discovery operator; two are rejected for this brief and three retained for discussion. None is a fabricated historical construction.

T03: “Save Gloaming. Park Gloming; no fire names.” State delta: `received_through=T03`; B01 parked/rejected for this brief; B02 active REFINE; favorites `[B02-C03]`; B02-C01 parked; fire exclusion cites T01/T03; unexplored = shutter/closing vocabulary. Save the exact T03 comment and consent in both session files. C02 remains unsaved. No automatic export follows.

Optional continuation: `historical-lexical-archaeology` → `intact-word-compounding` could add supplied “Room” to Gloaming, recording both intact units. `historical-lexical-archaeology` → `clipping` must state deletions and changes form status; a clipped result is not an attested archaic word. Unchanged rare vocabulary remains a complete outcome.
