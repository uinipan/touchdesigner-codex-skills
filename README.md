# TouchDesigner Codex Skills

English | [中文](./README.zh-CN.md)

A curated collection of reusable Codex skills and workflows for TouchDesigner learning, building, inspection, interaction, and debugging.

This repository is paired with [touchdesigner-codex-plugins](https://github.com/uinipan/touchdesigner-codex-plugins).

## Contents

The repository currently publishes 11 TouchDesigner skills and 5 supporting workflows. Each folder uses `SKILL.md` as its authoritative Codex instruction file; individual skill folders do not carry duplicate README files.

### TouchDesigner skills

| Skill | Purpose |
| --- | --- |
| [`td-audio-reactive`](./skills/td-audio-reactive/SKILL.md) | Build, connect, tune, and debug audio-reactive systems using the packaged TOX first, with manual analysis and tutorial patterns as supporting references. |
| [`td-compositing-render-tutorial`](./skills/td-compositing-render-tutorial/SKILL.md) | Learn reusable Render TOP, camera, lighting, compositing, feedback, and post-processing pipelines. |
| [`td-data-python-protocol-tutorial`](./skills/td-data-python-protocol-tutorial/SKILL.md) | Learn DAT, Python, callback, OSC, MIDI, WebSocket, HTTP, serial, and external-data workflows. |
| [`td-geometry-sop-tutorial`](./skills/td-geometry-sop-tutorial/SKILL.md) | Learn procedural SOP geometry, curves, surfaces, deformation, attributes, and mesh workflows. |
| [`td-glsl-control-panel`](./skills/td-glsl-control-panel/SKILL.md) | Expose GLSL controls and status through a readable TouchDesigner control surface. |
| [`td-glsl-shader-tutorial`](./skills/td-glsl-shader-tutorial/SKILL.md) | Learn GLSL TOP/MAT structure, uniforms, UV math, SDFs, raymarching, and GPU effects. |
| [`td-interaction-tracking-tutorial`](./skills/td-interaction-tracking-tutorial/SKILL.md) | Learn tracking, sensor input, calibration, smoothing, gesture mapping, and interaction design. |
| [`td-mediapipe-pinch-interaction`](./skills/td-mediapipe-pinch-interaction/SKILL.md) | Build and debug MediaPipe thumb-index pinch, cursor mapping, click, and drag controls. |
| [`td-particle-instancing-tutorial`](./skills/td-particle-instancing-tutorial/SKILL.md) | Build and debug particles, point clouds, image particles, and instancing systems. |
| [`td-progressive-region-reveal`](./skills/td-progressive-region-reveal/SKILL.md) | Reveal non-repeating regions progressively with persistent state and reset logic. |
| [`td-ui-panel-interface-tutorial`](./skills/td-ui-panel-interface-tutorial/SKILL.md) | Build operator interfaces with containers, panels, buttons, sliders, layouts, and Perform Mode. |

### Supporting workflows

These workflows coordinate tools or multiple skills. Some reflect `uinipan`'s local setup and working habits, so paths and dependencies may need adjustment before use.

| Workflow | Purpose |
| --- | --- |
| [`auto-touchdesigner-mcp`](./workflows/auto-touchdesigner-mcp/SKILL.md) | Bootstrap and repair the TouchDesigner MCP WebServer, then inspect or modify a live project. |
| [`obsidian-note-maintainer`](./workflows/obsidian-note-maintainer/SKILL.md) | Maintain Obsidian notes, indexes, workspace mirrors, and synchronization checks. |
| [`td-project-case-analysis-to-obsidian`](./workflows/td-project-case-analysis-to-obsidian/SKILL.md) | Research real TouchDesigner projects, reconstruct system logic, and write evidence-aware case studies to Obsidian. |
| [`video-tutorial-to-build`](./workflows/video-tutorial-to-build/SKILL.md) | Collect tutorial transcripts and keyframes, classify techniques, and extract reusable knowledge. |
| [`website-image-layout`](./workflows/website-image-layout/SKILL.md) | Arrange project and portfolio images into restrained responsive website galleries. |

## Installation

Copy the folder you need into your Codex skills directory. For example:

```powershell
Copy-Item -Recurse -Force ".\skills\td-mediapipe-pinch-interaction" "$env:USERPROFILE\.codex\skills\td-mediapipe-pinch-interaction"
Copy-Item -Recurse -Force ".\workflows\video-tutorial-to-build" "$env:USERPROFILE\.codex\skills\video-tutorial-to-build"
```

Install referenced companion skills when a workflow declares them, then restart Codex after installing or updating.

## Documentation policy

- Root README files are public, human-facing overviews.
- `SKILL.md` contains the executable instructions used by Codex.
- Reusable technical detail belongs in `references/`; deterministic helpers belong in `scripts/`.
- Personal maintenance logs, one-off validation history, and unfinished ideas remain in private development notes.
- Only skills with meaningful reusable content are published.

## License

MIT. See [LICENSE](./LICENSE).
