# PR Annotator

Enriches pull request descriptions with clickable GitHub diff links that jump directly to the referenced lines of code.

## When to Use

- After writing a PR description that references specific code changes
- When preparing a detailed PR for team review and you want every bullet to be navigable
- When documenting changes across many files and reviewers need quick access to each change
- After generating a PR description with another agent and want to add source links

## When NOT to Use

- For PRs with trivial changes (single file, few lines) where links add no value
- When the PR has not been pushed to GitHub yet (links won't resolve)
- For draft descriptions that are still being written and lines may shift

## Model Recommendations

| Model       | Suitability | Notes                                                                 |
|-------------|-------------|-----------------------------------------------------------------------|
| Claude Code | Excellent   | Best fit — has direct access to git, file reading, and shell commands |
| Cursor      | Good        | Can read files and run terminal commands in the IDE                   |
| Claude API  | Limited     | Needs file contents and git diff provided in the prompt context       |

## Context Requirements

This agent works best with:

- Access to the git repository (to run `git diff` and read files)
- The PR number and GitHub repository path (owner/repo)
- A written PR description with bullet points referencing code changes
- The base branch name (defaults to `main`)

## Limitations

- Line numbers are based on the current branch HEAD — if the branch changes after annotation, links may drift
- GitHub's diff anchor format (`#diff-{sha256}R{line}`) is specific to GitHub and won't work on GitLab, Bitbucket, etc.
- For very large PRs (50+ files), the annotation process requires reading many files and may take time
- Removed lines can only link to the file-level diff, not specific deleted line numbers

## Customization

Fork and modify for:

- **GitLab/Bitbucket** — change the URL format to match your platform's diff anchor scheme
- **Auto-generation** — combine with a PR description writer agent to generate and annotate in one pass
- **CI integration** — run as a post-push hook to automatically annotate PR descriptions
