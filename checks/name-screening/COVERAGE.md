# Coverage ledger

Create `SCREENING_LEDGER.json` beside the session's `NAME_CHECK.md`, outside this library. Plan query IDs before browsing; add newly justified queries without deleting unfinished ones. The JSON ledger owns counts and execution states; the report summarizes its result and links it. Older reports without a ledger are historical evidence, not newly validated checks.

Each query is `pending`, `partial`, `blocked` or `complete`. Before setting complete:

1. Confirm the executed query, mode, territory, class and status filters.
2. Observe settled results: loading has ended and rows or an explicit zero are visible. A spinner plus “No rows found” is pending.
3. Inspect all pages; keep each page's ordered office-qualified record IDs, including repeated series rows. The counted unit is a row for pagination, and office + application/serial number for unique records. Names, owners and registration/serial pairs are not deduplication keys. Retain separate jurisdictions and designations. IDs use an uppercase office prefix (letters/digits/underscore/hyphen), a colon, then the source's number containing at least one digit, e.g. `UKIPO:UK00001234567`, `WIPO-EU:1234567`, `WIPO-UK:1234567`. Preserve spaces/check digits within the source number; do not silently equate filing and registration numbers.
4. Reconcile raw rows with the displayed count and pages 1..N. If a site counts distinct records rather than rows, record that mismatch and resolve it before marking complete; do not fabricate IDs to satisfy arithmetic.
5. Preserve the date, source URL and gap. Unfinished queries need a concrete resume instruction. A zero-result search has one observed page with an empty ID list.

Minimal synthetic example (not a live search):

```json
{
  "check_id": "example-01",
  "scope_revision": "1",
  "risk_boundary": {"mode": null, "user_selection_turn": null},
  "decision": {"status": "clarify", "reason": "Boundary not chosen and research incomplete.", "next_action": "User: choose soft, balanced or strict; agent: complete planned research."},
  "planned_query_ids": ["UK-exact", "UK-similar"],
  "scope_gaps": ["Language and market checks not performed"],
  "queries": [
    {
      "id": "UK-exact", "office": "UKIPO", "mode": "Exact",
      "query": "aster", "checked_at": "2026-11-11",
      "source_url": "https://trademarks.ipo.gov.uk/ipo-tmtext",
      "filters": {"territories": ["UK"], "classes": "all", "statuses": "all; filed 1876-01-01 through 2026-11-11"},
      "state": "complete", "settled": true, "filters_verified": true,
      "displayed_count": 0, "pages_expected": 1,
      "pages": [{"page": 1, "record_ids": []}], "gap": ""
    }
  ],
  "findings": []
}
```

For a pending/blocked/partial query use the same identity, source, date and filter fields, set `state` and a nonempty `gap`; counts can remain unknown and are not accepted as complete. Each material finding uses:

```json
{
  "record_id": "OFFICE:application-number",
  "material": true,
  "primary_verified": false,
  "source_url": "https://example.org/observed-record",
  "next_action": "Agent: open the primary card by number and confirm actual goods/services."
}
```

Run from the library root when Python 3 is available:

```bash
python3 checks/name-screening/validate_coverage.py /absolute/session/path/SCREENING_LEDGER.json
```

Exit 0: entered evidence is internally complete for the declared plan/scope gaps and the decision contract is valid. Exit 1: incomplete/inconsistent coverage or invalid decision; read `issues` and `decision_issues` separately. Exit 2: file/JSON/usage error. A positive `potential_conflict` remains independent of `coverage_complete`. Exit 0 is neither legal clearance nor proof that the agent actually visited sources. The validator cannot discover omitted scope, verify UI facts or decide similarity. The agent must reconcile the plan with the selected scope and recipes before relying on its output.

Every new ledger records `risk_boundary` and `decision` as above. A selected mode is `soft`, `balanced` or `strict` with a nonempty `user_selection_turn`; pending selection uses null. Decision `status` is one of the four IDs in the [boundary policy](RISK_BOUNDARY.md#findings-and-decisions), with `reason` and `next_action`; `do_not_recommend` additionally needs `confirmed_basis` equal to the `record_id` of a material finding with verified primary evidence and a source URL. Explain its significance in `reason`. For market/domain findings, use a stable session finding ID (e.g. `MARKET-1`) and let `primary_verified` mean direct verification of that source, not legal verification. Query page IDs still require office:number format. `continue` requires complete coverage. Strict-mode Continue additionally requires nonempty `risk_boundary.priority_markets`, `categories` (main and adjacent), and `key_domains` arrays, plus `domain_strategy` describing availability or a realistic acquisition path; missing constraints lead to Clarify. `continue` and `do_not_recommend` require a user-selected boundary. Clarify/Not checked remain available while selection or evidence is pending. `decision_valid` validates this structure, not the truth of a selection turn, sufficient search scope or the merits of the judgment.

Old ledgers still receive coverage results but no valid new decision until these fields are added from an actual user choice and current assessment. Do not rewrite historical conclusions automatically or invent a selection turn. This changes the CLI success condition: consumers must inspect coverage and decision fields separately.

Without Python or file tools, keep the same fields and arithmetic in the report, label validation **manual**, and state that the automated check was not run. Do not require a software installation to conduct naming in Claude, Codex or Pi. Never infer that all required work is done merely because every opened tab has finished.
