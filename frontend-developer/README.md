# Frontend Developer

Builds responsive, accessible, and performant user interfaces with modern web technologies.

## When to Use

- Building new UI components or pages
- Implementing designs from mockups or wireframes
- Fixing layout, styling, or responsive issues
- Improving accessibility compliance
- Optimizing frontend performance
- Working with React, Vue, Angular, or vanilla JS/TS

## When NOT to Use

- Backend API development (use Backend API Developer)
- Mobile app development (use React Native Developer)
- Infrastructure or deployment (use Infrastructure Agent)
- General debugging (use Debugging Specialist)

## Model Recommendations

| Model       | Suitability | Notes |
|-------------|-------------|-------|
| Claude Code | Excellent   | Full project context enables consistent patterns |
| Cursor      | Excellent   | Inline component development with file context |
| Claude API  | Good        | Works well for isolated component questions |

## Context Requirements

This agent works best with:

- Design mockups or wireframes (if implementing designs)
- Existing component library patterns
- Project's styling approach (Tailwind, CSS modules, etc.)
- Framework version and conventions used
- Target browser support requirements

## Limitations

- Cannot run or preview the UI (needs user feedback on visual output)
- Cannot perform real accessibility audits (recommends manual testing)
- Static code analysis only — runtime behavior needs user verification
- Design decisions require user input on aesthetics

## Customization

Fork and modify for:

- Specific framework conventions (Next.js, Nuxt, SvelteKit)
- Company design system guidelines
- Stricter accessibility requirements (WCAG AAA)
- Specific CSS methodology (BEM, OOCSS)
