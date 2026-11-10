# Brand Naming Skills — Creative Research Library

A portable, English-language instruction library for research-enabled LLM agents creating **English brand names** while conversing with users in **any language**.

## Status

**Starter scaffold, not a completed 50-skill collection.** This release contains 5 draft skills and an indexed roadmap of 53 candidate entries requiring a distinctness audit. The other 48 entries are research and authoring targets. None of the five drafts has passed the revised acceptance standard yet.

## Quick start

1. Give an LLM agent access to this repository and its `AGENTS.md` instructions (or paste `AGENTS.md` into its project/system instructions).
2. Tell it what needs naming, in any language.
3. The agent builds a concise brief, suggests distinct creative paths, and asks which path to explore.
4. Work recursively: select a method, select a lexical universe, research sources, explore candidates, dig deeper, switch universe, or return to methods.
5. The agent updates session-owned `EXPLORATION_LOG.md` and `SHORTLIST.md` separately from this repository, where file tools are available.
6. The user decides when to stop; export `SHORTLIST.md` for later work.

## Repository map

- `AGENTS.md` — session conductor / master instructions
- `skills/*/SKILL.md` — five draft creative research skills
- `docs/METHOD_CATALOG.md` — 53-method roadmap and maturity labels
- `docs/SKILL_SPEC.md` — required skill authoring standard
- `lexical-universes/UNIVERSES.md` — reusable research territories to propose to the user
- `templates/EXPLORATION_LOG.md` and `templates/SHORTLIST.md` — **templates only**; real files live in the user's session/workspace
- `examples/DEMO.md` — fictional user flow illustrating state transitions

## Scope and safety

- In scope: discovery, invention, creative adaptation, source citations, preferences, shortlist curation.
- Out of scope: trademark clearance, patent analysis, domain availability, legal opinions and assertions of uniqueness.
- Never represent fictional, invented, or unverified words as attested dictionary terms. Distinguish direct citations/attested lexical items from adaptations and inventions.
- Do not reproduce lengthy passages from copyrighted books; extract only brief terms and cite bibliographic details when available.
- Cultural context matters: do not present sacred, restricted or culturally sensitive terms as neutral brand assets.

## Portability

The library is plain Markdown. An agent needs file-reading and preferably web research capabilities. With no file-write capability, it can maintain the two session documents inline and offer exports. Tools are optional, not assumed.

## Development status

See [project context](docs/context.md), [implementation milestone](docs/IMPLEMENTATION_PLAN.md), and [session state contract](docs/SESSION_PROTOCOL.md). This is a Markdown-only library; no runtime or API dependency is required.
