# Code Reviewer

A Senior Code Reviewer persona focused on thorough, constructive code review that catches issues while helping developers improve.

## When to Use

- Reviewing pull requests before merge
- Auditing existing code for quality issues
- Getting feedback on implementation approaches
- Security-focused code review
- Pre-commit sanity checks on your own code

## When NOT to Use

- Writing new code (use a development agent)
- Architectural decisions (use an architect agent)
- Debugging runtime issues (use a debugging agent)
- Automated linting (use actual linters)

## Model Recommendations

| Model | Suitability | Notes |
|-------|-------------|-------|
| Claude Code | Excellent | Can read full PR context, follow references |
| Cursor | Good | Works well for file-level review |
| Claude API | Good | Effective with diff content in prompt |

## Context Requirements

This agent works best with:

- The diff or changed code
- Context about what the change is supposed to do
- Access to related files for full understanding
- Knowledge of project conventions (if non-standard)

## Example Prompts

```
"Review this PR for our payments service"

"Check this function for security issues"

"I'm about to merge this — any concerns?"

"Review with focus on performance — this is a hot path"
```

## Limitations

- Cannot run the code — reviews statically
- May miss issues requiring deep domain knowledge
- Style feedback based on general best practices, not project-specific rules
- Security review is not a replacement for security specialists on sensitive code
