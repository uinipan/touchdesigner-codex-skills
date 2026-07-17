---
name: td-audio-reactive-tutorial
description: "Learn TouchDesigner tutorials focused on extracting reusable control data from sound: amplitude/RMS envelopes, beat/kick/snare triggers, onset detection, frequency-band values, spectrum textures, Audio Analysis COMP buses, smoothing, lag, range mapping, and routing audio-derived signals into later visual systems. Use when the tutorial's main reusable value is audio signal extraction, signal shaping, or audio-to-visual control data."
---

# TD Audio Reactive Tutorial

Use this skill to turn an audio-reactive TouchDesigner tutorial into a reusable library of audio-derived control signals. The primary question is: "What useful data is extracted from the music, what shape is that signal, and how can later visual projects use it?"

Do not treat audio as a visual style by itself. Treat it as a data source that can produce continuous values, pulses, binary states, counters, envelopes, or TOP textures for downstream geometry, TOP, particle, GLSL, render, or UI systems.

## Workflow

1. Identify the audio role.
   - Classify what data is extracted: amplitude/RMS, beat/kick/snare, onset, frequency band, spectrum image, Audio Analysis COMP bus, MIDI/control, or hybrid.
   - Record downstream use separately: geometry, particles, shader uniforms, TOP effects, camera, lighting, material values, or UI controls.
   - Note the audio source: Audio File In, Audio Device In, movie audio, MIDI, or external control.
   - Separate continuous modulation from event triggers. A bass envelope, a snare pulse, and a spectrum image should not be documented as the same kind of control signal.

2. Map the signal chain.
   - Preserve the exact CHOP path from source to final export/channel reference.
   - Split the chain into analysis, cleanup, smoothing, scaling, selection, and export.
   - Record channel names, sample rate changes, range conversions, and any Select/Rename/Math nodes that make expressions work.
   - For every exported value, record whether the tutorial uses parameter export, `op('node')['chan']`, `chop('node/chan')`, a CHOP reference, or a DAT/Python expression.

3. Extract modulation recipes.
   - Explain the intent of each control stage: isolate bass, average spectrum, detect peaks, compress dynamic range, smooth jitter, add decay, or clamp extremes.
   - Capture parameter mapping as source range -> target range, with units.
   - Mark whether the visual should respond instantly, ease in/out, pulse, accumulate, or decay.
   - Preserve why this sound feature is useful: bass often reads as weight, kick reads as impact, snare reads as a cut, high frequencies read as texture, and RMS reads as overall energy.

4. Distill direction knowledge.
   - Convert the tutorial's exact CHOP chain into a generalized audio-control recipe.
   - Add new classification signals when this tutorial reveals a subtype, such as amplitude, beat trigger, spectrum band, spectrum image, onset, Audio Analysis COMP bus, MIDI, or hybrid control.
   - Preserve reusable signal, mapping, smoothing, and debugging guidance. If TouchDesigner testing is needed, limit it to a single CHOP/control block and one target parameter.
   - Name the reusable recipe by control behavior, not final style, such as `bass envelope -> scale pulse`, `kick trigger -> switch index`, or `spectrum texture -> displacement map`.

5. Verify with both motion and stills.
   - Use keyframes for final look, but also test the channel behavior over time.
   - Debug in this order: audio input present, channel selection, value range, smoothing/lag, expression/export target, visual parameter sensitivity.
   - Classify visual checkpoints as `matches`, `close`, `different`, or `unknown because no audio/keyframe`.
   - When a still image looks correct but motion feels wrong, inspect the CHOP waveform and exported parameter over time before changing the visual network.

## Audio Signal Recipe Library

Use these recipes as the stable buckets for future audio tutorials. Add tutorial-specific nodes, parameter ranges, and failure notes under the closest recipe instead of inventing a new category too early.

