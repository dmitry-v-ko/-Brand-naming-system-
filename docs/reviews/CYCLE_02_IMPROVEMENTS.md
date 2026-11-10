# Cycle 02 improvements

Date: 2026-11-10. Response to the [Cycle 02 critique](CYCLE_02_CRITIQUE.md), under the unchanged [review protocol](REVIEW_PROTOCOL.md). This document records instruction changes and their checks, not a new score or successful trial.

## Cause and change

The observed failure was temporal evidence leakage in the walkthrough's persistence helper: future synthetic decisions entered earlier records, and a translated comment replaced its original wording. Core operator rewrites or more methods would not address that cause. The [session contract](../SESSION_PROTOCOL.md) now makes the received-evidence boundary explicit; both [exploration](../../templates/EXPLORATION_LOG.md) and [shortlist](../../templates/SHORTLIST.md) templates carry received-through and originating-turn references.

The contract separates original-language exact quotes from summaries/translations, preserves repeated-selection history, and requires reconciliation against only the received transcript prefix. Sequential executors and writing helpers must not access future fixture turns or expected answers. Trial controllers must arrange and document that boundary; these instructions alone cannot prove isolation.

Mutable working records advance forward, while audited checkpoints remain immutable. Repairs create later snapshots with correction events, preserving the failure and separating historical consistency from final reconciliation. A fresh-context resume receives only repository instructions and two session files; another read by an informed executor is labeled same-agent read-back. Candidate counts use unique IDs and distinguish conforming retained/rejected candidates from out-of-operator diagnostics, with favorites a separate subset.

These are internal memory/audit rules. Naming users still make lightweight creative choices; the changes add no approval gates or required user forms. The twelve draft procedures, inventory count and maturity remain unchanged.

## Checks and preserved evidence

Checked the edited protocol and templates together for consistent turn references, exact-comment treatment, repeated selections, count arithmetic and resume boundaries. Checked local Markdown links in the three edited files and this response. No executable implementation or mandatory test framework was added; documentation checks do not establish runtime compliance.

The [Cycle 01 critique](CYCLE_01_CRITIQUE.md), [Cycle 01 improvements](CYCLE_01_IMPROVEMENTS.md), [manual validation](CYCLE_01_MANUAL_VALIDATION.md), [walkthrough](CYCLE_01_WALKTHROUGH.md) and Cycle 02 critique are preserved unchanged. The external failed checkpoints were not edited. In particular, the T02 future T06 delegation/T03–T05 rejection entries, T07 future T08 comment and translated T05 comment remain historical failures; the repaired export does not make those checkpoints valid.

## Expected next evidence

A new blind sequential synthetic trial must use a new external directory and expose one user turn at a time. After each meaningful write, retain both records and compare them against only the received prefix. Exercise praise without consent, repeated explicit selection with an exact non-English comment, an ordered sourced hybrid, and explicit-favorites-only export. Preserve failures before any repair.

At a real pause, a separate fresh reader should receive only repository instructions and the two current session files, with inspectable input boundary and output. It must recover active/parked paths, exact favorites, rejected directions, unresolved sources and next options without inventing missing preferences. Report exactly which operators were exercised, reconstructible counts, checkpoint history and final checks separately. An independent reviewer must inspect that evidence before acceptance; all twelve procedures remain draft pending that decision. This improvement work does not run or predeclare the trial successful.
