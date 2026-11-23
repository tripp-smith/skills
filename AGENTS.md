# Skills catalog

This repository distributes specialized skills as plugins. One skill directory is the source of truth. Client manifests point at that directory; they do not carry a second copy of the instructions.

## Where things go

- A new ecosystem is `plugins/<name>/`, registered in all three marketplace files.
- A skill other people install is `plugins/<ecosystem>/skills/<skill-name>/SKILL.md`.
- A skill that only helps maintain this repository is `.agents/skills/<skill-name>/SKILL.md`.
- Do not put installable skills in `.agents/skills/`. That path loads on every session in this checkout.
- Do not nest categories under `skills/`. Discovery is `skills/<skill-name>/SKILL.md` only.
- Do not add `.codex-plugin/plugin.json`. Codex reads the root `plugin.json`. A second manifest can disagree with it.
- Do not add an empty `mcp.json` or `.mcp.json`. Add those only when a plugin actually ships an MCP server.

## Manifests that must stay in lockstep

For each plugin, these three files share `name`, `version`, `description`, and `keywords`:

| File | Clients |
| --- | --- |
| `plugin.json` | Codex, Grok, and other Agent Plugins clients |
| `.claude-plugin/plugin.json` | Claude Code |
| `.cursor-plugin/plugin.json` | Cursor |

The Agent Plugins file uses the closed schema at `https://agent-plugins.org/schemas/1.0.0/plugin.schema.json`. Skills always come from `skills/`. Do not add a `skills` or `mcpServers` field there. Codex-specific presentation goes under `extensions.com.openai`.

Bump `version` in all three files together when the plugin's skills or manifests change. Skill files do not get a `version` frontmatter field. Anthropic and OpenAI skill validators reject it.

## Marketplaces

| File | Entry source |
| --- | --- |
| `.claude-plugin/marketplace.json` | `"./plugins/<name>"` |
| `.cursor-plugin/marketplace.json` | `"./plugins/<name>"` |
| `.agents/plugins/marketplace.json` | `{ "source": "local", "path": "./plugins/<name>" }` |

Plugin names match the directory name. Marketplace name is `tripp-smith-skills`.

Cursor tries `.cursor-plugin/plugin.json` first and stops on the first manifest that parses, so the Cursor manifest has to exist even though it repeats the Claude manifest. Grok prefers root `plugin.json` and still understands Claude's marketplace.

## Skill shape

```text
skills/<skill-name>/
  SKILL.md
  scripts/
  references/
  assets/
  agents/openai.yaml
```

`name` in `SKILL.md` frontmatter matches `<skill-name>`: lowercase letters, digits, hyphens, no leading or trailing hyphen, no doubled hyphen, 64 characters or fewer. `description` says what the skill does and when to use it, in 1024 characters or fewer. Keep the body under 500 lines and move long reference material to `references/`.

`agents/openai.yaml` is optional and is for Codex's listing UI. Quote string values. `interface.default_prompt` must mention `$<skill-name>` when present. Leave `policy.allow_implicit_invocation` unset unless the skill should be explicit-only.

## After a change

Run `python3 scripts/validate-catalog.py`.

When the change adds a skill under `plugins/`, also add its name to that plugin's `skills/README.md` and to a group in `skills.sh.json`. `skills.sh.json` only affects the skills.sh repository page. It does not change installation.
