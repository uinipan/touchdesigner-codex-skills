# Note Workflow

Use this reference when the user wants tutorial notes, Obsidian/Notion sync, Markdown files, project logs, or asks to save current progress.

When `obsidian-note-maintainer` is available, let it own dated update records, obsolete-content cleanup, workspace/vault synchronization, and SHA-256 integrity checks. This reference continues to own tutorial-specific timing, evidence, filenames, indexes, and section structure.

## Default Timing

Generate or update notes at any of these moments:

- After initial video understanding: create a first note with video info, summary, timeline, TD tips, direction classification, and reusable patterns.
- After each natural learning phase: append what was learned, node paths, key parameters, reusable patterns, differences from related tutorials, and issues.
- After debugging or visual tuning: record the symptom, diagnosis, fix, and reusable lesson.
- At final completion: consolidate into a clean reference note with final technique overview and next skill-update ideas.
- Whenever the user asks: write the best current snapshot, even if the tutorial analysis is incomplete.

## Phase Detection

Do not hard-code phases such as audio reactive or post-processing for every project. Infer phases from the tutorial and project. Common phase types include:

- Source/assets/import
- Procedural geometry or data generation
- Simulation or animation
- Material/color/lookup
- Interaction, audio, or sensor control
- Camera/render/output
- Post-processing/compositing
- Export/recording
- Debugging/performance

Only include sections that exist in the current tutorial or project.

## Obsidian Format

For Obsidian notes:

- Write Markdown into the user's actual vault.
- Before writing a new note, inspect the target vault folder's existing notes and index. Read at least one recent similar note plus the tutorial index when available, then match the folder's established filename pattern, frontmatter keys, backlink line, section order, table shapes, and language style.
- For TouchDesigner tutorial notes in a vault that already has dated Chinese notes, default to `YYYY-MM-DD <Tutorial Title> 中文笔记.md`, include YAML frontmatter, add `返回索引：[[TouchDesigner/Tutorials/_TD Tutorial Index]]`, and update `_TD Tutorial Index.md` with the new note link.
- If an incorrectly named or duplicate note was created during the same task, replace it with the vault-style note and remove the duplicate after confirming the corrected note exists.
- Keep professional TD terms in English when clearer, such as `SOP`, `CHOP`, `TOP`, `Ramp TOP`, `Copy SOP`, `Audio Analysis`, `Render TOP`, and `Line MAT`.
- Use Chinese prose by default when the user prefers Chinese.
- Include the video link and timestamp links for important steps.
- Include backlinks or an index entry when a tutorial index exists.
- Prefer updating the existing tutorial note over creating duplicates.

### TouchDesigner Tutorial Note Shape

When existing notes do not provide a stronger local pattern, use this shape for TouchDesigner tutorial notes:

```markdown
---
type: tutorial-note
topic: TouchDesigner
source: <YouTube | Vimeo | Tencent VOD | local file | other>
video_id: <stable id or filename>
tags:
  - TouchDesigner
  - <direction tags>
  - tutorial
---

# YYYY-MM-DD <Tutorial Title> 中文笔记

返回索引：[[TouchDesigner/Tutorials/_TD Tutorial Index]]

## 视频信息
## 教程理解
## 教程类型路由
## 核心结构
## 分阶段时间线
## 关键参数
## TD Tips
## 视觉关键参数
## 可复用模式
## 视觉验证
## 不确定点
```

Omit sections that truly do not apply, but preserve this order for sections that are present. Use the phase timeline table shape from this file. Keep `Visual comparison` / `视觉验证` grounded in transcript timestamps, screenshots, or keyframes.

## No Note App Configured

Obsidian is optional. If no note app or vault is configured:

- Offer to write a regular Markdown file in the current workspace or another user-provided folder.
- If writing a file is not requested, output the note directly in chat.
- Keep the same note structure so the user can later move it into Obsidian, Notion, Typora, VS Code, or another Markdown tool.

## Note Content

Each note should include, when available:

- Video title and link.
- Current status: collected, classified, partially analyzed, skill updated, or blocked.
- Tutorial summary.
- Time-coded steps.
- TD tips grouped by workflow, parameters, visuals, and pitfalls.
- Visual-critical parameters: list the parameters that most affect the final look, grouped by geometry, motion/deformation, audio, post-processing, and color when relevant.
- Technique mapping: node paths, output chain, custom parameters, and visual role.
- Learning log: what was extracted in each phase.
- Phase timeline: map each learning phase to tutorial timestamp ranges, related node paths, and the next checkpoint to verify.
- Next steps.

## Phase Timeline Format

When the tutorial is being learned in stages, add a phase table:

| Phase | Video Range | Goal | Status | TD Nodes | Checkpoint |
| --- | --- | --- | --- | --- | --- |

Use status values such as `not started`, `in progress`, `learned`, `needs visual check`, or `skill updated`.

The phase table should let the user jump back to the exact tutorial section and see what has already been extracted as reusable knowledge.
Distinguish the tutorial phase endpoint from helper preview nodes. If a phase ends at a SOP, list the SOP endpoint in `TD Nodes` and mention Render TOP / Select TOP nodes only as preview helpers.

## Visual-Critical Parameters

For TD tutorial notes, add a compact tuning section:

- Group parameters by purpose, such as Geometry, Motion / Deformation, Audio Reactive, Post-processing, and Color.
- For each parameter, explain the visual effect and the likely tuning direction.
- Tie parameters to timestamps when known.
- Attach keyframe image paths or screenshot references when available, especially for parameters that are hard to understand from text alone.
- Include pitfalls, such as values that easily destroy the structure, create too much blur, clip the image, or make audio reaction explode.
