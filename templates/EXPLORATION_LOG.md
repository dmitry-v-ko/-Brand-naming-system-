# Exploration log — session template

Template only. Copy for a new session outside the checkout; never overwrite an existing session. Empty fields mean unknown, not an implicit decision. See [session contract](../docs/SESSION_PROTOCOL.md).

## Session and active state

- session_id:
- session_directory: (absolute path outside library)
- received_through: latest actually received user turn ID; no future fixture access
- brand_brief: offer; audience; voice; exclusions; pronunciation; assumptions
- current_stage: BRIEF
- active_branch: none
- active_method: none
- active_universe: none
- latest_user_decision: received turn ID; original-language exact quote; separately labeled summary if useful
- delegated_choices: received delegation turn ID and scope, if any; unknown/none is valid
- agent_provisional_choices: inferred branch/method/universe, reason and assumptions; never label as user preference or delegation
- candidate_pool_summary: unique IDs; total = conforming (retained + rejected) + diagnostics; by branch/form/evidence; saved subset
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

Update after meaningful research, branching, feedback and selection. Confirm a write only after it succeeds. Never erase parked paths or candidates merely because they were rejected for the current brief.

Before confirming persistence, check both files against received turns only. For audited trials, preserve immutable snapshots after meaningful writes; append corrections without overwriting failed snapshots. See the session contract for the input boundary and fresh-context resume requirements. Keep this audit guidance internal to the session memory.
