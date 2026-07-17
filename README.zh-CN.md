# TouchDesigner Codex Skills

[English](./README.md) | 中文

这是一个面向 TouchDesigner 学习、制作、工程检查和排错的 Codex Skill 与工作流合集。

配套插件仓库：[touchdesigner-codex-plugins](https://github.com/uinipan/touchdesigner-codex-plugins)。

## 仓库结构

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

这里只发布已经具有实际内容和复用价值的 Skill。只有标题的方向暂不上传，完善后再加入。

## Skills

| Skill | 用途 |
| --- | --- |
| `td-audio-reactive-tutorial` | 提取包络、触发、计数、频谱和音频到视觉参数的映射方法。 |
| `td-audio-plugin-handoff` | 将已打包的音频插件连接为命名清晰的下游 CHOP 接口。 |
| `td-ui-panel-interface-tutorial` | 使用 Container、Panel、Button、Slider、布局和 Perform Mode 构建操作界面。 |
| `td-glsl-control-panel` | 为 GLSL 系统暴露可读、可调且带状态反馈的控制面板。 |
| `td-particle-instancing-tutorial` | 构建并排查粒子、点云、图片粒子和实例化系统。 |
| `td-progressive-region-reveal` | 通过触发信号逐步激活不重复区域，并维护完成与重置状态。 |

## Workflows

| 工作流 | 用途 |
| --- | --- |
| `auto-touchdesigner-mcp` | 启动、连接和修复 TouchDesigner MCP WebServer，并检查或修改当前工程。 |
| `video-tutorial-to-build` | 收集教程字幕与关键帧、判断技术方向并提取可复用知识。 |

## 安装

将需要的文件夹复制到 Codex skills 目录，例如：

```powershell
Copy-Item -Recurse -Force ".\skills\td-glsl-control-panel" "$env:USERPROFILE\.codex\skills\td-glsl-control-panel"
Copy-Item -Recurse -Force ".\workflows\video-tutorial-to-build" "$env:USERPROFILE\.codex\skills\video-tutorial-to-build"
```

安装或更新后重启 Codex。

## 文档分工

- `README.md` 与 `README.zh-CN.md` 是面向使用者的公开介绍。
- `SKILL.md` 是供 Codex 执行的工作流与约束。
- 可复用的技术细节可以放入 `references/`。
- 个人路径、维护记录、单次验收历史和未完成想法保留在私人研发笔记中。

## 许可证

MIT，详见 [LICENSE](./LICENSE)。
