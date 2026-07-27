---
name: td-audio-plugin-handoff
description: Use the local TouchDesigner audio_reactive_tools.tox as a stable audio-control source, inspect its real outputs, and connect semantic downstream Null CHOP interfaces for triggers, counts, envelope, and speed. Use when the user asks to add audio controls with their packaged audio plugin, connect kick/snare or brightness data, explain which output controls what, or clean up project audio handoff nodes without rebuilding audio analysis.
---

# TD Audio Plugin Handoff

Use the packaged plugin instead of rebuilding its internal audio-analysis network.

## Plugin

- Locate `audio_reactive_tools.tox` in the user's plugin collection or cloned `touchdesigner-codex-plugins` repository. Do not assume a machine-specific absolute path.
- Input 0: an audio CHOP, normally Audio File In, Audio Device In, or a source Null CHOP.
- Do not modify or unpack the TOX unless the user explicitly asks to develop the plugin itself.
- Before wiring, inspect the loaded COMP and verify the output operators and channel names. Treat the list below as the expected contract, not a substitute for inspection.

## Expected Output Contract

| Plugin output | Signal shape | Intended use |
| --- | --- | --- |
| `out_envelope` | continuous bounded envelope | brightness, scale, opacity, displacement, feedback gain |
| `out_speed` | accumulated continuous value | phase, scrolling, rotation, noise evolution, time offset |
| `out_triggers` | kick/snare pulses | flashes, bursts, state advance, reset, one-shot events |
| `out_count` | kick/snare accumulated counts | indices, persistent progress, variation selection, event totals |

Never substitute count for pulse or speed for intensity merely because both values change with music.

## Handoff Workflow

1. Find an existing loaded `audio_reactive_tools` COMP. Load the TOX only when it is absent and the user asks to add audio processing.
2. Inspect its `out_*` operators, channel names, current values, and errors.
3. Connect only the outputs required by the visual system.
4. Create project-level Null CHOPs with semantic names. Do not leave downstream visuals coupled to `null4`, `null6`, or other positional names.
5. Keep original channel names for direct signals. Rename derived signals when their shape changes, such as `kick` to `kick_count` after a Count CHOP.
6. Add a nearby Text DAT only when it helps the user read the project. Keep it short: source output, signal shape, and target role.
7. Verify silence behavior, normal values, strong peaks, and reset behavior before tuning the visual.

## Naming

Use these defaults, optionally prefixed by the visual module name:

```text
audio_envelope_out
audio_speed_out
audio_triggers_out
audio_counts_out
```

For a mosaic module:

```text
mosaic_audio_envelope
mosaic_audio_triggers
mosaic_audio_counts
```

Name by role, not operator type. A visual module should be understandable without opening the plugin.

## Common Requests

- "Use my audio plugin and connect kick/snare to this effect."
- "Use audio_reactive_tools to control brightness."
- "Tell me which audio output controls what, and rename the Nulls clearly."
- "Connect count to progressive reveal and triggers to preview flashes."
- "Clean up the audio nodes without rebuilding the analyzer."

## Boundaries

- This skill owns plugin discovery, output verification, signal-shape explanation, and downstream handoff.
- The visual skill owns GLSL, TOP, geometry, reveal logic, and artistic tuning.
- Use `out_count` when an effect must remember how many events occurred. Use `out_triggers` when each event should fire once.
- If the plugin output contract differs from this file, report the actual interface and adapt the handoff. Do not silently modify the plugin.
