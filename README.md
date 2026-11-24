# Skills

Specialized skill ecosystems you can install in Cursor, Claude Code, Codex, Grok, GitHub Copilot, and Antigravity.

A skill is a folder with a `SKILL.md` file, in the open [Agent Skills](https://agentskills.io/specification) format. Related skills ship together as one plugin. The plugin is the ecosystem: writing, product, engineering, or media. Each client reads its own marketplace file and then loads the same `skills/` tree.

Repository: [github.com/tripp-smith/skills](https://github.com/tripp-smith/skills)

## Ecosystems

| Plugin | Install it for | Skills |
| --- | --- | --- |
| `writing` | Long-form writing, manuscripts, and reader-facing prose | `reader-first-communication` (cold-read titles, headings, and prose) |
| `product` | Specifications, planning, and product communication | — |
| `engineering` | Implementation, delivery, and verification workflows | — |
| `media` | Image, video, voice, and film workflows | — |

Add a skill inside an existing ecosystem, or add another plugin, without copying the skill for each client.

## Install

Marketplace name: `tripp-smith-skills`.

Claude Code, from inside a session:

```text
/plugin marketplace add tripp-smith/skills
/plugin install writing@tripp-smith-skills
```

Codex:

```text
codex plugin marketplace add tripp-smith/skills
```

Then install `writing`, `product`, `engineering`, or `media` from that marketplace.

Cursor reads `.cursor-plugin/marketplace.json` at the root of this repository. Each plugin also has `.cursor-plugin/plugin.json`, which is the manifest Cursor loads first.

Grok reads the Agent Plugins manifest at `plugins/<ecosystem>/plugin.json` and Claude's marketplace files.

Copilot and Antigravity do not install this marketplace. They read Agent Skills folders. Symlink or copy the one skill you want:

```text
plugins/<ecosystem>/skills/<skill-name>/
  ->  <project>/.agents/skills/<skill-name>/
```

`.agents/skills/` is the shared project path for Cursor, Codex, Copilot, and Antigravity. Claude Code and Grok read `.claude/skills/`.

## Layout

```text
.claude-plugin/marketplace.json      Claude Code catalog
.cursor-plugin/marketplace.json      Cursor catalog
.agents/plugins/marketplace.json     Codex catalog
plugins/<ecosystem>/
  plugin.json                        Codex, Grok, other Agent Plugins clients
  .claude-plugin/plugin.json         Claude Code
  .cursor-plugin/plugin.json         Cursor
  skills/<skill-name>/
    SKILL.md                         instructions and trigger description
    scripts/                         optional commands the agent runs
    references/                      optional detail, loaded only when needed
    assets/                          optional templates and static files
    agents/openai.yaml               optional Codex listing metadata
.agents/skills/                      skills that apply to this repository
.claude/skills                       symlink to ../.agents/skills
templates/plugin/                    copy for a new ecosystem
```

Keep skill directories flat under `skills/`. A folder such as `skills/editing/line-notes/SKILL.md` is invisible to Claude, Codex, and skills.sh, which look one level down. The ecosystem is the plugin, not a subdirectory.

Opening this repository loads `.agents/skills/add-skill` only. Skills inside `plugins/` load when that plugin is installed, so one ecosystem does not enter context just because the catalog is open.

## Add a skill or ecosystem

In this checkout, ask the agent to add a skill. It should follow `.agents/skills/add-skill`. The same steps are in `CONTRIBUTING.md`.

New ecosystem:

```bash
python3 scripts/new-plugin.py <name> \
  --description "What this ecosystem is for." \
  --category "Productivity" \
  --keywords writing,editing
```

Then add `<name>` to the tables in `README.md` and `plugins/README.md`.

Check the catalog before you commit:

```bash
python3 scripts/validate-catalog.py
```
