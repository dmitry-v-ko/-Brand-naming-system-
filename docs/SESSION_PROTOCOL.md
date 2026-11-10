# Stateful exploration contract

## Initialize and resume

Resolve a session directory outside the library checkout, such as a sibling `naming-sessions/<session-id>/`. Separate users and brands. Copy templates only for a new session; never overwrite existing records. Without write tools, keep equivalent state in chat and offer portable Markdown.

On resume, read both records, summarize the active branch and latest decision, and continue from recorded preferences. Missing state is unknown, not permission to invent previous decisions. Ask one focused question if contradictory feedback affects the next action.

## States and transitions

| State | Action | Exit condition |
|---|---|---|
| BRIEF | Establish offer, audience, character, exclusions; ask only questions affecting direction | Enough information for contrasting previews; mark assumptions |
| METHOD_MENU | Offer 3–6 different operators with examples and maturity labels | User selects a method or requests more |
| UNIVERSE_MENU | Offer 6–12 evocative worlds including distant domains, with evidence labels | User chooses; skip for methods without source research |
| DEEP_EXPLORE | Follow the skill, preserve sources, generate diverse clusters | Useful batch or research dead end |
| REFINE / NAVIGATE | Deepen, switch, combine, revisit, shortlist, review research, or stop | User selects next action |
| EXPORT | Return only explicitly saved names with origins and notes | User stops or returns to exploration |

States are navigation aids, not compulsory gates. Honor direct instructions from any state without requiring repeated confirmation. Menus invite creative choices; they are not permission checks for every research step. If the user delegates direction selection, record the provisional choice and proceed. Never auto-complete because a batch or count is reached.

## Branch and candidate identity

Use stable branch IDs (`B01`) and candidate IDs (`B01-C01`). Each branch records parent, method, universe, status, source references, feedback, and next opportunities. Park rather than erase branches when switching. On revisiting, recover sources and preferences. Hybrid branches name component methods and their execution order. Do not duplicate a candidate merely because it appears on multiple branches.

Separate candidate **form** (`attested`, `adapted`, `invented`) from **evidence** (`verified`, `unverified`, `not applicable`). A verified source word does not make its adapted candidate attested. Each research-derived candidate records the exact source term, source ID, supported meaning, and transformation. Sound inventions have no fabricated etymology.

## Persistence and consent

Update the exploration log after meaningful research, feedback, branching, or selection. Keep it compact but preserve enough references to recover parked paths. Detailed evidence may live in a session-owned `RESEARCH_NOTES.md`, outside the library.

Save only explicitly selected candidates to the shortlist. Praise alone is not a save instruction. Clarify ambiguous selections. Preserve exact spelling and user comments. Removal and substantive replacement require user approval. Repeated selection updates an existing entry rather than duplicating it. Around 20–25 entries offer voluntary review without blocking additions.

Export includes name, method, universe (or not applicable), origin, form, evidence, source references, and user comments when available. Keep unresolved claims labeled. State once that clearance has not been performed. Never claim a file was saved unless the write succeeded.


## Concrete evidence and reconciliation rules

`verified` applies to an ingredient/sense actually inspected, not to effectiveness, availability or the complete invented string. A supplied ordinary-English fixture ingredient may use `not applicable` when no external research claim is made. Mixed-source candidates list evidence per source; any unresolved asserted meaning makes overall lineage evidence `unverified`. Source IDs are scoped to a session; bibliography IDs must be explicitly labeled as such.

When switching, write the former branch as parked and create a child (derivation) or sibling (new direction). Preserve IDs across revisits. An unchanged candidate reused in a new branch keeps its original candidate ID and gains a branch reference. Reconcile favorites in both files after each consent event; if only one file was written, record the incomplete write and repair before claiming persistence. Never copy templates over a resumed session.

No write tools: emit the same fields in chat under “state” and “shortlist,” and state that no file was saved. On a failed write preserve the last confirmed state and provide exportable text. A resume summary names exact favorites, active branch, parked opportunities, rejected directions and the latest actual instruction; unknown prior feedback stays unknown.
