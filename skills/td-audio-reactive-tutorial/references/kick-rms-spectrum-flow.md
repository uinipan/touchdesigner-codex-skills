# kick.3.toe Kick RMS Spectrum Flow

Observed project shape:

```text
source: /project1/audiofilein1
```

## Node Lanes

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

Observed test read:

```text
audioAnalysis/out1 channels = low, mid, high, kick, snare, rythm, smsd, fmsd, spectralCentroid
count_events/kick = 26
count_events/snare = 0
analyze_rms/chan1 ~= 0.121
math_speed_out/chan1 ~= 1.141
null_spectrum = 1 channel / 22050 samples
```

