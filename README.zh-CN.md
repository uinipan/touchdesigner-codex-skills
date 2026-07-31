# TouchDesigner Codex Skills

[English](./README.md) | 中文

这是一个面向 TouchDesigner 学习、制作、工程检查、交互与排错的 Codex Skill 和工作流合集。

配套插件仓库：[touchdesigner-codex-plugins](https://github.com/uinipan/touchdesigner-codex-plugins)。

## 当前内容

目前公开 11 个 TouchDesigner Skill 和 5 个辅助工作流。每个目录以 `SKILL.md` 作为 Codex 的正式执行说明，不在单个 Skill 内重复放置 README。

### TouchDesigner Skills

| Skill | 用途 |
| --- | --- |
| [`td-audio-reactive`](./skills/td-audio-reactive/SKILL.md) | 优先使用已打包 TOX 构建、连接、调试音频响应系统，并以手动分析方法和教程模式作为补充参考。 |
| [`td-compositing-render-tutorial`](./skills/td-compositing-render-tutorial/SKILL.md) | 学习 Render TOP、相机、灯光、合成、反馈及后期处理流程。 |
| [`td-data-python-protocol-tutorial`](./skills/td-data-python-protocol-tutorial/SKILL.md) | 学习 DAT、Python、回调、OSC、MIDI、WebSocket、HTTP、串口和外部数据工作流。 |
| [`td-geometry-sop-tutorial`](./skills/td-geometry-sop-tutorial/SKILL.md) | 学习程序化 SOP 几何、曲线、曲面、形变、属性和网格流程。 |
| [`td-glsl-control-panel`](./skills/td-glsl-control-panel/SKILL.md) | 为 GLSL 系统建立可读、可调且带状态反馈的控制面板。 |
| [`td-glsl-shader-tutorial`](./skills/td-glsl-shader-tutorial/SKILL.md) | 学习 GLSL TOP/MAT 结构、uniform、UV、SDF、光线步进和 GPU 特效。 |
| [`td-interaction-tracking-tutorial`](./skills/td-interaction-tracking-tutorial/SKILL.md) | 学习追踪、传感器输入、校准、平滑、手势映射和交互设计。 |
| [`td-mediapipe-pinch-interaction`](./skills/td-mediapipe-pinch-interaction/SKILL.md) | 构建并排查 MediaPipe 拇指食指捏合、光标映射、点击与拖拽控制。 |
| [`td-particle-instancing-tutorial`](./skills/td-particle-instancing-tutorial/SKILL.md) | 构建并排查粒子、点云、图片粒子和实例化系统。 |
| [`td-progressive-region-reveal`](./skills/td-progressive-region-reveal/SKILL.md) | 通过触发信号逐步激活不重复区域，并维护完成与重置状态。 |
| [`td-ui-panel-interface-tutorial`](./skills/td-ui-panel-interface-tutorial/SKILL.md) | 使用 Container、Panel、Button、Slider、布局和 Perform Mode 构建操作界面。 |

### 辅助工作流

这些工作流用于协调工具或多个 Skill。部分内容带有 `uinipan` 的本地环境和个人工作习惯假设，其他人使用前可能需要调整路径与依赖。

| 工作流 | 用途 |
| --- | --- |
| [`auto-touchdesigner-mcp`](./workflows/auto-touchdesigner-mcp/SKILL.md) | 启动、连接和修复 TouchDesigner MCP WebServer，并检查或修改当前工程。 |
| [`obsidian-note-maintainer`](./workflows/obsidian-note-maintainer/SKILL.md) | 维护 Obsidian 笔记、索引、工作区镜像及同步校验。 |
| [`td-project-case-analysis-to-obsidian`](./workflows/td-project-case-analysis-to-obsidian/SKILL.md) | 调研真实 TouchDesigner 项目、重建系统逻辑，并把带证据层级的案例分析写入 Obsidian。 |
| [`video-tutorial-to-build`](./workflows/video-tutorial-to-build/SKILL.md) | 收集教程字幕与关键帧、判断技术方向并提取可复用知识。 |
| [`website-image-layout`](./workflows/website-image-layout/SKILL.md) | 将项目与作品集图片整理为克制、响应式的网站画廊排版。 |

## 安装

将需要的目录复制到 Codex skills 目录，例如：

```powershell
Copy-Item -Recurse -Force ".\skills\td-mediapipe-pinch-interaction" "$env:USERPROFILE\.codex\skills\td-mediapipe-pinch-interaction"
Copy-Item -Recurse -Force ".\workflows\video-tutorial-to-build" "$env:USERPROFILE\.codex\skills\video-tutorial-to-build"
```

如果工作流声明了配套 Skill，请一并安装。安装或更新后重启 Codex。

## 文档分工

- 仓库根目录 README 是面向使用者的公开介绍。
- `SKILL.md` 是供 Codex 执行的正式说明。
- 可复用的技术细节放在 `references/`，确定性工具放在 `scripts/`。
- 个人维护记录、单次验收历史和未完成想法保留在私人开发笔记中。
- 这里只发布已经具有实际内容和复用价值的 Skill。

## 许可证

使用 MIT 许可证，详见 [LICENSE](./LICENSE)。
