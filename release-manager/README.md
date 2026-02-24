# Release Manager

Orchestrates the full software release lifecycle — merging PRs, determining version bumps, updating changelogs, tagging, pushing, and creating GitHub releases with consistent conventional commits.

## When to Use

- Merging one or more PRs into a main branch and cutting a release
- Bumping versions and publishing a new release from current state
- Creating GitHub releases for existing tags that are missing them
- Preparing hotfix releases from a specific branch
- Catching up on release artifacts (changelogs, tags, GitHub releases) that fell behind

## When NOT to Use

- Making code changes or bug fixes (this agent packages and publishes, it doesn't write code)
- Setting up CI/CD pipelines (use the infrastructure agent)
- Writing detailed migration guides (use technical writing agents)
- Managing dependency updates or renovate/dependabot PRs

## Model Recommendations

| Model       | Suitability | Notes                                                    |
|-------------|-------------|----------------------------------------------------------|
| Claude Code | Excellent   | Full git/gh CLI access for end-to-end automated releases |
| Cursor      | Good        | Can edit version files and changelogs, limited CLI access |
| Claude API  | Limited     | Can draft changelogs and release notes, no CLI execution  |

## Context Requirements

This agent works best with:

- Access to the git repository (local clone with remote configured)
- GitHub CLI (`gh`) installed and authenticated
- Knowledge of which PRs or branches to include in the release
- The project's version file locations (e.g., `package.json`, multiple packages)
- Existing CHANGELOG.md (if updating rather than creating)

## Key Conventions

- **Merge strategy:** `--no-ff` merge commits by default (preserves branch history)
- **Merge commit format:** `Merge PR #N: Brief description`
- **Release commit format:** `chore(release): vX.Y.Z` (conventional commit)
- **Tags:** Annotated tags (`git tag -a vX.Y.Z -m "vX.Y.Z"`)
- **Changelog:** [Keep a Changelog](https://keepachangelog.com) format
- **Versioning:** [Semantic Versioning](https://semver.org) (MAJOR.MINOR.PATCH)
- **No AI attribution:** Never includes co-author lines or tool references in commits

## Example Prompts

```
"Merge PR #5 into main, bump the version, update the changelog, and push"

"Create a patch release from the current state of main"

"We have 3 PRs ready to merge — #10, #11, #12. Release them as v2.0.0"

"Tag v1.5.0 exists but there's no GitHub release for it. Can you create one?"

"Prepare a hotfix release for the auth bug fix on the hotfix/auth branch"
```

## Limitations

- Cannot auto-resolve merge conflicts — stops and reports for manual resolution
- Cannot determine version type (major/minor/patch) when change impact is ambiguous — will ask
- Does not modify CI/CD workflows or deployment configurations
- Requires `gh` CLI for GitHub release creation
- Cannot make code changes — only packages and publishes existing work

## Customization

Fork and modify for:

- Different merge strategies (squash, rebase)
- Alternative changelog formats (conventional-changelog, auto-changelog)
- Different version file locations or formats (pyproject.toml, Cargo.toml, build.gradle)
- Monorepo release orchestration with independent package versioning
- Release branch workflows (release/vX.Y.Z branches)
- Automated release note generation from conventional commit parsing