- `volume-envelope -> continuous parameter`: `Audio File In/Audio Device In -> Analyze CHOP RMS/peak -> Math CHOP -> Lag/Filter CHOP -> Null CHOP`. Produces a continuous value for scale, brightness, displacement, feedback gain, particle force, or camera shake. Preserve observed quiet/average/peak ranges, lag time, clamp behavior, and why the result was too weak or too explosive.
- `beat-trigger -> visual switch/reset`: `audio/onset source -> Select/Logic/Trigger/Count CHOP -> Null CHOP`. Produces a pulse, binary state, counter/index, or smoothed envelope for flashes, `Switch TOP`, `Invert TOP`, reset, camera punch, burst, or hard visual cuts. Record the expected signal shape because using a smoothed envelope where a pulse is needed causes missed triggers or flicker.
- `frequency-band -> separated layer control`: `Audio Spectrum CHOP -> Select frequency range -> Analyze/Math CHOP -> Lag/Filter CHOP -> Null CHOP`. Produces bass/mid/high control values for separate visual layers. Preserve band ranges, whether values are averaged or peaked, and rhythm mismatches caused by selecting the wrong frequency band.
- `spectrum-top -> image/mask/displacement source`: `Audio Spectrum CHOP -> CHOP to TOP -> TOP processing`. Produces an image/texture rather than a single parameter value. Use for lines, bars, scanlines, masks, displacement maps, UV offsets, and shader texture inputs. Preserve resolution, orientation, channel use, TOP format, and whether the image is a source layer or a control map.
- `audio-analysis-comp -> role-separated control bus`: `Audio Analysis COMP -> Select CHOP -> Rename/Null CHOP`. Produces a bus of ready-made channels such as volume, kick, snare, or other analysis outputs. Preserve which channels are available, which are continuous, which are hard triggers, and why one channel should not drive every visual decision.
- `signal-to-target-mapping -> downstream handoff`: `audio signal -> mapping/smoothing -> visual target`. Documents how audio-derived data enters another direction: TOP glitch, particles/instancing, GLSL uniforms/textures, SOP deformation, render/post controls, or UI. Keep the audio skill responsible for signal extraction and shape; let the downstream direction skill own the visual system details.
- `audio-filein-peak-speed block`: `Audio File In -> Math(chanop avg, gain) -> Analyze maximum -> Filter -> Math/Null + Speed`. Use for a compact overall-energy block when a project needs a continuous envelope plus an accumulated motion driver. Read `references/td-audio-filein-peak-speed.md` when exact tested node details are needed.
- `audio-kick-rms-spectrum block`: `Audio File In -> Audio Analysis kick/snare -> Count`, plus `RMS Power -> Speed`, plus `Audio Spectrum -> Null`. Use for a three-lane audio block where event triggers, continuous motion, and spectrum data stay separate. Read `references/td-audio-kick-rms-spectrum.md` when exact tested node details are needed.

## Internal Audio Blocks

This is the only audio skill. Do not split the following blocks into separate skills. Treat them like the UI button block inside `td-ui-panel-interface-tutorial`: reusable block patterns owned by this broader audio direction.

### File In Peak Speed Block

Use this block when one `Audio File In CHOP` should produce a compact overall-energy envelope and a cumulative motion driver. This is not the packaged `Audio Analysis COMP` workflow.

```text
audiofilein1 -> audiodevout1
audiofilein1 -> math3(chanop avg, gain 0.5)
              -> analyze1(function maximum)
              -> filter1(type gauss, width 0.2 seconds)
              -> math2(gain 100)
              -> null6
                                \-> speed2
```

- `null6/chan1`: continuous peak-loudness envelope for brightness, scale, displacement, feedback gain, force, camera shake, or any value that should follow overall energy.
- `speed2/chan1`: accumulated motion driver for time offsets, scrolling, rotation, noise evolution, or any value where stronger audio should advance motion faster.
- Create the speed lane only when needed; `Speed CHOP` output is cumulative and should not be compared numerically between separately started copies.
- Keep the block loose and inspectable in the project by default. Only wrap it in a Base/tox when the user explicitly asks for packaging.
- If the recreated block does not match the original, check `math3.chanop=avg` and `filter1.width=0.2 seconds` before changing downstream visuals.

