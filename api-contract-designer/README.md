# API Contract Designer

Design, review, and evolve API contracts that serve as the source of truth between producers and consumers.

## When to Use

- Designing a new REST, GraphQL, or async API from scratch
- Reviewing an existing OpenAPI/GraphQL spec for consistency and completeness
- Evaluating proposed API changes for backwards compatibility
- Standardizing naming, structure, and patterns across an API surface
- Planning versioning, deprecation, or migration strategies
- Preparing contracts for SDK generation or documentation publishing

## When NOT to Use

- Implementing the API (use the Backend API Developer agent)
- Infrastructure or deployment concerns (use the Infrastructure agent)
- Security architecture decisions (use the Security Analyst agent)
- Performance profiling of live endpoints (this agent works on contracts, not runtime)

## Model Recommendations

| Model | Suitability | Notes |
|-------|-------------|-------|
| Claude Code | Excellent | Can read existing specs, codebase patterns, and apply changes directly |
| Cursor | Excellent | Good for iterating on spec files within the project |
| Claude API | Good | Strong for design discussions, reviews, and schema generation |

## Context Requirements

This agent works best with:

- Existing API specification files (OpenAPI, GraphQL SDL, AsyncAPI, Protobuf)
- Examples of current endpoint patterns in the codebase
- Knowledge of which consumers exist (web, mobile, third-party)
- Any existing API style guide or naming conventions

## Example Prompts

```
"Design the API contract for a multi-tenant billing service"

"Review this OpenAPI spec for consistency issues"

"Is changing this field from optional to required a breaking change?"

"We need to deprecate v1 of the payments API. Plan the migration."

"Standardize error responses across all our endpoints"

"Design a pagination strategy for our search endpoints"
```

## Limitations

- Focuses on the contract surface, not implementation details
- Consistency recommendations require visibility into the broader API surface
- Cannot validate runtime behavior — only the declared contract
- Schema generation follows project conventions; does not prescribe a format

## Customization

Fork and modify for:

- Organization-specific API style guides (e.g., Google AIP, Microsoft, Zalando)
- Industry-specific contract requirements (healthcare HL7/FHIR, finance FIX/ISO 20022)
- Internal API governance workflows and review checklists
- Specific specification format enforcement (e.g., OpenAPI 3.1 only)
