# Agent Prompt Library

A collection of reusable AI agent prompts for development workflows.

## Usage

Each agent directory contains:

| File            | Purpose                                                        |
|-----------------|----------------------------------------------------------------|
| `prompt.md`     | The canonical prompt — copy/paste into your AI tool            |
| `README.md`     | When to use, model recommendations, limitations                |
| `delegation.md` | Routing description used when installing as a subagent (optional) |
| `examples.md`   | Example interactions and outputs (optional)                    |
| `changelog.md`  | Version history and iteration notes (optional)                 |

## Installing

Copy any `prompt.md` into your tool by hand, or install agents as Claude Code subagents with the bundled script:

```bash
./install.py --list                      # everything in the library
./install.py video-script-director       # one agent, available in every project
./install.py --category marketing        # a whole category
./install.py --all --dry-run             # preview without writing
./install.py hook-architect --project ~/code/app   # scope to one repository
```

Installs go to `~/.claude/agents/` by default, which makes an agent available everywhere; `--project` scopes it to a single repository instead. Existing files are left alone unless you pass `--force`. The script converts each `prompt.md` into subagent frontmatter, using `delegation.md` for the routing description when an agent ships one and the `agents.json` description otherwise. Standard library only — no dependencies.

## Agents

| Agent                                   | Category    | Description                           |
|-----------------------------------------|-------------|---------------------------------------|
| [API Contract Designer](./api-contract-designer/) | engineering | API contract design, review, and evolution |
| [Avatar & Offer Researcher](./avatar-offer-researcher/) | marketing | Psychographic customer avatar and offer immersion |
| [Backend API](./backend-api/)           | development | Server-side applications and APIs     |
| [Brand Architect](./brand-architect/)   | analysis    | Creative business naming from codebase analysis |
| [Changelog Writer](./changelog-writer/) | writing     | Keep a Changelog compliant changelogs |
| [Claim Validator](./claim-validator/)   | marketing   | Attaches proof to marketing claims    |
| [Code Review](./code-review/)           | review      | Code review and quality feedback      |
| [Debugging](./debugging/)               | development | Systematic bug diagnosis              |
| [Docusaurus Writer](./docusaurus-writer/) | writing     | User-facing product docs for Docusaurus sites |
| [Gap & Bridge Architect](./gap-and-bridge-architect/) | marketing | Problem, solution, and CTA sections of a video script |
| [Git Strategist](./git-strategist/)     | engineering | Complex git operations and branching strategy |
| [Hook Architect](./hook-architect/)     | marketing   | High-volume video ad hooks with visual treatments |
| [Infrastructure](./infrastructure/)     | engineering | DevOps, CI/CD, deployment pipelines   |
| [PR Annotator](./pr-annotator/)         | writing     | Enriches PR descriptions with clickable diff links |
| [PR Reviewer](./pr-reviewer/)           | review      | PR review with good/bad/ugly feedback |
| [Project Handoff](./project-handoff/)   | writing     | Branch handoff docs for AI session continuity |
| [React Native](./react-native/)         | development | Cross-platform mobile app development |
| [Refactoring](./refactoring/)           | development | Code structure improvement            |
| [Release Manager](./release-manager/)   | operations  | End-to-end release orchestration      |
| [Script Dimensionalizer](./script-dimensionalizer/) | marketing | Value stacks, comparison stacks, objection prevention |
| [Script Finalizer](./script-finalizer/) | marketing   | Final word-for-word script, shot list, and variants |
| [Technical Writer](./technical-writer/) | writing     | Documentation and technical writing   |
| [Video Script Director](./video-script-director/) | marketing | Orchestrates a full direct response video script |

See [`agents.json`](./agents.json) for the complete, machine-readable list.

### Agent Suites

Some agents are designed to work together. Call the orchestrator and it delegates to the rest.

