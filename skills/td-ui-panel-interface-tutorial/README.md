# td-ui-panel-interface-tutorial

## 中文

这是一个 TouchDesigner UI / Panel Interface 方向的 Codex skill，用来把 UI 教程整理成可复用的界面搭建方法。

它关注的是“人如何操作这个 TD patch”，而不是最终视觉效果本身。

它适合处理：

- Container COMP / Panel COMP 界面结构
- Button、Slider、Table、List、Field 等控件
- toggle、momentary、radio、inside、hover 等 button 状态
- Panel CHOP、Select CHOP、Merge CHOP 的状态总线
- 自定义按钮皮肤、on/off 图片、clone master、fade transition
- perform mode、控制面板、VJ surface、preset / cue 面板

当前这个 skill 是 UI / Panel Interface 的总入口。它下面包含几个常用内部模块，用来覆盖 TD 项目里最常见的界面搭建需求：

### 内部模块

#### 1. Button state block

这是按钮状态读取和语义化输出模块。

它把 `Button COMP` 的 panel 状态读出来，通过 `Panel CHOP -> Select CHOP -> Rename / Merge` 转成清晰的控制信号。

常见输出包括：

- `state`：toggle 持续开关状态，适合 on/off、enable/disable、模式保持。
- `select`：momentary 按下状态，适合触发、press-and-hold、临时动作。
- `inside`：鼠标是否进入按钮区域，适合 hover、hotspot、radar 区域检测。
- `radio state`：互斥按钮组选中状态，适合 mode selector、preset selector、cue selector。

适合场景：

- 需要把按钮点击变成稳定 CHOP 控制信号。
- 需要区分 toggle、momentary、radio、hover，不想把所有按钮都当成一个值。
- 需要把多个按钮合并成一个清晰的 `button_state_bus`。

#### 2. Button skin / image state block

这是按钮视觉皮肤模块。

它保留 `Button COMP` 作为真实交互区域，同时用内部 `text` Text COMP 显示 `off` / `on` 图片或 TOP。按钮状态通过 CHOP 信号决定显示哪个视觉状态。

它适合处理：

- 两张图片的 on/off 按钮皮肤。
- inactive 黑白图、active 彩色图。
- toggle / radio / inside 状态驱动视觉切换。
- 用 `Lag CHOP + Cross TOP` 做按钮淡入淡出 transition。

适合场景：

- 默认 Button COMP 外观不够用，需要自定义图片按钮。
- 需要按钮既能点击，又能显示清楚的视觉状态。
- 需要多个按钮共享同一套皮肤结构。

#### 3. Master / clone button group block

这是批量按钮和按钮组维护模块。

先做好一个 master button，再让其他按钮 clone 它的内部结构。每个实例保留自己的位置、名字和状态读取，但共享内部 skin / transition 逻辑。

适合场景：

- 要做一组很多按钮，比如 preset grid、cue grid、VJ trigger pad。
- 需要统一修改按钮内部结构，不想一个个手动改。
- 每个按钮有独立状态，但视觉逻辑保持一致。

#### 4. Slider / control panel block

这是滑条和控制面板模块。

它关注从 UI 输入到参数控制的完整链路：slider / field / table / button -> panel value -> mapping / range -> target parameter -> visual feedback。

适合场景：

- 做 perform mode 控制面板。
- 做亮度、速度、大小、阈值、颜色等参数控制。
- 做带 label / readout / reset 的 TD 工具界面。

button 相关内容属于这个 UI skill 的内部模块，不需要单独拆成一个 skill。

### 安装

从仓库根目录，把整个 skill 文件夹复制到自己的 Codex skills 目录：

```powershell
Copy-Item -Recurse -Force `
  ".\skills\td-ui-panel-interface-tutorial" `
  "$env:USERPROFILE\.codex\skills\td-ui-panel-interface-tutorial"
```

如果你只下载了这个 skill 文件夹本身，也可以在它的上一级目录运行：

```powershell
Copy-Item -Recurse -Force `
  ".\td-ui-panel-interface-tutorial" `
  "$env:USERPROFILE\.codex\skills\td-ui-panel-interface-tutorial"
```

### 触发方式

在 Codex 里可以这样说：

