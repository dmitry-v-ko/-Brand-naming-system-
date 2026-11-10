<div align="center">

# Brand Naming System

**Find a word worth building a brand around.**

18 detailed naming methods · unexpected lexical worlds · human-guided exploration

[![Methods: 18](https://img.shields.io/badge/methods-18-345A49?style=flat-square)](docs/METHOD_CATALOG.md)
[![Format: Markdown](https://img.shields.io/badge/format-Markdown-3B5268?style=flat-square)](SKILL.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-8A633C?style=flat-square)](LICENSE)

[**Install in Claude**](docs/INSTALL_CLAUDE.md) · [**Explore the methods**](docs/METHOD_CATALOG.md) · [**See examples**](examples/METHOD_SHOWCASE.md)

</div>

---

A creative naming library for Claude, Codex and other research-enabled agents. Discover an overlooked word, invent a new one, or follow an unexpected association. Explore the directions you like, revisit earlier branches, and build a shortlist with the origins intact.

**Converse in any language. Create English-language names.** Start with a few useful options; ask for deeper research when a direction deserves it. Verified rare words can be used unchanged.

## A taste of the methods

| Approach | Example | What happens |
|---|---|---|
| [Whole-word compounding](skills/intact-word-compounding/SKILL.md) | **Open Bench** | Join two intact words: open + bench. |
| [Fragment blending](skills/fragment-blending/SKILL.md) | **Weavora** | Keep weav from weave and ora from agora; cut both inputs. |
| [Overlap telescoping](skills/overlap-telescoping/SKILL.md) | **Gleamber** | Share the am in gleam + amber once. |
| [Historical word discovery](skills/historical-lexical-archaeology/SKILL.md) | **Gloaming** | Recover a supported twilight sense; use the word unchanged. |
| [Phonetic invention](skills/phonetic-invention/SKILL.md) | **Telo** | Build a two-syllable sound shape without inventing an etymology. |
| [Respelling](skills/respelling/SKILL.md) | **Kove** | Change cove's initial letter while targeting the same pronunciation. |

Constructed names and briefs are illustrative, with no availability claim. Gloaming's lexical basis is recorded in the [historical evidence](docs/research/HISTORICAL_METHODS_EVIDENCE.md). [See the exact transformations, drawbacks and next steps →](examples/METHOD_SHOWCASE.md)

## Start in Claude

### Claude Code

With Git and Claude Code installed, run in a macOS/Linux terminal:

```bash
mkdir -p "$HOME/.claude/skills"
git clone https://github.com/dmitry-v-ko/-Brand-naming-system-.git "$HOME/.claude/skills/brand-naming"
```

Open a new Claude Code session in your working project and type:

```text
/brand-naming Name a calm, practical repair service for kitchen tools.
Start with three contrasting directions. Speak in my language; names in English.
```

One installed entry point routes to all eighteen reference methods. No library API key, package install or build is required.

### Claude in the browser

[**Download the Claude skill ZIP**](https://github.com/dmitry-v-ko/-Brand-naming-system-/raw/refs/heads/main/downloads/brand-naming.zip), then open **Customize → Skills → Create skill → Upload a skill**, upload it and enable **brand-naming**. Claude's file-creation capability must be enabled.

[Full installation guide, updates and Claude Projects alternative →](docs/INSTALL_CLAUDE.md)

### Codex or another file-reading agent

Clone/open the repository and have the agent read [AGENTS.md](AGENTS.md). Describe what needs naming. Claude Code users opening the checkout directly also get the shared conductor through [CLAUDE.md](CLAUDE.md).

## How exploration feels

1. **Describe the brand.** Offer, audience, character and what to avoid. The agent asks only questions that affect the creative direction.
2. **See a few contrasting names.** Receive short reasons, drawbacks and a recommendation, without a mandatory menu.
3. **Follow your curiosity.** Deepen a method, discover another source world, combine techniques, or return to a parked branch.
4. **Save your choices.** Only explicitly selected names enter the shortlist. Export when you are satisfied.

For research, the agent proposes worlds such as bookbinding, cloud forms, old navigation, regional vocabulary and literary word formation. It distinguishes verified words from hypotheses and inventions. [Explore the universe cards →](lexical-universes/UNIVERSES.md)

Session records live in your working space, outside the library. If file writing is unavailable, use in-chat records and Markdown exports.

## Choose exploration breadth

After the brief, choose **three suitable methods** for a focused comparison or **all 18 methods** for a broad sweep. Each assigned method gets its own subagent and the same brief; the conductor combines results and shows useful contrasts. Limited concurrency runs the workers in a queue. Hosts without subagents can offer an explicitly labeled sequential alternative. You can also continue exploring one direction.

Names are compared with the same plain category descriptor and use context. Actual audience feedback and native-speaker review remain distinct from agent predictions. Broader exploration does not guarantee better names; methods retain their draft status.

## Inside the library

<details>
<summary><strong>Browse all 18 methods by family</strong></summary>

| Family | Methods |
|---|---|
| Word construction | [Compounding](skills/intact-word-compounding/SKILL.md), [fragment blending](skills/fragment-blending/SKILL.md), [overlap](skills/overlap-telescoping/SKILL.md), [clipping](skills/clipping/SKILL.md), [prefixes](skills/prefix-attachment/SKILL.md), [suffixes](skills/suffix-attachment/SKILL.md) |
| Sound | [Phonetic invention](skills/phonetic-invention/SKILL.md), [syllable recombination](skills/syllable-recombination/SKILL.md), [onomatopoeia](skills/onomatopoeic-naming/SKILL.md), [reduplication](skills/reduplication/SKILL.md) |
| Word discovery | [Lexical research](skills/lexical-research/SKILL.md), [cross-language search](skills/cross-language-mining/SKILL.md), [historical vocabulary](skills/historical-lexical-archaeology/SKILL.md), [etymology](skills/etymological-archaeology/SKILL.md), [corpus contrast](skills/corpus-contrast/SKILL.md) |
| Meaning and patterns | [Metaphor](skills/metaphor-mining/SKILL.md), [literary word formation](skills/literary-word-formation/SKILL.md) |
| Writing | [Respelling](skills/respelling/SKILL.md) |

Each procedure includes its mechanism, research strategy, intermediate artifacts, worked examples, weak-result recovery, assessment and ways to combine it with other methods. Source worlds are separate from methods; changing a genre or field does not add another technique.

</details>

| Read this | For this |
|---|---|
| [Method showcase](examples/METHOD_SHOWCASE.md) | Understand six operations through brief examples. |
| [Operational catalog](docs/METHOD_CATALOG.md) | Choose a method and distinguish neighboring techniques. |
| [Conductor](AGENTS.md) | Guide a nonlinear, user-directed naming session. |
| [Session templates](templates/EXPLORATION_LOG.md) · [Shortlist](templates/SHORTLIST.md) | Resume branches and keep explicit favorites. |
| [Source contract](docs/SOURCES_AND_RESEARCH.md) · [Research evidence](docs/research/EXPANSION_EVIDENCE.md) | Trace meanings, transformations and uncertainty. |
| [Review history](docs/reviews/README.md) | Inspect independent critiques, execution trials and remaining limits. |

## Status and scope

The collection contains **18 detailed draft methods**. The latest independent repository review scored **9.11/10** under its [documented rubric](docs/reviews/CYCLE_05_CRITIQUE.md); that is a bounded internal quality assessment, not evidence of commercial success or end-to-end acceptance of every method. The Claude adapter changes distribution, not method maturity.

The focus is creative discovery, invention and shortlisting. Trademark, patent, domain, registration and other clearance checks belong to a separate workflow. An unusual word or spelling does not establish availability.

[MIT License](LICENSE) · [Project decisions](docs/context.md) · [Contributing a method](docs/SKILL_SPEC.md)
