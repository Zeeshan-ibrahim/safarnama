# Suggested implementation sequence

## Phase 0 — Repository alignment
- [ ] Map frontend/backend, database, tests, scripts, CI, environments, deployment.
- [ ] Compare implementation with PRD/architecture.
- [ ] Resolve pilot cluster and blocking product decisions.
- [ ] Agree source and verification policy for travel data.

## Phase 1 — Trustworthy data foundation
- [ ] Model destinations, attractions, routes, stay areas, costs, provenance.
- [ ] Add safe import/curation and data-quality checks.
- [ ] Seed a small verified pilot dataset.

## Phase 2 — Discovery
- [ ] Search/filter destinations by interests, season, duration, region.
- [ ] Detail pages with source/freshness.
- [ ] Empty and unsupported coverage states.

## Phase 3 — Trip inputs and preview
- [ ] Origin, dates/duration, group, budget basis, transport, interests, pace, accommodation.
- [ ] Typed preview API and grounded candidate recommendations.

## Phase 4 — Itinerary engine
- [ ] Route graph/directions adapter.
- [ ] Deterministic stop ordering and day allocation.
- [ ] Feasibility, overnight logic, warnings, locked stops.
- [ ] Regression tests for impossible/disconnected/seasonally constrained routes.

## Phase 5 — Budget and editing
- [ ] Itemized low/base/high estimate and assumptions.
- [ ] Group/per-person totals.
- [ ] Add/remove/reorder/lock stops and recalculate.
- [ ] Save/reopen/delete trips and agreed authentication flow.

## Phase 6 — Closed pilot
- [ ] Test real trip-planning tasks with travellers.
- [ ] Measure successful plans, edits, saves, estimate trust, unsupported requests.
- [ ] Fix observed failures before expanding coverage.

## Later, based on evidence
Provider enquiries, bookings, payments, commissions, more regions, international travel.
