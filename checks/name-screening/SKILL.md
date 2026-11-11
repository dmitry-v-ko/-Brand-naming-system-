---
name: name-screening
description: Use when checking a candidate or shortlist for linguistic, brief, market and preliminary trademark risks, before a final naming recommendation, or when the user asks about name availability.
---

# Preliminary name screening

This is a review stage, not a nineteenth generation method or a legal opinion. Separate creative fit, user decisions and registry evidence. A trademark search is not a patent search; clarify that distinction briefly if needed. Filing, registrations, domain purchases, payments and contacting third parties are outside this workflow.

## 1. Load the chosen context and freeze scope

Load a tenant profile only when the user explicitly selects it, using [TENANT_PROFILE.md](../../templates/TENANT_PROFILE.md) as the portable structure. Record its path, revision and selection turn. Do not discover or inherit another tenant's rules from adjacent files, earlier sessions or a familiar brand name. Without a selected profile, use the current brief; no default countries, Nice classes, reference brands, languages or phonetic exclusions apply.

For each exact candidate spelling, keep its existing candidate ID and create a check ID plus scope revision in a session-owned [NAME_CHECK.md](../../templates/NAME_CHECK.md). Freeze:

- Exact display form and proposed pronunciation; search variants with punctuation removed, spaces, hyphens, case, close spelling/sound/meaning, translations where relevant. Normalization creates search keys; it is not a rule that a mark must be registered without punctuation.
- Actual goods/services, users, channels and plausible related goods/services. Map these to proposed Nice classes with reasons and a current classification reference; ask about missing material facts. Class numbers never replace the real goods/services description.
- Requested territories and applicable languages; distinguish countries, regional rights and international designations. Ask one focused question when scope is unknown rather than importing countries from a previous client.
- Selected profile's filters, reference/partner comparisons, prior decisions, required check order and any explicitly waived criterion. Record assumptions separately from user instructions.

A change in name, goods/services, territory, language or material profile rule starts a new scope revision. Mark prior conclusions **stale for the new scope**, preserve their dated evidence, and list what must be rerun; old results cannot authorize the new recommendation. A matching scope is still dated evidence, not perpetual availability.

## 2. Check decisions, meaning and fit

Read the selected tenant/session decision history first. Preserve rejection reason, date, source and whether it is taste, brief fit or a reported registry concern. Do not propose a rejected name/variant again without a new substantive argument or explicit request. Evaluate new evidence; when a verdict changes, state why and append a correction instead of erasing the old decision. Frustration or repetition alone is not new evidence.

Check relevant dictionary senses, idioms, sector-specific meanings, pronunciation, homophones, likely typos, unwanted associations, descriptiveness/distinctiveness, competitors, references and partners. Choose languages and domains from scope; no universal finance or European-language filter. Record supported senses and sources, untested audience impressions and access gaps separately. Report every material failed brief filter found, not just the first. Similarity to a selected reference is a configurable comparison, not an automatic legal conflict. Do not turn subjective exclusions into registry findings.

Give a concise explanation of strengths when supported and what breaks the brief. If a rejected candidate contains a useful mechanism, name it without launching another batch unless requested. Sparse or ambiguous input may need one clarification; do not guess whether a word is a candidate or a command when both readings change the action.

## 3. Search the selected territories

Use live accessible registry tools/browser evidence. Search snippets, memory, old client catalogs and generated fixtures are leads, not current results. If access is unavailable, record **not performed** or **incomplete** with a next-query plan; do not manufacture records or a negative result. Use permitted routes and request host access if necessary; no bypass of access controls.

