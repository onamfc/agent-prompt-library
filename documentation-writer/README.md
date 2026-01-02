# Documentation Writer

Analyzes existing codebases and generates comprehensive documentation including project overviews, architecture guides, and onboarding materials.

## When to Use

- Onboarding new developers to an unfamiliar codebase
- Creating documentation for undocumented projects
- Generating architecture documentation for technical reviews
- Capturing knowledge before team transitions
- Preparing documentation for compliance or audits
- Understanding a new project you've inherited

## When NOT to Use

- Writing documentation for code you're actively developing (use Technical Writer)
- Creating user-facing product documentation
- Writing API reference docs from scratch (use Technical Writer)
- Marketing or promotional content

## Model Recommendations

| Model       | Suitability | Notes |
|-------------|-------------|-------|
| Claude Code | Excellent   | Full codebase exploration enables comprehensive analysis |
| Cursor      | Good        | Works well for documenting specific modules or components |
| Claude API  | Limited     | Best for smaller codebases that fit in context |

## Context Requirements

This agent works best with:

- Access to the complete codebase
- Package/dependency files (package.json, requirements.txt, etc.)
- Existing documentation to build upon
- Configuration files and environment examples
- Access to run exploration commands (ls, find, etc.)

## Example Prompts

**Full project documentation:**
> "Analyze this codebase and create comprehensive documentation covering the architecture, key components, and how to get started as a new developer."

**Architecture focus:**
> "Document the architecture of this project. Map out the main components, how they interact, and the data flow through the system."

**Onboarding guide:**
> "Create an onboarding guide for new developers joining this project. Cover setup, key concepts, and common workflows."

**Specific area:**
> "Document the authentication system in this codebase — how it works, where the code lives, and how to extend it."

## Limitations

- Cannot document code it hasn't analyzed — needs codebase access
- May miss undocumented business logic that only exists in tribal knowledge
- Cannot determine original intent for unclear code without developer input
- Documentation accuracy depends on code exploration depth
- Best for codebases that can fit within context window or be explored incrementally

## Customization

Fork and modify for:

- Organization-specific documentation templates
- Required sections for compliance (SOC2, HIPAA, etc.)
- Integration with documentation platforms (Confluence, Notion, etc.)
- Domain-specific terminology and conventions
