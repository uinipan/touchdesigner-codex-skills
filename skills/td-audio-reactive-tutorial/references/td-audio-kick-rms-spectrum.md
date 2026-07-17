# TD Audio Kick RMS Spectrum

Reference three-lane project shape:

```text
source: /project1/audiofilein1
```

## Node Lanes

## Audio Analysis COMP Source

The event lane depends on a packaged Audio Analysis COMP. It is not a normal CHOP type that can be assumed to exist as `/project1/audioAnalysis1` in every project.

Build order for a new project:

1. Search the target parent for an existing COMP whose `out1` contains `kick` and `snare`.
2. Prefer a full Audio Analysis bus with channels:

```text
low, mid, high, kick, snare, rythm, smsd, fmsd, spectralCentroid
```

3. If one exists, copy that COMP into the new loose workflow and name it with the workflow prefix, for example `tdakrs2_audioAnalysis`.
4. If none exists, load the Palette tox directly:

```text
C:\Program Files\Derivative\TouchDesigner\Samples\Palette\Tools\audioAnalysis.tox
```

Use `parent.loadTox()` rather than GUI drag simulation, then rename the loaded component to `<prefix>audioAnalysis`.

Important loaded shape:

```text
loadedRoot = parent.loadTox(audioAnalysis.tox)
actualAudioAnalysis = loadedRoot.op('audioAnalysis')
actualAudioAnalysis/out1 -> kick/snare bus
```

The loaded root may not have a direct `out1`. Use the child `audioAnalysis` when present, or copy that child out and rename it to `<prefix>audioAnalysis`.

5. Connect the new audio-source null into the copied or loaded actual Audio Analysis COMP, then connect `<prefix>audioAnalysis/out1 -> select_kick_snare`.
6. Verify `<prefix>audioAnalysis/out1` exists and includes `kick` and `snare` before creating `select(kick snare)`.
7. If the Palette tox is missing or cannot load, report the missing template and ask the user to add the Palette Audio Analysis COMP or provide/import a known-good `.tox`.
8. A hand-built kick/snare detector may be used only as an explicit approximate fallback. It is not equivalent to the packaged Audio Analysis COMP and should be labeled separately.

Palette import was probed in TD 2023: `audioAnalysis.tox` loaded successfully, its child `audioAnalysis/out1` exposed `low`, `mid`, `high`, `kick`, `snare`, `rythm`, `smsd`, `fmsd`, and `spectralCentroid`.

### Event Lane

```text
audiofilein1 -> null5 -> audioAnalysis1 -> select1 -> count2
```

| Node | Type | Important Parameters / Channels |
| --- | --- | --- |
| `audioAnalysis1/out1` | `outCHOP` | channels: `low`, `mid`, `high`, `kick`, `snare`, `rythm`, `smsd`, `fmsd`, `spectralCentroid` |
| `select1` | `selectCHOP` | `channames=kick snare` |
| `count2` | `countCHOP` | `triggeron=increase`, channels: `kick`, `snare` |

Treat `count2` as an event counter, not as an intensity value.

### RMS Speed Lane

```text
audiofilein1 -> null5 -> math4 -> analyze2 -> speed3 -> math5
```

| Node | Type | Important Parameters |
| --- | --- | --- |
| `math4` | `mathCHOP` | `chanop=avg`, `gain=1.0` |
| `analyze2` | `analyzeCHOP` | `function=rmspower` |
| `speed3` | `speedCHOP` | cumulative motion driver |
| `math5` | `mathCHOP` | `gain=1.0` |

Treat `math5` as motion progress or phase.

### Spectrum Lane

```text
math4 -> audiospect1 -> null8
```

| Node | Type | Important Parameters |
| --- | --- | --- |
| `audiospect1` | `audiospectrumCHOP` | `mode=visual`, `fftsize=8192`, `frequencylog=1`, `highfreqboost=0.75`, `outlength=2048` |
| `null8` | `nullCHOP` | one channel, many samples |

Use this as raw frequency data. For direct visual use, convert with CHOP to TOP; for parameter control, reduce it into bands first.

## Tested Loose Rebuild

Default rebuild tested in a live TD project:

```text
audiofilein1 -> tdakrs_null_audio

tdakrs_null_audio -> tdakrs_audioAnalysis -> tdakrs_select_kick_snare -> tdakrs_count_events

tdakrs_null_audio -> tdakrs_math_avg -> tdakrs_analyze_rms -> tdakrs_speed_motion -> tdakrs_math_speed_out

tdakrs_math_avg -> tdakrs_spectrum -> tdakrs_null_spectrum
```

Notes:

- Original nodes and original wiring were left unchanged.
- Only one new line was added from `/project1/audiofilein1` into the new audio-source null.
- Nodes were placed below the original flow in three readable lanes.
- A working `/project1/audioAnalysis1` was copied into the new loose workflow so it stayed independently editable without wrapping it in a Base COMP.
- If this rebuild is attempted in a project without `/project1/audioAnalysis1`, first locate another valid Audio Analysis COMP by its `out1` channel set. If none exists, pause and ask for/import a template.

Observed test read:

```text
audioAnalysis/out1 channels = low, mid, high, kick, snare, rythm, smsd, fmsd, spectralCentroid
count_events/kick = 26
count_events/snare = 0
analyze_rms/chan1 ~= 0.121
math_speed_out/chan1 ~= 1.141
null_spectrum = 1 channel / 22050 samples
```
