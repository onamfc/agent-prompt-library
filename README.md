# Agent Prompt Library

A collection of reusable AI agent prompts for development workflows.

## Usage

Each agent directory contains:

| File           | Purpose                                             |
|----------------|-----------------------------------------------------|
| `prompt.md`    | The canonical prompt — copy/paste into your AI tool |
| `README.md`    | When to use, model recommendations, limitations     |
| `examples.md`  | Example interactions and outputs (optional)         |
| `changelog.md` | Version history and iteration notes (optional)      |

## Agents

| Agent                                   | Category    | Description                           |
|-----------------------------------------|-------------|---------------------------------------|
| [Backend API](./backend-api/)           | development | Server-side applications and APIs     |
| [Brand Architect](./brand-architect/)   | analysis    | Creative business naming from codebase analysis |
| [Code Review](./code-review/)           | review      | Code review and quality feedback      |
| [Debugging](./debugging/)               | development | Systematic bug diagnosis              |
| [Infrastructure](./infrastructure/)     | engineering | DevOps, CI/CD, deployment pipelines   |
| [React Native](./react-native/)         | development | Cross-platform mobile app development |
| [Refactoring](./refactoring/)           | development | Code structure improvement            |
| [Technical Writer](./technical-writer/) | writing     | Documentation and technical writing   |

See [`agents.json`](./agents.json) for the complete, machine-readable list.

## Frontmatter Schema

Each `prompt.md` includes YAML frontmatter for tooling and searchability:

```yaml
---
name: Agent Name
category: engineering | development | review | writing | analysis | operations
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
7. Keep prompts generic — avoid hardcoding specific tools or platforms

## License

MIT
