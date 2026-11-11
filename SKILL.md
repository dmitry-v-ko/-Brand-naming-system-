---
name: brand-naming
description: Explore and shortlist English brand names using 18 creative methods, unexpected word worlds and source research. Use for naming a brand, product, company or service.
---

# Brand Naming System

Use this library to help the user discover, construct, refine and select English-language brand names. Converse in the user's language; resolve customer-facing language separately from the audience brief under the [language contract](docs/SESSION_PROTOCOL.md#conversation-and-customer-languages). This is one entry-point skill with eighteen reference methods, not a nineteenth naming method.

## Load only what is needed

Resolve the library root as the directory containing this `SKILL.md`, not the current working directory. All paths below are relative to that root. Keep the whole folder when installing; copying this file alone omits the methods and source records.

Use the host's actual tools. Some clients, including stock Pi, do not provide subagents or web research. Follow the session contract's disclosed sequential fallback when workers are unavailable; unresolved source claims stay unverified. See [client setup](docs/INSTALL.md).

1. Read [AGENTS.md](AGENTS.md) for the conductor and [the method catalog](docs/METHOD_CATALOG.md) for available operations.
2. Read [the session contract](docs/SESSION_PROTOCOL.md) and [source contract](docs/SOURCES_AND_RESEARCH.md) before persisting state or making research claims.
3. Read the selected `skills/<method-id>/SKILL.md` before executing it. For combinations, read the child method and preserve its exact rules. Do not load all eighteen procedures into every conversation.
4. Use [lexical universes](lexical-universes/UNIVERSES.md) to propose source worlds. For examples, see [the showcase](examples/METHOD_SHOWCASE.md); examples are not the current user's preferences or verified new research.

## Start with useful names

If the brief is sufficient, begin with 2–3 contrasting directions or names, short reasons, concrete drawbacks and a recommendation. Ask only questions that materially change the creative direction. Offer broader menus and detailed research when useful or requested. An agent's provisional choice is not user delegation.

Research-enabled methods require actual accessible sources. Separate attested words, adapted forms and inventions from the evidence supporting their ingredients. Preserve citations and uncertainty internally; show a concise source story by default. A verified rare word may be used unchanged. Do not invent etymologies, historic attestations, author intent, audio observations or audience responses.

For expanded exploration, offer a focused comparison of three different directions or a broader search, explaining the result and relative effort in everyday language. The [parallel exploration contract](docs/SESSION_PROTOCOL.md#parallel-exploration-three-or-all-eighteen) owns the internal method/worker mapping, host fallback and central reconciliation; expose technical details on request.

## Keep the user in control

Deepen, switch worlds, combine methods, revisit parked branches or stop when asked. Save only explicitly selected names; praise alone is not consent. Keep exact spelling and comments, and never remove a favorite without approval.

Session files belong in the active user's writable workspace **outside this installed library**. Choose a session location appropriate to the host, then use the [exploration](templates/EXPLORATION_LOG.md) and [shortlist](templates/SHORTLIST.md) templates. On resume, read existing records without overwriting them. If persistent writing is unavailable, maintain equivalent in-chat records and offer Markdown exports without claiming files were saved. Do not assume another chat has this session's history.

All eighteen generation methods retain their documented maturity. Read and run [preliminary name screening](checks/name-screening/SKILL.md) before a final recommendation or on a direct check request. This auxiliary stage is not another generation method or legal approval. Label unchecked previews and requested unchecked exports; preserve check status and scope beside each name. Load real tenant profiles only by explicit selection and keep them outside the library. Filing, registration, domain purchases and payments are excluded.

## Focused deepening and name quality

An explicit request for several source worlds uses one worker per world with the same selected method, not the default three-method comparison. Follow the [assignment-axis contract](docs/SESSION_PROTOCOL.md#assignment-axis). Assess name form and shared product context before explaining the source story; when useful source words make weak names, use the [one bounded adaptation pass](docs/SESSION_PROTOCOL.md#one-bounded-adaptation-pass). These are orchestration rules, not new methods or audience validation.
