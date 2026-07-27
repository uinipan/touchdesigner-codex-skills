---
name: td-compositing-render-tutorial
description: Learn TouchDesigner tutorials focused on TOP compositing, Render TOP setups, cameras, lights, materials, feedback/post-processing, bloom, blur, color correction, edge/glow effects, and final visual polish. Use when the tutorial's main reusable value is render pipeline or image-processing style.
---

# TD Compositing Render Tutorial

Use this skill to turn rendering, camera, material, and TOP post-processing tutorials into reusable visual pipeline knowledge. The output should explain how the final image is assembled and which parameters control readability, depth, contrast, glow, and polish.

## Workflow

1. Identify the image pipeline.
   - Classify as 3D render setup, material/lighting, camera/composition, feedback TOP, image filter chain, color grading, bloom/glow, or hybrid.
   - Separate source imagery, render pass, post-processing pass, preview/output nodes, and export/movie nodes.
   - Record the final display/output node separately from intermediate helper previews.

2. Map visual layers.
   - Preserve each layer's role: background, geometry render, mask, edge, blur, displacement, feedback trail, glow, color correction, vignette, text/UI, final composite.
   - Record blend modes, opacity, resolution, pixel format, feedback reset behavior, and alpha handling.
   - Capture camera/lens/light/material settings that visibly change depth, scale, or highlights.

3. Extract reusable visual recipes.
   - Group chains as patterns such as `render -> edge -> blur -> add`, `feedback -> transform -> level`, `mask -> composite`, or `depth/normal pass -> post`.
   - Explain which parameters change softness, intensity, persistence, contrast, palette, and spatial framing.
   - Note whether the recipe depends on input resolution, alpha premultiplication, or HDR-like values.

4. Distill direction knowledge.
   - Convert the tutorial's exact render or TOP chain into a generalized visual pipeline recipe.
   - Add new classification signals when this tutorial reveals a subtype, such as camera/lighting, material lookdev, feedback trail, bloom/glow, color grade, or final output.
   - Preserve reusable layer maps, blend rules, polish controls, and debugging guidance. If TouchDesigner testing is needed, limit it to one render/material block, camera setup, TOP chain, feedback trail, or color/glow stage.

5. Verify the final image.
   - Compare keyframes for composition, contrast, color, glow radius, trail length, and framing.
   - Debug in this order: source/render visible, alpha/blend, resolution/aspect, feedback reset, level/brightness, camera/light/material, final output path.
   - Classify each checkpoint as `matches`, `close`, `different`, or `unknown because no keyframe/screenshot`.

## Knowledge To Preserve

- Full image pipeline from source to final output.
- Blend/composite choices and alpha assumptions.
- Camera, light, material, and render settings that control the look.
- TOP effect chain with visual-critical parameters.
- Tuning advice for black output, washed-out image, too much glow, missing transparency, blurry detail, or wrong framing.
- For painterly feedback / watercolor-cloud depth:
  - Use two nested `Feedback TOP` loops: first loop records color strokes with a slow fade (`Layer TOP` upper opacity ≈ 0.97), second loop diffuses the accumulated image.
  - Soften hard edges with `Slope TOP` (strength ~8, sample step 5,5) → `Blur TOP` → `Displacement TOP` with very small weight (0.001–0.01 range).
  - Create selective depth of field with `Luma Blur TOP` driven by a high-contrast monochrome `Noise TOP` mask (period ~2, low harmonics, low exponent) rather than the source image brightness.
  - Tune `Black Filter` / `White Filter` on `Luma Blur TOP` to blur only dark or only bright regions, giving some edges sharp while others stay dreamy.
  - Always keep resolutions consistent and use 32-bit Float on noise/displacement nodes to avoid banding or artifacts.
- For hard-edge glitch compositing, preserve:
  - `CHOP to TOP` or line source -> `Noise TOP` -> `Threshold TOP` -> `Composite TOP Difference` as the base black/white layer.
  - UV remap chains built from horizontal/vertical `Ramp TOP` into `Reorder TOP` RG maps, with `32-bit float` pixel format when offsets are composited into UVs.
  - Low-resolution Noise TOPs using nearest-neighbor smoothing for pixel-block offsets, and stripe noise made by scaling one transform axis to zero.
  - Time displacement chains such as `Texture 3D TOP -> Time Machine TOP`, with pixelated/noisy offset maps and a note about cache/performance cost.
  - Mirrored X/Y effect pairs, such as Displace X plus Displace Y or Feedback X plus Feedback Y, combined by Difference/Add/Over.

## Output Shape

Produce a compact tutorial type note with:

- `Type`: compositing/render.
- `Pipeline`: source/render -> post -> final output.
- `Layer map`: each visual layer and blend method.
- `Phase checklist`: timestamps, nodes, parameters, checkpoint images.
- `Polish controls`: contrast, glow, blur, persistence, color, framing.
- `Uncertainties`: missing render settings, screenshots, or output assumptions.
