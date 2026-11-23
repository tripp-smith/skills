# Plugin template

`scripts/new-plugin.py` creates the manifests and marketplace entries. This directory is only the skill skeleton those manifests expect.

Copy `skills/skill-name/` to `plugins/<ecosystem>/skills/<skill-name>/`, rename `SKILL.md.template` to `SKILL.md`, and rename `agents/openai.yaml.template` to `agents/openai.yaml` if Codex needs listing metadata. Then follow `CONTRIBUTING.md`.

Do not point a marketplace at this directory.
