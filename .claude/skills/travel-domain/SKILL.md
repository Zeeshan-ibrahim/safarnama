---
name: travel-domain
description: Apply travel-domain rules to destination discovery, route planning, itinerary generation, cost estimates, and seasonal constraints.
---
Read `05_Core_Travel_Planning_Logic`. Core entities: Destination, Attraction, RouteEdge, StayArea, CostItem, ConstraintRule; ProviderOffer is later phase. Invariants: unknown route is not zero duration; straight-line distance is not road distance; stale data is not current; estimates are not quotes; unsupported coverage must be visible; AI output must be grounded in structured facts and schema-validated. State and test invariants when implementing.
