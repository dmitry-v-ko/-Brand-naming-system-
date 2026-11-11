# Exploration log — session template

Template only. Copy for a new session outside the checkout; never overwrite an existing session. Empty fields mean unknown, not an implicit decision. See [session contract](../docs/SESSION_PROTOCOL.md).

## Session and active state

- session_id:
- session_directory: (absolute path outside library)
- received_through: latest actually received user turn ID; no future fixture access
- brand_brief: offer; audience; voice; exclusions; pronunciation; assumptions
- conversation_language:
- customer_language:
- language_basis: received user turn or provisional assumption; unresolved choices remain unknown
- category_descriptor: shared customer-language descriptor; see the session language contract
- active_tenant_profile: none unless explicitly selected; path / revision / selection turn
- name_checks: candidate ID → check ID / scope revision / preliminary status / date / report path; unknown is not cleared
- current_stage: BRIEF
- active_branch: none
- active_method: none
- active_universe: none
- latest_user_decision: received turn ID; original-language exact quote; separately labeled summary if useful
- delegated_choices: received delegation turn ID and scope, if any; unknown/none is valid
- agent_provisional_choices: inferred branch/method/universe, reason and assumptions; never label as user preference or delegation
- candidate_pool_summary: unique IDs; total = conforming (retained + parked + rejected) + diagnostics; by branch/form/evidence; label worker/conductor assessment layer; saved subset
- favorites: candidate IDs; shortlist is authoritative for saved details
- rejected_directions: direction, reason, user turn ID or explicitly agent assessment
- unexplored_ideas: concrete pending leads, not previously executed claims
- next_options: deepen; new universe; switch; combine; revisit; shortlist; stop

## Branch tree / explored paths

| Branch ID | Parent | Ordered method IDs | Universe | Status (active/parked/rejected) | Source IDs | Feedback / changed constraint | Next opportunity |
|---|---|---|---|---|---|---|---|

## Source ledger

| Source ID | Exact ingredient / script | Language / supported sense | URL + entry/sense locator | Access date/result | Evidence | Limit / failed route / next query |
|---|---|---|---|---|---|---|

For long extracts/maps use a session-owned RESEARCH_NOTES.md and point to its heading; do not use an unrecorded chat memory as evidence.

## Candidate pool

| Candidate ID | Exact English-facing name | Branch references | Proposed pronunciation/stress | Origin and exact ordered transformation | Form | Evidence of claimed lineage | Source IDs or none | Assessment / status |
|---|---|---|---|---|---|---|---|---|

Reuse an existing ID if exactly the same candidate returns; add branch references instead of creating duplicate candidates. Spelling alternatives are separate candidates when shown as selectable names.

## Decision and write journal

| Received turn ID/date | Original-language exact quote; summary separately labeled | Agent action / state delta | Save/remove consent with received turn ID | Write result / unresolved contradiction |
|---|---|---|---|---|

Update after meaningful research, branching, feedback and selection. Confirm a write only after it succeeds. Never erase parked paths or candidates merely because they were rejected for the current brief. For name decisions include reason, decision type (taste / brief / reported registry concern), source/date and new argument or correction. Screening reports preserve query coverage and previous scope revisions; a scope change marks the prior conclusion stale, never silently current.

Before confirming persistence, check both files against received turns only. For audited trials, preserve immutable snapshots after meaningful writes; append corrections without overwriting failed snapshots. See the session contract for the input boundary and fresh-context resume requirements. Keep this audit guidance internal to the session memory.

## Expanded exploration (only when used)

- run_id / brief_revision / received_through:
- brief_snapshot: audience; problem; promise; difference; voice; exclusions; countries; conversation_language; customer_language; language_basis; assumptions
- category_descriptor / shared_comparison_contexts:
- namescape: sample date, source URLs, observations and hypotheses; or not performed
- axis: methods / universes
- mode: three / all / selected universes
- execution: parallel / queued / explicitly agreed sequential fallback
- expected_assignments: assignment ID / method ID / universe ID, scoped to run_id + brief_revision

| Assignment ID + method + universe | Worker reference | Brief revision | Status | Result/source references | Failure, stale or no-yield reason |
|---|---|---|---|---|---|

Record exact-name duplicate mappings and conflicting lineages in the candidate pool. Keep participant observations separate from agent predictions. Native-speaker review: not performed unless supported by actual feedback. Never infer shortlist consent from worker output.

### Conductor comparison (only when combining results)

Keep worker assessments in their original records. For each proposed presentation representative record candidate ID, direction/near-variant group, brief fit, reading risk, explanation burden, and conductor decision/reason (present / park / reject). A worker-retained candidate may be parked centrally; this does not erase its valid construction or create a user preference. No representative is owed to any method. Favorites remain governed by explicit user consent.

### Ordered assessment and bounded adaptation

For each representative preserve name-only predictions, shared-context assessment, then origin/story assessment; record hard versus soft constraints and any actual blind-evaluator input boundary. Agent predictions are not audience observations.

For each adaptation pass record parent IDs, defect, required/optional source recognition and its user/agent basis frozen before generation, selected child method, up to two initial anchors/branches and three variants per anchor (a replacement stays in its branch and counts against the same budget), exact maps, comparison against unchanged controls, unresolved inherited concerns and stop decision. No improvement is valid; do not recursively adapt the variants. See the session contract for the owning procedure.

### Quality refinement and comparison

- source_lenses: object / action / outcome ingredient bank or gaps; not a candidate quota
- defect_route: anchor, observed defect, selected operator or replacement/stop, reason before generation
- control_budget: total candidate cap, reserved independent sound controls, reused branch or not performed
- standing_alternatives: actual session IDs, prior judgments and concerns; not inferred favorites
- comparison: improvement / tradeoff / observation that could change preference / tie or no improvement
- market_look: proposed leads, planned query/page limits, actual usage, dated sources/access gaps, close-category / other-category / unverified signal, next action; separate from registry coverage