### Kick RMS Spectrum Block

Use this block when one audio source needs three role-separated lanes: event triggers, continuous RMS motion, and raw spectrum data.

```text
audiofilein1 -> null5

null5 -> audioAnalysis1 -> select1(kick snare) -> count2

null5 -> math4(chanop avg, gain 1)
      -> analyze2(function rmspower)
      -> speed3
      -> math5

math4 -> audiospect1(mode visual, fftsize 8192, frequencylog 1, highfreqboost 0.75, outlength 2048)
      -> null8
```

- `select1/kick` and `select1/snare`: immediate event/binary channels from `audioAnalysis1/out1`.
- `count2/kick` and `count2/snare`: accumulating counters for switch indices, state changes, visual variation, or event counting. Do not treat them as intensity envelopes.
- `math5/chan1`: RMS-derived cumulative motion/progress driver for scroll, rotation, noise phase, texture offset, or time index.
- `null8`: raw spectrum data with many samples. Reduce it into bands or convert it with CHOP to TOP before expecting a convenient visual control.
- Build as loose project-level operators by default so thresholds, filters, speed, and spectrum parameters stay inspectable. Package into a Base/tox only when explicitly requested.
- Before building the event lane, resolve the `Audio Analysis COMP` source. Do not assume `/project1/audioAnalysis1` exists in every project.
  - First search the target project for a COMP whose `out1` channels include both `kick` and `snare`, ideally with the full bus `low`, `mid`, `high`, `kick`, `snare`, `rythm`, `smsd`, `fmsd`, and `spectralCentroid`.
  - If a valid component exists, copy it into the new loose block as `<prefix>audioAnalysis` so the new workflow is independently editable.
  - If no valid component exists, load the Palette tox directly instead of asking the user to drag it: `C:\Program Files\Derivative\TouchDesigner\Samples\Palette\Tools\audioAnalysis.tox`.
  - The Palette tox loads as an outer container whose actual Audio Analysis component is usually the child `audioAnalysis`. After `loaded = parent.loadTox(path)`, use `loaded.op('audioAnalysis')` when the loaded root has no direct `out1`.
  - Rename or copy the actual Audio Analysis component to `<prefix>audioAnalysis`, then connect the new audio-source null to it.
  - After loading or copying, verify `<prefix>audioAnalysis/out1` exists and exposes `kick` and `snare`. If it does not, report the missing channel set and do not create a broken `select(kick snare)` chain.
  - If the Palette tox is missing or cannot load, then ask the user to add the Palette Audio Analysis COMP once, or provide/import a known-good `.tox`, then continue the build.
  - Only use a hand-built kick/snare fallback when the user explicitly accepts approximate detection. Label it as fallback because it will not match the packaged Audio Analysis COMP thresholds or channel set.
- For a reusable Base, include or copy a working `Audio Analysis COMP` inside the Base; do not make a Base that only references an external `/project1/audioAnalysis1/out1`.

## Downstream Handoffs

- TOP glitch: preserve `speed`, `kick/snare`, and `spectrum` as separate lanes. `speed` drives Noise/Time/Transform; `kick/snare` drives Switch/Invert/hard cuts; `spectrum` drives lines, bars, scanline masks, or UV maps. Cross-reference compositing/render notes for 32-bit float UV remap, Time Machine TOP, and feedback precision.
- Particles/instancing: preserve bass or RMS as birth rate, size, force, or turbulence intensity; preserve spectrum bins as instance scale, height, color, or point attributes; preserve kick as reset, burst, or emitter pulse. Cross-reference particle/instancing notes for count, resolution, and performance.
- GLSL: preserve whether audio enters as CHOP-exported uniforms, parameter expressions, or spectrum TOP textures. Cross-reference GLSL notes for shader architecture, uniform names, ranges, texture sampling, and coordinate assumptions.
- Geometry/render: preserve only the audio signal and mapping in this skill; leave detailed SOP, material, camera, glow, or post-processing structure to the relevant direction skill.

