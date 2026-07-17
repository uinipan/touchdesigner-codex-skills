# Particle Evidence Map

Use this map to avoid confusing a search result, a tutorial observation, and a local TD test.

## Tutorial Corpus

The classification note groups particle tutorials around these recurring subtypes:

- audio-reactive particle cloud;
- TOP/state-texture point particles;
- cellular-noise instancing;
- image/video-driven 3D point clouds;
- particle cloud plus plexus/post-processing;
- image/video to POP points and copied geometry.

The raw classification is a routing map, not proof of exact parameters. Only promote details after captions plus keyframes or a local reproduction.

## Studied Tutorials

### Image to 3D Particles (`6mFQRTk5b10`)

- Evidence: captions, local keyframes, structured learning note.
- Confirmed: `TOP -> POP`, silhouette filtering, `pscale`/Y rotation attributes, Copy POP geometry, depth layers, Noise POP deformation, color inheritance, SSAO/Bloom handoff.
- Boundary: this is mostly a stateless POP/instancing system, not a lifetime simulation.

### Image / Video to particlesGPU (`TbM2_Cvygww`)

- Evidence: captions, local keyframes, structured learning note.
- Confirmed: ramp-built RGB position texture, separate color input, birth/life/size/turbulence tuning, float render for feedback, source/particle mask composite.
- Boundary: exact component parameter names must be checked against the installed palette version.

### Animated FBX into Particles (`NGL1BNI-mgM`)

- Evidence: captions/timeline.
- Confirmed: Import Select SOP, Deform SOP, Sprinkle SOP, SOP-to-CHOP-to-TOP RGB conversion, particlesGPU source, age-based color/size lookup.
- Visual status: treat exact appearance as provisional when no compared keyframes are loaded.

### Image Sampling with GLSL POP (`_sdtHmMir7g`)

- Evidence: captions and structured note; no extracted keyframes in that run.
- Confirmed conceptually: point-position UV mapping, image sampling, POP color/scale attribute writing, Copy POP rendering.
- Exact GLSL template functions and visual match remain provisional until checked in the active TD version.

## Local TD Tests

### Bubble Overlay particlesGPU block

- Evidence: local builder, inspection/repair scripts, rendered previews, live parameter reads.
- TD-tested: palette `particlesGpu.tox` loading, 30k default target, float sprite texture, raw particle output separation, background-independent simulation, mouse force handoff, wrap-boundary shader patch, particle-only bloom before background composite.
- Lesson: a valid simulation can still look black because the failure lies in sprite alpha, material/render selection, or composite order. Preserve raw-layer diagnostics.

### TD 2023 adaptive image-to-particles block

- Evidence: live TouchDesigner 099.2023.11280 build, forced cooks, point-array comparisons, rendered previews, aspect-ratio probes, and saved `.toe` versions.
- TD-tested: POP availability gate; aspect-preserving Fit TOP limit behavior for landscape/portrait/square/small sources; Script SOP ownership of `P`, `Cd`, alpha, and `N`; low-poly Circle plus Copy SOP rendering; removal of generated Geometry COMP Torus; raw RGBA16-float output; stable `OUT_PARTICLES`.
- TD-tested failure: Noise SOP amplitude and time translate evaluated correctly while point displacement stayed exactly zero because one-vertex particle polygons had no usable normal. Writing nonzero `N` produced measurable motion; a small geometry tilt made brightness-derived Z depth visible.
- TD-tested usability: a fixed square sample stretched the source; raising sample density without reducing particle radius caused overlap and apparent blur; direct editable resolution limits generalized across input aspect ratios.
- Boundary: this is a stateless CPU SOP/Copy compatibility route for moderate counts, not a lifetime simulation and not the preferred architecture for tens of thousands of dynamic particles.

## Updating This Skill

Add a rule to the main skill only when it is either:

1. repeated across at least two independent tutorial systems; or
2. reproduced in the active TouchDesigner project.

Keep tutorial-specific parameter values and version-sensitive node details in references. Mark unresolved claims `provisional`.
