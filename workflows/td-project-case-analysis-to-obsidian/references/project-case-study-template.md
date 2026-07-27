# TouchDesigner Project Case Study Note Template

Adapt field names and section order to the inspected vault convention. Remove irrelevant sections instead of filling them with generic text.

```markdown
---
type: project-case-study
topic: TouchDesigner
project: <official project title>
speaker: <speaker or studio>
source: <YouTube / Vimeo / official site / local file>
source_url: <exact URL>
status: analyzed
tags:
  - TouchDesigner
  - project-case-study
  - <domain tags>
---

# <Speaker or Studio>｜<Project> 项目案例分析

返回索引：[[TouchDesigner/Project Case Studies/_Project Case Studies Index]]

> [!info] YYYY-MM-DD · 初版
> 根据 <sources> 整理。重点分析 <TD-oriented focus>。

## 项目定位

用一至三段解释体验目标、受众、场地和 TouchDesigner 在项目中的角色。

```text
experience / input
  → data and control
  → TouchDesigner
  → render / external engine
  → display / lighting / physical output
```

## 已确认事实

- 仅记录来源明确支持的事实。
- 数字、协议、软件、设备和规模尽量附出处或时间戳。

## 证据状态

| 结论 | 状态 | 来源或依据 |
|---|---|---|
| <claim> | verified / corroborated / reconstruction / unknown | <URL, timestamp or reason> |

## TouchDesigner 逻辑拆解

### 1. 输入与传感

说明来源、数据格式、频率、坐标系、缺帧和校准。

### 2. 数据与特征

说明清洗、映射、特征提取、数据库或外部服务。

### 3. 状态与控制

说明状态机、消息协议、操作界面、同步和握手。

### 4. 视觉与渲染

说明 SOP / CHOP / TOP / DAT / COMP / GLSL / Unreal 的职责与边界。

### 5. 输出与空间

说明屏幕、投影、灯光、音频、媒体录制和物理安装。

### 6. 部署与运维

说明配置、自动启动、监控、日志、模拟器、恢复和现场操作。

## 推荐工程结构

```text
/services
/input
/features-or-logic
/state
/visual
/output
/ops
```

## 制作逻辑的核心判断

总结真正可复用的系统思想，避免只重复节点名。

## 参数与校准重点

| 参数 | 影响 | 校准方式 | 失败表现 |
|---|---|---|---|
| <parameter> | <effect> | <method> | <symptom> |

## 风险与常见坑

- 记录协议、性能、同步、环境和运维风险。

## 可复用模块

- <module and interface>

## 不确定点与验证边界

- 明确没有源码、关键帧、设备规格或节点网络时无法确认的内容。
- 将复刻建议与原作者实现分开。

## 资料

- [官方来源](<URL>)
- 本地字幕：`<absolute path>`
- 本地关键帧：`<absolute path>`，或注明未取得
```

## Index Entry Template

```markdown
## 项目案例分析

### <theme>

- [[YYYY-MM-DD <Project> 项目案例分析]]
  - <one-line TD system focus>
```
