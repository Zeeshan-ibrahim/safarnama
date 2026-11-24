---
name: itinerary-engine
description: Design deterministic day-by-day itinerary generation, route ordering, feasibility validation, and itinerary edits.
---
Read `05_Core_Travel_Planning_Logic`. Pipeline: normalize origin/dates/group/budget/transport/interests/pace; check data coverage; select candidates; build route graph; exclude known blocked edges; order stops; allocate visits/travel/overnights; calculate itemized costs; validate and repair/flag; return assumptions, warnings, confidence, and provenance. Start with a deterministic heuristic, not a complex optimizer. Preserve locked stops. Test disconnected graph, impossible day, season boundary, unknown route, locked stop, over-budget plan, and edits that invalidate dependent calculations.
