# Changelog Writer

Generates and maintains changelogs following the Keep a Changelog conventions for consistent, human-readable release documentation.

## When to Use

- Creating a changelog for a new project
- Adding entries from recent commits or PRs
- Preparing release notes for a new version
- Converting ad-hoc release notes to proper changelog format
- Reviewing and improving existing changelog quality

## When NOT to Use

- Generating machine-readable release metadata (use conventional commits tooling)
- Writing marketing release announcements
- Creating detailed migration guides (use separate docs)
- Documenting internal-only changes

## Model Recommendations

| Model       | Suitability | Notes                                           |
|-------------|-------------|-------------------------------------------------|
| Claude Code | Excellent   | Can read commits and diffs directly             |
| Cursor      | Excellent   | Good for updating changelog alongside code      |
| Claude API  | Good        | Requires pasting commits/changes manually       |

## Context Requirements

This agent works best with:

- Git commit history or PR descriptions
- Repository URL (for generating comparison links)
- Current version number
- Existing CHANGELOG.md (if updating)

## Keep a Changelog Conventions

The agent follows [keepachangelog.com](https://keepachangelog.com) standards:

**Change Categories (in order):**
- Added — New features
- Changed — Changes in existing functionality
- Deprecated — Soon-to-be removed features
- Removed — Now removed features
- Fixed — Bug fixes
- Security — Vulnerability fixes

**Key Principles:**
- Changelogs are for humans, not machines
- Latest version first (reverse chronological)
- Dates in ISO 8601 format (YYYY-MM-DD)
- Semantic Versioning for version numbers
- Comparison links at the bottom

## Limitations

- Cannot automatically detect breaking changes (relies on commit messages)
- Comparison links require repository URL to be provided
- May need clarification on vague commit messages
- Internal refactors may be incorrectly categorized without context

## Customization

Fork and modify for:

- Different date formats (though ISO 8601 is recommended)
- Additional categories for specific project needs
- Integration with conventional commits
- Automated version suggestion rules
- Language/localization of category headers
