# CHOP Network Pattern

## Source landmarks

Inspect the normalized-data CHOP and select channels equivalent to:

```text
h1:thumb_tip:x
h1:thumb_tip:y
h1:thumb_tip:z
h1:index_finger_tip:x
h1:index_finger_tip:y
h1:index_finger_tip:z
```

Also select a reliable hand-presence channel, such as `h1:hand_active`, or derive presence from the plugin's active/score output.

Do not hardcode `h1` if the project selects hands by handedness. Resolve the desired hand first and keep the channel prefix consistent.

## Derived signals

Given thumb tip `T=(tx,ty,tz)` and index tip `I=(ix,iy,iz)`:

```text
midpoint = (T + I) / 2
delta = T - I
distance = sqrt(dx*dx + dy*dy + dz*dz)
```

If noisy Z data destabilizes the gesture, use XY distance instead:

```text
distance_xy = sqrt(dx*dx + dy*dy)
```

Choose one method and validate it with live values.

## Recommended operator layout

```text
MediaPipe normalized data
  → Select thumb XYZ ─┐
                      ├→ Math midpoint → Select X/Y/Z → coordinate Math CHOPs
  → Select index XYZ ─┘
          │
          └→ subtract/delta → square/sum/sqrt → pinch distance

hand presence ───────────────┐
distance → threshold/state ──┴→ AND → pinch_active
                                  ├→ off-to-on → pinch_start
                                  └→ on-to-off → pinch_end

mapped position + distance + radius + states
  → Merge/Rename
  → OUT_HAND_PINCH
```

Use explicit Rename CHOPs or channel-name parameters so the output contract does not depend on upstream MediaPipe names.

## Pinch threshold

Start by observing the distance during:

- firm pinch;
- relaxed pinch;
- open fingers;
- tracking jitter.

Set separate thresholds when possible:

```text
close_threshold < release_threshold
```

Example normalized starting values:

```text
close_threshold   = 0.055
release_threshold = 0.075
```

These are starting points, not universal constants. Hand size, camera distance, model output, and whether Z is included all affect the values.

Use a Logic CHOP, Count/State pattern, or small callback only when necessary to implement hysteresis. Add a short Filter/Lag or debounce after measurement if the state flickers, but keep release on lost tracking immediate.

## Cursor and interaction

Example output position domain:

```text
x = -0.5 .. 0.5
y = -0.5 .. 0.5
```

Example distance-to-radius mapping:

```text
distance 0.00 .. 0.08
radius   0.025 .. 0.20
```

Clamp mapped position and radius unless deliberate overscan is required.

For a Circle TOP:

```text
center_x = pinch_active ? x : 2
center_y = pinch_active ? y : 2
radius_x = pinch_active ? radius : 0
radius_y = pinch_active ? radius : 0
```

Moving to `(2,2)` is optional but useful when the downstream interaction scans an input TOP and a zero-radius cursor might still leave a pixel or stale hit.

For a component with a Pull/held parameter:

```python
op('/project1/OUT_HAND_PINCH')['pinch_active'].eval()
```

Use the actual absolute or component-relative path in the live project.
