<div align="center">

# Brand Naming System

**Find a word worth building a brand around.**

18 detailed naming methods · unexpected lexical worlds · human-guided exploration

[![Methods: 18](https://img.shields.io/badge/methods-18-345A49?style=flat-square)](docs/METHOD_CATALOG.md)
[![Format: Markdown](https://img.shields.io/badge/format-Markdown-3B5268?style=flat-square)](SKILL.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-8A633C?style=flat-square)](LICENSE)

[**Use in Claude Code, Codex or Pi**](docs/INSTALL.md) · [**Explore the methods**](docs/METHOD_CATALOG.md) · [**See examples**](examples/METHOD_SHOWCASE.md)

</div>

---

A creative naming library for Claude Code, Codex, Pi and other file-reading agents. Discover an overlooked word, invent a new one, or follow an unexpected association. Explore the directions you like, revisit earlier branches, and build a shortlist with the origins intact.

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

## Start with a local client

The complete Git checkout is the distribution: no archive, package install or build is needed for this library. Install and sign in to your chosen client separately; its model access and research tools remain host requirements.

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

You can also open an ordinary checkout in Claude Code and ask for naming help; [CLAUDE.md](CLAUDE.md) imports the conductor. [Installation and updates →](docs/INSTALL.md#claude-code)

### Codex or another file-reading agent

Clone the repository if you do not already have a checkout:

```bash
git clone https://github.com/dmitry-v-ko/-Brand-naming-system-.git brand-naming
```

Open the local `brand-naming` folder as your Codex project and start a chat in that project. Paste this prompt; replace the dinner-service sentence with your idea in any language:

```text
Read AGENTS.md in this repository and use Brand Naming System.
I want to name a ready-made dinner delivery service. I do not know where to start.
```

This file-reading route needs no `/brand-naming` command, package installation or server. Expect a few relevant questions with examples when your brief is incomplete, then two or three contrasting names with reasons, drawbacks and a recommendation. The agent should respond in your language; customer-facing examples use the audience's language, which it will infer explicitly or clarify. If it gives a repository review instead, ask it to use AGENTS.md for an actual naming session.

The agent creates session records outside this library and gives you a link or resolved path to `SHORTLIST.md`. A typical location is a sibling `naming-sessions/<session-id>/SHORTLIST.md`; the exact writable location depends on the host. Only names you explicitly select are saved. Ask “Show my shortlist and its file location” to find it. Without file-writing tools, ask for a Markdown export in chat.

Claude Code users opening the checkout directly also get the shared conductor through [CLAUDE.md](CLAUDE.md).

### Pi

From the cloned `brand-naming` folder, run:

```bash
pi --skill ./SKILL.md
```

Then enter:

```text
/skill:brand-naming I want to name a ready-made dinner delivery service. I do not know where to start.
```

Pi reads the same conductor and methods. Stock Pi has no built-in subagents: wider exploration is offered sequentially in the same chat, with that limitation stated before you choose. Research depends on enabled tools; unavailable sources remain unverified. [Other skill-folder locations and client checks →](docs/INSTALL.md#pi)

### Claude in the browser

Claude web is a separate product from local Claude Code. These checkout commands do not give a browser chat access to your local files or install a web skill. A [manual Claude Projects workflow](docs/INSTALL.md#claude-web-and-projects) is available; this repository does not ship an upload archive.

## How exploration feels

1. **Describe the brand.** Offer, audience, character and what to avoid. The agent asks only questions that affect the creative direction.
2. **See a few contrasting names.** Receive short reasons, drawbacks and a recommendation, without a mandatory menu.
3. **Follow your curiosity.** Deepen a method, discover another source world, combine techniques, or return to a parked branch.
4. **Save your choices.** Only explicitly selected names enter the shortlist. Export when you are satisfied.

Before a final recommendation, the agent performs a [preliminary name check](checks/name-screening/SKILL.md): language and brief fit, relevant market context, and scoped trademark searches where tools permit. You can request a check at any stage. Unchecked creative previews and requested exports remain clearly labeled; incomplete coverage is never a claim that a name is available. A [tenant profile](templates/TENANT_PROFILE.md) can supply your own filters and stricter check order, loaded only when you explicitly select it.

For research, the agent proposes worlds such as bookbinding, cloud forms, old navigation, regional vocabulary and literary word formation. It distinguishes verified words from hypotheses and inventions. [Explore the universe cards →](lexical-universes/UNIVERSES.md)

Session records live in your working space, outside the library. If file writing is unavailable, use in-chat records and Markdown exports.

## Choose exploration breadth

After the brief, ask for **three different directions** for a focused comparison, or **a broad search** for more varied possibilities. The broader search takes longer and uses more work; it does not guarantee a stronger name. The agent selects the techniques and shows useful contrasts. You can also keep developing a direction you already like, without choosing a search mode.

Names are compared with the same plain category descriptor and use context in the intended customer language, even when you chat in another language. Actual audience feedback and native-speaker review remain distinct from agent predictions. Methods retain their draft status.

<details>
<summary>How the wider search works</summary>

The focused option uses three suitable methods; broad search covers all 18. Each assigned method gets a dedicated subagent and the same brief; limited concurrency queues workers. Hosts without subagents can offer an explicitly labeled sequential alternative. You can request particular methods or execution details. The [session contract](docs/SESSION_PROTOCOL.md#parallel-exploration-three-or-all-eighteen) defines coverage and comparison.

</details>

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

The collection contains **18 detailed draft methods**. The earlier Cycle 05 repository review scored **9.11/10** under its [documented rubric](docs/reviews/CYCLE_05_CRITIQUE.md); that is a bounded internal quality assessment, not evidence of commercial success or end-to-end acceptance of every method. The [live parallel-mode trial](docs/reviews/PARALLEL_LIVE_TRIAL.md) records newer execution evidence and scoped repairs without changing method maturity.

The library combines creative discovery and shortlisting with a separate preliminary screening stage. The eighteen generation methods are unchanged; screening is not a nineteenth generator or a legal opinion. Registration, filing, payments and domain purchases are outside scope. An unusual word, empty search page or completed limited search does not establish legal availability.

[MIT License](LICENSE) · [Project decisions](docs/context.md) · [Contributing a method](docs/SKILL_SPEC.md)