Use [TMview](https://www.tmdn.org/tmview/) as an overview, then verify significant records in the relevant primary offices. For an EU scope, include EUIPO rights/applications, relevant national rights and international registrations designating the applicable territories. For UK, use the [direct UKIPO search](https://www.gov.uk/search-for-trademark); EU and UK are separate. For US, use [USPTO search](https://www.uspto.gov/trademarks/search) and record related market/common-law search coverage separately. For other territories, select their competent offices and relevant international designations. US is not required if it is outside the chosen scope.

Cover live applications and registrations, exact and similar/compound marks (including exact, starts-with and contains controls where available), and a broader history pass across all classes without a live-status restriction. Record any unavailable mode as a coverage gap. Include related goods/services and adjacent classes: a matching class is not an automatic bar, and a different class is not an automatic escape. Assess potentially relevant sound, appearance, meaning and commercial impression with the goods/services relationship; leave the legal conclusion to a qualified specialist. See [USPTO similarity guidance](https://www.uspto.gov/trademarks/search/likelihood-confusion) and [search breadth guidance](https://www.uspto.gov/trademarks/search/federal-trademark-searching). [WIPO](https://www.wipo.int/en/web/madrid-system/check-availability) also cautions that international collections can be incomplete; check local offices.

For every query record the exact query/variants, actual filters, date, source, tab/URL and access outcome. Old SPA hash URLs are examples, not a guaranteed current API: use current controls and verify their effective values. Wait for result rows, not only a counter. Inspect all pages in the declared query scope; reconcile displayed counts, unique rows and pagination. A counter of 120 with 100 inspected rows is incomplete. Confirm the active tab and URL before acting. If rows, filters or pagination cannot be verified, report that limit instead of interpreting an empty/loading page as no matches.

Also flag evidence of a well-known or reputed mark even when the ordinary goods/services relationship is weak: applicable law may protect it beyond that relationship. Record the evidence and territory-specific question for counsel; neither a different class nor fame alone decides the outcome. For example, [USPTO guidance on well-known marks](https://www.uspto.gov/ip-policy/trademark-policy/well-known-marks) describes conditional protection against dilution on dissimilar products. Verify the relevant jurisdiction's current requirements; do not impose a universal ban on any familiar brand.

## 4. Inspect significant records

Open exact matches in target goods/services and material similar/compound neighbors. Record office and application/registration number, mark/type, filing and registration dates, current status and observation date, classes and the actual substance of goods/services, territories/designations, primary source and unresolved discrepancies. TMview is an official aggregation service, not a substitute for the issuing office's record. Keep both observations when sources disagree; do not silently select the convenient status.

Do not name private individual owners in user-facing notes: use “private individual” and the record number. Report an owner's type only with evidence; do not guess that a holder is a naming agency from its name or portfolio. Unknown is valid.

Age or possible non-use is a **question for counsel**, not automatic availability, cancellation or freedom to use. Some jurisdictions have five-year non-use rules, but conditions and the starting event differ; do not calculate a universal deadline from a filing/registration date. If a date is requested, verify the current official rule and relevant starting event before any qualified calculation, retain exceptions, and state that actual use has not been investigated. For example, [UKIPO non-use guidance](https://www.gov.uk/government/publications/trade-marks-revocation/revocation-non-use-proceedings) describes a revocation procedure, not automatic removal. No filing or payment follows from this screening.

## 5. Report bounded findings

Lead with exact candidate, scope/date and preliminary status. Use only bounded language:

- **Not performed** — no relevant check executed.
- **Incomplete** — missing scope, failed access, incomplete pages/filters, unresolved significant records or unperformed required checks.
- **Potential conflict** — evidence warrants specialist review; state the concrete match and goods/territory relationship. Completeness is a separate field: a potential conflict may coexist with incomplete coverage.
- **No material match found in the checked scope** — only for the documented completed checks, never “free”, “clean”, “closed” or legal permission.

Summarize significant exact matches and neighbors, per-territory findings/limitations, linguistic and brief-fit issues, corrections and questions for a specialist. Include source links and check IDs. Keep company-name records, domains and actual market use as separate checked/not-checked sections; domain availability is not trademark entitlement. The [USPTO comprehensive-search guidance](https://www.uspto.gov/trademarks/search/comprehensive-clearance-search-similar-trademarks) explains why registry-only searching cannot establish comprehensive US clearance.

## 6. Return to naming with state intact

Creative previews may be unchecked if clearly labeled. Before a final recommendation, screen the candidate/shortlist or explicitly report incomplete/unperformed checks and limit the recommendation to a creative working choice. A directly requested unchecked export is allowed with gaps beside the names; do not invent a permission gate. A selected profile may require stricter registry-before-preview/acceptance ordering; honor it and withhold unscreened recommendations when that profile requires it.

Persist check ID, scope revision, status, date and report link alongside each candidate in the shortlist/export. Keep lexical evidence status separate. Never remove a favorite without user instruction merely because its check found a concern; record the concern and options. Offer decision-history updates with reasons/dates; apply any document-change convention only inside the explicitly selected tenant, not globally.

## Source limits

The official guidance linked above supports the search framework; it is not evidence about any candidate. Registry results and laws need current verification in each check. The [EUIPO availability entry point](https://www.euipo.europa.eu/the-office/help-centre/tm/faq-search-availability) is also relevant for EU searches; access may be restricted, which must remain an explicit gap rather than a claimed check. No territory is added merely because its office appears in this guide.
