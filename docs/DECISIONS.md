# Decision log

Add newest accepted decisions at the top with date, status, context, decision, consequences, and owner.

## Accepted direction — 24 November 2026
- Pakistan-first domestic leisure travel.
- Planning-first MVP: discovery, itinerary preview, route feasibility, transparent estimates, manual editing, saved trips.
- Marketplace, provider booking, payments, full hotel inventory, native apps, and international travel are later phase.
- Hybrid engine: deterministic rules and structured data enforce route feasibility and cost arithmetic; AI interprets preferences and explains supported options.
- Proposed stack: Next.js/TypeScript, FastAPI/Python, PostgreSQL/PostGIS, Redis/worker, provider-agnostic LLM adapter, maps provider TBD, object storage if needed.

## Still open
See `OPEN_QUESTIONS.md`. Do not silently hard-code unresolved decisions.
