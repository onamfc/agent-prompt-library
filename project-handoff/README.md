# Project Handoff

Produces branch handoff documents that let a fresh AI session resume work with no loss of continuity. Captures state, decisions, reasoning, open questions, and gotchas.

## When to Use

- Ending a session where work will resume later in a fresh context
- Approaching a context limit and needing to checkpoint state before a new session
- Passing a branch to another developer or AI session
- Reaching a milestone on a long-running branch and wanting a snapshot
- After a deep debugging session that uncovered non-obvious state

## When NOT to Use

- Single-commit, trivial branches with nothing to hand off
- Documenting a completed feature for human readers — use a PR description or changelog
- Generating release notes — use [Changelog Writer](../changelog-writer/)
- Producing project-wide documentation — use [Documentation Writer](../documentation-writer/)
- Capturing meeting notes, planning docs, or specs — this agent is for in-flight work, not pre-work

## Model Recommendations

| Model       | Suitability | Notes                                                                              |
|-------------|-------------|------------------------------------------------------------------------------------|
| Claude Code | Excellent   | Direct access to git state, files, conversation context, and task tracking         |
| Cursor      | Excellent   | Can inspect repo state, current diff, and active editor context                    |
| Claude API  | Limited     | Requires the user to paste git output, file contents, and conversation manually    |

## Context Requirements

This agent works best with:

- Access to git state (branch name, commits ahead of base, uncommitted changes, diff)
- The current conversation history (to extract user preferences, corrections, and validated approaches)
- Project convention files (e.g., `CLAUDE.md`, `AGENTS.md`, contributor docs)
- Task tracking state, if available in the host environment

## Optimized For AI Ingestion

The output is **optimized for ingestion by another AI session**, not for casual human reading. That means:

- Dense, structured, tabular where possible
- Absolute file paths instead of relative or vague references
- No filler or marketing copy
- Explicit hedges on uncertain claims
- Honest flagging of incomplete or untested work

A human can still read the output and find it useful — but it won't read like a polished design doc.

## Output Location

Default path:

```
.handoffs/HANDOFF-<branch-name>-<YYYYMMDD>.md
```

If the project already uses a different convention for in-progress notes (e.g., `.devnotes/`, a `.brandon/` directory, or any other established location), the agent will respect that. It checks the existing structure before creating a new one.

## Doc Structure (11 Sections)

1. TL;DR
2. Branch Context (branch, base, commits ahead, uncommitted, last commit)
3. Goal & Motivation
4. State of Work (Done / In Progress / Not Started)
5. Key Decisions (with reasoning, alternatives, invalidation triggers)
6. Files Touched
7. Conventions Established
8. Open Questions
9. Next Steps
10. Gotchas & Landmines
11. References

## Limitations

- Cannot infer user intent or rationale that wasn't expressed during the session — if the user never explained *why*, the agent will note "rationale not captured" rather than fabricate one
- Cannot verify claims about external systems (deploys, CI runs, third-party services) — flags them as unverified
- The "Honesty Audit" pass relies on the agent's awareness of its own gaps; a session that never ran tests should expect a doc that says so, but ambiguous coverage may slip through
- Quality of the handoff is bounded by the quality of the conversation — vague or abandoned threads produce thin sections

## Customization

Fork and modify for:

- Different output paths or filename conventions
- Additional sections specific to your team's workflow (e.g., "Stakeholders Notified", "Deployment State", "Feature Flag Status")
- Integration with task trackers or issue boards (auto-link Linear/Jira tickets)
- Pairing with a complementary "Handoff Ingestor" agent that reads the doc at the start of new sessions
- Auto-committing the handoff doc as part of the workflow
- Multi-branch handoffs for monorepos where one session spans multiple branches
