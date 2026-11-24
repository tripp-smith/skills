# Reader-first Communication Agent Skill

A portable, instruction-only Agent Skill for chart and slide titles, report structures, document headings, headlines, correspondence, and explanatory writing. It targets writer-centric context leakage: wording that makes sense to the author but not to a first-time external reader. It prefers conventional domain wording, keeps standard technical terms when they are the precise vocabulary, and checks presuppositions, outline continuity, and tight-length hierarchy under cold-read review.

## Installation

Preferred: install the `writing` plugin from this repository's marketplace.

```text
/plugin marketplace add tripp-smith/skills
/plugin install writing@tripp-smith-skills
```

To use only this skill, place the `reader-first-communication/` folder in a skills directory your agent reads. A common project location is `.agents/skills/reader-first-communication/`; a personal Codex location is `~/.agents/skills/reader-first-communication/`. Preserve the folder and its `SKILL.md` file.

The skill follows the Agent Skills format: https://agentskills.io/specification

## Files

- `SKILL.md`: core operating instructions, conventional-wording rule, audience presupposition check, outline continuity, and cold-read quality gate.
- `references/title-patterns.md`: before/after examples, including conventional technical terms vs idiosyncratic labels.
- `references/evaluation.md`: detailed audit and red-team procedure.
- `tests/acceptance-cases.md`: 12 scenario-based smoke tests.
- `agents/openai.yaml`: optional presentation metadata for supporting agents.

## Quick invocation

> Apply the reader-first-communication skill. Rewrite this deck's titles to communicate each supported finding to a reader who has not seen the conversation. Prefer conventional domain wording. Preserve data fidelity and expose key qualifications.

## Adoption note

Skills are loaded on demand by compatible agents; placing the skill in a directory does not guarantee universal activation. For teams requiring this rule on every writing task, reference this skill from the project's standing agent instructions.
