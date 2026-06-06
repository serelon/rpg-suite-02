---
type: entity
entity-kind: vehicle-class
campaign: eisrand
zoom: full
faction: "[[ironreach-combine]]"
operators:
  - "[[ragna]]"
  - "[[freyke]]"
tags:
  - mechanical
  - load-bearing
crew: 6
max-depth-m: 410
traverse-rate-kmh: 11
---

# Eisrand Walkers

## Index Line

Six-legged pressure-hulled ice walkers; the Combine's only way across the deep shelf. See [[ironreach-combine]].

## Summary

The walkers are the logistical spine of the Eisrand crossing. Each hull carries a
crew of six, rated to 410 m of shelf-ice pressure, making 11 km/h on open pack.
Operated under [[ironreach-combine]] charter; [[ragna]] and [[freyke]] are both
licensed pilots.

## Crew

Standard complement is six: pilot, mate, two leg-engineers, a quartermaster, and
a shelf-reader. The shelf-reader outranks the pilot on route decisions — a rule
written in blood after the Hollow Run collapse.

## Capabilities

- Rated depth: 410 m below shelf surface
- Traverse: 11 km/h sustained on pack ice, 4 km/h on rotten ice
- Endurance: 9 days at full crew without resupply

## Stats

```json
{
  "hull": {"rating_m": 410, "compartments": 4, "ballast": "wet-cell"},
  "legs": {"count": 6, "actuator": "hydraulic", "spare_joints": 2},
  "consumables": {"fuel_days": 9, "rations_days": 12, "water": "recycler"}
}
```

## GM Notes

The walkers should feel *old* — every campaign scene aboard one should include at
least one maintenance ritual or failing subsystem. Never let a crossing be routine.

## Secrets

Walker hull 7 carries contraband below the ballast deck. [[ragna]] knows; [[freyke]] does not.
