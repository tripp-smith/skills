# Contributing

Skills in this repository are portable Agent Skills packages. An ecosystem is a plugin. A skill is one directory inside that plugin. Client-specific files are manifests only.

## Add a skill to an existing ecosystem

1. Pick `plugins/writing`, `plugins/product`, `plugins/engineering`, `plugins/media`, or another plugin that already exists.
2. Create `plugins/<ecosystem>/skills/<skill-name>/`.
3. Add `SKILL.md`. The directory name and the frontmatter `name` match. Use lowercase letters, digits, and single hyphens.
4. Write `description` as one line that says what the skill does and when to use it. Do not add `version`.
5. Put commands the agent should run in `scripts/`, long reference in `references/`, and templates or other static files in `assets/`.
6. If Codex should show a custom title or example prompt, add `agents/openai.yaml`. Quote every string. A `default_prompt` must mention `$<skill-name>`.
7. Add the skill name to `plugins/<ecosystem>/skills/README.md`. Remove the "None yet" row if it is still there.
8. Add the skill name to a group in `skills.sh.json`. Create a group for the ecosystem if one does not exist yet.
9. Bump `version` in all three of these files, together, using the same semver:
   - `plugins/<ecosystem>/plugin.json`
   - `plugins/<ecosystem>/.claude-plugin/plugin.json`
   - `plugins/<ecosystem>/.cursor-plugin/plugin.json`
10. Run `python3 scripts/validate-catalog.py`.

Keep `SKILL.md` under 500 lines. Link supporting files by relative path from `SKILL.md`.

Names must be unique across the whole catalog. A skill installed from two plugins into `.agents/skills/` would collide.

## Add an ecosystem

```bash
python3 scripts/new-plugin.py <name> \
  --description "What this ecosystem is for." \
  --category "Productivity" \
  --keywords topic,topic
```

`<name>` becomes the plugin id and the directory under `plugins/`. Then add a row for it in `README.md` and `plugins/README.md`. The validator checks that both files mention the directory name.

Use `Developer Tools` or `Productivity` for `--category` unless a Codex category fits more tightly. The script registers the plugin in:

- `.claude-plugin/marketplace.json`
- `.cursor-plugin/marketplace.json`
- `.agents/plugins/marketplace.json`

Do not register `templates/plugin/`. It holds the skill skeleton only. The sample file is named `SKILL.md.template` so clients do not load it.

## MCP servers

Add MCP config only when the plugin calls a live server.

- `plugins/<ecosystem>/mcp.json` uses the Agent Plugins schema and `"type": "streamable-http"` for remote servers. Codex reads this file.
- `plugins/<ecosystem>/.mcp.json` is the Claude, Cursor, and Grok file. Cursor reads `.mcp.json` before `mcp.json`.

Do not commit secrets. Declare variable names in the Cursor manifest and use placeholders.

## Versioning

Plugin manifests carry the version. Skill frontmatter does not. A skill or manifest change bumps the patch version unless the change is a breaking replacement of a skill's behavior, in which case bump minor.

The three manifests for a plugin always carry the same `version`, `description`, and `keywords`.

## Local check

```bash
python3 scripts/validate-catalog.py
```

The validator checks marketplace membership, manifest lockstep, skill frontmatter, flat skill layout, unique skill names, the `.claude/skills` symlink, and `skills.sh.json` coverage.
