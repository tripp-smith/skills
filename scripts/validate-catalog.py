#!/usr/bin/env python3
"""Check that ecosystem plugins stay portable across skill clients."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")
AGENT_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
AGENT_KEYS = {
    "$schema",
    "name",
    "version",
    "description",
    "author",
    "homepage",
    "repository",
    "license",
    "keywords",
    "extensions",
}
SHARED_KEYS = ("name", "version", "description", "keywords")
ERRORS: list[str] = []


def error(message: str) -> None:
    ERRORS.append(message)


def load_json(path: Path) -> dict | None:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        error(f"missing {path.relative_to(ROOT)}")
        return None
    except json.JSONDecodeError as exc:
        error(f"{path.relative_to(ROOT)} is not valid JSON: {exc}")
        return None
    if not isinstance(payload, dict):
        error(f"{path.relative_to(ROOT)} must be a JSON object")
        return None
    return payload


def plugin_names(document: dict | None, label: str) -> list[str]:
    if document is None:
        return []
    plugins = document.get("plugins")
    if not isinstance(plugins, list):
        error(f"{label} plugins must be an array")
        return []
    names: list[str] = []
    for entry in plugins:
        if not isinstance(entry, dict) or not isinstance(entry.get("name"), str):
            error(f"{label} has a plugin entry without a string name")
            continue
        names.append(entry["name"])
        source = entry.get("source")
        expected = f"./plugins/{entry['name']}"
        if label == "codex":
            path = source.get("path") if isinstance(source, dict) else None
            if path != expected:
                error(f"{label} entry {entry['name']} source.path must be {expected}")
        elif source != expected:
            error(f"{label} entry {entry['name']} source must be {expected}")
    if len(names) != len(set(names)):
        error(f"{label} lists a plugin more than once")
    return names


def parse_frontmatter(text: str, path: Path) -> dict[str, str] | None:
    if not text.startswith("---\n"):
        error(f"{path.relative_to(ROOT)} must start with YAML frontmatter")
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        error(f"{path.relative_to(ROOT)} frontmatter is not closed")
        return None
    body = text[end + 5 :].strip()
    if not body:
        error(f"{path.relative_to(ROOT)} body is empty")
    raw = text[4:end]
    fields: dict[str, str] = {}
    lines = raw.splitlines()
    index = 0
    while index < len(lines):
        line = lines[index]
        if not line.strip() or line.lstrip().startswith("#"):
            index += 1
            continue
        if line.startswith((" ", "\t")) or ":" not in line:
            error(f"{path.relative_to(ROOT)} has unsupported frontmatter line: {line}")
            index += 1
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value in {">", "|", ">-", "|-"} or value == "":
            index += 1
            collected: list[str] = []
            while index < len(lines) and (lines[index].startswith((" ", "\t")) or not lines[index].strip()):
                collected.append(lines[index].strip())
                index += 1
            value = " ".join(part for part in collected if part)
        else:
            index += 1
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
            value = value[1:-1]
        fields[key] = value
    return fields


def check_skill(path: Path, names_seen: dict[str, Path]) -> None:
    relative = path.relative_to(ROOT)
    if path.parent.parent.name != "skills":
        error(f"{relative} is nested. Skills must be skills/<skill-name>/SKILL.md")
        return
    fields = parse_frontmatter(path.read_text(encoding="utf-8"), path)
    if fields is None:
        return
    if "version" in fields:
        error(f"{relative} sets version. Version the plugin manifests instead")
    name = fields.get("name", "")
    if name != path.parent.name:
        error(f"{relative} name {name!r} must match directory {path.parent.name!r}")
    if not NAME_RE.fullmatch(name) or len(name) > 64:
        error(f"{relative} name must be a lowercase hyphenated id of at most 64 characters")
    description = fields.get("description", "")
    if not description or len(description) > 1024 or "\n" in description:
        error(f"{relative} description must be one non-empty line of at most 1024 characters")
    previous = names_seen.get(name)
    if previous is not None:
        error(f"duplicate skill name {name}: {previous.relative_to(ROOT)} and {relative}")
    elif name:
        names_seen[name] = path


def check_plugin(plugin_dir: Path) -> None:
    name = plugin_dir.name
    agent = load_json(plugin_dir / "plugin.json")
    claude = load_json(plugin_dir / ".claude-plugin" / "plugin.json")
    cursor = load_json(plugin_dir / ".cursor-plugin" / "plugin.json")
    manifests = [item for item in (agent, claude, cursor) if item is not None]
    if agent is not None:
        unknown = sorted(set(agent) - AGENT_KEYS)
        if unknown:
            error(f"plugins/{name}/plugin.json has fields outside the Agent Plugins schema: {', '.join(unknown)}")
        if agent.get("$schema") != AGENT_SCHEMA:
            error(f"plugins/{name}/plugin.json must declare the Agent Plugins schema")
        if "skills" in agent or "mcpServers" in agent:
            error(f"plugins/{name}/plugin.json must not override component paths")
    for manifest in manifests:
        if manifest.get("name") != name:
            error(f"plugins/{name} manifest name is {manifest.get('name')!r}")
        version = manifest.get("version")
        if not isinstance(version, str) or not SEMVER_RE.fullmatch(version):
            error(f"plugins/{name} version must be semver, found {version!r}")
    if len(manifests) == 3:
        for key in SHARED_KEYS:
            values = {json.dumps(manifest.get(key), sort_keys=True) for manifest in manifests}
            if len(values) != 1:
                error(f"plugins/{name} {key} differs across plugin manifests")
    for filename in ("README.md", "skills/README.md"):
        if not (plugin_dir / filename).is_file():
            error(f"plugins/{name}/{filename} is missing")
    if (plugin_dir / "SKILL.md").exists():
        error(f"plugins/{name}/SKILL.md would make the whole plugin one skill. Use skills/<name>/SKILL.md")


def skill_files() -> list[Path]:
    roots = [ROOT / "plugins", ROOT / ".agents" / "skills"]
    found: list[Path] = []
    for root in roots:
        if not root.exists():
            continue
        found.extend(sorted(root.rglob("SKILL.md")))
    return found


def main() -> None:
    claude_market = load_json(ROOT / ".claude-plugin" / "marketplace.json")
    cursor_market = load_json(ROOT / ".cursor-plugin" / "marketplace.json")
    codex_market = load_json(ROOT / ".agents" / "plugins" / "marketplace.json")
    for label, document in (
        ("claude", claude_market),
        ("cursor", cursor_market),
        ("codex", codex_market),
    ):
        if document is not None and document.get("name") != "tripp-smith-skills":
            error(f"{label} marketplace name must be tripp-smith-skills")

    listed = {
        "claude": plugin_names(claude_market, "claude"),
        "cursor": plugin_names(cursor_market, "cursor"),
        "codex": plugin_names(codex_market, "codex"),
    }
    if len({tuple(names) for names in listed.values()}) != 1:
        error(
            "marketplace plugin lists differ: "
            + ", ".join(f"{key}={value}" for key, value in listed.items())
        )

    plugins_root = ROOT / "plugins"
    directories = sorted(path for path in plugins_root.iterdir() if path.is_dir()) if plugins_root.exists() else []
    directory_names = [path.name for path in directories]
    if set(listed["claude"]) != set(directory_names):
        error(
            f"plugins/ directories {directory_names} do not match marketplace entries {listed['claude']}"
        )

    readme = (ROOT / "README.md").read_text(encoding="utf-8") if (ROOT / "README.md").is_file() else ""
    plugins_readme = (
        (plugins_root / "README.md").read_text(encoding="utf-8") if (plugins_root / "README.md").is_file() else ""
    )
    for name in directory_names:
        check_plugin(plugins_root / name)
        if f"`{name}`" not in readme:
            error(f"README.md does not mention `{name}`")
        if f"`{name}`" not in plugins_readme:
            error(f"plugins/README.md does not mention `{name}`")

    names_seen: dict[str, Path] = {}
    catalog_skills: list[str] = []
    for path in skill_files():
        check_skill(path, names_seen)
        if "plugins" in path.parts:
            catalog_skills.append(path.parent.name)
            plugin_name = path.relative_to(plugins_root).parts[0]
            index = plugins_root / plugin_name / "skills" / "README.md"
            if index.is_file() and path.parent.name not in index.read_text(encoding="utf-8"):
                error(f"{index.relative_to(ROOT)} does not list {path.parent.name}")

    link = ROOT / ".claude" / "skills"
    if not link.is_symlink() or link.readlink() != Path("../.agents/skills"):
        error(".claude/skills must be a symlink to ../.agents/skills")

    catalog = load_json(ROOT / "skills.sh.json")
    grouped: set[str] = set()
    if catalog is not None:
        groupings = catalog.get("groupings")
        if not isinstance(groupings, list) or not groupings:
            error("skills.sh.json groupings must be a non-empty array")
        else:
            for group in groupings:
                if not isinstance(group, dict):
                    error("skills.sh.json has a grouping that is not an object")
                    continue
                skills = group.get("skills")
                if not isinstance(skills, list) or not skills:
                    error(f"skills.sh.json group {group.get('title')!r} needs at least one skill")
                    continue
                grouped.update(str(item) for item in skills)
    for name in sorted(names_seen):
        if name not in grouped:
            error(f"skills.sh.json does not list {name}")
    missing = sorted(grouped - set(names_seen))
    for name in missing:
        error(f"skills.sh.json lists {name}, which has no SKILL.md")

    if ERRORS:
        print(f"{len(ERRORS)} catalog error(s):", file=sys.stderr)
        for item in ERRORS:
            print(f"- {item}", file=sys.stderr)
        sys.exit(1)
    print(
        f"ok: {len(directory_names)} ecosystem(s), {len(names_seen)} skill(s), "
        f"{len(catalog_skills)} installable"
    )


if __name__ == "__main__":
    main()
