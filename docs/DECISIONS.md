# Decision log

Add newest accepted decisions at the top with date, status, context, decision, consequences, and owner.

## Delivery approach and first slice: 24 November 2026
- **Status:** accepted. **Owner:** product owner.
- **Context:** the roadmap (doc 07) asks for interviews, competitor research, a pilot dataset and prototype validation before committing to the full MVP.
- **Decision:**
  - The first slice is provenance-first destination discovery (PRD FR-02), split into five milestones: foundation, data foundation, backend discovery, frontend discovery, and integration and QA.
  - Each milestone gets its own branch and PR and needs owner review before the next one starts.
  - Product validation runs alongside the foundation work. Approving a milestone does not commit us to the full MVP. The go/no-go decision still happens before itinerary, budget or editing work.
- **Consequences:** only Milestone 1 is approved so far. Later milestones need separate approval.

## Milestone 1 stack and tooling: 24 November 2026
- **Status:** accepted. **Owner:** product owner.
- **Decision:**
  - Monorepo with `apps/web` (Next.js 16, TypeScript, Tailwind CSS 4, pnpm) and `apps/api` (FastAPI, Python 3.13, uv).
  - PostgreSQL 18 + PostGIS 3.7 runs locally through Docker Compose on `127.0.0.1:5433`.
  - SQLAlchemy 2 and Alembic are approved. They will be added in Milestone 2.
  - Tooling: pytest, Vitest + Testing Library, Ruff, mypy (strict), ESLint, Prettier. CI runs on GitHub Actions.
  - TypeScript is pinned to 6.0.x because typescript-eslint does not support TypeScript 7 (it requires `<6.1.0`).
  - ESLint is pinned to 9.x because the React, jsx-a11y and import plugins used by `eslint-config-next` only support up to ESLint 9.
- **Constraints:**
  - No paid maps or LLM APIs.
  - No Redis or worker until a feature needs one.
  - No production resources, deployments or real secrets.
- **Consequences:** revisit the TypeScript and ESLint pins when the lint plugins add support for newer versions.

## Data and discovery constraints: 24 November 2026
- **Status:** accepted. **Owner:** product owner.
- Regions are configurable database records with a coverage status. No pilot region is hardcoded.
- The four initial freshness data types are `destination_profile`, `attraction_profile`, `seasonal_access` and `visit_duration`. Their policies stay unset until verification rules are agreed. Records without a policy show as "not assessed".
- Automated tests use fictional fixtures. The UI must always label synthetic data visibly and never present it as a real recommendation.
- Discovery filters by month. Interest tags are configurable, and the final taxonomy will be agreed before real curated data is added.
- Milestone 2 will include a short ADR on a shared `places` table versus separate destination and attraction tables. It will pick the simplest model that doesn't block route planning.

## Accepted direction: 24 November 2026
- Pakistan-first domestic leisure travel.
- Planning-first MVP: discovery, itinerary preview, route feasibility, transparent estimates, manual editing, saved trips.
- Marketplace, provider booking, payments, full hotel inventory, native apps, and international travel are later phase.
- Hybrid engine: deterministic rules and structured data enforce route feasibility and cost arithmetic; AI interprets preferences and explains supported options.
- Proposed stack: Next.js/TypeScript, FastAPI/Python, PostgreSQL/PostGIS, Redis/worker, provider-agnostic LLM adapter, maps provider TBD, object storage if needed.

## Still open
See `OPEN_QUESTIONS.md`. Do not silently hard-code unresolved decisions.
