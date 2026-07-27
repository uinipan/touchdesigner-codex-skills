# Calibration and Debugging

## Coordinate calibration

Do not assume normalized MediaPipe `0..1` maps directly to the output. Account for:

- camera mirroring;
- TOP flips;
- aspect-ratio crop;
- fit mode such as Fill, Fit, or Native Resolution;
- final interaction domain;
- panel or render transforms after the cursor TOP.

Calibrate with four poses: left, right, top, and bottom. Record the live midpoint value at each visible output edge and use those measured values as the Math CHOP From Range.

Example for a horizontally cropped camera feed:

```text
input X  0.275 .. 0.725
output X -0.5  .. 0.5
```

This example is project-specific. Measure again if the camera or output aspect ratio changes.

For direction:

```text
normal X:  input low..high → output -0.5..0.5
mirror X:  input low..high → output  0.5..-0.5
normal Y:  choose direction that matches the displayed camera after all TOP flips
```

If Y aligns but X does not, change only the X From Range or reverse its To Range. Do not disturb the working Y mapping.

## Aspect-ratio crop formula

When a source of aspect ratio `As` is center-cropped to output aspect ratio `Ao`:

- If `As > Ao`, horizontal content is cropped. The visible normalized X width is `Ao / As`.
- If `As < Ao`, vertical content is cropped. The visible normalized Y height is `As / Ao`.

For horizontal crop:

```text
visible_width = Ao / As
x_min = (1 - visible_width) / 2
x_max = 1 - x_min
```

Use this only as an initial estimate. Final calibration should use measured live edge positions because upstream components may already crop or transform the image.

## Common faults

### Cursor moves in the opposite X direction

Reverse the X output range or remove one redundant mirror. Check both the camera display path and the landmark path; mirroring only one path causes mismatch.

### Cursor is centered but cannot reach the sides

Narrow the input From Range to the actually visible camera crop. Do not enlarge the output range beyond the interaction domain.

### Cursor jumps to the center when no hand is present

Gate the cursor with `hand_active`. Hide it and optionally move it offscreen. MediaPipe channels often fall back to zero when tracking disappears; mapping zero can create a valid-looking center or edge position.

### Pinch flickers

Use close/release hysteresis, add a small debounce, and inspect whether Z noise dominates the distance. Consider XY-only distance.

### A pinch starts interaction but never releases

Ensure loss of hand presence forces `pinch_active=0`. Verify the downstream component receives both the held state and its falling edge.

### Click works but drag does not

The downstream component probably receives `pinch_start` instead of `pinch_active`. A drag requires the held signal for every frame until release.

### Drag works but a discrete action repeats

The downstream action probably receives `pinch_active` every frame. Feed it the one-frame `pinch_start` pulse instead.

### Parameter changed but output did not

Inspect cooking and active/bypass flags. Force-cook only the relevant operator, then verify the real output. Do not treat parameter assignment as proof that the visual or CHOP result changed.

## Final evidence

Before reporting completion, record:

- actual source channel names;
- measured input edge ranges;
- final output ranges;
- pinch close/release thresholds;
- whether distance uses XYZ or XY;
- output Null path and channel values;
- downstream binding expressions;
- errors/warnings;
- saved project path.
