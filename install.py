#!/usr/bin/env python3
"""Install agents from this library as Claude Code subagents.

Reads agents.json, converts each agent's prompt.md into the subagent format
Claude Code expects, and writes it to an agents directory.

  ./install.py --list                       show every agent in the library
  ./install.py video-script-director        install one agent, user-level
  ./install.py --category marketing         install a whole category
  ./install.py --all --dry-run              preview installing everything
  ./install.py --all --project ~/code/app   install into a specific project

User-level (the default, ~/.claude/agents) makes an agent available in every
project. Project-level (--project) scopes it to one repository.

No dependencies beyond the standard library. Python 3.8+.
"""

import argparse
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.abspath(__file__))
USER_AGENTS_DIR = os.path.expanduser("~/.claude/agents")

# Colors are cosmetic in Claude Code but help distinguish agents in the UI.
# Keyed by category so installs are deterministic and repeatable.
CATEGORY_COLORS = {
    "engineering": "orange",
    "development": "green",
    "review": "red",
    "writing": "blue",
    "analysis": "purple",
    "operations": "yellow",
    "marketing": "pink",
    "meta": "cyan",
}
DEFAULT_COLOR = "blue"

FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n+", re.DOTALL)


class InstallError(Exception):
    pass


def load_manifest():
    path = os.path.join(REPO, "agents.json")
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)["agents"]
    except FileNotFoundError:
        raise InstallError(f"no manifest at {path}")
    except (json.JSONDecodeError, KeyError) as exc:
        raise InstallError(f"malformed manifest at {path}: {exc}")


def strip_frontmatter(text, source):
    """Remove the library's YAML frontmatter, leaving the prompt body."""
    if not text.startswith("---"):
        return text.lstrip("\n")
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise InstallError(f"{source}: frontmatter opened but never closed")
    return text[match.end():]


def read_description(agent):
    """Prefer a delegation.md override; fall back to the manifest description.

    The manifest description is a one-liner meant for humans browsing the
    library. Claude Code uses this field to decide when to route work to the
    agent, so an agent that benefits from richer routing guidance can ship a
    delegation.md next to its prompt.md and have that used instead.
    """
    override = os.path.join(REPO, os.path.dirname(agent["path"]), "delegation.md")
    if os.path.exists(override):
        with open(override, encoding="utf-8") as fh:
            text = fh.read().strip()
        if text:
            return text
    return agent["description"]


def render(agent):
    prompt_path = os.path.join(REPO, agent["path"])
    try:
        with open(prompt_path, encoding="utf-8") as fh:
            body = strip_frontmatter(fh.read(), agent["path"])
    except FileNotFoundError:
        raise InstallError(f"{agent['id']}: no prompt at {agent['path']}")

    if not body.strip():
        raise InstallError(f"{agent['id']}: prompt is empty after stripping frontmatter")

    color = CATEGORY_COLORS.get(agent.get("category"), DEFAULT_COLOR)

    # json.dumps produces a correctly escaped double-quoted scalar. JSON string
    # escaping is a valid subset of YAML's, so quotes, colons, and newlines in
    # the description survive intact.
    header = (
        "---\n"
        f"name: {agent['id']}\n"
        f"description: {json.dumps(read_description(agent))}\n"
        "model: inherit\n"
        f"color: {color}\n"
        "---\n\n"
    )
    return header + body


def select(agents, args):
    if args.all:
        return agents
    if args.category:
        chosen = [a for a in agents if a.get("category") == args.category]
        if not chosen:
            categories = sorted({a.get("category", "?") for a in agents})
            raise InstallError(
                f"no agents in category '{args.category}'. "
                f"available: {', '.join(categories)}"
            )
        return chosen

    by_id = {a["id"]: a for a in agents}
    unknown = [name for name in args.agents if name not in by_id]
    if unknown:
        raise InstallError(
            f"unknown agent(s): {', '.join(unknown)}. Run --list to see what exists."
        )
    return [by_id[name] for name in args.agents]


def main():
    parser = argparse.ArgumentParser(
        description="Install agents from this library as Claude Code subagents.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__.split("\n\n", 1)[1],
    )
    parser.add_argument("agents", nargs="*", help="agent ids to install")
    parser.add_argument("--all", action="store_true", help="install every agent")
    parser.add_argument("--category", help="install every agent in a category")
    parser.add_argument(
        "--project",
        metavar="PATH",
        help="install into PATH/.claude/agents instead of user-level",
    )
    parser.add_argument("--dest", metavar="DIR", help="install into an explicit directory")
    parser.add_argument("--list", action="store_true", help="list available agents and exit")
    parser.add_argument("--force", action="store_true", help="overwrite existing files")
    parser.add_argument("--dry-run", action="store_true", help="show what would happen")
    args = parser.parse_args()

    try:
        agents = load_manifest()

        if args.list:
            width = max(len(a["id"]) for a in agents)
            for agent in sorted(agents, key=lambda a: (a.get("category", ""), a["id"])):
                category = agent.get("category", "?")
                print(f"  {agent['id']:<{width}}  {category:<12}  {agent['description']}")
            print(f"\n{len(agents)} agents")
            return 0

        if not (args.agents or args.all or args.category):
            parser.print_help()
            return 2

        if args.dest and args.project:
            raise InstallError("use either --dest or --project, not both")
        if args.dest:
            dest = os.path.expanduser(args.dest)
        elif args.project:
            dest = os.path.join(os.path.expanduser(args.project), ".claude", "agents")
        else:
            dest = USER_AGENTS_DIR

        chosen = select(agents, args)

        # Render everything before writing anything, so a failure partway
        # through does not leave a half-installed set on disk.
        rendered = [(a, render(a)) for a in chosen]

        existing = [
            a["id"] for a, _ in rendered
            if os.path.exists(os.path.join(dest, f"{a['id']}.md"))
        ]
        if existing and not (args.force or args.dry_run):
            raise InstallError(
                f"already installed: {', '.join(existing)}. "
                f"Re-run with --force to overwrite."
            )

        print(f"{'Would install' if args.dry_run else 'Installing'} to {dest}\n")
        if not args.dry_run:
            os.makedirs(dest, exist_ok=True)

        for agent, content in rendered:
            out = os.path.join(dest, f"{agent['id']}.md")
            note = " (overwrite)" if agent["id"] in existing else ""
            if not args.dry_run:
                with open(out, "w", encoding="utf-8") as fh:
                    fh.write(content)
            print(f"  {agent['id']}{note}")

        print(f"\n{len(rendered)} agent(s).", end=" ")
        print("Nothing written." if args.dry_run else "Restart Claude Code to pick them up.")
        return 0

    except InstallError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
