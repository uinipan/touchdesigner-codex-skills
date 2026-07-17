# TouchDesigner Tutorial Workflow

Use this reference when the video is about TouchDesigner and the user wants to extract reusable learning from it.

## Read First

- Inspect tutorial keyframes or screenshots before judging the visual technique. Transcript-only evidence is enough for a rough classification, but not enough to claim a visual pattern is understood.
- Identify whether visual changes belong in TOP, CHOP, SOP, MAT, GLSL, or COMP parameters.
- For GPU particle systems, trace color through lookup/ramp inputs, GLSL multi TOPs, renderselect TOPs, instance color TOPs, geometry instancing, and material switches.

## Block-Based TD Experiments

Use TouchDesigner MCP as a small experiment workspace, not as a whole-project completion engine.

- Choose one block per experiment: SOP geometry block, CHOP control block, TOP post block, GLSL pass, particle/instance data block, UI/panel control block, protocol/data block, tracking input block, material/render block, or camera/composition block.
- Define the hypothesis before editing: what visual or data behavior should change, and which tutorial timestamp/keyframe supports it.
- Keep the edited boundary explicit: parent COMP, input nodes, output node, and parameters touched.
- Prefer temporary helper nodes with clear names when testing. Preserve the original network unless the user explicitly asks to integrate the result.
- After each experiment, record observations, failed attempts, useful parameter ranges, and whether the finding should update an existing direction skill.
- Stop after the block is understood. Do not expand into adjacent blocks unless the user asks or the current hypothesis requires one dependent block.

## Extract Reusable Structure

Include:

- Core node families and parameters.
- Important node chains and why they work.
- Expected visual result for each learning phase.
- Tutorial timestamp range for each phase.
- Tutorial keyframe timestamp(s) for each phase.
- Expected phase endpoint type, such as SOP, CHOP, TOP, MAT, or COMP. Do not treat helper preview/render nodes as the tutorial endpoint unless the tutorial itself ends there.

## TD Tips Output

When learning a TD tutorial, always extract reusable tips instead of treating the tutorial as a one-off build:

- Node workflow tips: useful node chains, conversions, and where data changes family, such as SOP to CHOP to TOP.
- Parameter tips: exact parameters that matter, their suggested ranges, and why they affect the look.
- Visual-critical parameters: parameters that are most useful for tuning the image after the node network is built.
- For visual-critical parameters, link them to keyframes or current TD screenshots when available, so tuning is grounded in images rather than only parameter names.
- Visual-design tips: color, scale, motion, post-processing, camera, and composition choices.
- Common pitfalls: errors, confusing node names, hidden component internals, performance risks, and places where users often connect the wrong data type.
- Reuse ideas: how to apply the technique to a different model, asset, audio input, or visual style.

Keep each tip tied to a timestamp when available.

## Common TD Patterns

- Ramp-driven color: `rampTOP -> nullTOP/colorLookup -> GLSL/lookup -> pColor/null_pColor -> geometry instancecolorop`.
- Material-driven color: `constantMAT/phongMAT/lineMAT -> switchMAT -> nullMAT -> geometry material`.
- Final output: `renderTOP -> post TOPs -> outTOP/nullTOP/moviefileoutTOP`.
