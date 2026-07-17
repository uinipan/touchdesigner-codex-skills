# Particle Debugging and Acceptance

## Symptom Checks

### Nothing is visible

1. Inspect source and raw particle output separately.
2. Confirm count/birth/life and pulse reset once.
3. Confirm position bounds overlap the camera.
4. Set scale and alpha to obvious nonzero constants.
5. Replace the material/sprite with a simple visible test.
6. Bypass feedback, bloom, GLSL color, and final composite.
7. Check render camera, geometry/material assignment, transparency, and composite input order.

### All particles sit at the origin

- Position channels/texture are constant, missing, or mapped to the wrong input.
- CHOP-to-TOP format may not be RGB XYZ.
- Instance Translate OP/channel names may be wrong.
- TOP position format may be clamped/quantized instead of float.

### A rectangular cloud appears instead of the subject

- Source background or alpha was not removed.
- Delete POP/filter condition keeps empty pixels.
- Color input includes an opaque background.
- Position and color resolutions/aspect ratios disagree.

### The image is stretched, cropped unexpectedly, or blurry

- A fixed square resolution may be stretching a landscape or portrait input.
- Use an aspect-preserving Fit/Limit stage and treat its width/height as maximum bounds, not a forced output shape.
- Test landscape, portrait, square, and smaller-than-limit inputs.
- Keep one scale for X and Y when mapping pixels into world space.
- When sampling resolution increases, retune particle radius; unchanged copies can overlap and make a sharper source look like a solid blurry shape.

### Color is missing or wrong

- Copy POP template color attribute is disabled.
- Material ignores point/instance color.
- Lookup input or age/color mode points to the wrong operator.
- RGB/RGBA data is reordered or sampled at a different resolution.
- A post/composite stage overwrites alpha or color.

### Motion explodes, jitters, or disappears

- Disable all forces, then restore one at a time.
- Inspect velocity magnitude and coordinate units.
- Lower turbulence magnitude before changing period.
- Check damping/drag, life, bounds behavior, and reset feedback.
- Distinguish frame-random noise from coherent time-translated noise.
- If Noise SOP amplitude changes but point displacement remains zero, inspect `N`. Position noise acts along point normals; degenerate one-vertex polygons may not produce a usable computed normal.
- Compare actual point arrays at motion `0` and a nonzero value. Do not accept parameter evaluation alone as evidence.
- For speed, compare noise-space translate values and point samples at two times. Speed cannot be visible until motion produces nonzero displacement.

### Depth changes numerically but not visually

- A front orthographic camera hides Z-only displacement.
- Confirm the SOP Z bounds change first, then add a small camera or geometry tilt and compare raw renders at depth `0` and a nonzero value.
- Keep depth validation separate from noise so the two controls do not mask one another.

### A white blob or unrelated shape renders

- Inspect the Geometry COMP interior for its generated default Torus or other SOP with Display/Render enabled.
- Confirm the particle source primitive type using its actual menu value.
- Reduce copied radius when sampling density increases; overlapping alpha-blended copies can saturate toward white.
- Record point, primitive, and vertex counts before blaming the material.

### Feedback bands or unstable colors

- Use floating-point Render TOP/state textures where accumulation requires it.
- Reduce feedback gain/opacity below 1.
- Inspect premultiplied alpha and composite operation.
- Bypass bloom/color grading to isolate the feedback loop.

### FPS collapses

- Reduce source resolution, particle count, copy geometry complexity, depth layers, and render resolution in that order while observing impact.
- Confirm only one intended render batch is active.
- Disable unused viewers and expensive post stages for comparison.
- Record active/max particles rather than only the requested count.
- Record active Viewer state, but preserve the user's requested Viewer policy instead of changing every Viewer by assumption.

## Acceptance Scorecard

Score each item `pass`, `close`, `fail`, or `unknown`.

| Check | Pass condition |
| --- | --- |
| Source | Correct asset/geometry is visible and bounded |
| Aspect | Landscape, portrait, square, and small inputs preserve aspect under the resolution limit |
| Count | Point/particle count is nonzero, plausible, and recorded |
| Position | Distribution matches the source; no unintended origin pileup/rectangle |
| State | Birth, life, reset, and update behave over time when stateful |
| Attributes | Scale, rotation, color, alpha, life/age/ID have known owners |
| Render | Raw particle layer is visible without post-processing |
| Motion | One isolated force/deformation produces the intended direction and timing |
| Controls | Each public control changes measured data or raw render output in its documented way |
| Performance | FPS and main cost drivers are recorded at the tested resolution/count |
| Replaceability | Source or sprite can be replaced without rewiring unrelated blocks |
| Output | Stable `OUT_PARTICLES`/`OUT_INSTANCES` exists and is documented |

Do not call a system complete when only the final composite looks plausible. Source, state, raw render, and performance must be independently inspectable.

## Minimal User Test

Invoke the skill with one of these prompts:

- `Use $td-particle-instancing-tutorial to turn this transparent image into a POP point-cloud block. Keep the source replaceable and expose OUT_INSTANCES.`
- `Use $td-particle-instancing-tutorial to inspect my current particlesGPU network. Diagnose why the particle layer is black; do not modify it.`
- `Use $td-particle-instancing-tutorial to build a 30k GPU particle block from the palette particlesGpu component, then report the acceptance scorecard.`
- `Use $td-particle-instancing-tutorial to learn this particle tutorial and update only reusable architecture or debugging knowledge.`
