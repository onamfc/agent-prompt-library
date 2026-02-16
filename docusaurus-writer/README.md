# Docusaurus Writer

Analyzes codebases and produces user-facing product documentation structured for Docusaurus sites, including conceptual articles, feature guides, tutorials, API reference, and getting started content.

## When to Use

- Creating public-facing product documentation from an existing codebase
- Building a Docusaurus documentation site for a product or platform
- Documenting product features, APIs, and SDKs for external users
- Writing getting started guides, tutorials, and conceptual articles
- Generating comparison and migration content for competitive positioning
- Restructuring existing documentation into Docusaurus conventions

## When NOT to Use

- Internal codebase documentation or architecture docs (use Documentation Writer)
- Writing inline code comments or developer-facing docstrings (use Technical Writer)
- README files for open-source libraries (use Technical Writer)
- Marketing copy or promotional landing pages
- Documentation that does not target a Docusaurus site

## Model Recommendations

| Model       | Suitability | Notes |
|-------------|-------------|-------|
| Claude Code | Excellent   | Full codebase exploration enables comprehensive feature discovery and accurate documentation |
| Cursor      | Good        | Effective for documenting specific features or modules within a larger site |
| Claude API  | Limited     | Best for smaller codebases or when supplementing with feature descriptions |

## Context Requirements

This agent works best with:

- Access to the complete codebase to analyze features and workflows
- API route definitions, controllers, and data models
- Existing documentation or product descriptions to build upon
- Configuration files, environment examples, and SDK source code
- Access to run exploration commands for comprehensive codebase analysis
- Knowledge of the target audience (end-users, integrating developers, or both)

## Example Prompts

**Full documentation site:**
> "Analyze this codebase and create a complete Docusaurus documentation site covering getting started, feature guides, API reference, and conceptual articles."

**Feature documentation:**
> "Document the link creation feature for our docs site. Cover both the dashboard workflow and the API approach with working examples."

**Getting started guide:**
> "Create a getting started guide that gets a new user from signup to their first successful API call in under 5 minutes."

**Conceptual article:**
> "Write a Learn article explaining what mobile attribution is, why it matters, and how our platform approaches it. Target both technical and non-technical readers."

**API reference:**
> "Generate API reference documentation for all public endpoints. Include authentication, request/response examples, and error codes."

**Proposed site structure:**
> "Review this codebase and propose a documentation site structure with sidebar organization, estimated page counts, and priority order for writing."

## Limitations

- Cannot document features that do not exist in the codebase — needs access to actual code
- May not capture product positioning or business context that exists only in team knowledge
- Documentation accuracy depends on codebase exploration depth and code clarity
- Cannot determine intended user experience for ambiguous implementations without input
- Produces Docusaurus-specific output — adaptation needed for other documentation platforms
- Best suited for codebases that can be explored incrementally within context limits

## Customization

Fork and modify for:

- Organization-specific documentation templates and style guides
- Required sections for compliance or regulatory documentation
- Product-specific terminology glossaries
- Custom Docusaurus plugins or MDX components your site uses
- Specific sidebar structures or navigation patterns
- Integration with documentation review workflows
