# Corpus contrast: actual bounded retrieval and counting

Date: 2026-11-10. This report records actual opened pages and a count calculation, not a simulated retrieval. The naming brief and feedback in the skill are synthetic. The comparison design, selection judgments and workflow are editorial adaptations; NOAA and Collins do not endorse a naming algorithm.

## Collection design and reproducible boundaries

Question: which ingredients appear more concentrated in short coastal-motion explanations (A) than in short inland/mixed-water habitat explanations (B)? B is a **specialist topical reference**, not general English. Both sets use NOAA National Ocean Service public educational facts pages, contemporary pages displaying last-updated 2026-09-23. Same publisher and genre reduce some variation; unequal length, topic overlap and paragraph roles remain limitations.

Documents were selected purposively for accessible short explanations after opening them; the paragraph rule was fixed before the count calculation, not before browsing. This is a transparent demonstration sample, not random sampling, representative coverage or a preregistered study. No documents were replaced to improve a candidate's score. The table of terms was selected by reading the included material, before dictionary checking, and is an inspected candidate inventory rather than an exhaustive ranked vocabulary.

Each URL below was actually opened with the web tool on 2026-11-10. Line locators refer to that extraction; paragraph descriptions and endpoint anchors allow browser repetition without that tool. Include whole specified paragraphs, including text inside inline links, but no headings, captions, image text, navigation, or transcript. Count only the following spans:

