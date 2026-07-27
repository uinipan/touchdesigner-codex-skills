---
name: obsidian-note-maintainer
description: Create, update, clean, and synchronize local Obsidian Markdown notes while preserving vault conventions. Use when the user asks to write or update an Obsidian note, save current project or debugging progress, maintain a skill note, add a dated change record, update a vault index, synchronize a workspace mirror with the actual vault, or verify that mirrored notes match.
---

# Obsidian Note Maintainer

Maintain readable Obsidian notes and keep configured workspace mirrors synchronized with the actual vault. Treat the domain skill or inspected artifact as the source of technical truth; this skill owns note structure, change records, cleanup, and synchronization.

## Workflow

1. Identify the facts to record.
   - Reuse conclusions, measurements, paths, and evidence from the active task.
   - When paired with another skill, let that skill own domain correctness. Do not turn guesses into documented facts.
   - Separate verified results from provisional ideas or remaining questions.

2. Discover the note and destination.
   - Prefer updating an existing note over creating a duplicate.
   - Inspect the target folder, relevant index, and at least one similar recent note before creating a new note.
   - Match established filename patterns, frontmatter keys, backlink style, section order, language, Wiki Links, and table shapes.
   - Detect whether both a workspace mirror and an actual Obsidian vault exist. Do not assume paths outside the current project.

3. Reconcile before editing.
   - Compare paired files before overwriting either copy.
   - If they differ, determine which contains newer user edits and merge safely. Do not blindly replace a newer vault note with an older mirror.
   - Preserve unrelated user edits.

4. Update the note.
   - Keep Markdown encoded as UTF-8.
   - Set an existing `updated:` frontmatter field to the current local date in `YYYY-MM-DD`. Add it only when compatible with the note's established frontmatter.
   - Update the existing index or backlink when required by the vault pattern.
   - Remove or replace incorrect, duplicated, or obsolete body content. Do not keep bad guidance merely to preserve history.
   - Use `apply_patch` for workspace note edits.

5. Record material changes.
   - Maintain a `## 更新记录` or locally equivalent section near the top when the note is expected to evolve.
   - Sort entries newest first. Never invent dates for older changes whose date is unknown.
   - Merge multiple changes of the same type on the same day instead of creating repetitive entries.
   - Record concise outcomes, not a line-by-line diff.
   - Use native Obsidian Callouts so colors survive normal theme changes:
     - `> [!success] YYYY-MM-DD · 新增` for green verified additions;
     - `> [!warning] YYYY-MM-DD · 修正` or `· 删除` for orange corrections and removals;
     - `> [!example] YYYY-MM-DD · 验收` for purple validation additions;
     - `> [!info] YYYY-MM-DD · 初版` or `· 同步` for blue general records.
   - Add a dated Callout near a materially changed body section only when it improves scanning. Do not decorate every sentence.

6. Synchronize configured copies.
   - Prefer editing the workspace mirror first when the project already uses one, then copy the confirmed result to the actual vault.
   - Request approval before writing outside allowed workspace roots.
   - Copy only the intended note and any explicitly required index files. Do not synchronize an entire vault unless the user asks.

7. Verify completion.
   - Re-read the destination note and check frontmatter, Wiki Links, headings, code fences, tables, and Callout syntax.
   - Compute SHA-256 for the workspace and vault copies when both exist. Matching hashes mean their byte content is identical at verification time.
   - Treat SHA-256 as an integrity check, not as a backup or version history.
   - If hashes differ, inspect and reconcile the files; never report synchronization as complete.

## Pairing with Other Skills

Use this skill alongside the active domain skill in the same turn:

- A TouchDesigner skill builds, diagnoses, and validates the TD network; this skill records the verified changes in Obsidian.
- `video-tutorial-to-build` owns tutorial evidence, timestamps, keyframes, and tutorial-specific note sections; this skill owns dated maintenance, cleanup, mirror synchronization, and integrity checks.
- A code, document, or research skill owns its source facts; this skill preserves them using the vault's conventions.

Explicit invocation is supported, for example:

```text
使用 $td-particle-instancing-tutorial 继续测试当前工程；完成后使用
$obsidian-note-maintainer 把本轮修正写入对应 Skill 笔记并同步 Vault。
```

Natural requests such as “把这次修改记到 Obsidian”“更新对应说明笔记” or “同步工作区笔记和 Vault” should also trigger this skill without requiring the user to repeat the formatting rules.

## Completion Report

Report only what matters:

- note or index files updated;
- date and change categories recorded;
- obsolete content removed or replaced, when applicable;
- workspace/vault synchronization status;
- SHA-256 match status when paired copies exist;
- unresolved conflict or missing destination, if any.
