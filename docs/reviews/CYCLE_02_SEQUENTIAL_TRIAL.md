# Cycle 02: controller-led sequential trial and isolated resume

Date: 2026-11-10. This records actual agent execution with synthetic user messages, not consumer research or commercial effectiveness. It follows the [second critique](CYCLE_02_CRITIQUE.md) and [targeted improvements](CYCLE_02_IMPROVEMENTS.md). Earlier failed-run reports and checkpoints were preserved. No quality score is assigned here.

## Input isolation and execution

The controller created a new executor with no inherited conversation. It received library instructions and only T01, then stopped. The controller inspected its actual files before supplying T02, and again before supplying T03. Future messages, expected comments, and later selections were not provided to the executor or a scripted helper. A different fresh-context agent received only library instructions and frozen copies of the two T03 session records; it first assessed state without writing. Only after that assessment did the controller supply the new T04 message. The original executor never received T04.

All session artifacts are outside the checkout. The English summary below is portable; machine-specific paths are supplementary audit locations, not runtime dependencies:

- `/workspace/naming-review-runs/cycle-02-sequential/`: exact original-language messages and responses, current files, source evidence, and immutable checkpoints T01-W01, T02-W02, T02-W03, T03-W04.
- `/workspace/naming-review-runs/cycle-02-controller-audit.json`: controller prefix checks and SHA-256 baselines for the tracked checkpoints, frozen inputs, and final artifacts.
- `/workspace/naming-review-runs/cycle-02-resume-input/`: the two frozen T03 files and `RESUME_ASSESSMENT.md`, which lists every input actually read.
- `/workspace/naming-review-runs/cycle-02-resumed/`: resumed records, T04 response/transcript, final export, and T04-W05 checkpoint.

## Received messages and observed results

| Turn | User request, translated | Actual result and prefix checks |
|---|---|---|
| T01 | Name short shared lunchtime walks for colleagues: calm conversation, no sports, tourism, or productivity promise. Offer three approaches; save nothing. | Whole-word previews Noon Walk / Easy Company; metaphor previews Interlude / Porch; sound previews Mavo / Navo. Six distinct preview IDs, no selected method, no favorites. Agent recommendation remains separate from user preference. Only T01 facts occur in the snapshot. |
| T02 | Save exactly Noon Walk with a specific Russian comment; Easy Company is interesting but unsaved. Delegate an unexpected lexical world and request two reference terms, with helpful and adverse implications. Save no new names. | One selected row B01-C01 with exact comment. Executor chooses musical notation. Caesura and Fermata remain unverified after two reference routes return HTTP 403. Conditional interpretations are not presented as inspected definitions. No future choices or comments occur. |
| T03 | Save Noon Walk again with a new exact comment while preserving the old one. Caesura is interesting but unsaved. Find an accessible Fermata reference, then combine the verified term with intact Walk; show two options and save neither. | Same selected row retains both exact comments. Britannica's Fermata entry is actually retrieved and read. B05 records lexical-research → intact-word-compounding, producing Fermata Walk and Walk Fermata. Both unsaved. B04 remains parked with source history; other paths are retained. Received prefix ends at T03. |
| Resume pause | No naming-user message. A separate reader receives only instructions and the two frozen records. | Reader recovers B05 active, four parked branches, one exact favorite with both comments, remaining unverified leads, source history, and unknown preferences. It distinguishes reported earlier verification from its own research. It neither saves names nor assumes export. |
| T04 | Save exactly Fermata Walk with a specific Russian comment. Caesura remains interesting but unsaved. Export only saved names and stop. | Fresh reader continues in a separate output directory. Exactly B01-C01 and B05-C01 are selected and exported. All three exact comments survive. The two frozen inputs remain unchanged. Stop follows actual user instruction. |

The original-language comments remain in external files. Their meanings are respectively “calm and unpretentious,” “simple, keep it in the final,” and “unusual, but the meaning needs explaining.” Translations here never replace original comments in state or export.

## Source and transformation evidence

Initial Merriam-Webster entries and Dolmetsch glossary routes for caesura/fermata returned HTTP 403; no definitions were claimed from those failures. At T03 the executor tried alternate access, actually retrieved [Britannica: Fermata](https://www.britannica.com/art/fermata) through Python urllib with a Mozilla User-Agent, and inspected the “List of Musical Symbols / Fermata” block. The record preserves raw evidence and distinguishes this successful retrieval from a failed connector open. A discovery search is not treated as a lexical definition.

The inspected sense supports prolonging a note or rest beyond written duration at the player/conductor's discretion. The proposed analogy to an unhurried break is editorial interpretation; the drawback is tension with a short break. Caesura remains unverified. No pronunciation or market preference is asserted as measured.

- Noon Walk: intact noon + walk; invented compound, lexical evidence not applicable.
- Fermata: unchanged term, recorded attested/verified for the inspected sense.
- Fermata Walk and Walk Fermata: exact retrieved ingredient followed by intact-word ordering; invented compounds, verified sourced lineage only. Walk is user-supplied vocabulary. Neither compound becomes an attested expression because its ingredient is verified.

The received pool ends with ten unique conforming candidate IDs, zero diagnostics, zero rejected candidates, and two selected favorites as a subset. No-save is not rejection. Parked is not rejected. The later save does not retroactively alter the T03 snapshot.

## Checks performed and limitations

The controller read both records after each stage, checked the received-through boundary, exact selection/comment history, and prior tracked checkpoint hashes. It froze and hashed the two T03 inputs before launching the fresh reader. After T04 it checked unchanged inputs and earlier tracked snapshots, equality of current records to T04-W05, exactly two final selected IDs, and all three exact comments. These checks passed. An initial controller assertion assumed a table-format export; the actual export used candidate sections. The controller corrected its parser to inspect those headings and passed without changing the export.

The new trial is **clean with respect to future-feedback leakage and shortlist consent**, not flawless in every detail. T02-W02 had a stale audit sentence and malformed Markdown rows; T02-W03 openly corrected them while preserving W02. Some appended earlier audit/reconciliation paragraphs remain stale beneath an unambiguous current received-through header and later update. The fresh reader recognized them as historical. This is a compactness/usability limitation, not invented user evidence; do not erase it from the assessment.

This run independently exercises menu previews, bounded lexical retrieval/fallback, intact compounding, branching, exact consent, repeated selection, real isolated resume, and explicit-only export. It does not independently execute every step of all twelve procedures. Earlier Cycle 01 work supplies additional construction/sound execution evidence while retaining its temporal failure. Neither run establishes consumer appeal, universal pronunciation, native acceptance, or legal/commercial availability. All twelve skills remain draft pending the independent acceptance decision; the trial itself does not promote them.
