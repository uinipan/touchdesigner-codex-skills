---
name: td-geometry-sop-tutorial
description: Learn TouchDesigner tutorials focused on geometry, SOP networks, procedural meshes, curves, surfaces, deformation, normals, UVs, instancing source geometry, and camera-visible 3D form. Use when a tutorial's main value is reusable SOP construction or geometric transformation knowledge.
---

# TD Geometry SOP Tutorial

Use this skill to turn a geometry-heavy TouchDesigner tutorial into reusable procedural modeling knowledge. The output should help future tutorial analysis answer: "What node pattern creates this form, which parameters control the look, and how do I recognize the technique?"

## Workflow

1. Identify the geometric primitive and endpoint.
   - Name the tutorial's final visible geometry: grid, line web, tube, sphere, metaball, text, imported mesh, point cloud, or custom SOP.
   - Record the real tutorial endpoint node/type separately from preview Render TOPs or helper Nulls.
   - Note whether the geometry is generated, imported, copied, instanced, deformed, or converted from TOP/CHOP data.

2. Build a phase map.
   - Split the tutorial into phases: base shape, topology/detail, deformation, attributes, material/readability, camera/render.
   - For each phase, record timestamp range, nodes added, parameters changed, expected visual result, and common wrong-looking result.
   - Preserve any parameter that changes silhouette, density, scale, orientation, smoothing, or surface continuity.

3. Extract reusable SOP patterns.
   - Group node sequences as patterns such as `grid -> noise -> displace`, `line -> resample -> sweep`, `copy to points`, `attribute transfer`, `feedback deformation`, or `SOP from CHOP/TOP`.
   - Explain why the sequence works, not only which nodes appear.
   - Mark required coordinate assumptions: units, axis orientation, normalized ranges, aspect ratio, and origin placement.

4. Distill direction knowledge.
   - Convert the tutorial's exact node chain into a generalized geometry recipe.
   - Add new classification signals when this tutorial reveals a subtype, such as curves, surface deformation, topology repair, or SOP-from-data.
   - Preserve reusable node, parameter, and debugging guidance. If TouchDesigner testing is needed, limit it to a single geometry block such as one SOP chain, deformation stage, or attribute conversion.

5. Verify visually.
   - Compare against keyframes or screenshots at each phase endpoint.
   - Classify each phase as `matches`, `close`, `different`, or `unknown because no keyframe/screenshot`.
   - Debug in this order: topology/count, transform/scale, deformation amplitude/frequency, normals/material, camera/render.

## Knowledge To Preserve

- Node pattern name and exact node chain.
- Visual-critical parameters and their effect on silhouette, density, motion, or readability.
- Range mapping choices, especially values normalized into `0..1`, `-1..1`, world units, or pixel units.
- For woven / thread-line geometry:
  - Start with a point distribution (scatter/sprinkle) on a source shape (text, mesh, image, or particle set).
  - Generate connections in a Script SOP or Python-driven geometry block: connect nearby points, add random jitter, sag, and drape threads across gaps.
  - Visual-critical parameters: point density, layer count, thread spacing, sag/gap sag, drape amount/reach, edge jitter, and thread weight.
  - CPU implementation is easy to customize but hits a bottleneck with video/high-res inputs; GPU version bakes the weave once and drives motion with POPs/GLSL.
  - Common pitfall: high-resolution TOP inputs create too many points and kill CPU performance; downsample before weaving.
- Any trick that prevents broken geometry: resampling, fusing, normal recalculation, converting primitives, or matching point counts.
- Minimal reusable recipe that can explain a different tutorial in the same direction.

## Output Shape

Produce a compact tutorial type note with:

- `Type`: geometry/SOP.
- `Core pattern`: the reusable node chain.
- `Phase checklist`: timestamps, nodes, parameters, checkpoint images.
- `Visual-critical parameters`: what each parameter changes and how to tune it.
- `Reusable recipe`: a generalized version that does not depend on the exact tutorial scene.
- `Uncertainties`: timestamps or visuals still requiring confirmation.
