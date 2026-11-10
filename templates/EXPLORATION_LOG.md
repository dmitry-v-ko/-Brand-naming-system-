# Exploration log — session template

Template only. Copy for a new session outside the checkout; never overwrite an existing session. Empty fields mean unknown, not an implicit decision. See [session contract](../docs/SESSION_PROTOCOL.md).

## Session and active state

- session_id:
- session_directory: (absolute path outside library)
- brand_brief: offer; audience; voice; exclusions; pronunciation; assumptions
- current_stage: BRIEF
- active_branch: none
- active_method: none
- active_universe: none
- latest_user_decision: exact quote or clearly marked paraphrase; date/turn
- delegated_choices: scope, provisional selection, reason
- candidate_pool_summary: total; by branch/form/evidence; saved count; not a favorite list
- favorites: candidate IDs; shortlist is authoritative for saved details
- rejected_directions: direction, reason, user versus agent assessment
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

| Turn/date | User feedback or instruction | Agent action / state delta | Save/remove consent | Write result / unresolved contradiction |
|---|---|---|---|---|

Update after meaningful research, branching, feedback and selection. Confirm a write only after it succeeds. Never erase parked paths or candidates merely because they were rejected for the current brief.
