# Security Analyst

Identifies vulnerabilities, assesses security risks, and provides actionable remediation guidance for applications and infrastructure.

## When to Use

- Reviewing code changes for security implications
- Assessing new features before deployment
- Auditing authentication and authorization logic
- Evaluating third-party dependencies for vulnerabilities
- Planning security improvements for existing systems
- Preparing for compliance audits

## When NOT to Use

- General code review (use Code Reviewer)
- Performance optimization
- Writing new features from scratch
- Infrastructure deployment decisions

## Model Recommendations

| Model       | Suitability | Notes |
|-------------|-------------|-------|
| Claude Code | Excellent   | Full codebase access enables thorough analysis |
| Cursor      | Excellent   | Good for inline security review during development |
| Claude API  | Good        | Effective for reviewing specific code snippets |

## Context Requirements

This agent works best with:

- Access to the full codebase or relevant modules
- Understanding of the application's trust boundaries
- Knowledge of what data is sensitive
- Information about the deployment environment
- Existing security controls and requirements

## Limitations

- Cannot perform dynamic testing (fuzzing, penetration testing)
- Static analysis only — may miss runtime-specific issues
- Requires context about business logic to assess impact accurately
- Cannot guarantee finding all vulnerabilities

## Customization

Fork and modify for:

- Organization-specific compliance requirements (add your framework mappings)
- Custom severity ratings aligned with your risk appetite
- Industry-specific security requirements (healthcare, finance, etc.)
- Integration with specific security tools (SAST, SCA)
