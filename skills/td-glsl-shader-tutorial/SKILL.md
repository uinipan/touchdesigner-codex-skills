---
name: td-glsl-shader-tutorial
description: Learn TouchDesigner tutorials focused on GLSL TOP/MAT, shader code, raymarching, signed distance fields, feedback shaders, uniforms, texture inputs, UV math, color functions, and GPU visual effects. Use when the tutorial's main reusable value is shader structure or GPU code patterns.
---

# TD GLSL Shader Tutorial

Use this skill to turn GLSL and shader tutorials into reusable code patterns. The output should preserve shader architecture, uniform wiring, coordinate assumptions, and debugging checkpoints so the idea can be reused beyond the original scene.

## Workflow

1. Identify the shader role.
   - Classify as GLSL TOP, GLSL MAT, compute-style TOP feedback, raymarch/SDF, image filter, displacement/material shader, or hybrid.
   - Record all inputs: textures, CHOP uniforms, DAT code, resolution, time, mouse/control values, audio, or camera data.
   - Note whether the tutorial depends on TouchDesigner-provided uniforms or custom parameters.

2. Map the code structure.
   - Preserve function roles: coordinate setup, noise, distance field, normal, lighting, palette/color, feedback, compositing, and output.
   - Record uniform names, types, ranges, default values, and TouchDesigner parameter bindings.
   - Capture texture sampling assumptions: UV origin, aspect correction, channel usage, wrap mode, and pixel/normalized coordinates.

3. Extract reusable shader patterns.
   - Explain the idea behind each important function or formula in plain language.
   - Keep compact code snippets only when the exact formula matters.
   - Mark dependencies between code and network nodes, especially feedback loops and multi-pass setups.

4. Distill direction knowledge.
   - Convert the tutorial's exact shader into a generalized shader architecture or formula pattern.
   - Add new classification signals when this tutorial reveals a subtype, such as image filter, raymarch/SDF, feedback shader, GLSL MAT, or multi-pass TOP.
   - Preserve reusable code structure, uniform wiring, coordinate assumptions, and debugging guidance. If TouchDesigner testing is needed, limit it to one shader pass, uniform group, feedback loop, or texture-input block.

5. Verify visually and by errors.
   - Check TouchDesigner node errors after code changes.
   - Use flat color, UV gradient, or simple signed distance previews to isolate failures.
   - Debug in this order: compile errors, output alpha, UV/aspect, uniforms, texture inputs, feedback persistence, color/tonemapping.
   - Classify visual checkpoints as `matches`, `close`, `different`, or `unknown because no keyframe/screenshot`.

## Knowledge To Preserve

- Shader type and network context.
- Uniform list with source nodes and parameter ranges.
- Core functions and formulas that define the look.
- Multi-pass or feedback wiring.
- Debugging notes for black output, compile errors, wrong aspect ratio, inverted UVs, unstable feedback, or washed-out color.

## Output Shape

Produce a compact tutorial type note with:

- `Type`: GLSL/shader.
- `Shader architecture`: inputs -> functions -> output.
- `Uniform map`: names, ranges, bindings, defaults.
- `Phase checklist`: timestamps, code/network changes, checkpoint images.
- `Reusable code patterns`: formulas or structures worth saving.
- `Uncertainties`: missing code, unclear uniforms, or visuals requiring confirmation.
