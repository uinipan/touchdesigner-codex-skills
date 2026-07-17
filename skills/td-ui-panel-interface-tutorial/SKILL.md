---
name: td-ui-panel-interface-tutorial
description: Learn TouchDesigner tutorials focused on Container COMP, Panel COMP, Button COMP, Slider COMP, Table COMP UI, custom control panels, perform mode interfaces, parameter dashboards, preset/cue panels, VJ control surfaces, and tool-like operator interfaces. Use when a tutorial's main reusable value is building a human-operated UI inside TouchDesigner.
---

# TD UI Panel Interface Tutorial

Use this skill to turn Container COMP and Panel COMP tutorials into reusable TouchDesigner UI knowledge. This direction is about how a person operates a patch, not the visual system being controlled.

When learning a series of UI tutorials, maintain one direction-level note instead of one note per video. Append series evidence, timestamps, and reusable findings there, then link to concrete tutorial notes only when a single video becomes a standalone build note.

Chapters are only a table of contents. For real UI learning, read the captions/transcript and inspect keyframes before preserving any parameter, expression, panel-state, or layout rule.

## Workflow

1. Identify the UI role.
   - Classify as control panel, perform mode interface, dashboard, preset/cue manager, VJ surface, parameter editor, status monitor, tool UI, or reusable component UI.
   - Record which UI family appears: Container COMP, Panel COMP, Button COMP, Slider COMP, Field COMP, Table COMP, List COMP, parameter COMP, custom panel callbacks, or layout COMPs.
   - Separate UI layout, input controls, state storage, callbacks, parameter binding, visual feedback, and target system.
   - For Web GUI or external-control tutorials, keep this skill responsible for the operator-facing surface and mark Python/protocol details as crossover material for `td-data-python-protocol-tutorial`.

2. Map the UI block.
   - Preserve parent/child COMP hierarchy, panel names, control names, custom parameters, panel values, callbacks, and target operator paths.
   - Record layout behavior: resolution, anchors, margins, align/order rules, scaling, aspect assumptions, and perform mode constraints.
   - Note interaction states: hover, select, press, toggle, drag, disabled, active cue, current preset, and error/status feedback.
   - Split the block into six layers when possible: layout shell, controls, state ownership, binding/routing, visual feedback, and deployment/performance.

3. Extract reusable UI patterns.
   - Group the tutorial into layout shell, controls, binding/state, callbacks, visual feedback, and target mapping.
   - Explain whether values flow through panel values, custom parameters, CHOP exports, DAT tables, callbacks, or storage.
   - Preserve ergonomics: labels, control density, grouping, defaults, reset behavior, and live-performance safety.
   - Always write an interaction map in the form: user action -> state change -> target effect -> feedback.
   - Always identify the source of truth for each value: panel value, custom parameter, CHOP export, DAT, callback, storage, extension, or external protocol.

4. Run block experiments when useful.
   - Limit each TouchDesigner experiment to one UI block: one button logic, one slider mapping, one table/list interaction, one preset row, one status indicator, or one perform-mode layout.
   - Define the hypothesis: what user action should happen, which value should change, and where it should be observed.
   - Record observations, failed attempts, useful parameter/callback patterns, and what should update this skill.

5. Reuse and verify the active project API.
   - When extending an existing TD project, copy a currently working operator of the same type or inspect its actual parameters before scripting a new one.
   - Never invent or assume a parameter such as `par.rename`; confirm it exists with `pars()` or reuse the working operator's parameter pattern. For the tested Select CHOP, use `channames`, `renamefrom`, and `renameto`.
   - Treat an error as an implementation mistake first. Claim a TD version difference only after comparing actual operator parameters or documented behavior across versions.
   - Separate scripting verification from interaction verification. Python parameter assignment can confirm paths and values, but it may bypass Panel behavior, callbacks, and Button Group interaction.

## Series Learning Patterns

