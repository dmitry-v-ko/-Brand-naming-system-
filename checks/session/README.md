# Session checks

Read-only Python standard-library checks for the [session contract](../../docs/SESSION_PROTOCOL.md). Run from the library root; session data belongs outside the checkout. These are internal checks, not additional user approvals. Fix failures before claiming persistence, generating a bounded batch or delivering a report. If Python/tools are unavailable, perform the same reconciliation manually and explicitly record that automated validation was not performed.

## Current state

```sh
python3 -B checks/session/validate_session.py state /absolute/session-directory T08
```

Supply the latest **actually received** turn from the conversation independently of the files. Each file must contain exactly one `session-state` JSON object, as in the [log](../../templates/EXPLORATION_LOG.md) and [shortlist](../../templates/SHORTLIST.md) templates. Rewrite these identical current blocks; preserve history separately. Keep the stable `## Active favorites` heading and first two table columns (`Candidate ID`, `Exact name`), even when surrounding narrative is translated. Put archived rows under a separate heading.

Required fields: nonempty `session_id`, `received_through`, inline `brand_brief`, `conversation_language`, `language_basis`, `category_descriptor`, `current_stage`; `customer_language` and `active_branch` may be null while unresolved. Use an explicit provisional descriptor/brief when appropriate, never fabricated user choices. `latest_user_decision` contains its originating `turn` and exact `quote` (it can predate the latest received question). `favorites` is an ordered list of `{"id":"B01-C01","name":"Luma"}` objects; `name_checks` is a candidate-ID map; `next_options` is a list. Other template fields preserve existing session details and must also agree across the two blocks.

Keep profile path/revision/selection turn, onboarding method IDs/turn, delegated scope/turn, provisional choices/reasons, pool counts/assessment layer and rejected directions/reasons/turns in their named fields. Each `name_checks` entry preserves check ID, scope revision, selected boundary, decision status, coverage, date and report path; unknown does not mean cleared. The checker verifies state equality, current turn and active row identity/order/spelling; it cannot establish that a shared fact or consent is true. Reconcile those against received evidence. Never silently migrate an old session: snapshot it, resolve contradictions and replace its current header explicitly.

## Bounded refinement

Before generation, save a session-owned plan (synthetic example):

```json
{
  "pass_id": "P01",
  "anchors": [{
    "parent_id": "B01-C01",
    "defect": "Awkward final cluster",
    "method": "phonetic-invention",
    "source_recognition": "optional",
    "recognition_basis": "T05: user permits a new sound",
    "slots": ["B02-C01", "B02-C02", "B02-C03"]
  }],
  "sound_controls": []
}
```

```sh
python3 -B checks/session/validate_session.py refinement /absolute/session/plan.json
python3 -B checks/session/validate_session.py refinement /absolute/session/plan.json /absolute/session/result.json
```

The first command is preflight: retain its successful output and `plan_sha256` before invoking the method. At most two distinct parents, three unique slots each; independent sound replacements spend those same slots. `sound_controls` lists any reserved independent control IDs (at most two total), within the slots, not an additional allowance.

The second command is postflight. Result shape: `{"plan_sha256":"<saved preflight hash>","generated_ids":["B02-C01","B02-C02"]}`. Include all generated candidates, even rejected spoken forms and separately selectable spellings; empty output is valid. Do not refill consumed slots. Preserve exact forms/edits and assessments in the candidate log. A changed plan/hash or fourth variant fails; a new authorized pass needs a new plan. The fingerprint detects alteration against the retained preflight result; it does not prove timing or detect output omitted from the ledger. Review those boundaries, never regenerate a hash to conceal an overrun.

## Report language

Before delivery, include exactly one metadata block with the session's actual language choices:

```report-language
{"narrative":"ru","customer_examples":"en"}
```

```sh
python3 -B checks/session/validate_session.py report /absolute/session/report.md ru en
```

Pass expected languages from current state, not from the report itself. If customer language is still unknown, resolve it or explicitly omit customer examples and reconcile it before export. Preserve exact names and source quotes; mark source quotations as blockquotes and customer copy in `customer-example` fenced blocks. Translate narrative headings, findings and recommendations. The command checks metadata and a rough Cyrillic/Latin majority for Russian/English prose (at least 20 letters outside fences, quotes, tables and structured key prefixes; field values still count). It is **not language detection**: always review actual narrative, tables and customer examples; other languages receive only metadata/prose-presence checks. Do not claim semantic language validation from a passing script check.

Exit codes: `0` supplied data passes these checks, `1` contract violation, `2` input/JSON/usage error. The checker writes nothing and performs no network requests. Run regression tests with `python3 -B -m unittest discover -s tests -v`.