- “帮我整理这个 TD UI 教程”
- “用 Container COMP 做一个控制面板”
- “做一组 button / slider 控件”
- “做 TouchDesigner perform mode UI”
- “修一下 Button COMP 的状态读取”

### 文件结构

```text
td-ui-panel-interface-tutorial/
  SKILL.md
  README.md
  agents/
    openai.yaml
```

## English

This is a Codex skill for TouchDesigner UI and panel-interface tutorial learning. It turns UI tutorials into reusable interface-building patterns.

The focus is how a person operates a TouchDesigner patch, not the final visual output itself.

Use it for:

- Container COMP / Panel COMP interface structure
- Button, Slider, Table, List, and Field controls
- toggle, momentary, radio, inside, and hover button states
- Panel CHOP, Select CHOP, and Merge CHOP state buses
- custom button skins, on/off images, clone masters, and fade transitions
- perform mode interfaces, control panels, VJ surfaces, and preset / cue panels

This skill is the main entry point for UI / Panel Interface work. It includes several internal reusable blocks for the most common TouchDesigner interface-building needs:

### Internal Blocks

#### 1. Button state block

This block reads and normalizes Button COMP panel states.

It turns `Button COMP` interaction data into clear control signals through `Panel CHOP -> Select CHOP -> Rename / Merge`.

Common outputs include:

- `state`: persistent toggle state for on/off, enable/disable, and mode holding.
- `select`: momentary press state for triggers, press-and-hold controls, and temporary actions.
- `inside`: pointer-inside state for hover, hotspot, and radar-region behavior.
- `radio state`: mutually exclusive selection state for mode selectors, preset selectors, and cue selectors.

Use it when:

- button clicks need to become stable CHOP control signals;
- toggle, momentary, radio, and hover states should stay separate;
- multiple buttons need to be merged into a readable `button_state_bus`.

#### 2. Button skin / image state block

This block handles custom button visuals.

The `Button COMP` remains the real interaction hitbox, while its internal `text` Text COMP displays `off` / `on` images or TOPs. CHOP state signals decide which visual state is shown.

Use it for:

- two-image on/off button skins;
- inactive black-and-white images and active color images;
- visual switching driven by toggle, radio, or inside states;
- fade transitions with `Lag CHOP + Cross TOP`.

Use it when:

- the default Button COMP look is not enough;
- a button must stay clickable while showing a custom visual state;
- many buttons should share the same visual structure.

#### 3. Master / clone button group block

This block manages repeated buttons and button groups.

Build one master button first, then clone its internal structure into other buttons. Each instance keeps its own position, name, and state reader, while sharing the same skin / transition logic.

Use it when:

- building many buttons, such as a preset grid, cue grid, or VJ trigger pad;
- the internal button structure should be updated once and reused everywhere;
- each button needs independent state but consistent visual behavior.

#### 4. Slider / control panel block

This block covers sliders and broader control-panel layouts.

It focuses on the full chain from UI input to parameter control: slider / field / table / button -> panel value -> mapping / range -> target parameter -> visual feedback.

Use it when:

- building a perform mode control panel;
- controlling brightness, speed, size, threshold, color, or other live parameters;
- creating a TouchDesigner tool interface with labels, readouts, and reset behavior.

Button-related knowledge belongs inside this UI skill and does not need to be split into a separate skill.

### Install

From the repository root, copy the whole skill folder into your Codex skills directory:

```powershell
Copy-Item -Recurse -Force `
  ".\skills\td-ui-panel-interface-tutorial" `
  "$env:USERPROFILE\.codex\skills\td-ui-panel-interface-tutorial"
```

If you downloaded only this skill folder, run this from its parent directory:

```powershell
Copy-Item -Recurse -Force `
  ".\td-ui-panel-interface-tutorial" `
  "$env:USERPROFILE\.codex\skills\td-ui-panel-interface-tutorial"
```

### Example Prompts

- "Help me summarize this TouchDesigner UI tutorial."
- "Build a control panel with Container COMP."
- "Create a group of button and slider controls."
- "Make a TouchDesigner perform mode UI."
- "Fix Button COMP state reading."

### Structure

```text
td-ui-panel-interface-tutorial/
  SKILL.md
  README.md
  agents/
    openai.yaml
```