- Basic controls: learn `Container shell -> Button/Slider controls -> value/state -> target binding -> visual feedback`.
- Buttons: distinguish momentary, toggle, radio/select, rollover/hover, disabled, and error states. Record the group owner for radio or preset buttons.
- Button state heuristic: use `state` for persistent toggle state; use `select` for momentary/cue/pulse behavior; use `u/v` for pointer-position controls and rollover interaction.
- Four button/switch semantics from TD testing:
  - Toggle switch: `Button COMP -> Panel CHOP -> Null CHOP -> Select CHOP(state) -> toggle_state`. Use for persistent on/off.
  - Momentary switch: `Button COMP -> Panel CHOP -> Null CHOP -> Select CHOP(select) -> momentary_select`. Use for press/hold trigger.
  - Radio group switch: several radio buttons share one Button Group Label, then each branch selects its chosen-state channel into `radio_*_state`; merge them as one mode selector. Use real panel clicks to verify that exactly one button remains selected and observe whether `state` or `value0` is the faithful public source. Do not use direct Python assignment to `value0` as proof of radio mutual exclusion.
  - Inside trigger: `Button COMP -> Panel CHOP -> Null CHOP -> Select CHOP(inside) -> inside_btn_inside`. Use for radar/hotspot/region-presence behavior, not click state.
