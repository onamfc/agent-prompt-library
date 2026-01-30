# Brand Architect

Analyzes codebases to understand the business domain and generates creative company/product name suggestions.

## When to Use

- Starting a new project and need a company or product name
- Rebranding an existing product
- Naming a new feature or sub-product
- Brainstorming name ideas with creative rationale
- Getting an outside perspective on what your code communicates

## When NOT to Use

- Legal trademark searches (consult a trademark attorney)
- Domain availability checks (use a registrar)
- Logo or visual identity design
- Marketing copy or tagline writing

## Model Recommendations

| Model       | Suitability | Notes                                                    |
|-------------|-------------|----------------------------------------------------------|
| Claude Code | Excellent   | Can directly scan codebase for deep analysis             |
| Cursor      | Excellent   | Full codebase context enables thorough understanding     |
| Claude API  | Good        | Requires pasting code/docs manually; still generates well|

## Context Requirements

This agent works best with:

- Access to the full codebase (or key files: README, main modules, models)
- Any existing product descriptions or pitch decks
- Information about target audience and competitors
- Stated preferences for naming style (playful vs. serious, etc.)

## Limitations

- Cannot verify domain availability in real-time
- Cannot perform actual trademark searches
- Name suggestions should be validated before legal/business commitment
- Cultural and linguistic nuances may require native speaker review for international markets

## Customization

Fork and modify for:

- Industry-specific naming conventions (e.g., pharma, legal tech)
- Regional/language preferences
- Company naming policies or brand guidelines
- Integration with domain checking APIs
