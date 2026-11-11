<div align="center">

# Brand Naming System

**Find a name worth building a brand around.**

Turn your AI agent into a naming partner — with 18 creative methods, unexpected word discoveries, and a shortlist you control.

[![Methods: 18](https://img.shields.io/badge/methods-18-345A49?style=flat-square)](docs/METHOD_CATALOG.md)
[![Format: Markdown](https://img.shields.io/badge/format-Markdown-3B5268?style=flat-square)](SKILL.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-8A633C?style=flat-square)](LICENSE)

[**Start naming →**](#quick-start) · [**Explore all 18 methods**](#all-18-naming-methods) · [**See examples**](examples/METHOD_SHOWCASE.md)

For **Claude Code, Codex and Pi** · Open source · No library build or package install

</div>

## Your next brand starts with a better search

Naming a startup, product or service? Start with your idea. Brand Naming System guides your AI agent from a rough brief through contrasting creative directions to names you can compare, refine and shortlist.

Discover a word in old navigation. Borrow a construction from literature. Build a new name around its sound. Follow the direction that feels right — and keep the others for later.

- **Explore different ways to name the same idea.** Compare three suitable methods or run all 18 with dedicated subagents.
- **Understand each candidate.** See why it fits, how it was formed, and where pronunciation, meaning or associations may let it down.
- **Find vocabulary beyond your industry.** Explore worlds such as bookbinding, sailing, cloud forms and historical language, with sources for researched meanings.
- **Keep creative control.** Deepen a promising branch, combine methods, revisit earlier ideas and save only the names you explicitly choose.
- **Know what still needs checking.** Preliminary screening separates market findings, possible conflicts and gaps in the evidence.

Speak in your own language; create **English-language brand names**. You do not need to know naming terminology to begin.

## Quick start

With Git and your preferred local AI client installed:

```bash
git clone https://github.com/dmitry-v-ko/-Brand-naming-system-.git brand-naming
cd brand-naming
```

Open this folder in **Codex or Claude Code**, then send:

```text
Read AGENTS.md in this repository and use Brand Naming System.
I want to name a ready-made dinner delivery service. I do not know where to start.
```

Replace the second sentence with your idea, in any language. The agent introduces all 18 methods, asks any necessary brief questions, then offers a few contrasting names with reasons, drawbacks and a recommendation. Let it choose the methods or request your own.

**Using Pi?** Run `pi --skill ./SKILL.md` from the checkout, then enter `/skill:brand-naming` followed by your brief.

**Want it available across projects?** Follow the [installation guide](docs/INSTALL.md) for personal skill setup, updates and the separate manual Claude browser workflow. Keep the complete repository folder: the entry point loads the methods and supporting documents. Your client supplies model access; research and parallel work depend on its available tools.

## Choose how far to explore

| Mode | Ask for | What happens |
|---|---|---|
| **Focused: 3 methods** | “Use three suitable methods and compare the strongest names.” | Three methods address the same brief from different angles. |
| **Broad: all 18** | “Run all 18 methods, one subagent per method.” | Each method gets a dedicated worker and the same brief; the conductor brings the results together for comparison. |
| **Go deeper** | “Explore sailing, weaving and watchmaking.” | Develop selected word worlds, with one worker per world when parallel execution is available. |

Limited concurrency queues the workers. Hosts without subagents, including stock Pi, offer a clearly stated sequential alternative. Broader exploration uses more time and model work; it does not guarantee a better name.

You can keep developing a direction without choosing another mode. Names are assessed for their form and product fit before their origin stories; promising candidates are compared in the same customer context.

## All 18 naming methods

Each method includes a step-by-step procedure, worked examples, comparison criteria and ways to recover when a direction runs thin.

| # | Method | Creative move |
|---|---|---|
| 1 | [Whole-word compounding](skills/intact-word-compounding/SKILL.md) | Join complete words into a new idea: **open + bench → Open Bench**. |
| 2 | [Fragment blending](skills/fragment-blending/SKILL.md) | Cut two words and join their meaning-bearing fragments. |
| 3 | [Overlap telescoping](skills/overlap-telescoping/SKILL.md) | Fuse words through a shared ending and beginning, using the overlap once. |
| 4 | [Clipping](skills/clipping/SKILL.md) | Shorten one word by removing its beginning or ending. |
| 5 | [Prefix attachment](skills/prefix-attachment/SKILL.md) | Add a prefix to change a stem's stance or meaning. |
| 6 | [Suffix attachment](skills/suffix-attachment/SKILL.md) | Add an ending to shape a stem's role, character or rhythm. |
| 7 | [Syllable recombination](skills/syllable-recombination/SKILL.md) | Arrange a bank of spoken syllables into new words. |
| 8 | [Phonetic invention](skills/phonetic-invention/SKILL.md) | Build a name from sounds, syllable structure and stress. |
| 9 | [Lexical research](skills/lexical-research/SKILL.md) | Find existing words whose supported meanings fit the brief. |
| 10 | [Cross-language mining](skills/cross-language-mining/SKILL.md) | Explore other languages, verify meanings and assess English adaptation. |
| 11 | [Metaphor mining](skills/metaphor-mining/SKILL.md) | Turn the brand promise into an image from another domain. |
| 12 | [Historical lexical archaeology](skills/historical-lexical-archaeology/SKILL.md) | Recover words through dated senses, spellings and historical context. |
| 13 | [Etymological archaeology](skills/etymological-archaeology/SKILL.md) | Follow documented word histories to meaningful naming ingredients. |
| 14 | [Literary word formation](skills/literary-word-formation/SKILL.md) | Study how writers construct words, then apply the pattern to new material. |
| 15 | [Corpus contrast](skills/corpus-contrast/SKILL.md) | Compare two text collections to uncover distinctive vocabulary. |
| 16 | [Onomatopoeic naming](skills/onomatopoeic-naming/SKILL.md) | Translate a sound event into a spoken name. |
| 17 | [Reduplication](skills/reduplication/SKILL.md) | Repeat or echo a unit to create rhythm and character. |
| 18 | [Respelling](skills/respelling/SKILL.md) | Change a word's spelling while keeping its intended pronunciation. |

Methods can work together: discover a word, shorten it, then compare it with an independently invented sound. [The operational catalog](docs/METHOD_CATALOG.md) explains where each technique fits and how neighboring methods differ. [Word worlds](lexical-universes/UNIVERSES.md) supply fresh material without changing the method.

## See the creative range

| Direction | Illustrative name | Why explore it — and what to question |
|---|---|---|
| A welcoming maker space | **Open Bench** · compounding | Familiar words suggest an accessible place to work; “bench” may imply a physical workshop. |
| An evening writing room | **Gloaming** · historical discovery | An attested twilight word creates atmosphere; a “gloom” association may work against warmth. |
| A precise, welcoming product | **Telo** · phonetic invention | Two open syllables offer a compact sound; an abstract form needs context to carry meaning. |

These are illustrative briefs and candidates, not cleared brand recommendations. [See their exact origins, transformations and drawbacks →](examples/METHOD_SHOWCASE.md)

## From promising name to informed choice

Ask to deepen a direction, compare favorites or check a candidate at any stage. The agent preserves explored branches and records a name in your shortlist only when you explicitly select it.

Before a development recommendation, it takes a bounded look at relevant market neighbors. Before a final recommendation, it runs [preliminary screening](checks/name-screening/SKILL.md) covering language, brief fit, market context and scoped trademark searches where tools permit. You choose the [occupancy boundary](checks/name-screening/RISK_BOUNDARY.md): soft coexistence, balanced independent brand, or strict high uniqueness. An existing use or taken domain is assessed in that context.

Session notes and `SHORTLIST.md` live outside the public library. Ask **“Show my shortlist and its file location”** to find them, or request a Markdown export when file writing is unavailable.

## Open methods. Visible limits.

All **18 procedures are fully written drafts**, with public [review history and live trials](docs/reviews/README.md). Trials cover both search modes, deeper word exploration and an equal-budget refinement comparison; they do not establish commercial naming success. Researched words, adaptations and inventions remain distinguishable, and missing evidence stays visible.

Preliminary screening is not legal clearance. Audience response, native-speaker suitability and registration decisions need their own validation.

**Explore the system:** [Installation and troubleshooting](docs/INSTALL.md) · [Examples](examples/METHOD_SHOWCASE.md) · [Agent instructions](AGENTS.md) · [Research standards](docs/SOURCES_AND_RESEARCH.md)

**Help improve it:** [Contribute a method](docs/SKILL_SPEC.md) · [Report an issue](https://github.com/dmitry-v-ko/-Brand-naming-system-/issues) · Maintained by [Dmitry](https://github.com/dmitry-v-ko)

[MIT License](LICENSE)
