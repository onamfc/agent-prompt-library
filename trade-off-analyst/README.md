# Trade-Off Analyst

Evaluates competing options and decisions by explicitly analyzing their benefits, costs, risks, and second-order effects. This agent provides structured, objective analysis to support informed, defensible decision-making.

## When to Use

- Choosing between multiple technical approaches or architectures
- Evaluating framework, library, or tool selection
- Assessing design patterns or implementation strategies
- Making build-vs-buy decisions
- Analyzing performance vs. maintainability trade-offs
- Deciding on short-term fixes vs. long-term refactoring

## When NOT to Use

- When there's only one viable option
- For straightforward decisions with clear best practices
- When you need immediate action without analysis
- For decisions that have already been made (use Code Reviewer)

## Model Recommendations

| Model       | Suitability | Notes |
|-------------|-------------|-------|
| Claude Code | Excellent   | Can analyze full codebase context for impact assessment |
| Cursor      | Good        | Effective for localized trade-off analysis |
| Claude API  | Excellent   | Works well for architectural and design discussions |

## Context Requirements

This agent works best with:

- Clear description of the decision being made
- List of options or alternatives to compare
- Project constraints (time, budget, team skills)
- Success criteria or priorities (performance, maintainability, cost)
- Existing architecture or technical decisions
- Long-term goals and roadmap context

## Example Prompts

```
"Compare REST vs GraphQL for our API layer"

"Should we use Redis or in-memory caching? Analyze the trade-offs"

"Evaluate migrating from monolith to microservices"

"Analyze performance vs maintainability for this optimization"

"Compare serverless vs container deployment for this service"

"Should we refactor now or ship the feature with technical debt?"
```

## Limitations

- Cannot predict future requirements with certainty
- Requires clear priorities to make meaningful recommendations
- May not have domain-specific knowledge for specialized decisions
- Cannot measure actual performance — provides analytical assessment
- Does not make final decisions — provides analysis for decision-makers

## Customization

Fork and modify for:

- Industry-specific evaluation criteria (healthcare, finance, gaming)
- Organization-specific risk tolerance and priorities
- Custom decision matrices or scoring frameworks
- Integration with your architecture decision records (ADRs)
- Domain-specific trade-off dimensions
