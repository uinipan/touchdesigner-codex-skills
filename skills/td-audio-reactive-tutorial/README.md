# td-audio-reactive-tutorial

## 中文

这是一个 TouchDesigner 音频响应方向的 Codex skill，用来把音频教程整理成可复用的控制信号方法，而不是只记录某个视觉效果。

它适合处理：

- `Audio File In` / `Audio Device In` 输入
- 音量、RMS、peak、kick、snare、onset 等信号提取
- 频段分析、spectrum texture、Audio Analysis COMP
- 音频信号到视觉参数的映射、平滑、缩放和调试

当前这个 skill 是唯一的 audio skill。它下面包含两个内部 block，用来覆盖两种常见音频控制需求：

### 内部模块

#### 1. `filein peak speed block`

这是一个轻量的整体音量控制模块。

它从 `Audio File In CHOP` 读取音频，把左右声道合成一个整体能量值，再经过 peak / filter / gain 处理，输出两个常用控制信号：

- `envelope`：平滑后的音量包络，适合控制亮度、scale、displacement、feedback gain、camera shake 等连续参数。
- `speed`：由音量推动的累计运动值，适合控制旋转、滚动、noise evolution、time offset 等持续推进的运动。

适合场景：

- 只需要“音乐越响，视觉越强”的整体响应。
- 想快速从一首歌得到一个稳定的连续控制值。
- 不需要区分 kick、snare、低频、高频。

参考文件：`references/kick-filein-flow.md`

#### 2. `kick rms spectrum block`

这是一个更完整的三路音频分析模块。

它把同一个音频源拆成三条不同用途的 lane：

- `event lane`：通过 `Audio Analysis COMP` 提取 `kick` / `snare`，再用 `Count CHOP` 变成事件计数或触发信号。适合做闪烁、切换、burst、reset、节拍触发。
- `RMS speed lane`：用 RMS Power 提取整体能量，再进 `Speed CHOP`，得到连续运动进度。适合做跟随音乐强度推进的 motion / phase。
- `spectrum lane`：用 `Audio Spectrum CHOP` 输出频谱数据。适合做频段分离、spectrum texture、CHOP to TOP、shader / displacement / scanline 控制。

适合场景：

- 需要同时使用节拍触发、整体能量和频谱数据。
- 视觉系统里有不同层分别响应 kick、RMS、spectrum。
- 需要把“事件触发”和“连续运动”分开，避免一个音频值到处乱接。

参考文件：`references/kick-rms-spectrum-flow.md`

这两个 block 不再拆成独立 skill。它们作为音频方向的可复用模块保存在 `references/` 里，由这个 audio skill 统一管理。

### 安装

从仓库根目录，把整个 skill 文件夹复制到自己的 Codex skills 目录：

```powershell
Copy-Item -Recurse -Force `
  ".\skills\td-audio-reactive-tutorial" `
  "$env:USERPROFILE\.codex\skills\td-audio-reactive-tutorial"
```

如果你只下载了这个 skill 文件夹本身，也可以在它的上一级目录运行：

```powershell
Copy-Item -Recurse -Force `
  ".\td-audio-reactive-tutorial" `
  "$env:USERPROFILE\.codex\skills\td-audio-reactive-tutorial"
```

### 触发方式

在 Codex 里可以这样说：

- “帮我整理这个 TD 音频响应教程”
- “做一个 Audio File In peak speed block”
- “用 kick / RMS / spectrum 做 TD 控制信号”
- “把音频信号映射到视觉参数”

### 文件结构

```text
td-audio-reactive-tutorial/
  SKILL.md
  README.md
  agents/
    openai.yaml
  references/
    kick-filein-flow.md
    kick-rms-spectrum-flow.md
```

## English

This is a Codex skill for TouchDesigner audio-reactive tutorial learning. It turns audio tutorials into reusable control-signal recipes instead of only documenting a final visual look.

Use it for:

- `Audio File In` / `Audio Device In` input
- volume, RMS, peak, kick, snare, and onset extraction
- frequency-band analysis, spectrum textures, and Audio Analysis COMP workflows
- mapping, smoothing, scaling, and debugging audio-driven visual controls

This is the single audio skill. It includes two internal reusable blocks for two common audio-control needs:

### Internal Blocks

#### 1. `filein peak speed block`

This is a lightweight overall-loudness control block.

It reads audio from an `Audio File In CHOP`, combines the channels into one energy signal, then processes it through peak / filter / gain stages. It produces two useful control outputs:

- `envelope`: a smoothed loudness envelope for brightness, scale, displacement, feedback gain, camera shake, and other continuous parameters.
- `speed`: a cumulative motion value driven by loudness, useful for rotation, scrolling, noise evolution, time offsets, and other continuously advancing motion.

Use it when:

- you only need a general "louder music means stronger visuals" response;
- you want a quick stable continuous control value from a track;
- you do not need separate kick, snare, low, mid, or high-frequency signals.

Reference: `references/kick-filein-flow.md`

#### 2. `kick rms spectrum block`

This is a fuller three-lane audio-analysis block.

It splits one audio source into three lanes with different purposes:

- `event lane`: uses `Audio Analysis COMP` to extract `kick` / `snare`, then uses `Count CHOP` for event counts or trigger signals. Good for flashes, switches, bursts, resets, and beat-triggered changes.
- `RMS speed lane`: uses RMS Power and `Speed CHOP` to create continuous motion progress. Good for motion, phase, or animation speed driven by overall energy.
- `spectrum lane`: uses `Audio Spectrum CHOP` to output frequency data. Good for band separation, spectrum textures, CHOP to TOP workflows, shader control, displacement, and scanline-style modulation.

Use it when:

- you need beat triggers, overall energy, and spectrum data at the same time;
- different visual layers should respond to kick, RMS, and spectrum separately;
- you want to keep event triggers separate from continuous motion values.

Reference: `references/kick-rms-spectrum-flow.md`

These blocks are not separate skills. They are reusable audio modules stored under `references/` and managed by this audio skill.

### Install

From the repository root, copy the whole skill folder into your Codex skills directory:

```powershell
Copy-Item -Recurse -Force `
  ".\skills\td-audio-reactive-tutorial" `
  "$env:USERPROFILE\.codex\skills\td-audio-reactive-tutorial"
```

If you downloaded only this skill folder, run this from its parent directory:

```powershell
Copy-Item -Recurse -Force `
  ".\td-audio-reactive-tutorial" `
  "$env:USERPROFILE\.codex\skills\td-audio-reactive-tutorial"
```

### Example Prompts

- "Help me summarize this TouchDesigner audio-reactive tutorial."
- "Build an Audio File In peak speed block."
- "Use kick, RMS, and spectrum data as TD control signals."
- "Map an audio signal to visual parameters."

### Structure

```text
td-audio-reactive-tutorial/
  SKILL.md
  README.md
  agents/
    openai.yaml
  references/
    kick-filein-flow.md
    kick-rms-spectrum-flow.md
```


