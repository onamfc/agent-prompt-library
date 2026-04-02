# Git Strategist

Guide complex git operations, design branching strategies, and resolve version control problems without data loss.

## When to Use

- Stuck in a broken rebase, merge conflict, or detached HEAD state
- Recovering lost commits, branches, or stashed work
- Choosing or changing a branching strategy for a team
- Planning a repository migration, split, or consolidation
- Removing sensitive data (secrets, large files) from git history
- Setting up git workflows and conventions for a new project
- Debugging unexpected git behavior

## When NOT to Use

- CI/CD pipeline design (use the Infrastructure agent)
- Release orchestration — tagging, changelogs, publishing (use the Release Manager agent)
- Code review workflow (use the Code Review or PR Review agents)
- Day-to-day commits and simple merges that aren't causing problems

## Model Recommendations

| Model | Suitability | Notes |
|-------|-------------|-------|
| Claude Code | Excellent | Can inspect repo state, run git commands, and apply fixes directly |
| Cursor | Good | Useful for visualizing and resolving conflicts in-editor |
| Claude API | Good | Strong for strategy discussions and workflow design |

## Context Requirements

This agent works best with:

- Output of `git status`, `git log`, and `git reflog` when troubleshooting
- The team's current branching model (if one exists)
- Release cadence and deployment strategy
- Number of contributors and their git experience level

## Example Prompts

```
"I ran git rebase and now I have 30 conflicts. What do I do?"

"We need a branching strategy for a team of 8 with biweekly releases"

"I accidentally force-pushed over my colleague's commits. Can we recover?"

"We want to split this monorepo into separate repos without losing history"

"There's an AWS key in our git history from 6 months ago. Help me remove it."

"Should we squash-merge or rebase-merge our feature branches?"
```

## Limitations

- Cannot inspect remote repository state directly — needs the user to provide `git log`, `git reflog`, etc.
- Strategy recommendations depend on team context — there is no universally correct branching model
- History rewriting (filter-repo, force-push) requires coordination with all collaborators
- Cannot recover commits that have been garbage collected (typically 90 days after orphaning)

## Customization

Fork and modify for:

- Organization-specific branching policies and naming conventions
- Monorepo-specific tooling integration (Nx, Turborepo, Bazel)
- Compliance requirements around commit signing and audit trails
- Inner-source contribution workflows with fork-based development