**Video Script Suite** — [Video Script Director](./video-script-director/) runs a four-phase pipeline (Research → Brainstorm → Dimensionalize → Finalize) that turns "here's what I sell" into a word-for-word shooting script. It delegates to [Avatar & Offer Researcher](./avatar-offer-researcher/), [Hook Architect](./hook-architect/), [Gap & Bridge Architect](./gap-and-bridge-architect/), [Claim Validator](./claim-validator/), [Script Dimensionalizer](./script-dimensionalizer/), and [Script Finalizer](./script-finalizer/). Each specialist also works standalone.

## Frontmatter Schema

Each `prompt.md` includes YAML frontmatter for tooling and searchability:

```yaml
---
name: Agent Name
category: engineering | development | review | writing | analysis | operations | marketing
models: ["claude-code", "cursor", "claude-api"]
context_window: small | medium | large
version: 1.0.0
author: github-handle
tags: ["relevant", "tags"]
---
```

### Categories

- `engineering` — devops, infrastructure, architecture
- `development` — coding, debugging, refactoring
- `review` — code review, PR review, security audit
- `writing` — docs, technical writing, copywriting
- `analysis` — data, research, investigation
- `operations` — support, triage, incident response
- `marketing` — advertising, scripts, positioning, sales copy

### Context Window

- `small` — <4k tokens
- `medium` — 4-16k tokens
- `large` — 16k+ tokens

## Programmatic Access

The `agents.json` manifest enables CLI tools and automation to consume this library without parsing individual files.

### Manifest Structure

```json
{
  "version": "1.0.0",
  "agents": [
    {
      "id": "infrastructure",
      "name": "Infrastructure Agent",
      "category": "engineering",
      "description": "DevOps, CI/CD, deployment pipelines",
      "path": "infrastructure/prompt.md",
      "context_window": "large",
      "tags": ["devops", "ci-cd", "github-actions", "deployment"]
    }
  ]
}
```

### Fetching Prompts

```bash
# Get the manifest
curl https://raw.githubusercontent.com/onamfc/agent-prompt-library/main/agents.json

# Get a specific prompt
curl https://raw.githubusercontent.com/onamfc/agent-prompt-library/main/infrastructure/prompt.md
```

### Example: List All Agents

```bash
curl -s https://raw.githubusercontent.com/onamfc/agent-prompt-library/main/agents.json | jq '.agents[] | {id, name, category}'
```

### Example: Fetch Prompt by ID

```bash
ID="infrastructure"
PATH=$(curl -s https://raw.githubusercontent.com/onamfc/agent-prompt-library/main/agents.json | jq -r ".agents[] | select(.id==\"$ID\") | .path")
curl -s "https://raw.githubusercontent.com/onamfc/agent-prompt-library/main/$PATH"
```

## Design Principles

### Keep prompts generic

Prompts should define **how an agent thinks and behaves**, not encode specific tools or platforms.

**Do this:**
```markdown
- Integrate with the project's deployment platform
- Use platform CLI/actions in workflows
```

**Not this:**
```markdown
- Integrate with Railway for deployments
- Use Railway CLI in GitHub Actions
```

**Why?**
- LLMs already have knowledge of specific platforms
- Generic prompts work across tools without modification
- Users provide specifics via context: *"Set up CI/CD. We deploy to Vercel."*
- Maintenance stays flat — no need for platform-specific variants

### Prompt = behavior specification

The prompt defines the agent's:
- Role and expertise
- Decision-making philosophy
- Output format and style
- Boundaries (what it won't do)

The prompt does NOT need to include:
- Platform-specific implementation details
- Exhaustive tool documentation
- Information the LLM already knows

## Contributing

1. Copy the `_template/` directory and rename it for your agent
2. Fill in `prompt.md` with frontmatter and the canonical prompt
3. Fill in `README.md` explaining when/how to use it
4. Update this README's agent index table
5. Add your agent to `agents.json` manifest
6. Optionally add `examples.md` if the agent's output format isn't obvious
7. Optionally add `delegation.md` if the agent needs richer routing guidance than the one-line manifest description — useful when it should only fire in specific situations, or is easily confused with a neighbouring agent
8. Keep prompts generic — avoid hardcoding specific tools or platforms
9. Verify it installs cleanly with `./install.py <your-agent> --dry-run`

## License

MIT
