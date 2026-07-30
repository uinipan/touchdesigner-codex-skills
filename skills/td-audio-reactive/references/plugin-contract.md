# Audio Reactive TOX Contract

Use this reference when locating, loading, inspecting, or wiring `audio_reactive_tools.tox`.

## Discovery

Prefer, in order:

1. an existing loaded `audio_reactive_tools` COMP in the current project;
2. a TOX path supplied by the user;
3. a project-local or known plugin folder search for `audio_reactive_tools.tox`.

Do not rely on the historical path below without checking it:

```text
D:\capsulework\2605_mcpres\plugin_uinipan\audio_reactive_tools.tox
```

That path was recorded in an older note but was not present during the 2026-07-30 skill consolidation.

## Expected Interface

Treat this as an expected contract that must be verified against the loaded COMP.

| Output | Expected shape | Typical targets |
| --- | --- | --- |
| `out_envelope` | continuous bounded envelope | brightness, scale, opacity, displacement, feedback gain, camera shake |
| `out_speed` | accumulated continuous value | rotation, scrolling, noise evolution, phase, time offset |
| `out_triggers` | kick/snare pulses | flashes, bursts, reset, switch advance |
| `out_count` | kick/snare accumulated counts | indices, progressive reveal, persistent variation, totals |

The current documented plugin does not expose a full spectrum lane as a primary output. Add a separate spectrum branch when needed.

## Inspection Checklist

- Confirm the plugin input connector accepts the intended audio CHOP.
- List actual `out_*` operators.
- List channel names and signal dimensions for each required output.
- Check cook errors and nonzero values.
- Confirm whether trigger channels are pulses or latched binary states.
- Confirm whether counts and speed reset through plugin parameters.
- Inspect exposed controls such as input gain, envelope smoothing, kick/snare thresholds, beat sensitivity, count maximum, and reset pulses.
- Adapt to the real interface if it differs; do not silently edit the TOX.

## Semantic Handoff

Use project-level Null CHOPs:

```text
audio_envelope_out
audio_speed_out
audio_triggers_out
audio_counts_out
```

Use module prefixes where several visual systems consume different mappings:

```text
particles_audio_envelope
particles_audio_triggers
reveal_audio_counts
feedback_audio_speed
```

Keep a short Text DAT nearby only when it materially improves readability. Record source, signal shape, target, and reset behavior.

## Parameter Meaning

- Envelope input/output gain changes sensitivity and final range.
- Envelope smoothing trades responsiveness for stability.
- Kick/snare thresholds trade missed events against false triggers.
- Beat sensitivity changes the analysis energy before event detection.
- Count maximum limits or wraps persistent event state.
- Reset operations matter for repeatable shows, previews, and progressive effects.

Never use count as intensity, speed as loudness, or a smoothed trigger as a reliable one-shot event.
