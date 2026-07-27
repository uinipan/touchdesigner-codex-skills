---
name: td-mediapipe-pinch-interaction
description: Build, inspect, calibrate, and debug TouchDesigner MediaPipe thumb-index pinch interactions. Use when Codex needs to extract raw hand landmarks, map hand coordinates into TOP or panel space, calculate pinch distance and midpoint, show or hide an interaction cursor, convert pinch state into click/drag signals, repair mirrored or offset tracking, or connect MediaPipe control channels to interactive TouchDesigner components.
---

# TouchDesigner MediaPipe Pinch Interaction

Create a stable control layer between MediaPipe hand landmarks and downstream TouchDesigner interaction. Inspect the live project before editing; do not assume component or Null CHOP names.

## Workflow

1. Connect to the current TouchDesigner process using the available TD control method. If `auto-touchdesigner-mcp` is available, use its live-project inspection and error-checking workflow.
2. Locate the MediaPipe normalized landmark CHOP and enumerate its actual channel names.
3. Select the thumb-tip and index-tip XYZ channels from one hand. Prefer raw landmarks over a plugin-provided midpoint when precise mapping is required.
4. Compute midpoint, distance, hand presence, mapped position, cursor radius, and pinch state.
5. Publish a stable output Null CHOP contract.
6. Bind the output to the cursor and interaction component.
7. Validate mirroring, crop, loss of tracking, pinch transitions, and project errors before saving.

Read [references/network-pattern.md](references/network-pattern.md) when building or repairing the CHOP network. Read [references/calibration-and-debug.md](references/calibration-and-debug.md) when the hand and cursor do not align, the pinch flickers, or interaction remains active after tracking is lost.

## Inspect Before Editing

- Confirm the current `.toe`, target component, MediaPipe version, camera resolution, output resolution, and whether the camera image is mirrored or cropped.
- Enumerate real channels. Common examples are `h1:thumb_tip:x`, `h1:index_finger_tip:y`, and `h1:hand_active`, but naming varies.
- Read existing Select, Math, Logic, Filter/Lag, Null, Circle, and interaction parameters.
- Preserve unrelated nodes and user edits.

## Output Contract

Create one clearly named Null CHOP such as `OUT_HAND_PINCH` with:

```text
x
y
z
distance
radius
hand_active
pinch_active
pinch_start
pinch_end
```

Use `pinch_active` as a held state for click-drag. Use `pinch_start` as a one-frame click pulse. Use `pinch_end` for release-dependent behavior.

Never expose an active pinch when the tracked hand is absent:

```text
pinch_active = hand_active AND pinch_distance_below_threshold
```

## Interaction Binding

- Drive cursor position from mapped `x` and `y`.
- Drive cursor size from `radius` only if the visual design calls for distance-dependent size.
- When inactive, set radius/opacity to zero. Optionally also move the cursor outside the visible domain to protect downstream TOP-based hit testing.
- For drag behavior, bind the component's held/pull input to `pinch_active`.
- For discrete click behavior, bind a pulse action to `pinch_start`; do not feed a one-frame pulse into a system that expects a held mouse-down state.

## Validation

Test these cases:

1. No hand: `hand_active=0`, `pinch_active=0`, cursor hidden, no interaction.
2. Open hand: cursor may track if desired, but no click/drag.
3. Pinch begins: exactly one `pinch_start` pulse.
4. Pinch held while moving: continuous `pinch_active=1` and stable drag.
5. Pinch released: exactly one `pinch_end` pulse.
6. Tracking lost mid-pinch: release immediately and hide the cursor.
7. Move to all four camera edges: verify direction, crop, and reachable output bounds.
8. Inspect operator errors/warnings and confirm output channels numerically.

Save only after the live values and downstream behavior have been verified.
