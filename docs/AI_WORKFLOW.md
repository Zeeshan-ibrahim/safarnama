# Claude Code workflow

1. Discover: inspect repository, docs, tests, and conventions.
2. Plan: agree outcome, scope, acceptance criteria, dependencies, and risks.
3. Implement: one reviewable vertical slice at a time.
4. Verify: run targeted tests, then relevant broader checks.
5. Review: use QA reviewer or code-review skill.
6. Record: update decisions and docs when behaviour or architecture changes.

Claude is not the product owner. Human approval is required for paid APIs, production data, destructive DB operations, production migrations, deployments, cloud changes, secrets, and external commitments.

First session is assessment-only. Use `CLAUDE_BOOTSTRAP_PROMPT.md`. Do not ask Claude to build the whole product in one prompt.
