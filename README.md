# TouchDesigner Skills

## 中文

这是一个 TouchDesigner Codex skills 仓库，用来公开可复用的 TD 学习和工作流技能。

当前包含两个 skill：

- [`td-audio-reactive-tutorial`](skills/td-audio-reactive-tutorial/README.md)：音频响应方向。整理 `Audio File In`、RMS、peak、kick/snare、spectrum、Audio Analysis COMP，以及音频信号到视觉参数的映射。
- [`td-ui-panel-interface-tutorial`](skills/td-ui-panel-interface-tutorial/README.md)：UI / Panel Interface 方向。整理 Container COMP、Panel COMP、Button、Slider、Table/List、widgets、perform mode 和控制面板。

每个 skill 目录里都有自己的 `README.md` 和 `SKILL.md`。

### 安装

从仓库根目录运行：

```powershell
Copy-Item -Recurse -Force ".\skills\td-audio-reactive-tutorial" "$env:USERPROFILE\.codex\skills\td-audio-reactive-tutorial"
Copy-Item -Recurse -Force ".\skills\td-ui-panel-interface-tutorial" "$env:USERPROFILE\.codex\skills\td-ui-panel-interface-tutorial"
```

安装后，在 Codex 里可以用自然语言触发，例如：

- “帮我整理这个 TD 音频响应教程。”
- “用 kick / RMS / spectrum 做 TD 控制信号。”
- “用 Container COMP 做一个控制面板。”
- “做一组 button / slider 控件。”

## English

This repository contains public TouchDesigner Codex skills for reusable TD learning and workflow patterns.

Included skills:

- [`td-audio-reactive-tutorial`](skills/td-audio-reactive-tutorial/README.md): audio-reactive workflows, including `Audio File In`, RMS, peak, kick/snare, spectrum, Audio Analysis COMP, and audio-to-visual parameter mapping.
- [`td-ui-panel-interface-tutorial`](skills/td-ui-panel-interface-tutorial/README.md): UI / Panel Interface workflows, including Container COMP, Panel COMP, Button, Slider, Table/List, widgets, perform mode, and control panels.

Each skill folder includes its own `README.md` and `SKILL.md`.

### Install

Run from the repository root:

```powershell
Copy-Item -Recurse -Force ".\skills\td-audio-reactive-tutorial" "$env:USERPROFILE\.codex\skills\td-audio-reactive-tutorial"
Copy-Item -Recurse -Force ".\skills\td-ui-panel-interface-tutorial" "$env:USERPROFILE\.codex\skills\td-ui-panel-interface-tutorial"
```

After installing, you can invoke the skills in Codex with natural language, for example:

- "Help me summarize this TouchDesigner audio-reactive tutorial."
- "Use kick, RMS, and spectrum data as TD control signals."
- "Build a control panel with Container COMP."
- "Create a group of button and slider controls."

