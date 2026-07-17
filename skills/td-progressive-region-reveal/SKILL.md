---
name: td-progressive-region-reveal
description: Build and debug TouchDesigner effects that progressively activate non-repeating image, grid, instance, map, LED, or region cells from event pulses or counters, with next-region preview, persistent reveal state, complete coverage, hold time, manual reset, and delayed automatic reset. Use when the user asks for cumulative lighting/coloring, one region per kick/snare/MIDI event, filling an image over time, random activation without duplicates, or reset only after every region has activated.
---

# TD Progressive Region Reveal

Build a reusable event-to-state system, not a project-specific mosaic look.

## Trigger Examples

Use this skill for requests such as:

- "One kick should permanently light one more block."
- "Reveal random regions until the whole image is filled."
- "Preview the next unlit region, then commit it on snare."
- "Do not repeat cells, and reset only after everything is active."
- "Hold the completed image for five seconds before reset."
- "Use MIDI notes, OSC messages, button presses, or sensor events to accumulate regions."

Applicable targets include image tiles, maps, LED layouts, instanced geometry, point grids, seating plans, architectural facades, and particle zones.

## State Model

Keep these roles separate:

```text
event pulse -> increment progress
progress -> committed region mask
progress index -> next-region preview mask
continuous envelope -> preview brightness only
complete coverage -> hold timer -> reset
manual reset -> progress 0 immediately
```

Do not use a continuous audio envelope as the persistent reveal state. Do not let preview flicker overwrite already committed regions.

## Required Controls

Expose controls with stable names:

```text
steps
region_count
random_seed
preview_level
auto_reset
reset_delay
reset_now
```

`region_count` must equal the number of unique reveal regions. Do not treat it as an artistic speed control.

## Non-Repeating Order

Use a true permutation of `[0, region_count - 1]`.

- Verify unique count equals `region_count`.
- Verify missing count is zero.
- Verify duplicate count is zero.
- Changing `random_seed` must change ordering, not merely translate a diagonal scan.
- Avoid hash-and-modulo selection unless collisions are explicitly resolved.
- For a 2D shear permutation, each shear update may depend on the other axis only; self-dependent mixed terms can destroy bijection.

Run a CPU-side verification using the same formula before trusting the visual result.

## Reset Sequence

1. Increment until `steps == region_count`.
2. Render every committed region.
3. Start the hold timer only after full coverage is reached.
4. Ignore incoming progress events during the hold.
5. Reset after `reset_delay`, or immediately when `reset_now` is pulsed.

Do not reset on the same event that reaches the final region. Do not reset merely because a configured `max_steps` was reached without verifying complete coverage.

## Verification

- At silence or without events, progress must not change.
- One event must advance exactly one step unless the user requests grouped events.
- Preview must target only the next uncommitted region.
- Committed regions must remain stable.
- At the final step, the full target must be visibly covered.
- The full state must remain visible for `reset_delay` seconds.
- Manual reset must not disable future event detection.

Use `td-audio-plugin-handoff` when events come from the user's packaged audio plugin. Use `td-glsl-control-panel` when the reveal is implemented in GLSL and needs visible controls.
