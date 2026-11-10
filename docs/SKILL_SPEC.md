# Skill authoring specification

Each ready skill should live at `skills/<slug>/SKILL.md` and include:

1. `id`, `family`, `status: ready`, `requires: research-optional/research-recommended`, `outputs`.
2. **Purpose** — the distinct generative mechanism, not merely a new source list.
3. **When to use / avoid** — creative positioning and failure cases.
4. **Inputs** — brief plus method-specific optional constraints; the agent must infer defaults.
5. **Procedure** — stages with concrete quantities, branching logic, candidate transformations, and stopping guidance.
6. **Research plan** — sources, queries, provenance and fallback if the agent cannot browse.
7. **Interaction loop** — what semi-developed options to show before deep diving; when to seek user approval.
8. **Output contract** — English candidate, pronunciation cue, lineage, invented/attested tag, short creative rationale.
9. **Variations** — ways to go deeper or hybridize with other skills.
10. **Failure modes** — hallucinations, stale resources, cliches, cultural misuse and overly similar options.
11. **Example run** — illustrative outputs clearly labeled as synthetic if not verified.

Avoid pseudo-distinct skills that simply swap one source domain for another; use `lexical-universes/UNIVERSES.md` for source domain examples.

A method is distinct if its *transformation, search or selection algorithm* materially changes; a source universe is a parameter to a method when only its corpus changes.

## Acceptance gates

Use `draft` until every gate passes; file existence does not establish readiness.

- Identify the closest neighboring method and demonstrate a materially different operator or research decision. A changed corpus alone fails.
- State intended outcome, method-specific use and avoidance conditions, required and optional inputs, and defaults.
- Provide reproducible extraction, transformation, diversification, and stopping rules. Quantities are defaults, not mandatory user-facing quotas.
- Give source classes, example queries, verification steps, and unavailable-source behavior.
- Show a complete worked run from a small brief through intermediate material to contrasting candidates. Label synthetic examples and unverified claims.
- Provide method-specific assessment criteria and demonstrate recovery from a weak result. Generic warnings alone fail.
- Name useful method combinations and their execution order, keeping contributions traceable.
- Follow `SESSION_PROTOCOL.md`, separating form from evidence and tracking sources and pronunciation where useful.
- Demonstrate a feedback turn, navigation choice, and correct memory behavior.

Record review evidence and unresolved gaps before changing `draft` to `ready`. Acceptance concerns operational usability, not uniqueness or legal clearance.
