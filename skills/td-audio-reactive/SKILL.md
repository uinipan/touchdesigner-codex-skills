---
name: td-audio-reactive
description: Build, connect, tune, inspect, and debug practical audio-reactive TouchDesigner systems. Prefer the user's audio_reactive_tools.tox for envelope, speed, kick/snare triggers, and event counts; route those signals into TOP, SOP, particles, GLSL, feedback, camera, lighting, or UI systems. Use for requests involving audio-reactive visuals, audio TOX integration, beat or frequency response, signal mapping and smoothing, spectrum workflows, or diagnosing weak, jittery, delayed, overdriven, or non-responsive audio control.
---

# TD Audio Reactive

Treat audio as a set of control signals, not as a visual style. Build a clear handoff from sound analysis to the visual system, with the packaged TOX as the default implementation.

## Operating Policy

1. Reuse an existing loaded `audio_reactive_tools` COMP when present.
2. Otherwise locate the user's `audio_reactive_tools.tox`; do not assume a stale absolute path is valid.
3. Inspect the loaded COMP's actual inputs, `out_*` operators, channel names, values, and errors before wiring.
4. Use the TOX outputs when they satisfy the request.
5. Build custom CHOP analysis only when the TOX lacks the required signal, the user asks to modify the analyzer, or a tutorial experiment specifically requires it.
6. Keep the visual network outside the TOX. Do not unpack or edit the plugin unless the user explicitly asks to develop the plugin itself.
7. Name downstream handoff Null CHOPs by signal role rather than node position.

## Workflow

### 1. Define the visual behavior

Translate the request into one or more signal shapes:

| Desired behavior | Signal shape |
| --- | --- |
| Brightness, scale, opacity, displacement follows loudness | continuous envelope |
| Rotation, scrolling, noise evolution advances with energy | accumulated speed |
| Flash, burst, reset, one-shot state change | trigger pulse |
| Persistent index, progressive reveal, variation selection | event count |
| Separate bass, mid, and high responses | frequency-band values |
| Bars, scanlines, masks, displacement maps, shader texture | spectrum data or TOP texture |

Do not substitute one shape for another merely because both change with music.

### 2. Resolve the audio source and TOX

- Identify `Audio File In CHOP`, `Audio Device In CHOP`, movie audio, or an existing source Null.
- Search the current project for an existing audio plugin COMP first.
- If absent, use a TOX path explicitly supplied by the user.
- If no path is supplied, search only relevant project/plugin folders for `audio_reactive_tools.tox`.
- If no valid file is found, report the missing TOX and continue with a manual block only when that remains within the request.
- After loading, verify the input connector and real output contract. Never claim the expected contract was verified when it was not.

Read [plugin-contract.md](references/plugin-contract.md) when loading, wiring, renaming, or debugging the TOX.

### 3. Select the smallest sufficient outputs

Expected outputs are:

- `out_envelope`: bounded continuous loudness/energy.
- `out_speed`: accumulated continuous motion or phase.
- `out_triggers`: kick/snare pulses.
- `out_count`: accumulated kick/snare counts.

Connect only what the visual needs. Preserve original channel names for direct signals; rename derived channels when their meaning changes.

Default project-level handoff names:

```text
audio_envelope_out
audio_speed_out
audio_triggers_out
audio_counts_out
```

Prefix them with the consuming module when useful, such as `particles_audio_triggers`.

### 4. Map signal to target

For every connection, record:

- source output and channel;
- signal shape;
- observed silence, normal, and peak values;
- Math CHOP input and output ranges;
- smoothing, threshold, attack, decay, or clamp;
- target parameter and intended behavior;
- reset behavior for speed, counts, feedback, and states.

Tune the driver range before changing many target parameters. Keep pulses crisp for switches and resets; bound continuous signals used for intensity.

### 5. Add missing analysis only when needed

Use manual CHOP blocks for:

- full spectrum or CHOP-to-TOP textures not exported by the TOX;
- custom bass/mid/high frequency bands;
- alternate onset or beat detection;
- analyzer development;
- teaching or reproducing a tutorial's internal method.

Read [manual-analysis-recipes.md](references/manual-analysis-recipes.md) before constructing these blocks. Keep custom lanes outside the packaged TOX unless plugin development was explicitly requested.

### 6. Connect the visual system

Keep ownership boundaries clear:

- This skill owns audio source resolution, signal extraction, signal shaping, range mapping, semantic handoffs, and audio-side debugging.
- The relevant visual skill owns detailed TOP, SOP, particle, GLSL, render, camera, feedback, or UI architecture.
- When using another visual skill, hand it a documented envelope, speed, trigger, count, band value, or spectrum texture.

### 7. Verify in motion

Verify:

1. audio source is cooking;
2. TOX input and required outputs exist;
3. selected channels change with the expected musical feature;
4. silence behavior is safe;
5. strong peaks do not pin or explode the target;
6. smoothing does not destroy triggers;
7. count and speed reset behavior is understood;
8. the visual response has acceptable latency;
9. the final output remains owned by the project's intended render/display chain.

A correct still frame is not enough. Inspect CHOP viewers and the driven parameter over time.

## Decision Guide

- Use `envelope` for “音乐越响，画面越强.”
- Use `speed` for continuous phase, scroll, rotation, or time progression.
- Use `triggers` for flashes, bursts, resets, or one-shot changes.
- Use `count` when the effect must remember how many kick/snare events occurred.
- Use frequency bands when visual layers should respond to different parts of the music.
- Use spectrum texture when the frequency distribution itself becomes imagery or a shader input.
- Combine signals deliberately: for example, envelope controls brightness, kick triggers a burst, count selects a variation, and speed advances noise.

## Troubleshooting Order

1. Confirm the source contains nonzero audio.
2. Confirm the plugin or analysis nodes cook without errors.
3. Confirm exact output and channel names.
4. Inspect raw values before mapping.
5. Confirm the target is not overridden by another export or expression.
6. Adjust one Math/Filter/Lag/Trigger stage at a time.
7. Inspect buffering and cook rate when response is late.
8. Inspect the downstream visual only after the audio handoff is proven.

Common interpretations:

- No response: missing source, wrong channel, disabled export, stale path, or overridden target.
- Weak response: source range is smaller than expected; remap once near the handoff.
- Always maxed: gain/input range is too aggressive; clamp or compress the driver.
- Jitter: add suitable filtering to continuous signals, not to event pulses.
- Missed or flickering events: wrong threshold or a trigger was treated as a smooth envelope.
- Wrong rhythm: separate kick, snare, overall energy, and frequency roles.
- Delayed response: distinguish audio buffering latency from deliberate smoothing.

## Tutorial Knowledge

Tutorials are reference material, not the default execution workflow. Use them to choose a visual mapping pattern or to extend the analyzer; do not rebuild every tutorial network when the TOX already provides the needed signal.

Read [tutorial-patterns.md](references/tutorial-patterns.md) when the user asks what effects are possible, wants to reproduce one of the classified tutorials, or needs inspiration for downstream mappings.

## Completion Report

Report:

- resolved audio source and TOX location, or that the TOX was not found;
- inspected output/channel contract;
- outputs connected and semantic handoff names;
- mapping, smoothing, threshold, and reset choices;
- downstream targets;
- motion checks performed;
- any custom analysis added and why the TOX was insufficient.