## Tuning Heuristics

- Use `Math CHOP` range mapping before changing many visual parameters. First confirm the driver reaches a useful range, then tune the target.
- Use `Lag CHOP`, `Filter CHOP`, `Speed CHOP`, or `Trigger CHOP` according to desired behavior: eased motion, smoothed noise, accumulated motion, or attack/decay pulse.
- Keep trigger signals crisp for binary targets such as `Switch TOP` index, reset pulses, and state toggles. Smoothing these signals can cause flicker or missed transitions.
- Keep continuous signals bounded for visual intensity targets. Clamp, compress, or lower gain when values pin at maximum or make geometry explode.
- Record quiet, average, and loud observed values when available. Audio mappings without observed ranges are hard to reuse.
- Treat latency separately from smoothing. If the visual is late, inspect buffering, audio device settings, and CHOP cook rate before simply lowering lag.

## Knowledge To Preserve

- Audio analysis pattern and CHOP node chain.
- Channel names and export/reference syntax.
- Source/target range mappings and why they were chosen.
- Smoothing, lag, filter width, threshold, decay, and gain values.
- Observed signal ranges for silence, normal sections, peaks, and beat hits.
- Whether each control is continuous, binary, pulse-based, accumulated, or image/texture-based.
- Reset behavior for feedback, counters, triggers, and Switch TOP state.
- The downstream handoff boundary: what audio signal is exported and which other skill should own the visual system.
- Tuning advice for common failures: no response, jitter, delayed response, always-maxed values, weak movement, or mismatched frequency bands.
- For minimal TOP glitch systems, preserve three separate audio roles:
  - `speed`: RMS or amplitude analyzed through `Analyze CHOP -> Speed CHOP`, used as a continuous translate/time driver for Noise TOPs, remap offsets, and texture/time motion.
  - `kick` / `snare`: `Audio Analysis COMP -> Select CHOP`, used as discrete triggers for `Switch TOP`, `Invert TOP`, color toggles, and hard visual state changes.
  - `spectrum`: `Audio Spectrum CHOP -> CHOP to TOP`, used directly as source imagery for lines, bars, grids, and scanline masks.
- When documenting beat-triggered switches, record whether the target parameter expects a pulse, binary index, or smoothed value; wrong signal shape causes flicker or no switching.
- For synthetic validation, use `lfoCHOP` as a stand-in for audio before real sound is available:
  - `lfoCHOP -> lagCHOP -> nullCHOP` can simulate `volume-envelope -> continuous parameter`.
  - `lfoCHOP -> logicCHOP -> triggerCHOP -> nullCHOP` can simulate `beat-trigger -> visual switch/reset`.
  - `noiseTOP -> levelTOP -> outTOP` with `levelTOP.brightness1` driven by the simulated envelope is enough to visually confirm mapping, smoothing, and nonblank output.
  - When executing TD Python through the MCP HTTP endpoint, create operators by string type names such as `parent.create('lfoCHOP', 'amp_source')`; class globals such as `lfoCHOP` may not be defined in that execution context.
- For real Audio File In validation, prefer testing with actual audio as soon as a source exists:
  - `audiofileinCHOP -> analyzeCHOP(function='rmspower') -> mathCHOP -> lagCHOP -> nullCHOP` produced a usable `volume-envelope -> continuous parameter` chain.
  - In TouchDesigner 2023, `Analyze CHOP` exposes RMS as menu name `rmspower` / label `RMS Power`, not `rms`.
  - Start by watching observed values before range mapping. A too-small Math CHOP input range makes the visual stay maxed out; retune the source range before changing many visual targets.
  - For quick visual inspection, drive `levelTOP.brightness1` from the mapped envelope and turn on viewers for the source CHOP, analysis CHOP, mapped Null CHOP, Level TOP, and Out TOP.
  - Do not turn on `display` or `render` flags just to inspect a test block. Keep `viewer=True` for observation and leave display/render ownership to the actual project output chain.
