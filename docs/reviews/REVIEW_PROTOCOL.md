# Independent improvement cycle

The owner requested repeated independent criticism and repository improvement until the overall score reaches at least 9/10. Each critic starts with a fresh context and inspects the actual repository. A separate improvement agent receives the critique and implements changes before a new critic reviews the resulting files.

## Fixed scoring rubric

Use the same weighted dimensions in every cycle. Score each dimension from 1 to 10 and compute the weighted mean, retaining two decimals. Do not round a score below 9 up to meet the stopping condition.

| Dimension | Weight | Evidence |
|---|---:|---|
| Operational depth | 35% | Independently executable, narrow procedures; intermediate artifacts; worked transformations; recovery rules |
| Coverage and distinctness | 20% | Useful range of creative routes, separate narrow operators, explicit boundaries, no domain-only inflation |
| Agent usability and state | 20% | Discoverable instructions, efficient research and interaction, portable session memory, navigation and consent |
| Provenance and honesty | 15% | Traceable sources, accurate form/evidence labels, honest maturity, no fabricated access or clearance |
| Demonstrated creative outcomes | 10% | Inspectable worked runs, varied candidates, concrete selection and feedback, scenario validation |

There is no method-count quota. Assess coverage against the accepted project scope, not a requirement for 50 methods. Do not require software, consumer studies, or clearance. Do not treat name categories or source universes as independent operators without a distinct procedure.

## Review output

Each `CYCLE_NN_CRITIQUE.md` records dimension scores, weighted result, evidence paths, blocking defects, prioritized changes, and concrete acceptance checks. Each improvement response records what changed, checks performed, and remaining gaps. Preserve earlier reports as historical snapshots; do not rewrite their scores after changes.

Ready status requires actual acceptance evidence. At 9/10 or above, stop only if no unresolved critical defect contradicts the score; report remaining limitations. This is a repository-quality review, not proof of commercial naming success.