| Fixture source / set | Opened document and exact included span | Tokens |
|---|---|---:|
| S01 / D1 / A | [NOAA, Why does the ocean have waves?](https://oceanservice.noaa.gov/facts/wavesinocean.html), first two narrative paragraphs below the video teaser, extracted lines 8–9. Begin “The ocean is never still.” End “along the coast.” Stop before the paragraph about hazardous waves. | 127 |
| S02 / D2 / A | [NOAA, What is a rip current?](https://oceanservice.noaa.gov/facts/ripcurrent.html), two consecutive factual paragraphs, lines 5–6. Begin “Rip currents are powerful”; end “an Olympic swimmer.” Exclude the preceding beach/video teaser and subsequent swimmer advice. | 53 |
| S03 / R1 / B | [NOAA, What is a watershed?](https://oceanservice.noaa.gov/facts/watershed.html), paragraph beginning “The size of a watershed”, line 5; through “a single county.” Includes parenthesized HUC and linked Hydrologic Unit Codes. Exclude preceding image caption and following Did you know box. | 52 |
| S04 / R2 / B | [NOAA, What is an estuary?](https://oceanservice.noaa.gov/facts/estuary.html), first narrative paragraph, line 6; begin “Estuaries and their surrounding wetlands”; end “salty seawater.” Exclude video teaser and next paragraph about freshwater ecosystems. | 43 |

A total = 127 + 53 = **180** tokens. B total = 52 + 43 = **95**. Do not count duplicated heading summaries or video transcripts. If live paragraphs change, record a new version/date and recalculate; do not silently present these historical counts as current.

## Token rule and transparent calculation

Lowercase each span. A token is one maximal consecutive run of ASCII letters `a`–`z`. Every other character separates tokens. Count all tokens, including articles and conjunctions; no stopword removal in denominators. Thus `Wind-driven` becomes `wind`, `driven`; `fast-moving` becomes `fast`, `moving`; `U.S.` becomes `u`, `s`; `scales—referred` becomes `scales`, `referred`. No lemmatization: `wave` and `waves`, `lake` and `lakes`, `current` and `currents` stay distinct. No multiword counts or term-family aggregation were used.

Manual reproduction needs only the four opened spans: number their tokens using this rule, tally each displayed term by document, and recompute totals on a second pass. The author additionally ran a temporary Python regular-expression/Counter calculation outside the repository on transcribed spans; no script or runtime is needed to use the method. This is same-agent checking, not independent acceptance. Spot checks: D1 `wind` includes the hyphenated occurrence; D2 contributes two `currents` and no singular `current`.

`A rate = 1000 × (D1 + D2) / 180`; `B rate = 1000 × (R1 + R2) / 95`; `delta = A rate − B rate`. No smoothing, ratios or significance test. Rounding is to two decimals **after** division. Example: `surface = 1000 × 3/180 = 16.67`, versus zero in B. A zero count requires no mathematical repair for subtraction.

| Inspected term | D1 | D2 | R1 | R2 | A / 1,000 | B / 1,000 | Delta |
|---|---:|---:|---:|---:|---:|---:|---:|
| water | 4 | 1 | 0 | 3 | 27.78 | 31.58 | −3.80 |
| ocean | 5 | 0 | 0 | 0 | 27.78 | 0.00 | +27.78 |
| waves | 8 | 0 | 0 | 0 | 44.44 | 0.00 | +44.44 |
| wind | 4 | 0 | 0 | 0 | 22.22 | 0.00 | +22.22 |
| surface | 3 | 0 | 0 | 0 | 16.67 | 0.00 | +16.67 |
| crest | 1 | 0 | 0 | 0 | 5.56 | 0.00 | +5.56 |
| horizon | 1 | 0 | 0 | 0 | 5.56 | 0.00 | +5.56 |
| basin | 1 | 0 | 1 | 0 | 5.56 | 10.53 | −4.97 |
| friction | 1 | 0 | 0 | 0 | 5.56 | 0.00 | +5.56 |
| lake | 1 | 0 | 1 | 0 | 5.56 | 10.53 | −4.97 |
| currents | 0 | 2 | 0 | 0 | 11.11 | 0.00 | +11.11 |
| watershed | 0 | 0 | 2 | 0 | 0.00 | 21.05 | −21.05 |
| estuaries | 0 | 0 | 0 | 2 | 0.00 | 21.05 | −21.05 |

Every positive row has A document spread **1/2**. This flags a weak basis for generalization. `basin` and `lake` occur once per set but have negative deltas because the denominators differ. The table exposes rather than hides this normalization effect. Common topic labels dominate; single occurrences of `crest`, `horizon` and `friction` tie numerically. Choosing among them requires contextual and editorial judgment. None is established as a rare English word by this comparison.

## Context and sense verification

Opened separately on 2026-11-10, after corpus reading/counting. These dictionary pages are **verification sources only**, excluded from corpus denominators. English-facing pronunciation in the skill is proposed, not a listening test. Initial capitalization is presentation, with no deleted or added lexical units.

| Fixture source | Exact opened locator | Supported claim / lineage boundary |
|---|---|---|
| S05 | [Collins, crest](https://www.collinsdictionary.com/dictionary/english/crest), COBUILD sense 1, extracted lines 224–226 | Top of a hill or wave. Supports B01-C01's lexical sense, not calmness or performance. D1 occurrence is the wave-creation paragraph. |
| S06 | [Collins, horizon](https://www.collinsdictionary.com/dictionary/english/horizon), COBUILD sense 1, lines 36–38 | Apparent distant meeting line of sky and land/sea. D1 occurrence is in the first paragraph's view from beach/boat. B01-C02's planning association is editorial; no claim that this sense means planning. |
| S07 | [Collins, surface](https://www.collinsdictionary.com/dictionary/english/surface), COBUILD sense 1, lines 224–226 | Top/outside of something. D1's three occurrences are in its second included paragraph. B01-C03's workspace association is editorial. |
| S08, supplementary | [Collins, basin](https://www.collinsdictionary.com/dictionary/english/basin), COBUILD senses 3–4, lines 60–69; Webster's New World sense 7, lines 157–159 | Confirms distinct drainage and ocean-depression contexts; counting one spelling does not merge its senses into a single claim. Not a promoted candidate. |
| S09, opened but unused | [NWS Glasgow Glossary C](https://www.weather.gov/ggw/GlossaryC), opening extraction through early C entries | Opened as a possible crest reference, but no crest definition was inspected there. No lexical claim rests on this route; S05 supplied the relevant sense. |

S01 supports the occurrence of `friction` and its context between wind and surface water. No additional dictionary definition, etymology or pronunciation verification is claimed for B01-C04. Its spelling is attested; evidence is verified only for that occurrence/context. Calling it “effortless” would be unsupported. Hazard implications of the rip-current source also explain why a high concentration of current-related language is not automatically desirable for the synthetic calm brief.

## Audit boundary and fallback

Checked: opened exact documents; reconstructed four spans; computed 127/53/52/43 denominators and 13 table rows; verified three promoted senses; kept negative rows and the rejected positive case. No general corpus, paid tool, historical dictionary survey, consumer response, legal clearance or independent reader trial was used. The skill remains draft.

When a source fails, record unavailable/insufficient status, try one accessible counterpart, and define a new manifest if the collection changes. If only passage reading is feasible, label the output **qualitative manual comparison**: source-located observations with no frequency claims or artificial scores. If the source is unavailable altogether, leave its vocabulary as unverified leads. Neither silence in a sample nor silence in an archive establishes global rarity, historical nonexistence or obsolescence.
