# TouchDesigner Codex Skills

English | [中文](./README.zh-CN.md)

A curated collection of reusable Codex skills and workflows for TouchDesigner learning, building, inspection, and debugging.

This repository is paired with [touchdesigner-codex-plugins](https://github.com/uinipan/touchdesigner-codex-plugins).

## Repository structure

```text
skills/
  td-audio-reactive-tutorial/
    references/
    companion-skills/td-audio-plugin-handoff/
  td-ui-panel-interface-tutorial/
  td-glsl-control-panel/
  td-particle-instancing-tutorial/
  td-progressive-region-reveal/

workflows/
  auto-touchdesigner-mcp/
  video-tutorial-to-build/
```

Only skills with meaningful, reusable content are published. Placeholder directions remain unpublished until they are ready.

## Skills

| Skill | Purpose |
| --- | --- |
| `td-audio-reactive-tutorial` | Extract reusable envelopes, triggers, counters, spectrum data, and audio-to-visual mappings. |
| `td-audio-plugin-handoff` | Connect the packaged audio plugin to clearly named downstream CHOP interfaces. |
| `td-ui-panel-interface-tutorial` | Build operator interfaces with containers, panels, buttons, sliders, layouts, and perform mode. |
| `td-glsl-control-panel` | Expose GLSL controls and status through a readable TouchDesigner control surface. |
| `td-particle-instancing-tutorial` | Build and debug particles, point clouds, image particles, and instancing systems. |
| `td-progressive-region-reveal` | Reveal non-repeating regions progressively from triggers, with persistent state and reset logic. |

## Workflows

These workflows are published mainly for personal reuse and reference. They reflect `uinipan`'s local setup and working habits, so paths, dependencies, and environment assumptions may need adjustment before use. They are less general-purpose than the skills above.

| Workflow | Purpose |
| --- | --- |
| `auto-touchdesigner-mcp` | Bootstrap and repair the TouchDesigner MCP WebServer, then inspect or modify a live project. |
| `video-tutorial-to-build` | Collect tutorial transcripts and keyframes, classify techniques, and extract reusable knowledge. |

## Installation

Copy the folder you need into your Codex skills directory. For example:

```powershell
Copy-Item -Recurse -Force ".\skills\td-glsl-control-panel" "$env:USERPROFILE\.codex\skills\td-glsl-control-panel"
Copy-Item -Recurse -Force ".\workflows\video-tutorial-to-build" "$env:USERPROFILE\.codex\skills\video-tutorial-to-build"
```

Restart Codex after installing or updating a skill.

## Documentation policy

- `README.md` and `README.zh-CN.md` are public, human-facing overviews.
- `SKILL.md` contains the executable instructions used by Codex.
- Reusable technical detail may live in `references/`.
- Personal paths, maintenance logs, one-off validation history, and unfinished ideas belong in private development notes rather than this repository.

## License

MIT. See [LICENSE](./LICENSE).