- Button state extraction pattern: keep one semantic Select CHOP per button role, rename the output to intent-level names, then merge into one `button_state_bus`. Avoid keeping exploratory hover/inside buses in final blocks unless visual feedback or radar behavior is the actual feature.
- Button test-node layout: when building a learning/debug block, keep each button's state reader in one horizontal row in the network editor: `Button COMP -> Panel CHOP -> Null CHOP -> Select CHOP`. Stack multiple button rows vertically, and place the merged `*_state_bus` to the right or downstream. This is a node-graph readability rule only; do not hard-code visible UI x/y placement from it.
- Button UI hierarchy rule: build visible button interfaces in a `Container COMP`, not a plain `Base COMP`. A `Base COMP` is good for system/logic packaging, but it does not act as the visible panel shell for child Button COMPs. Use `Base COMP` for the larger module if needed, then put a `Container COMP` inside it for the operator-facing UI.
- Button build order: create the visible `Container COMP` first, then create Button/Slider/Text panel controls inside that container. Moving the parent Container should move the whole UI group; moving node positions in the network editor only tidies the graph and does not change panel-screen placement.
- Reparenting warning: wiring a button into a Container with TOP/CHOP connections does not make it a UI child. Panel hierarchy follows operator paths, e.g. `/project1/radar_ui_panel/radar_btn01`, and Panel CHOP `Component` paths must be updated after reparenting.
- Radio buttons: set `Button Type = radio down`, then define the mutually exclusive group with either shared `Button Group Label` or `Button Group DAT`. Prefer the DAT when buttons are distributed across multiple containers or network locations. Verify mutual exclusion by clicking the rendered buttons; setting multiple `value0` parameters from Python can bypass the group interaction and produce a misleading test result.
- Select CHOP scripting rule from the active project: select one semantic channel with `par.channames`, then rename it with `par.renamefrom` and `par.renameto`. Do not assume a separate `par.rename` enable parameter exists. Before scripting any unfamiliar operator parameter, inspect a working same-type node or enumerate its actual parameters.
- Button customization: use real panel channels such as rollover, select, and on/off state to drive DAT/expression-based background, border, font, and text changes. Button labels can be stateful, not just static captions.
- General two-image Button skin pattern from TD testing: use two replaceable TOP assets named `off` and `on`, a semantic Button channel, and the Button's internal `text` Text COMP as the rendered image layer. This applies to toggle (`state`), momentary (`select`), radio (`selected state`, after verifying `state` vs `value0`), and inside/radar (`inside`) buttons. In newer Button COMP builds, setting the outer Button `top`/Background TOP may not visibly replace the default button look; drive the internal `text.par.top` instead.
- Two-image asset strategies: use `off Movie File In TOP + on Movie File In TOP` when the two states have independently designed images; use `on Movie File In TOP -> Monochrome TOP -> off` when the inactive state is a derived black-and-white version. Keep stable `off`/`on` node names so later image replacement only changes Movie File In `File` parameters.
- Semantic image-swap expressions: derive the current Button instance name and use the matching semantic Select CHOP. The generic shape is `me.parent(2).op('on') if me.parent(2).op(me.parent().name + '_STATE_SUFFIX')[me.parent().name + '_CHANNEL_SUFFIX'].eval() > 0.5 else me.parent(2).op('off')`. Use `_state_select/_state`, `_select_select/_select`, the verified radio selected suffix/channel, or `_inside_select/_inside` according to Button role.
- Button image-skin roles: the Button COMP remains the hitbox/interaction owner; `Panel CHOP -> Null CHOP -> semantic Select CHOP` remains the visual-condition and public-logic source; the internal `text` Text COMP renders the image; `off`/`on` TOPs are replaceable visual assets. Set `text.par.topfill = 'best'`, clear text/font alpha/background alpha, enable `clickthrough`, and turn off borders on both the outer Button and internal Text COMP.
- Button skin node layout: place shared `off`/`on` assets together in a dedicated skin-assets area, separate from the Button state-reader rows. Keep every Button logic row horizontal as `Button -> Panel -> Null -> Select`, stack rows vertically, and place the merged semantic bus to the right/downstream. Do not hard-code visible UI x/y placement.
- Button group naming/layout/bus rule: once a UI contains multiple Button groups, name every group consistently from group 1 onward: `<semantic>_btn1_1`, `<semantic>_btn1_2`, then `<semantic>_btn2_1`, `<semantic>_btn2_2`. Treat each explicit group number or new functional prefix as a separate Button group. Place each new group's node rows in a separate network block to the right of the previous group and create a separate Merge CHOP/public bus such as `<semantic>_group1_bus` and `<semantic>_group2_bus`; do not silently merge groups.
- Per-group Master and skin assets: the `_1` Button in each group is that group's Master. Other Buttons in the same group clone it. Give each group independent replaceable skin assets named `groupN_off` and `groupN_on`, even when the initial files are identical. This allows one group to change images, internal structure, or fade timing without affecting another group. Groups may share the same visible UI Container.
- Group rename safety: when converting an ungrouped first set such as `inside_btn01...15` into `inside_btn1_1...1_15`, rename its Button, Panel CHOP, Null CHOP, semantic Select CHOP, renamed output channel, skin asset nodes, and Merge bus together. Repair Panel CHOP `Component` paths and refresh clones after the rename so instance-name-based expressions continue resolving.
- Master + Clone button-skin pattern: finish one Button COMP as the master, then set the other Button COMPs' `Clone` parameter to the master and enable cloning. Use a clone-safe internal expression that derives the instance name, for example: `me.parent(2).op('on') if me.parent(2).op(me.parent().name + '_state_select')[me.parent().name + '_state'].eval() > 0.5 else me.parent(2).op('off')`. This lets every cloned internal `text` COMP use the shared skin structure while reading its own state channel.
- Clone refresh rule from TD testing: `Enable Cloning` allows an instance to synchronize from its master, but master parameter edits may not propagate live. After editing the master's internal network or parameters, pulse `Enable Cloning Pulse` on each clone that should refresh. The pulse overwrites clone-local internal edits; disable `Enable Cloning` before customizing an instance independently.
- Clone boundary: cloning synchronizes the component's internal network, including the internal `text` skin layer, after a clone refresh, but per-instance outer Button parameters such as panel x/y, label, value/state, and other parent-level settings remain instance-owned. Normalize outer no-label/no-border settings once when creating the instances; use the master for later internal skin-structure changes.
- Button image-transition pattern: avoid switching `text.par.top` directly between `off` and `on` when a fade is required. Inside the Button Master, use `semantic state -> Select CHOP -> Lag CHOP`, feed `groupN_off` and `groupN_on` through Select TOPs into a Cross TOP, reference the lagged 0-1 value in Cross TOP `Cross`, then render the Cross TOP in the internal `text` Text COMP. A tested default is `Lag 1 = 0.5 seconds` and `Lag 2 = 0.5 seconds`. Disabling Clone for one instance does not remove its existing fade network; it only stops future Master synchronization.
- Button Lag CHOP rule: treat `skin_lag` as the reusable visual-transition layer between the raw semantic state and visual parameters. Keep the public semantic bus raw and immediate; use the lagged value only for visuals such as Cross TOP image fades, opacity, color, glow, scale, or border intensity. `Lag 1` controls the transition toward a rising/on value and `Lag 2` controls the transition toward a falling/off value. Default both to `0.5 seconds`; lower values feel snappier, while unequal values create different fade-in and fade-out speeds. Toggle, radio, and inside states suit visible fades; use a shorter lag for momentary/select when the press must still feel responsive.
- Sliders: record input domain, output range, clamp/default behavior, label/readout format, and target mapping. Avoid driving targets directly from raw panel position unless the mapping is resolution-safe.
- Slider variants: check the stock Slider Type parameter first for horizontal, vertical, 2D, or UV-style behavior before building a custom slider.
- Custom sliders: model as `track/background -> draggable handle -> normalized value -> mapped output -> label/fill feedback`. Derive drag ranges from parent size, lock the non-active axis, and route values through Math CHOP/custom parameters before targets.
- Text/readout sizing: when a Text TOP is used inside a control, check whether it should follow `me.parent().width` and `me.parent().height` so labels stay readable when the control resizes.
- Text components: newer Button workflows may use Text COMP internally. Prefer Text COMP for scalable/editable button text when the tutorial or TD version exposes it; avoid assuming older Text TOP-only internals.
- Widgets: record widget value ownership, custom parameter exposure, Parameter COMP use, dropdown/menu state, tabs, visibility toggles, and `Paste Bind`/export/callback method.
- Parameter COMP: use it as a bridge from component parameters/custom parameters to an operator-facing dashboard, and record whether it is read-only, editable, or bound to a target.
- Layout: treat window size, parent/child hierarchy, Children page, Fill Mode, children alignment, spacing, margin, Align Order, fill width/height, nested layouts, anchors, and layout bugs as first-class learning targets.
- Resizable roots: when a UI should adapt to the output window, check `Size From Window` on the root panel and verify the layout after resizing or reopening the Window COMP.
- Manual placement exception: when a child should not participate in the parent's auto-layout, record `Parent Alignment = Ignore` and the manual x/y rule.
- Perform mode: separate operator controls, audience/projector output, preview/status surfaces, root perform panel, Window COMPs, monitor targeting, fullscreen/windowed mode, border visibility, and exit/safety behavior.
- Web GUI: record browser-side controls, TD custom parameters, min/max constraints, bidirectional sync, remote monitor/status feedback, WebSocket server dependency, and the boundary where protocol details should move to the data/protocol skill.
- Dynamic UI routing: for Switch CHOP or mode selectors, record button selected/deselected values, active input, input ordering, invalid-index behavior, fallback path, and visible active feedback.

