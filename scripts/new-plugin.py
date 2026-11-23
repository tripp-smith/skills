#!/usr/bin/env python3
"""Create an ecosystem plugin and register it in every marketplace."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
AUTHOR = {"name": "trippsmith", "email": "trippsmith@authid.ai"}
AGENT_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
CLAUDE_SCHEMA = "https://json.schemastore.org/claude-code-plugin-manifest.json"
MARKETPLACE_NAME = "tripp-smith-skills"
MARKETPLACE_DESCRIPTION = (
    "Specialized skill ecosystems for Cursor, Claude, Codex, and other Agent Skills clients."
)

CLAUDE_MARKET = ROOT / ".claude-plugin" / "marketplace.json"
CURSOR_MARKET = ROOT / ".cursor-plugin" / "marketplace.json"
CODEX_MARKET = ROOT / ".agents" / "plugins" / "marketplace.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("name", help="Plugin id, used as plugins/<name>")
    parser.add_argument("--description", required=True, help="What this ecosystem is for")
    parser.add_argument(
        "--category",
        default="Productivity",
        help="Codex marketplace category. Default: Productivity",
    )
    parser.add_argument(
        "--keywords",
        default="",
        help="Comma-separated discovery tags",
    )
    parser.add_argument(
        "--capability",
        action="append",
        dest="capabilities",
        help="Codex capability label. Repeat for more than one.",
    )
    return parser.parse_args()


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    sys.exit(1)


def keywords_from(raw: str, name: str) -> list[str]:
    items = [part.strip() for part in raw.split(",") if part.strip()]
    if name not in items:
        items.insert(0, name)
    return items


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def claude_marketplace() -> dict:
    return {
        "name": MARKETPLACE_NAME,
        "description": MARKETPLACE_DESCRIPTION,
        "owner": AUTHOR,
        "metadata": {
            "description": MARKETPLACE_DESCRIPTION,
            "version": "0.1.0",
        },
        "plugins": [],
    }


def cursor_marketplace() -> dict:
    return {
        "name": MARKETPLACE_NAME,
        "owner": AUTHOR,
        "metadata": {
            "description": MARKETPLACE_DESCRIPTION,
            "version": "0.1.0",
        },
        "plugins": [],
    }


def codex_marketplace() -> dict:
    return {
        "name": MARKETPLACE_NAME,
        "interface": {"displayName": "trippsmith skills"},
        "plugins": [],
    }


def ensure_marketplaces() -> None:
    if not CLAUDE_MARKET.exists():
        dump(CLAUDE_MARKET, claude_marketplace())
    if not CURSOR_MARKET.exists():
        dump(CURSOR_MARKET, cursor_marketplace())
    if not CODEX_MARKET.exists():
        dump(CODEX_MARKET, codex_marketplace())


def upsert(path: Path, entry: dict) -> None:
    document = load(path)
    plugins = document.setdefault("plugins", [])
    for index, existing in enumerate(plugins):
        if existing.get("name") == entry["name"]:
            plugins[index] = entry
            break
    else:
        plugins.append(entry)
    dump(path, document)


def write_readme(plugin_dir: Path, name: str, description: str) -> None:
    title = " ".join(part.capitalize() for part in name.split("-"))
    (plugin_dir / "README.md").write_text(
        "\n".join(
            [
                f"# {title}",
                "",
                description,
                "",
                f"Install `{name}` from the `{MARKETPLACE_NAME}` marketplace.",
                "Skills in this ecosystem are one directory deep at `skills/<skill-name>/SKILL.md`.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    skills = plugin_dir / "skills"
    skills.mkdir(parents=True, exist_ok=True)
    readme = skills / "README.md"
    if not readme.exists():
        readme.write_text(
            "\n".join(
                [
                    "# Skills",
                    "",
                    "Each skill is a sibling directory containing `SKILL.md`.",
                    "",
                    "| Skill | What it does |",
                    "| --- | --- |",
                    "| _None yet._ | |",
                    "",
                ]
            ),
            encoding="utf-8",
        )


def write_manifests(
    plugin_dir: Path,
    name: str,
    description: str,
    keywords: list[str],
    category: str,
    capabilities: list[str],
) -> None:
    agent = {
        "$schema": AGENT_SCHEMA,
        "name": name,
        "version": "0.1.0",
        "description": description,
        "author": AUTHOR,
        "license": "MIT",
        "keywords": keywords,
        "extensions": {
            "com.openai": {
                "interface": {
                    "displayName": " ".join(part.capitalize() for part in name.split("-")),
                    "shortDescription": description,
                    "developerName": AUTHOR["name"],
                    "category": category,
                    "capabilities": capabilities,
                }
            }
        },
    }
    client = {
        "name": name,
        "version": "0.1.0",
        "description": description,
        "author": AUTHOR,
        "license": "MIT",
        "keywords": keywords,
    }
    claude = {"$schema": CLAUDE_SCHEMA, **client}
    dump(plugin_dir / "plugin.json", agent)
    dump(plugin_dir / ".claude-plugin" / "plugin.json", claude)
    dump(plugin_dir / ".cursor-plugin" / "plugin.json", client)


def main() -> None:
    args = parse_args()
    name = args.name.strip()
    if not NAME_RE.fullmatch(name):
        fail("name must be lowercase letters, digits, and single hyphens")
    if len(name) > 64:
        fail("name must be 64 characters or fewer")
    description = " ".join(args.description.split())
    if not description:
        fail("description is empty")
    if len(description) > 1024:
        fail("description must be 1024 characters or fewer")
    plugin_dir = ROOT / "plugins" / name
    if plugin_dir.exists():
        fail(f"{plugin_dir.relative_to(ROOT)} already exists")

    keywords = keywords_from(args.keywords, name)
    capabilities = args.capabilities or ["Write"]
    ensure_marketplaces()
    plugin_dir.mkdir(parents=True)
    write_manifests(plugin_dir, name, description, keywords, args.category, capabilities)
    write_readme(plugin_dir, name, description)
    source = f"./plugins/{name}"
    upsert(
        CLAUDE_MARKET,
        {"name": name, "source": source, "description": description},
    )
    upsert(
        CURSOR_MARKET,
        {"name": name, "source": source, "description": description},
    )
    upsert(
        CODEX_MARKET,
        {
            "name": name,
            "source": {"source": "local", "path": source},
            "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
            "category": args.category,
        },
    )
    print(f"created plugins/{name}")
    print("next: mention it in README.md and plugins/README.md, then run scripts/validate-catalog.py")


if __name__ == "__main__":
    main()
