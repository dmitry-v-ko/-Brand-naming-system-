# Use Brand Naming System with Claude

One entry-point skill gives Claude access to all eighteen methods. The method files are supporting instructions, not eighteen separately installed commands. Keep the full library folder; it contains the sources, navigation and session templates.

## Claude Code: install once

With Git and Claude Code already installed, run this in a macOS/Linux terminal:

```bash
mkdir -p "$HOME/.claude/skills"
git clone https://github.com/dmitry-v-ko/-Brand-naming-system-.git "$HOME/.claude/skills/brand-naming"
```

Start a new Claude Code session in your working project, then type:

```text
/brand-naming Name a calm, practical repair service for kitchen tools. Give me three contrasting directions. Speak in my language; names in English.
```

The skill is available across your local projects. It reads the conductor and selected method on demand. Keep session files in your working project or another writable session directory, outside the installed skill folder.

To update an existing Git installation:

```bash
git -C "$HOME/.claude/skills/brand-naming" pull --ff-only
```

If you already have a folder at that destination, inspect it before installing; `git clone` will not overwrite it. If you installed the ZIP instead, replace that installed copy deliberately rather than running `git pull` in it.

### Work directly in a checkout

You can also clone the repository anywhere and open that folder in Claude Code. Its [CLAUDE.md](../CLAUDE.md) imports the shared conductor. Ask for naming help in plain language. The `/brand-naming` command is supplied by the personal installation above; a plain checkout alone does not register that command.

## Claude in the browser: upload the skill

1. [Download brand-naming.zip](https://github.com/dmitry-v-ko/-Brand-naming-system-/raw/refs/heads/main/downloads/brand-naming.zip).
2. Enable file creation/code execution in Claude's capabilities if it is off.
3. Open **Customize → Skills**, choose **+ / Create skill → Upload a skill**, and upload the ZIP.
4. Enable **brand-naming**, then ask: “Use brand-naming to explore English names for my product. Start with three contrasting directions.”

The ZIP has one `brand-naming/` folder containing `SKILL.md` and its reference files. Do not upload only an individual method file. Research availability depends on the tools enabled in the conversation; unavailable sources must remain unverified. Skill controls can be restricted by an organization's settings.

## Claude Projects: document-only alternative

If you prefer project knowledge instead of a custom skill:

1. Create a Claude Project. Paste [AGENTS.md](../AGENTS.md) into its project instructions.
2. Add the [catalog](METHOD_CATALOG.md), [session contract](SESSION_PROTOCOL.md), [source contract](SOURCES_AND_RESEARCH.md), [universes](../lexical-universes/UNIVERSES.md), and the method files you intend to use to project knowledge.
3. Give uploaded method files distinct names, such as `fragment-blending.md`, so their repeated `SKILL.md` filenames are unambiguous. Include any child method and evidence document referenced by the selected procedure.
4. Tell Claude to interpret repository paths as document labels. If a needed file is absent, it should ask for that material or use an available method rather than invent its contents.

Without writable session files, keep the log and shortlist in chat and request Markdown exports. To resume elsewhere, provide the latest records; do not assume project knowledge automatically contains every decision from another chat. This alternative does not install a slash command.

## Check your setup

Ask Claude to identify the installed library, confirm eighteen active methods, and explain the difference between fragment blending and overlap telescoping. Then give a small brief: expect a few names with reasons and drawbacks. Source ledgers and exact transformations should be available on request, not dumped into the first reply. No real favorites should be saved until you select them.

## Reference and verification

Installation conventions were checked against these official pages on 2026-11-10:

- [Claude Code skills](https://code.claude.com/docs/en/skills): personal skill directories, supporting files and invocation.
- [Claude Code memory](https://code.claude.com/docs/en/memory): `CLAUDE.md` file imports.
- [Using skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude): capability settings and ZIP upload.
- [Creating custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills): metadata and archive structure.
- [Claude Projects](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects): project instructions and knowledge documents.

The packaged file layout, metadata and bundled references are checked locally. Upload, activation and actual generation in a signed-in Claude account have not been tested in this workspace; no Claude Code executable is installed here. The library needs no Python/API runtime; Claude's own capabilities and permissions remain host requirements.
