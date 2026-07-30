# Manual Audio Analysis Recipes

Use these recipes only when the packaged TOX lacks the required signal, the user requests analyzer development, or a tutorial experiment needs internal CHOP access.

## Overall Envelope and Motion

```text
Audio File In / Audio Device In
-> Math CHOP (average channels)
-> Analyze CHOP (Maximum or RMS Power)
-> Filter/Lag CHOP
-> Math CHOP (map and clamp)
-> Null CHOP
```

Branch the smoothed value through `Speed CHOP` for accumulated motion.

Verified TouchDesigner 2023 details:

- RMS Power menu name is `rmspower`.
- A tested peak block used `Math chanop=avg`, gain `0.5`, `Analyze maximum`, and a Gaussian Filter width of `0.2 seconds`.
- `Speed CHOP` output depends on elapsed run time and reset timing.

## Kick/Snare Event Lane

Preferred custom lane:

```text
audio source
-> Audio Analysis COMP
-> Select CHOP (kick snare)
-> Trigger and/or Count CHOP
-> Null CHOP
```

Verify that the Audio Analysis COMP output actually includes `kick` and `snare`. A typical full bus may include:

```text
low mid high kick snare rythm smsd fmsd spectralCentroid
```

Use the raw/trigger lane for one-shot events and Count CHOP for persistent state. A manually thresholded detector is only an approximate fallback.

## RMS Speed Lane

```text
audio source
-> Math CHOP (average)
-> Analyze CHOP (RMS Power)
-> Speed CHOP
-> Math CHOP
-> Null CHOP
```

Use for scroll, rotation, noise phase, texture offset, and time progression. Do not use accumulated speed as a loudness value.

## Frequency Bands

```text
Audio Spectrum CHOP
-> select/reduce bass, mid, or high range
-> Analyze/Math CHOP
-> Filter/Lag CHOP
-> Null CHOP
```

Record frequency boundaries, reduction method, observed ranges, and smoothing. Choose bands by the musical event that should control each visual layer.

## Spectrum Texture

```text
Audio Spectrum CHOP
-> CHOP to TOP
-> TOP processing
```

TouchDesigner 2023 notes:

- Operator type string: `audiospectrumCHOP`.
- Point CHOP to TOP at the spectrum path through its `chop` parameter rather than connecting CHOP and TOP families directly.
- A square custom output such as 512×512 is easier to use than a thin `rowscropped` result.
- Inspect and normalize the mask before Add/Over compositing to avoid washing the image white.

Use spectrum textures for bars, scanlines, masks, displacement, UV offsets, and GLSL texture inputs.

## Debugging

Inspect in this order:

1. source waveform;
2. analysis output;
3. mapped/smoothed Null;
4. exported target parameter;
5. visual output.

Use viewer flags for inspection without taking over the project's display/render flags.
