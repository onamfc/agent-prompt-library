# Prompt Critic

Evaluates, stress-tests, and improves prompts used by humans or other agents to make them clearer, more robust, and more reliable.

## When to Use

- Creating or modifying agent prompts in your library
- Debugging unexpected or inconsistent agent behavior
- Standardizing prompts across teams or workflows
- Preparing prompts for production use
- Identifying edge cases and failure modes in instructions
- Reviewing prompts before deploying them to users

## When NOT to Use

- Writing prompts from scratch (use this for review, not creation)
- General code review or debugging
- Testing actual agent execution (this reviews the prompt text, not runtime behavior)
- Non-prompt documentation editing

## Model Recommendations

| Model       | Suitability | Notes |
|-------------|-------------|-------|
| Claude Code | Excellent   | Can analyze prompts in context of full agent library |
| Cursor      | Good        | Useful for inline prompt editing and review |
| Claude API  | Excellent   | Great for isolated prompt review and improvement |

## Context Requirements

This agent works best with:

- The full prompt text to be reviewed
- Information about the intended use case and target model
- Examples of desired vs. undesired agent behavior (if available)
- Context about the system or workflow the agent will operate in
- Any existing issues or failure cases observed

## Limitations

- Cannot test actual agent execution or runtime behavior
- Analysis quality depends on understanding the intended use case
- May not catch issues specific to certain model versions or platforms
- Cannot guarantee all edge cases will be identified
- Focuses on prompt structure, not domain expertise validation

## Customization

Fork and modify for:

- Organization-specific prompt templates or conventions
- Domain-specific validation criteria (e.g., safety, compliance)
- Integration with prompt versioning systems
- Custom evaluation metrics for your use cases
- Platform-specific prompt optimization (Claude Code vs. Cursor, etc.)

## Example Prompts

### Basic Review
```
Review this agent prompt for clarity and robustness:
[paste prompt here]
```

### Targeted Analysis
```
This agent sometimes fails to handle edge cases when processing user input.
Can you identify potential failure modes in the prompt?
[paste prompt here]
```

### Improvement Request
```
Improve this prompt to make it more specific about output format:
[paste prompt here]
```

### Consistency Check
```
We have 5 agents in our library. Review this new prompt to ensure it follows
the same conventions and structure as the existing ones.
```
