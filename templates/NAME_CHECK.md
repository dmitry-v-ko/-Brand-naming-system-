# Preliminary name check

Template only. Actual records belong outside this library. This is a dated screening report, not legal clearance.

Translate all narrative headings, findings and recommendations into the session's conversation language. Keep names and exact quotes unchanged; customer examples use the customer language. Fill this metadata from current state and run the [report language check](../checks/session/README.md#report-language) before delivery; stable keys are not translated.

```report-language
{"narrative": null, "customer_examples": null}
```

- check_id / candidate_id / exact_display_form:
- checked_at / scope_revision / current_or_stale:
- selected_profile_path_and_revision / selection_turn: none unless explicitly selected
- actual_goods_services / related_goods_services:
- proposed_Nice_classes / rationale / classification_source:
- requested_territories / languages:
- exact_forms_and_search_variants / normalization_notes:
- assumptions / missing_inputs:
- risk_boundary: soft / balanced / strict / pending; see [boundary policy](../checks/name-screening/RISK_BOUNDARY.md)
- boundary_user_selection_turn / exact_user_words / key_domain_and_market_constraints:
- decision_status: continue / clarify / do_not_recommend / not_checked (translate labels for the user)
- decision_reason / confirmed_basis_if_do_not_recommend: material finding record_id with confirmed primary evidence
- potential_conflict: evidence flag, not an automatic rejection
- coverage_complete: yes / no, with scope-specific gaps
- lexical_lineage_status: separate from screening status
- coverage_ledger_path / validator_result / validation_mode: automated or manual; see [coverage contract](../checks/name-screening/COVERAGE.md)
- recommended_next_action / owner / completion_condition:

## Findings and next actions

Repeat this card for each finding; lead with the most important one.

- Finding: stable record_id; exact name/business/domain and source; office/number/status for registry records (or explicitly unverified lead).
- Why it matters: concrete connection to our product, audience and territory; actual goods/services relationship for rights findings.
- Confirmed: verified facts and source/date, separate from assumptions.
- Unknown: the missing fact most likely to change the assessment.
- Effect in selected mode: rights / market distinguishability / practicality; or pending user choice.
- Next action: one recommended action, its owner and completion condition; no unauthorized third-party contact.
- Coverage: completed work and remaining scope, separate from risk status.

## Meaning and brief fit

| Check (meanings, idioms, sector senses, sound, typos, associations, distinctiveness, references/competitors/partners, tenant rules) | Observation and source | User preference or evidence? | Issue / unperformed work |
|---|---|---|---|

## Query and coverage ledger

| Query ID | Date / tool / source / actual tab URL | Executed mode, exact query and variants | Effective status, territory, class and other filters | Displayed count / raw rows / unique office+application IDs / pages | Settled? / state / gap and resume action |
|---|---|---|---|---|---|

## Significant records and neighbors

Plan IDs before browsing and retain unfinished queries. Use the [registry recipes](../checks/name-screening/REGISTRY_RECIPES.md); detailed page IDs/counts live in the session JSON ledger. A new run does not silently re-date old evidence.

| Office / number / primary URL | Exact mark / word or figurative type | Filed / registered / status observed at | Classes and actual goods/services | Territory / designations | Owner type with evidence (no private name) | Relevance / discrepancy / unresolved detail |
|---|---|---|---|---|---|---|

Record any evidenced fame/reputation concern and its jurisdiction-specific specialist question separately, including where goods/services are dissimilar. Fame alone is not an automatic rejection.

## Territorial conclusions

| Requested territory | Checks actually completed | Bounded finding and reasons | Missing work / specialist questions |
|---|---|---|---|

## Separate checks

| Company names | Domains | Actual market/common-law use | Native-speaker feedback | Non-use question |
|---|---|---|---|---|
| Not checked unless evidenced | Not checked unless evidenced | Not checked unless evidenced | Not checked unless actual feedback exists | Use not investigated; ask counsel about applicable rule/start event, not automatic availability |

## Decisions, corrections and next action

| Date / received turn | Decision or correction | Type and reason | Prior record preserved / new argument | Effect on shortlist and scope |
|---|---|---|---|---|

State what changed since any earlier conclusion. Changing the name, goods/services, territories, languages, risk boundary/constraints or material profile rule makes the old conclusion stale for the new scope. Preserve history, identify required rechecks, and export the status/date/scope/report link beside the name. Unchecked export is allowed when requested; no filings, purchases or payments are performed.
