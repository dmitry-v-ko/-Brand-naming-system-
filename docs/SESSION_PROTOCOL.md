# Stateful exploration contract

## Initialize and resume

Resolve a session directory outside the library checkout, such as a sibling `naming-sessions/<session-id>/`. Separate users and brands. Copy templates only for a new session; never overwrite existing records. Without write tools, keep equivalent state in chat and offer portable Markdown.

On resume, read both records, summarize the active branch and latest decision, and continue from recorded preferences. Missing state is unknown, not permission to invent previous decisions. Ask one focused question if contradictory feedback affects the next action.

For review evidence, distinguish a same-agent read-back from a fresh-context resume. A fresh reader receives only library instructions and the two current session files, without the executor's transcript, future scenario or expected answers. Record the actual input boundary and reader output outside the library; a disk read by an already informed agent does not demonstrate context isolation.

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

## Received-evidence boundary (internal memory and audit)

Assign received user turns stable IDs (`T01`, `T02`, …), including synthetic turns. Record `received_through` in both session files and cite the originating received turn for decisions, delegation scope, rejection and shortlist consent/comments. These are internal references, not extra questions or forms for the naming user. Agent hypotheses, provisional choices and pending questions stay explicitly labeled; they are not user preferences.

Keep exact quotes in their original language and spelling. Put translations or summaries in a separate labeled field; never present them as exact comments. Repeated selection retains the candidate ID and the prior consent/comment history with its turn IDs.

In sequential trials, the executor and any writing helper may access only the received transcript prefix. Do not read future fixture turns, expected preferences, expected comments or answer keys, even when available on disk. The trial controller supplies one turn at a time and keeps future material outside the executor's accessible context; an instruction alone is not evidence that this boundary held.

After each meaningful write, reconcile both files against that received prefix: latest decision, delegated choices, rejected directions, favorites and exact comments. Check that every asserted user fact cites a received turn and no field anticipates a later instruction. Normal session files evolve forward. For audited trials, retain immutable copies of both records at each meaningful write, labeled by received-through turn and write sequence. Append a correction event and create a later snapshot if repair is needed; never replace failed historical checkpoints or retroactively validate them using later feedback. Record final-state reconciliation and historical consistency separately.

Use unique candidate IDs as the counting unit. Report `total records = conforming candidates + out-of-operator diagnostics`; divide conforming candidates into retained and rejected for the current brief. A mechanically valid but rejected candidate remains conforming; an invalid construction remains a diagnostic even if discussed. Shortlisted count is a separate subset of conforming candidates, not an additional total. Keep branch references from double-counting reused IDs and state any other counting unit explicitly.
