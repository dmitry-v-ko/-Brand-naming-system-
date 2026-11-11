# Registry search recipes

Operational reference checked against the public interfaces on 2026-11-11. Labels can change: inspect the current form and confirm the executed query. These recipes supply search operations, not legal clearance or universal territories/classes. Replace `aster` with the candidate's search key; it is a syntax example, not a screened name.

## Start with a bounded search plan

Use the selected scope, not a default market. Reuse a confirmed brief. If only an industry is known, ask about actual operations in ordinary language (for example payments, lending or investment), and continue all-class name searches while the service scope stays provisional.

Before searching, create query IDs for each requested territory: literal wording, prefix, contains, and similar spellings; include the display form and plausible punctuation-free, spaced and hyphenated forms. Record which variants are relevant and why. For similar forms, start with pronunciation-driven substitutions and one-character additions/deletions/substitutions; do not silently label a fuzzy algorithm a complete phonetic search. Declare the exact variants and any unsearched remainder.

Run an all-class, all-status history pass first. Prioritize the resulting records by actual goods/services, then use narrower related-service searches if the broad result set is too large. A narrower search is a new query; the broad query remains partial. Keep live applications as well as registrations. Material findings can justify an early report, with unfinished planned queries still visible.

## TMview — overview including EU national rights

Open [TMview](https://www.tmdn.org/tmview/). In the name field select the operator explicitly:

| Purpose | Control | Field value |
|---|---|---|
| Exact display / normalized key | **Is** | `aster` (separate query per relevant form) |
| Prefix / compounds | **Begins with** | `aster` |
| Substring / compounds | **Contains** | `aster` |
| Spelling neighbors | **Fuzzy search** | `aster` |

Select **Territories** by protection sought. For EU, select European Union and record the resulting EUIPO, national offices and WIPO selections; do not select EUIPO alone and call it EU-wide prior-right coverage. Leave classes and statuses unrestricted for the history pass. Press **SEARCH** after changing the operator or filters, then verify the result header, query and effective filters. Changing the dropdown alone does not execute a search.

Read every page in the declared query, retaining office + application number per row. Fuzzy search is spelling-distance assistance, not proof of phonetic or conceptual coverage. Open material records and follow the issuing office. If a detail page fails, preserve the list observation and number, then use the primary office's number search; if that also fails, record the unresolved record and next query. A failed detail page never means the mark is absent.

Source: [TMview help](https://www.tmdn.org/static/tmdsview/tmview/helpFiles/en/help.html). Some help is historical: current visible controls and results determine the executed mode. TMview is an aggregation service, not the legally authoritative register.

## EUIPO — primary EUTM verification

Open [eSearch plus](https://euipo.europa.eu/eSearch/). Use the basic search field for the candidate or a known application number. Record this as **basic**, not exact equality: name searches can return containing words. Select the **Trade marks** results, inspect pagination, then open the result's **+ info** link for the full card.

Verify the number, word/figurative type, filing/registration dates, current status, owner type, classes and expanded goods/services. Record the language shown. Do not copy a UK comparable mark's goods or owner into the EUTM record. Use the full detail URL in the report. For exact/prefix/contains/fuzzy discovery use the TMview controls above and verify material EUTMs here; do not invent EUIPO query operators. If using advanced controls, log their actual labels and values as a separate query.

## UKIPO — separate UK search

From [GOV.UK](https://www.gov.uk/search-for-trademark), choose **Search by keyword, phrase or image** → **Word**. In **Search type**, run separate queries:

| Purpose | Search type | Search word(s) |
|---|---|---|
| Literal form | **Exact** | `aster` |
| Prefix | **Starts With** | `aster` |
| Substring | **Contains String** | `aster` |
| Neighbors | **Similar** | `aster` |

Set **Status: All**; clear class selections; inspect the entire filed-between range, including its upper date, and record it. Use up to 50 results per page and read every page. Retain series rows but deduplicate record counts by full UK/UK-designating application number, not name. Keep raw row and unique record counts separate.

The form may display a zero result under “To continue, please address…”; treat it as zero only when the message explicitly says no marks match, loading has ended and the submitted query/filters remain visible. Open a material result by number; **Display content without tabs → Open all** exposes goods/services. Preserve **Application Published**, **Registered**, **Protected** and **Dead** as distinct observed statuses.

## USPTO — use the field-tag interface

Open [Trademark Search](https://tmsearch.uspto.gov/). Select **Field tag and Search builder** before entering these queries; confirm the selected mode. Leave **Live** and **Dead** included and classes unselected for the history pass.

| Purpose | Query | Interpretation |
|---|---|---|
| Literal wording | `CM:aster` | Combined-mark wording; not equality of the whole mark |
| Multiword / spaced form | `CM:"as ter"` | Phrase; inspect punctuation and tokenization in returned marks |
| Prefix | `CM:aster*` | Prefix in the combined-mark field, not necessarily at the beginning of the displayed name |
| Contains | `CM:*aster*` | Substring expansion; official regex alternative `CM:/.*aster.*/` |
| Similar | Separate CM queries for declared spelling/pronunciation variants, plus a justified shorter prefix | Not equivalent to TMview fuzzy or exhaustive sound similarity |

CM includes mark-related text; inspect the actual wordmark. Never promote a Wordmark-mode wildcard zero to a valid prefix/contains result. If a query errors or disagrees with a known result, inspect the mode, current Help/Search builder and filters; rerun the intended query once with documented syntax. Keep the failed attempt separately. Do not blindly add escaping to user names containing query syntax: use the current builder/help to construct a literal query and record it.

After loading ends, record the count, page size, all inspected serial numbers and active filters. Open material results; expand **Goods and services** and inspect **View in TSDR** when status/history needs clarification. Record both serial and registration numbers without counting them as separate marks. A cancelled federal registration is not proof that market use ended.

Primary references: [federal searching and expansion](https://www.uspto.gov/trademarks/search/federal-trademark-searching), [field-tag guide](https://www.uspto.gov/sites/default/files/documents/TM-FederalTrademarkSearching-FieldTags-handout.pdf), [current Help](https://tmsearch.uspto.gov/?page=help). Registry coverage and US market/common-law coverage remain separate.

## National offices and international designations

EU national and international discovery uses the selected TMview territory/office list. Verify material national records through that office's current **application/registration number** search; record the office, full number and actual controls. There is no shared national-office query syntax. For a material international registration, use [WIPO Madrid Monitor](https://www3.wipo.int/madrid/monitor/en/) by IR number and inspect the specific designation and its current status, then the designated office where needed. A global IR status does not establish protection in every requested territory. Missing offices, designation checks and failed records stay explicit coverage gaps.

For a German lead, open [DPMAregister basic trademark search](https://register.dpma.de/DPMAregister/marke/basis), enter the full number in **Aktenzeichen/Registernummer**, and press **Recherche starten**. Verify **Markendarstellung**, **Aktenzustand**, dates and **Waren/Dienstleistungen** on the result card. Keep **Aktenzeichen** (filing number) and **Registernummer** separately: they can differ by a check digit. This number-lookup fallback was exercised; it does not constitute a fresh broad search of Germany.

## Completion and the next action

Use [COVERAGE.md](COVERAGE.md) for query states, counts and the executable ledger check. Once a material neighbor is found, complete one compact finding card before expanding more searches:

> **Finding:** exact mark, office/number, current status and primary link.  
> **Why it matters:** concrete similarity and actual related goods/services.  
> **Unknown:** the one missing fact that most affects the decision.  
> **Next action:** one recommended action, its owner and completion condition.  
> **Coverage:** completed work and remaining scope; finding and completeness are independent.

| Observed condition | Recommended next action |
|---|---|
| Only an aggregate hit or card error | Agent opens primary number search; done when status and actual goods are confirmed, otherwise preserve a named gap |
| Primary record shows a close mark and related goods | Prepare the comparison and recommend specialist assessment; done when the material similarity/services question is assessed. Continue already authorized bounded searches without another permission question |
| Service scope is too vague to compare | Ask one concrete product-operation question; continue independent name searches |
| Query is partial/loading/blocked | Resume the missing page or inspect the current form and rerun once; after persistent failure record the blocker and primary-source fallback |
| No material match in completed declared queries | Report that bounded result, then name the highest-priority unperformed language/market/service check |

Do not remove the favorite or generate a replacement batch automatically. Offer parking or alternatives only when a user decision is useful. The default next action is a recommendation, never an instruction to contact a third party without authorization.
