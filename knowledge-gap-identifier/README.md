# Knowledge Gap Identifier

Detects missing, unclear, or insufficient information that materially impacts decision quality or execution success. This agent acts as an analytical skeptic, surfacing critical unknowns early to prevent wasted effort and poor decisions.

## When to Use

- Reviewing requirements before starting implementation
- Analyzing project plans for missing information
- Validating assumptions before making architectural decisions
- Assessing feasibility when context seems incomplete
- Pre-mortem analysis of proposals or designs
- Clarifying underspecified tasks or user requests

## When NOT to Use

- When all requirements are clearly defined and validated
- For straightforward tasks with no ambiguity
- When you're intentionally prototyping with known unknowns
- For post-implementation code review (use Code Reviewer)

## Model Recommendations

| Model       | Suitability | Notes |
|-------------|-------------|-------|
| Claude Code | Excellent   | Can analyze full project context to identify gaps |
| Cursor      | Good        | Effective for analyzing specific files or features |
| Claude API  | Excellent   | Works well for analyzing requirements documents |

## Context Requirements

This agent works best with:

- Requirements documents or task descriptions to analyze
- Existing project context (architecture, constraints, goals)
- Stakeholder expectations or success criteria
- Related decisions or dependencies
- Timeline or resource constraints

## Example Prompts

```
"Analyze these feature requirements for missing information"

"Review this implementation plan - what critical details are we missing?"

"We need to add payment processing. What do we need to know before deciding?"

"Identify knowledge gaps in this API design before I start building"

"What assumptions are we making that could derail this project?"
```

## Limitations

- Does not make decisions or fill gaps with assumptions
- Requires sufficient context to identify meaningful gaps
- Cannot validate whether information is factually correct
- Does not prioritize business value — focuses on decision quality
- May identify low-priority gaps that are acceptable to ignore

## Customization

Fork and modify for:

- Domain-specific checklists (e.g., compliance requirements for finance)
- Organization-specific decision frameworks
- Integration with your planning templates or processes
- Custom severity classifications aligned with your risk tolerance
