---
name: td-particle-instancing-tutorial
description: Build, analyze, debug, and validate TouchDesigner particle, point-cloud, and instancing systems. Use for particlesGPU, GPU particles, POP point fields, TOP-to-POP image particles, animated-mesh emitters, SOP/CHOP/TOP position conversion, Copy POP/SOP, Geometry COMP instancing, particle sprites, forces, life/age, feedback trails, and particle performance or visibility problems. Also use when learning particle tutorials or turning an image, video, mesh, audio signal, or tracking input into many moving points or repeated objects.
---

# TD Particle and Instancing

Treat every particle system as a data pipeline:

`source -> representation -> state/update -> attributes -> render -> post`

Do not begin with styling. First prove where positions live, whether the system is stateful, and how one point becomes one visible particle or instance.

## Start Here

1. Inspect the active TouchDesigner version and existing operators before editing. Confirm whether POPs exist. Reuse a working same-type operator or enumerate its real parameters and menu names; do not invent parameter names or enum values.
2. Decide whether the user wants analysis, a build, a repair, or tutorial learning. Do not modify a live project for an analysis-only request.
3. Choose one architecture with the decision table below.
4. Build or inspect one block at a time: source, update, attributes, render, then post.
5. Record the public input/output contract and run the acceptance checks before calling the result complete.

## Architecture Decision

| Need | Preferred architecture | State |
| --- | --- | --- |
| Image/video becomes editable points, boxes, or layers | `TOP -> TOP to POP -> attributes -> Copy POP` | Usually stateless deformation |
| TD 2023/no POP, moderate image point count | `TOP -> adaptive Fit TOP -> Script SOP -> Noise SOP -> Copy SOP` | Stateless deformation |
| Tens of thousands of particles with life, velocity, forces, or trails | `particlesGPU` / GPU state textures | Stateful simulation |
| Animated FBX/mesh emits particles | `Import Select SOP -> Deform SOP -> Sprinkle SOP -> SOP to CHOP -> CHOP to TOP -> particlesGPU` | Stateful simulation |
| Image directly writes POP color/scale/depth | `Grid POP -> Attribute POP -> GLSL POP -> Copy POP` | Usually stateless unless feedback is added |
| Repeated geometry follows CHOP/SOP attributes without life/forces | Geometry COMP instancing / Copy SOP or POP | Stateless instancing |

Read [references/architecture-recipes.md](references/architecture-recipes.md) before building one of these architectures. Use the smallest architecture that satisfies the motion requirement. Do not call `Noise POP` deformation a particle simulation when it has no life, velocity, or persistent state.

## Required Data Map

Before building or debugging, write a compact map:

| Field | Owner | Representation | Consumer |
| --- | --- | --- | --- |
| position | source or simulation | POP `P`, SOP point, CHOP channels, or RGB float TOP | update/render |
| velocity | simulation | state texture or point attribute | next update |
| scale | source/update | `pscale`, instance scale channels, age lookup | Copy/instance/render |
| rotation | source/update | `rot`, quaternion, instance rotation channels | Copy/instance/render |
| color/alpha | source/lookup | `Cd`, RGBA TOP, age lookup, sprite texture | material/render |
| life/age/ID | simulation | state texture or attributes | update/lookups |

Mark coordinate space and range explicitly: UV `0..1`, centered `-1..1`, pixels, SOP/world units, degrees, radians, normalized age, or raw audio range.

## Build and Inspection Workflow

### 1. Prove the source

- Display source geometry, point cloud, or position TOP without forces or post effects.
- Confirm point count, bounds, aspect ratio, alpha, and coordinate range.
- For image-driven systems, keep position and color inputs at identical resolution and aspect ratio.
- Preserve the input aspect ratio when limiting resolution. Test landscape, portrait, square, and smaller-than-limit inputs instead of forcing every source into one fixed width/height.
- For mesh emission, center the animated mesh and confirm `Deform SOP` animation before sprinkling points.

### 2. Prove the representation

