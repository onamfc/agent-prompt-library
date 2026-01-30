# PR Reviewer

Reviews pull requests with structured feedback on code quality, testing, and craftsmanship — categorized as The Good, The Bad, and The Ugly.

## When to Use

- Reviewing pull requests before merge
- Getting a second opinion on code changes
- Learning what makes code good or bad
- Establishing quality standards for a team
- Training developers on craftsmanship principles

## When NOT to Use

- Automated CI/CD checks (this is for human-readable reviews)
- Style/formatting issues (use linters instead)
- Reviewing auto-generated code
- Quick prototype or spike code explicitly marked as throwaway

## Model Recommendations

| Model       | Suitability | Notes                                              |
|-------------|-------------|----------------------------------------------------|
| Claude Code | Excellent   | Can access full PR context and codebase            |
| Cursor      | Excellent   | Great for reviewing changes in IDE context         |
| Claude API  | Good        | Requires pasting diff; works well with clear input |

## Context Requirements

This agent works best with:

- The full PR diff or changed files
- Context about the PR's purpose (feature, bugfix, refactor)
- Access to surrounding code for understanding patterns
- Information about team conventions if non-standard

## Principles Referenced

The agent's feedback is grounded in:

- **Refactoring** (Fowler) — Code smells, safe transformations
- **The Pragmatic Programmer** (Hunt & Thomas) — DRY, orthogonality, broken windows
- **Clean Code** (Martin) — Naming, functions, comments, formatting
- **Design Patterns** (GoF) — Appropriate pattern usage, composition over inheritance

## Limitations

- Cannot run tests or verify code actually works
- Style preferences may differ from team conventions
- May not know project-specific patterns without context
- Craftsmanship scores are subjective guidelines, not metrics

## Customization

Fork and modify for:

- Team-specific coding standards
- Language-specific idioms and patterns
- Different output formats or scoring systems
- Integration with specific PR platforms (GitHub, GitLab, etc.)
- Adjusting strictness level (startup vs. enterprise)
