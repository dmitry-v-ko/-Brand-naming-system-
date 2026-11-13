# Use Brand Naming System in Claude Code, Codex and Pi

Keep the complete source folder: `SKILL.md` routes to `AGENTS.md`, the catalog, method files and session templates. Git is the distribution; the library has no package installation, build or required archive. Your client still needs its own model access. Web research and delegation depend on the tools available in that session.

## Open a checkout

Screening includes an optional Python 3 [coverage validator](../checks/name-screening/COVERAGE.md); [session checks](../checks/session/README.md) also validate current state, bounded refinement and report language metadata/script. Both use only the standard library. Without Python, the agent performs and labels the same checks manually. Live registry access still depends on the host's research/browser tools; validators check recorded evidence, not websites or legal availability.

```bash
git clone https://github.com/dmitry-v-ko/-Brand-naming-system-.git brand-naming
cd brand-naming
```

Start your local client here: `claude`, `codex`, or `pi --skill ./SKILL.md`. Alternatively open this folder as a project in Codex Desktop or Claude Code Desktop. For Claude Code or Codex, send:

```text
Read AGENTS.md in this repository and use Brand Naming System.
I want to name a ready-made dinner delivery service. I do not know where to start.
```

Use your own language and idea in the second sentence. For Pi, invoke `/skill:brand-naming` with your idea after starting it as shown below. `AGENTS.md` is the shared conductor; `CLAUDE.md` imports it for Claude Code. No separate Pi adapter is needed.

## Claude Code

For use across projects, with Git and Claude Code already installed:

```bash
mkdir -p "$HOME/.claude/skills"
git clone https://github.com/dmitry-v-ko/-Brand-naming-system-.git "$HOME/.claude/skills/brand-naming"
```

Start a new local Claude Code session in your working project, then enter `/brand-naming` followed by your brief. A plain checkout uses `CLAUDE.md`; it does not register that personal slash command by itself. Keep the full folder, including references. See the official [skills guide](https://code.claude.com/docs/en/skills) and [memory imports](https://code.claude.com/docs/en/memory).

## Codex

The checkout route above works through `AGENTS.md` and the explicit starter prompt; no slash command is required. The [README](../README.md#quick-start) gives the expected first response; its [shortlist guide](../README.md#from-promising-name-to-informed-choice) explains how to find saved names.

For a personal skill available across projects:

```bash
mkdir -p "$HOME/.agents/skills"
git clone https://github.com/dmitry-v-ko/-Brand-naming-system-.git "$HOME/.agents/skills/brand-naming"
```

Start a new session and ask Codex to use `brand-naming` for your brief. Follow the official [local skill locations](https://learn.chatgpt.com/docs/build-skills) and [AGENTS.md discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md). Do not install a second copy at the same scope/name if one already exists.

## Pi

From this checkout, load the entry file explicitly:

```bash
pi --skill ./SKILL.md
```

Then enter:

```text
/skill:brand-naming I want to name a ready-made dinner delivery service. I do not know where to start.
```

From another working folder, use `pi --skill /absolute/path/to/brand-naming/SKILL.md`. Keep all referenced files beside that entry point. Pi can also discover skill folders in `~/.pi/agent/skills/` and the shared `~/.agents/skills/` location; a whole clone named `brand-naming` can live there. An existing shared Codex installation can serve Pi too. Use one discovery route per installation to avoid name collisions.

Stock Pi does not include subagents. The conductor offers a focused or broad comparison **one direction at a time in the same chat**, disclosing sequential execution before the choice. It records the same coverage without inventing worker launches. If a session actually exposes a delegation extension, the ordinary worker contract can be used. No extension installation is required. Web lookup is separate: without a working research tool, source claims stay unverified and the agent can offer a query plan or a sound/word-construction route.

See Pi's official [skill loading and commands](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/skills.md) and [capability scope](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/README.md).

## Claude web and Projects

Claude in a browser does not gain access to your checkout from these commands. This guide does not install a Claude web custom skill or claim that a repository URL loads the library.

For a manual document-only workflow, create a Claude Project, paste `AGENTS.md` into its instructions, and upload the catalog, session/source contracts and the method files you need. Rename repeated `SKILL.md` filenames to their method names, include referenced child/evidence documents, and tell Claude to interpret paths as document labels. Missing material must be requested rather than invented. Keep state in chat and request Markdown exports unless the conversation supports actual file writes. This is manual setup, not automatic synchronization; see [Claude Projects documentation](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects).

## Check, save and update

An incomplete brief should get a few relevant questions with examples; enough detail should lead to two or three contrasting names, reasons, drawbacks and a recommendation. The agent offers a focused or broader search in everyday language. Conversation language and customer-copy language are separate. A praise-only response must leave the shortlist unchanged; explicitly selected names must appear in it.

Session files belong outside the library, usually in your working space or a sibling `naming-sessions/<session-id>/`. Ask for the shortlist link/path. If the client's sandbox blocks the chosen location, choose a permitted workspace or use an in-chat Markdown export; do not claim an unsuccessful write was saved.

For an existing Git installation, run `git -C /path/to/brand-naming pull --ff-only`, then start a fresh client session (Pi also offers `/reload`). Inspect an existing destination before cloning; do not overwrite another installation. Older non-Git copies need deliberate replacement with a full checkout.

Instructions are checked against official documentation and installed client interfaces. A successful file/skill-loading check does not prove an authenticated model session, web research, native-speaker suitability or naming availability in every client.