## UI Series Experiment Blocks

When moving from video learning into TouchDesigner testing, prefer these small blocks before combining them into a full dashboard:

- Button State Reader: `Container -> toggle/momentary/radio buttons -> Panel CHOP -> Null CHOP -> text/color feedback`. Verify `state`, `select`, radio grouping, and rollover.
- Button State Reader refined output: use `button_state_bus` as the only public output bus when testing logic. Include the four semantic roles if needed: toggle/state, momentary/select, radio group/selected state, and inside/inside trigger.
- Slider Value + Readout: `Container -> stock slider or custom handle/track -> Panel/Widget value -> Math CHOP -> target parameter -> Text TOP/Text COMP readout`. Verify normalized value, mapped range, label, and fill.
- Container Layout Shell: `Root Container -> header/control column/preview/status row`. Verify Children page, Fill Mode, margin/spacing, Align Order, nested containers, and `Size From Window`.
- Widget + Parameter Dashboard: `Widget controls -> custom parameters / Parameter COMP -> target visual preview`. Verify `Paste Bind`, label display, tabs, visibility, and source-of-truth ownership.
- Perform Window + Output Surface: `Operator UI Container` plus `Output Container -> Window COMP -> monitor/projector target`. Verify Window Operator, fullscreen/border/monitor settings, root sizing, and safe exit.

## Knowledge To Preserve

- UI component hierarchy and panel layout rules.
- Control-to-target mapping and binding method.
- State ownership: panel value, custom parameter, DAT, CHOP, storage, or extension.
- Callback signatures and event timing.
- Visual feedback rules for active, hover, selected, disabled, and error states.
- Live-use pitfalls: accidental reset, hidden focus, wrong panel path, stale target, bad scaling, and perform mode mismatch.
- Deployment constraints: perform root, Window COMP, target monitor, resizable/fullscreen behavior, and operator/audience surface separation.
- Evidence boundaries: if subtitles or keyframes are missing, mark conclusions as metadata/chapter-based and do not preserve exact parameter or expression claims.

## Output Shape

Produce a compact tutorial type note with:

- `Type`: UI/panel/interface.
- `UI block`: hierarchy, controls, layout, and target.
- `Interaction map`: user action -> state change -> target effect -> feedback.
- `State model`: where values live and how they update.
- `Block experiments`: scope, hypothesis, observations, failed attempts.
- `Reusable patterns`: layout rules, callbacks, bindings, and live-use safeguards.
- `Uncertainties`: missing callbacks, unresolved target paths, or UI behavior needing TD verification.
