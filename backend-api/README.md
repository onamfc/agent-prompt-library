# Backend API Developer

A Senior Backend API Developer persona focused on building secure, reliable, and performant server-side applications and APIs.

## When to Use

- Designing new API endpoints
- Building server-side business logic
- Working with databases (queries, schemas, migrations)
- Implementing authentication and authorization
- Debugging backend issues
- API performance optimization

## When NOT to Use

- Frontend development (use a frontend agent)
- Infrastructure/DevOps (use an infrastructure agent)
- Mobile app development (use a mobile agent)
- Pure database administration (for complex DBA work)

## Model Recommendations

| Model | Suitability | Notes |
|-------|-------------|-------|
| Claude Code | Excellent | Can see full project context, apply changes |
| Cursor | Excellent | Good for working within existing codebase |
| Claude API | Good | Works well for design discussions and reviews |

## Context Requirements

This agent works best with:

- Understanding of the project's framework and language
- Database technology being used
- Existing API patterns in the codebase
- Authentication approach (if already established)

## Example Prompts

```
"Design a REST API for user management (CRUD + auth)"

"This query is slow. Help me optimize it."

"Add an endpoint to handle file uploads"

"Implement rate limiting for the public API"

"Review this endpoint for security issues"
```

## Limitations

- Works with the project's existing stack — doesn't prescribe frameworks
- Focuses on application-level concerns, not infrastructure
- Security review is thorough but not a replacement for security audit
- Database work is at application level, not DBA-level administration
