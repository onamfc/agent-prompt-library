# Testing Specialist

Designs and implements comprehensive test suites including unit, integration, and end-to-end tests.

## When to Use

- Writing tests for new features or bug fixes
- Adding test coverage to existing code
- Debugging failing or flaky tests
- Designing a testing strategy for a project
- Setting up testing infrastructure
- Reviewing test code quality

## When NOT to Use

- Writing the feature code itself (use appropriate developer agent)
- Performance testing and profiling
- Security testing (use Security Analyst)
- General debugging without test context

## Model Recommendations

| Model       | Suitability | Notes |
|-------------|-------------|-------|
| Claude Code | Excellent   | Full codebase context enables accurate mocking and integration |
| Cursor      | Excellent   | Inline test writing alongside feature code |
| Claude API  | Good        | Works for isolated unit test questions |

## Context Requirements

This agent works best with:

- The code being tested (functions, classes, modules)
- Existing test patterns in the project
- Testing framework configuration (Jest, Vitest, Pytest, etc.)
- Understanding of external dependencies to mock
- Knowledge of what behaviors are critical to test

## Limitations

- Cannot run tests (needs user to execute and report results)
- Cannot debug runtime test failures without stack traces
- Static analysis only — may miss timing-sensitive issues
- E2E test selectors need user verification in the actual UI

## Customization

Fork and modify for:

- Specific testing frameworks (Jest, Mocha, Pytest, RSpec)
- Organization testing standards and coverage requirements
- Domain-specific testing patterns (financial calculations, ML pipelines)
- Performance or load testing focus
