---
name: td-glsl-control-panel
description: Create and maintain visible TouchDesigner control surfaces for GLSL TOP, MAT, or POP systems by exposing shader uniforms through clearly named CHOP controls, state channels, reset pulses, error/status DATs, and nearby documentation. Use when the user asks to make shader code easier to tune, expose color/opacity/seed/grid/count/timing parameters, visualize shader state, explain which control affects what, or clean up hard-coded GLSL constants.
---

# TD GLSL Control Panel

Make shader behavior adjustable and observable without requiring the user to edit GLSL for routine tuning.

## Workflow

1. Inspect the shader and list values that are artistic controls, structural controls, runtime state, or diagnostics.
2. Keep structural constants in code unless changing them safely requires coordinated logic updates.
3. Create one clearly named Constant CHOP for user controls and a separate CHOP for runtime state.
4. Bind controls to GLSL uniforms with explicit expressions or exports.
5. Add reset pulses for persistent state instead of asking the user to edit state channels manually.
6. Keep an Info DAT or nearby diagnostics node for compile errors and warnings.
7. Add a short Text DAT beside the control block when parameter roles are not obvious.
8. Remove unused controls and unnamed default channels.

## Control Categories

Use descriptive snake_case names:

| Category | Examples |
| --- | --- |
| appearance | `color_r`, `color_g`, `color_b`, `opacity`, `brightness`, `base_detail` |
| layout | `grid_count`, `cell_scale`, `gap`, `region_width`, `region_height` |
| order | `random_seed`, `direction`, `sequence_mode` |
| timing | `attack`, `decay`, `hold_time`, `reset_delay` |
| behavior | `auto_reset`, `preview_enable`, `reset_now` |
| state | `steps`, `active_index`, `filled_count` |

Do not label a control `opacity` unless its exact affected layer is documented, such as unlit base opacity or preview opacity.

## Ownership

- User controls: editable Constant CHOP.
- Runtime state: separate Constant/Count/Cache/Feedback CHOP as appropriate.
- Audio or external data: semantic input Nulls owned by the source handoff.
- Shader uniforms: consume the above sources; do not own user-facing naming.

## Layout

Place nodes in readable rows:

```text
external controls -> semantic input Nulls
user controls     -> shader uniform bindings
runtime state     -> shader state uniforms
shader source     -> GLSL operator -> info/error DAT
```

Keep related controls adjacent. Avoid scattered one-off Constant CHOPs unless they are independently reusable modules.

## Verification

- Move every exposed control through min, typical, and max values.
- Confirm its label matches the visible behavior.
- Confirm controls do not silently depend on one specific source image resolution.
- Confirm reset controls pulse and return to zero.
- Confirm GLSL compiles after binding changes.
- Confirm no unused uniform, channel, or default `chanN` output remains.
- Keep source comments ASCII when the current TD/DAT encoding displays Chinese comments as mojibake; place detailed Chinese explanations in a UTF-8 Text DAT or Obsidian note instead.

Use `td-progressive-region-reveal` for cumulative region state and coverage rules. Use `auto-touchdesigner-mcp` for live inspection and repair through port 9981.
