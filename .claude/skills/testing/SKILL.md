---
name: testing
description: Plan and implement tests for discovery, itinerary feasibility, budget estimates, APIs, and traveller journeys.
---
Use existing test tools. Prioritize pure unit tests for constraints and cost arithmetic; API tests for validation/permissions/errors; integration tests for persistence and adapters; frontend tests for forms/edits/warnings; end-to-end tests for the core journey. Use synthetic fixtures. Mock maps/LLM in normal tests; keep live integration tests opt-in. Every bug fix needs a regression test. Report exact commands and results.