- Additional TouchDesigner 2023 operator facts:
  - The Audio Spectrum CHOP type string is `audiospectrumCHOP`, not `audioSpectrumCHOP`.
  - `audiospectrumCHOP -> choptoTOP` should be wired by setting `choptoTOP.par.chop` to the spectrum CHOP path; do not connect the CHOP output connector directly into the TOP input.
  - Useful initial `audiospectrumCHOP` parameters are `mode='visual'`, `fftsize='1024'`, `frequencylog=1`, `highfreqboost=0.5`, and `outlength=128`.
  - A first CHOP to TOP spectrum preview may appear as a very thin nonblank line when `layout='rowscropped'`, because the spectrum CHOP can have very long sample rows and only a few channels. Treat that as a layout problem, not a failed audio analysis.
  - For an operable spectrum texture, set `choptoTOP.par.layout='square'`, `outputresolution='custom'`, `resolutionw=512`, `resolutionh=512`, and inspect the result before adding masks or composites.
  - `triggerCHOP` exposes parameters such as `threshold`, `attack`, and `decay`; `countCHOP` exposes `limitmax`, `triggeron`, and `output`. Use these to turn an envelope into pulse/counter candidates, but tune thresholds after watching the song.
- Spectrum TOP mask test pattern:
  - First fix the CHOP to TOP layout. `rowscropped` can make the spectrum look like a thin line; `square` produces a usable 2D texture from the long sample row.
  - `real_spectrum_to_top(square) -> levelTOP -> thresholdTOP -> blurTOP` can turn the spectrum into a larger mask/control texture.
  - If most energy is concentrated near the bottom, crop or fit the low-frequency band only after confirming the source texture dimensions. `Crop TOP` defaults to fraction units; switch crop units to pixels when using pixel counts.
  - Tune by inspecting the mask-only TOP before the final composite. Over-brightening plus `Composite TOP Add` can wash the whole preview white.
  - A stable first composite is `noise/background TOP + spectrum mask -> Composite TOP Multiply`; use Add/Over only after the mask has a controlled range.
  - Keep mask preview nodes viewer-only (`viewer=True`, `display=False`, `render=False`) so the test block does not take over the project output.
- Reusable packaged-analyzer pattern:
  - This project contains two distinct audio-processing methods. Method A is a packaged multi-role analyzer: `audiofilein1 -> null5 -> audioAnalysis1 -> out1`, then `select1(kick snare) -> count2` for event counters. Method B is hand-built direct CHOP processing from the same source: separate loudness, RMS/speed, and spectrum branches outside the COMP.
  - Treat a finished audio-analysis COMP as a reusable control bus, not just a black box. In this project `audioAnalysis1/out1` exposes nine 60 FPS one-sample channels: `low`, `mid`, `high`, `kick`, `snare`, `rythm`, `smsd`, `fmsd`, and `spectralCentroid`.
  - The useful top-level handoff from Method A is `audioAnalysis1/out1 -> select1(kick snare) -> count2`. `select1` isolates discrete kick/snare channels; `count2` turns them into accumulating counters for switch indices, state changes, or event-driven visual variation.
  - Method B is easier to inspect and retune for one visual target: `audiofilein1 -> math3(gain 0.5) -> analyze1(maximum) -> filter1 -> math2(gain 100) -> null6` for a continuous loudness-style control; `audiofilein1 -> null5 -> math4 -> analyze2(rmspower) -> speed3 -> math5` for an RMS-derived motion/speed lane; and `audiofilein1 -> null5 -> math4 -> audiospect1 -> null8` for raw spectrum data.
  - `audioAnalysis1` splits bands internally with `audiofilterCHOP -> renameCHOP(low/mid/high) -> analyzeCHOP(rmspower) -> math/limit/filter -> switch -> Null`. Observed tuning: low gain `2.0`, threshold `0.1`; mid gain `4.0`, threshold `0.1`, smooth `0.1`; high gain `3.5`, threshold `0.2`, smooth `0.1`.
  - Kick/snare detection inside the COMP is thresholded from band energy: kick uses low-band `rmspower -> math preoff -0.038 -> limit -> logic -> trigger -> null_kickSignal`; snare uses high-band `rmspower -> math preoff -0.311515 -> limit -> logic -> nullsnareSignal`. Document whether the downstream target needs the raw pulse, a binary state, or an accumulated `Count CHOP` value.
  - `audioAnalysis1` also contains a spectrum/feature lane: `switch_neutone -> audiospectrumCHOP(mode visual, fftsize 8192, frequencylog 1, highfreqboost 1, outlength 2048) -> shuffle/analyze/trail` to derive rhythm density, moving partial density, and spectral centroid. This belongs in the `audio-analysis-comp -> role-separated control bus` recipe, while a direct `audiospectrumCHOP -> CHOP to TOP` belongs in `spectrum-top -> image/mask/displacement source`.
  - If testing a copied `.toe`, preserve its relative media folders. Moving the `.toe` without referenced audio files can make current output values read as zero even though the network topology is valid.

