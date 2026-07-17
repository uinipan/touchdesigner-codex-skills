# Particle Architecture Recipes

Use only the recipe matching the requested behavior. Parameter names can vary by TouchDesigner release; inspect the active operator before scripting.

## 1. Image or Video to POP Instances

Use when pixels should become editable POP points or copied geometry without lifetime simulation.

```text
source TOP
-> Fit TOP
-> optional Edge/Threshold/alpha mask
-> TOP to POP
-> delete empty points
-> Noise/Random/Attribute POP
-> Copy POP with Box/Circle/custom geometry
-> Geometry COMP -> Render TOP
```

Data contract:

- valid source pixels become points;
- source color/alpha becomes POP color and deletion mask;
- `pscale`, axis-specific `rot`, and color must be enabled as template attributes;
- point count is approximately valid source pixels; copied geometry and depth layers multiply cost.

Tutorial-confirmed starting heuristics:

- begin near `200 x 200`, then raise only when needed;
- threshold near `0.2` is a useful first silhouette test, not a universal default;
- random `pscale` around `0.5..1` and Y-only rotation around `-90..90` preserve readability better than full-axis randomness;
- keep duplicated depth layers close; excessive Z spacing makes disconnected slices;
- use `Noise POP` for deformation, but describe it as stateless unless persistent state is present.

## 2. Image or Video to particlesGPU

Use for high particle counts, life, velocity, forces, and feedback-style motion.

```text
source color TOP ---------------------------> color input
Ramp X + Ramp Y + optional height/depth TOP
-> Reorder TOP as RGB position texture ----> particle source input
particlesGPU -> raw particle TOP -> optional feedback/post
```

Data contract:

- R/G encode planar position; B encodes depth/height;
- position and color textures use identical resolution/aspect;
- alpha/background filtering happens before color input;
- particle state contains position, velocity, color/rotation, and life in floating-point textures.

Tutorial-confirmed tuning order:

1. disable gravity/bounce and strong forces;
2. use a simple line/circle sprite;
3. raise birth rate until the source forms quickly;
4. tune life and size;
5. add mild turbulence;
6. add feedback and color styling last.

TD-tested local pattern:

- the Derivative palette `particlesGpu.tox` can act as a stable simulation engine;
- a local bubble overlay used 30,000 particles, a replaceable RGBA16-float sprite, a separate raw output, and one GPU render batch;
- keeping background and particle simulation independent prevented background replacement from breaking state;
- bloom worked more predictably on the transparent particle layer before final background composite;
- inspect actual component internals and parameter names before automating across versions.

## 3. Animated Mesh Emitter to particlesGPU

Use when an animated FBX or SOP mesh defines the birth surface.

```text
FBX COMP
-> Import Select SOP (static mesh path)
-> Deform SOP (Skeleton Root Path)
-> center/transform
-> Sprinkle SOP
-> SOP to CHOP
-> CHOP to TOP (RGB XYZ)
-> particlesGPU source
```

Tutorial-confirmed checks:

- select the real geometry SOP, not the animated joint component;
- verify deformation before point distribution;
- center the source mesh before conversion;
- start around 20,000 sprinkle points only if the GPU budget permits;
- set CHOP-to-TOP data format to RGB so XYZ becomes position texture channels;
- disable point interpolation when preserving the emitter silhouette matters;
- age lookup can drive color and size independently of the source mesh.

## 4. GLSL POP Image Sampling

Use when image values should directly write POP attributes.

```text
Grid POP
-> Attribute POP (declare color/pscale/etc.)
-> GLSL POP (position -> UV -> texture sample -> attributes)
-> Copy POP
```

Core mapping:

```glsl
uv = P.xy * 0.5 + 0.5;
imageColor = texture(imageSampler, uv);
```

Confirm the generated GLSL POP template for exact input/output functions. Attribute names and vector sizes must match. Use brightness to drive `pscale`, Z displacement, rotation, or alpha. If the source point domain is not centered `-1..1`, correct the UV mapping instead of compensating with the camera.

## 5. Plain Instancing

Use when repeated objects need no particle life or simulation.

```text
SOP/CHOP/DAT source
-> position/scale/rotation/color attributes
-> Geometry COMP instancing or Copy SOP/POP
-> material/render
```

Prefer this over particlesGPU for dashboards, grids, datasets, static point clouds, and deterministic repeated geometry. Make attribute lengths agree; a single missing or mismatched channel can place instances at the origin or repeat stale values.

## 6. TD 2023 Image Particles with SOPs

Use when POPs are unavailable and the image produces a moderate CPU-side point count.

```text
source TOP
-> Fit TOP (aspect-preserving resolution limit)
-> Script SOP (P, Cd, alpha, N)
-> optional Noise SOP
-> Circle/low-poly source + Copy SOP
-> Geometry COMP + Constant MAT
-> Render TOP -> OUT_PARTICLES
```

TD-tested contract:

- Set the Fit TOP to an editable maximum width/height and preserve input aspect. With a `256 x 256` limit, verify `1280 x 720 -> 256 x 144`, `720 x 1280 -> 144 x 256`, `512 x 512 -> 256 x 256`, and do not upscale `100 x 50`.
- Fit the resulting point domain into a bounded world box using one scale for both axes, for example `scale = min(maxWorldW / pixelW, maxWorldH / pixelH)`. Do not stretch X and Y independently.
- Store position in `P`, image color in `Cd`, transparency in alpha, and an explicit nonzero `N` when using one-vertex or otherwise degenerate primitives.
- Noise SOP Position mode moves points along `N`. Parameter amplitude can evaluate correctly while geometry displacement remains zero if normals are zero.
- Inspect real menu values. In TD 2023 the Circle SOP polygon value is `poly`; assigning an invented value such as `polygon` may silently leave another primitive type active.
- Set Copy SOP attribute transfer explicitly when copied geometry must inherit point color/alpha. Use low-division source geometry and record copied primitive/vertex counts.
- Delete or disable the Geometry COMP's generated default SOP before adding the particle Select SOP. A rendered default Torus can masquerade as a white particle blob.
- Use a slight camera or geometry angle when brightness-derived Z relief must be visible. A straight orthographic view proves silhouette but hides depth.
- Prefer this Copy SOP route as a moderate-count compatibility fallback. Move to GPU particles or POPs for substantially larger dynamic systems.

Keep one replaceable source TOP, one raw render, and one stable `OUT_PARTICLES`. Treat resolution limits, point size, threshold, depth, motion, and speed as public controls only after each control passes a measured response test.
