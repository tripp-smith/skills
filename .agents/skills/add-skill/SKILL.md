---
name: add-skill
description: Add or update a skill in this catalog so Cursor, Claude Code, Codex, Grok, Copilot, and Antigravity can load the same files. Use when creating a skill, adding an ecosystem plugin, editing SKILL.md under plugins/, or changing marketplace manifests in this repository.
license: MIT
---

# Add a skill

This catalog stores installable skills inside ecosystem plugins. Maintainers' skills stay in `.agents/skills/`. Read `AGENTS.md` if a path below is unfamiliar.

## Choose the destination

- The skill is for people who install one ecosystem: `plugins/<ecosystem>/skills/<skill-name>/`.
- The skill only helps work inside this repository: `.agents/skills/<skill-name>/`.
- The work is a new ecosystem, not a new skill: run `python3 scripts/new-plugin.py` as described in `CONTRIBUTING.md`, then add the plugin name to the tables in `README.md` and `plugins/README.md`.

Use an existing plugin when the skill belongs to writing, product, engineering, or media. Do not create a plugin for a single skill unless that skill starts a new ecosystem.

## Write the skill

Create a directory whose name is the skill id.

```text
<skill-name>/
  SKILL.md
  scripts/       # optional, executable, deterministic steps
  references/    # optional, read only when the task needs them
  assets/        # optional templates and static files
  agents/openai.yaml   # optional Codex listing metadata
```

`SKILL.md` starts with frontmatter:

```markdown
---
name: skill-name
description: What it does and when to use it. Include the phrases a user would actually say.
license: MIT
---
```

Rules that validators enforce:

- `name` matches the directory, is 1–64 characters, and uses lowercase letters, digits, and single hyphens.
- `description` is one non-empty line of at most 1024 characters. Say what the skill does and when to use it.
- Do not set `version` in the skill. Version lives on the plugin manifests.
- The skill name is unique across `plugins/*/skills/` and `.agents/skills/`.
- The body stays under 500 lines. Link a file in `references/` instead of pasting a long guide.

Do not put the skill in a category subdirectory. `skills/editing/line-notes/SKILL.md` will not be discovered.

## Codex listing metadata

Add `agents/openai.yaml` only when Codex needs a display name or a default prompt. Quote every string. Keep keys unquoted.

```yaml
interface:
  display_name: "Human title"
  short_description: "Twenty five to sixty four characters"
  default_prompt: "Use $skill-name to do the specific task."
```

`short_description` must be 25–64 characters when present. `default_prompt` must mention `$<skill-name>`. Omit `policy.allow_implicit_invocation` unless the skill must be explicit-only.

## Register it

For a plugin skill:

1. Add a row to `plugins/<ecosystem>/skills/README.md`. Delete the "None yet" row.
2. Add the skill name to a group in `skills.sh.json`. Add a group named for the ecosystem if needed.
3. Bump the patch version in all three manifests to the same value:
   - `plugins/<ecosystem>/plugin.json`
   - `plugins/<ecosystem>/.claude-plugin/plugin.json`
   - `plugins/<ecosystem>/.cursor-plugin/plugin.json`

Keep `name`, `description`, and `keywords` identical across those three files. On the root `plugin.json`, do not add `skills`, `mcpServers`, or `displayName`. Those fields violate the Agent Plugins schema. Codex display copy goes under `extensions.com.openai`.

A repository-local skill skips the plugin version bump. Still add its name to `skills.sh.json`.

## Finish

Run:

```bash
python3 scripts/validate-catalog.py
```

Fix every reported line before considering the skill added. Do not copy the skill into a second directory to satisfy another client. `.claude/skills` is already a symlink to `.agents/skills`, and installed plugins expose their own `skills/` tree.