## Troubleshooting

- Reference block: `audio-filein-peak-speed` captures a tested single-flow Audio File In pattern. Important verified parameters are `math3.chanop=avg`, `math3.gain=0.5`, `analyze1.function=maximum`, `filter1.type=gauss`, `filter1.width=0.2 seconds`, and `math2.gain=100`. Treat `speed2` as cumulative motion/integration, not a value that should numerically match between separately started copies.
- Reference block: `audio-kick-rms-spectrum` captures a tested three-lane pattern. Important verified paths are `audioAnalysis1/out1 -> select1(kick snare) -> count2`, `math4(chanop avg) -> analyze2(rmspower) -> speed3 -> math5`, and `math4 -> audiospect1(mode visual, fftsize 8192, highfreqboost 0.75, outlength 2048) -> null8`.
- If `audio-kick-rms-spectrum` fails in another project, check Audio Analysis availability first. The common failure is not CHOP wiring; it is that the target project has no existing `Audio Analysis COMP` to copy. Resolve or import that component before creating `select(kick snare)`.

- No reaction: confirm the audio source cooks, the channel is selected by the exact name, exports are enabled, and the target parameter is not overridden by another expression/export.
- Weak reaction: inspect the observed audio range, raise gain in one place, or remap to a more sensitive target range.
- Always maxed out: lower gain, clamp the Math CHOP output, use RMS instead of peak, or add compression-like remapping.
- Jitter: smooth the driver, average more samples, or move high-frequency detail to a visual target that can tolerate it.
- Late reaction: reduce lag/filter time, check audio buffering, and confirm the visual target is not being delayed by feedback or cache-heavy TOPs.
- Wrong rhythm: separate kick, snare, hat, amplitude, and spectrum roles; do not reuse one mixed channel for every visual decision.

## Output Shape

Produce a compact tutorial type note with:

- `Type`: audio-reactive.
- `Extracted data`: amplitude/RMS, beat/kick/snare, onset, frequency band, spectrum image, Audio Analysis COMP bus, MIDI/control, or hybrid.
- `Signal chain`: source -> analysis -> cleanup/smoothing -> mapping -> exported control.
- `Signal shape map`: channel/texture -> continuous/pulse/binary/counter/envelope/image -> downstream handoff.
- `Phase checklist`: timestamps, CHOPs, parameters, visual/audio checkpoints.
- `Recipe library updates`: which stable recipe bucket this tutorial improves.
- `Downstream use`: what kind of visual project can consume the signal and which direction skill should own the visual details.
- `Uncertainties`: audio source, missing channel names, or visual moments requiring confirmation.