- For RGB position TOPs, use floating-point format and inspect R/G/B independently.
- For TOP-to-POP, reduce resolution first; pixels become points and copies multiply geometry count.
- For SOP/CHOP/TOP conversion, confirm the CHOP-to-TOP data format stores XYZ as RGB.
- For POP copies, confirm template attributes such as `pscale`, `rot`, and color are enabled.
- For Script SOP points, record `P`, `Cd`, alpha, and `N` ownership. A Noise SOP acting on position displaces along point normals; prove normals are nonzero when points use degenerate or one-vertex primitives.

### 3. Prove state and motion

- Start with gravity, turbulence, external forces, and feedback disabled.
- Confirm reset behavior and a stable birth/life baseline.
- Add one motion source at a time; observe bounds and lifetime over time.
- Test controls against data, not only parameter evaluation: compare point positions at zero/nonzero motion, compare frames for speed, and compare raw render output at zero/nonzero depth.
- Keep audio or tracking responsible for control signals only. This skill owns how those signals change birth, size, force, turbulence, reset, or attributes.

### 4. Prove visibility

- Use a simple circle/sprite or constant material first.
- Confirm transparency, camera, bounds, material assignment, particle map, and composite order.
- Inspect the Geometry COMP interior and remove or disable generated default SOP geometry before judging the particle render.
- A front orthographic camera hides Z-only relief. Add a small verified viewing angle when `Depth` is meant to be visible.
- Keep particle layer separate from background and post-processing until it is visible.
- Add bloom, feedback, color grading, or background sampling only after the raw layer passes.

### 5. Measure performance

- Record active/max particle count, source resolution, copied primitive count, render resolution, pixel format, and FPS.
- Change one cost driver at a time.
- Prefer GPU state textures and one instanced render batch for large dynamic systems.
- Reduce TOP/POP resolution before reducing visual clarity elsewhere.
- Preserve the user's Viewer state unless they explicitly ask to change it. Record active viewers when diagnosing cook cost; do not assume they should all be on or off.

## Debug Order

Always debug upstream to downstream:

1. source exists;
2. count/resolution is nonzero and plausible;
3. positions vary and lie inside expected bounds;
4. simulation is born/resetting/updating;
5. scale and alpha are nonzero;
6. sprite/material and transparency are valid;
7. camera/render sees the bounds;
8. composite/post preserves the particle layer.

Read [references/debugging-and-acceptance.md](references/debugging-and-acceptance.md) for symptom-specific checks and the test scorecard.

## Evidence Rules

Label extracted knowledge as one of:

- `tutorial-confirmed`: supported by captions plus keyframe or visible node evidence;
- `TD-tested`: reproduced or inspected in the current TouchDesigner project;
- `provisional`: inferred from metadata, transcript-only evidence, or a different TD version.

Do not promote exact node parameters or performance claims from `provisional` evidence. Read [references/evidence-map.md](references/evidence-map.md) when learning from the current particle tutorial corpus or updating this skill.

## Output Contract

For analysis, learning, builds, and repairs, report:

- `Goal and architecture`
- `Boundary`: parent COMP, inputs, output node, operators touched
- `Data map`: position, velocity, scale, rotation, color/alpha, life/age/ID
- `Build phases`: source, representation, update, attributes, render, post
- `Critical controls`: parameter -> visual/motion effect -> failure cue
- `Performance`: count, resolution, format, FPS if observable
- `Validation`: each checkpoint as `pass`, `close`, `fail`, or `unknown`
- `Evidence`: tutorial-confirmed, TD-tested, or provisional
- `Uncertainties and next smallest test`

For a build request, leave one stable public output such as `OUT_PARTICLES` or `OUT_INSTANCES` and keep temporary diagnostics clearly named. Preserve the user's existing network unless integration was explicitly requested.

## Handoff Boundaries

- Let `td-audio-reactive-tutorial` own audio analysis and signal shaping; consume its clean envelope, trigger, or spectrum output.
- Let `td-glsl-shader-tutorial` own nontrivial shader code; this skill owns particle attribute and simulation contracts around it.
- Let `td-compositing-render-tutorial` own final grading and complex feedback looks; this skill must first expose a valid raw particle render.
- Let `td-interaction-tracking-tutorial` own tracking and calibration; consume normalized positions, IDs, confidence, or gestures.
