---
name: td-interaction-tracking-tutorial
description: Learn TouchDesigner tutorials focused on interaction, body/hand/face tracking, MediaPipe, Kinect, LiDAR, depth cameras, sensors, OSC input, motion control, calibration, smoothing, and mapping human or device input into visuals. Use when a tutorial's main reusable value is live input, tracking data, or interaction design.
---

# TD Interaction Tracking Tutorial

Use this skill to turn interaction and tracking tutorials into reusable input-system knowledge. Treat TouchDesigner MCP as a block experiment workspace: test one input, mapping, calibration, or smoothing block at a time.

## Workflow

1. Identify the input source.
   - Classify as MediaPipe, Kinect/Azure Kinect, LiDAR, depth camera, webcam, OSC/mobile sensor, MIDI/control surface, mouse/touch, or custom plugin.
   - Record required devices, plugins, environment assumptions, and whether the tutorial can be learned without hardware.
   - Separate tracking acquisition, cleanup, mapping, interaction logic, and final visual response.

2. Map the data shape.
   - Preserve coordinate systems, units, confidence values, IDs, landmarks, skeleton joints, depth channels, and frame rate.
   - Record whether data appears as CHOP channels, DAT tables, TOP textures, SOP points, or custom COMP outputs.
   - Note calibration assumptions: camera orientation, body scale, screen mapping, origin, mirroring, and sensor range.

3. Extract reusable interaction patterns.
   - Group the tutorial into input capture, filtering/smoothing, selection, gesture/event detection, range mapping, visual target, and feedback.
   - Explain which parameters control latency, stability, sensitivity, dead zones, thresholds, and spatial mapping.
   - Preserve debugging cues for missing devices, dropped IDs, jitter, mirrored axes, bad scale, and unreliable confidence.

4. Run block experiments when useful.
   - Limit each TD experiment to one input or mapping block.
   - Define the hypothesis: what value should change, what visual/data output should prove it, and which tutorial timestamp supports it.
   - Record observations, failed attempts, useful ranges, and what should update this skill.

## Knowledge To Preserve

- Input source and data format.
- Calibration and coordinate assumptions.
- Smoothing, filtering, threshold, confidence, and dead-zone rules.
- Gesture or event detection logic.
- Mapping from human/device input to visual parameter.
- Hardware/plugin requirements and fallback strategies.

## Output Shape

Produce a compact tutorial type note with:

- `Type`: interaction/tracking.
- `Input map`: source -> data format -> cleaned channels/points.
- `Interaction logic`: gestures, events, thresholds, and mapping rules.
- `Block experiments`: scope, hypothesis, observations, failed attempts.
- `Reusable patterns`: calibration, smoothing, mapping, and debugging heuristics.
- `Uncertainties`: hardware needs, missing plugin details, or visuals requiring confirmation.
