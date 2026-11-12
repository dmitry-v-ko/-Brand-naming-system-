# Shortlist — session template

Template only. Actual session file belongs outside the checkout. Empty means no explicit selections yet. Praise is not consent. Preserve exact spelling and candidate ID; repeated selection updates comments on the existing row. Only the user may authorize removal or substantive replacement. At about 20–25 entries offer voluntary grouping/pruning; continue additions if desired.

## Session and active state

Replace this current block after every meaningful write and copy it identically to the other session file. Fill known facts from received turns; `null` means unknown. Keep an inline brief with offer, audience, scope, voice, exclusions and assumptions. See the [state schema and check](../checks/session/README.md#current-state). Historical decisions belong below, not in another current block.

```session-state
{
  "session_id": null,
  "session_directory": null,
  "received_through": null,
  "brand_brief": null,
  "conversation_language": null,
  "customer_language": null,
  "language_basis": null,
  "category_descriptor": null,
  "active_tenant_profile": null,
  "name_checks": {},
  "onboarding_methods_shown": null,
  "current_stage": "BRIEF",
  "active_branch": null,
  "active_method": null,
  "active_universe": null,
  "latest_user_decision": {
    "turn": null,
    "quote": null
  },
  "delegated_choices": null,
  "agent_provisional_choices": [],
  "candidate_pool_summary": null,
  "favorites": [],
  "rejected_directions": [],
  "unexplored_ideas": [],
  "next_options": []
}
```

## Active favorites

| Candidate ID | Exact name | Proposed pronunciation | Ordered method IDs | Universe or not applicable | Origin / source term and supported sense | Exact transformations | Form | Evidence of claimed lineage | Source references | Selection turn ID / exact original-language comments with turn IDs | Boundary / decision status / coverage / date / scope revision / report |
|---|---|---|---|---|---|---|---|---|---|---|---|

Keep source citations sufficient for standalone export: URL, exact entry/section, access date and uncertainty, not bare IDs pointing to inaccessible memory. A verified ingredient never makes an invented name an attested word. Export only these explicitly selected rows and preserve every field.

Keep screening status separate from lexical evidence. A changed name, goods/services, territory, language, risk boundary/constraints or material profile rule makes the old conclusion stale for the new scope. Preserve prior records and state missing rechecks beside the name; a requested unchecked export is allowed with explicit gaps.

Preserve prior consent/comments on repeated selection. Label any translation or summary separately from exact quotes. Reconcile with the log against received turns only; future fixture comments are unavailable evidence. Audit snapshots and corrections follow the session contract, without adding user-facing steps.

When an exact spelling has multiple derivations, preserve each alternative lineage with its own ordered methods, origin, form, evidence and sources in the row or a linked export section. Never merge incompatible evidence into a single verified story.

## History

Preserve removed selections and prior comments here with their received turn IDs. Do not leave removed candidates in the active table.
