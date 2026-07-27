---
name: td-project-case-analysis-to-obsidian
description: Research real TouchDesigner artworks, installations, talks, case studies, and commercial deployments; reconstruct their TD-oriented system logic; separate verified evidence from engineering inference; draft structured Chinese project-case notes; and write, index, synchronize, and verify them in Obsidian. Use when the user asks to investigate a TouchDesigner project or speaker, find related information or videos, explain the production logic, compare TD with Unreal or external systems, document installation architecture or deployment practices, preview project case studies, or save project analyses into an Obsidian `Project Case Studies` hierarchy.
---

# TD Project Case Analysis to Obsidian

Turn incomplete public project material into an evidence-aware TouchDesigner system analysis, then maintain it as a navigable Obsidian note.

## Required Pairing

- Use `video-tutorial-to-build` when a video, talk, transcript, or local recording is a primary source. Let it own transcript retrieval, timestamps, keyframes, and visual-evidence status.
- Use relevant TD direction skills for domain-specific correctness. Common routes:
  - `td-data-python-protocol-tutorial`: DAT, Python, Extensions, databases, OSC, UDP, NDI, MIDI, Art-Net, web APIs, external applications.
  - `td-interaction-tracking-tutorial`: mocap, sensors, MediaPipe, Kinect, LiDAR, gesture and calibration.
  - `td-glsl-shader-tutorial`: GLSL, SDF, uniforms and GPU effects.
  - `td-compositing-render-tutorial`: TOP routing, Render TOP, feedback and final output.
  - `td-particle-instancing-tutorial`: particles, point clouds and instancing.
  - `td-geometry-sop-tutorial`: SOP geometry and procedural form.
- Use `obsidian-note-maintainer` before any Obsidian write. Let it own vault convention discovery, mirror reconciliation, index maintenance, synchronization, approval and SHA-256 verification.

Read [references/td-system-analysis-checklist.md](references/td-system-analysis-checklist.md) before analyzing the implementation. Read [references/project-case-study-template.md](references/project-case-study-template.md) before drafting or writing a note.

## Workflow

### 1. Establish Scope

Identify:

- project title, speaker or studio, event and date when available;
- what the user wants emphasized;
- whether the current deliverable is research, a preview draft, or an authorized Obsidian write;
- available sources: official project page, official video, talk transcript, portfolio, press material, screenshots, source files or `.toe`.

Do not ask for details that can be discovered safely. If several projects are requested, create one note per project and one shared index entry.

### 2. Gather Evidence

Search official sources first, then reputable secondary sources. When using web search, link the exact pages that support the claims.

For video sources:

1. Collect metadata and subtitles.
2. Build a timestamped timeline.
3. Extract representative keyframes when the visual or node network matters.
4. If keyframes fail, explicitly mark the analysis as transcript-only; do not claim visual confirmation.

Maintain an evidence ledger while researching:

| Level | Meaning | Writing rule |
|---|---|---|
| Verified | Explicitly stated or visibly confirmed | Present as fact and cite the source |
| Corroborated | Supported by multiple indirect clues | State with limited confidence |
| Reconstruction | A practical TD implementation inferred from evidence | Label as recommended or plausible |
| Unknown | Source does not resolve it | Put in validation boundaries |

Never convert a standard TD practice into a claim about the original project.

### 3. Reconstruct the System

Analyze the project from goal to operations:

```text
experience goal
  → input and sensing
  → data cleanup and feature extraction
  → state, control and external services
  → visual generation and rendering
  → media, lighting and physical output
  → deployment, monitoring and recovery
```

For each layer, record:

- confirmed tools and protocols;
- likely TD operator families or COMP boundaries;
- the data shape entering and leaving the layer;
- timing, calibration and failure behavior;
- parameters that materially affect the experience;
- what can become a reusable module.

Prefer module-level logic over invented node-by-node networks. Give node chains only when supported by evidence or clearly labeled as a reconstruction.

### 4. Route the TD Knowledge

Choose one primary TD direction skill and up to two secondary skills. Record:

- primary skill;
- secondary skills;
- why the routing fits;
- which reusable pattern belongs in each skill.

Use this routing to improve technical depth, but keep the final note project-centered rather than turning it into a generic tutorial.

### 5. Draft the Analysis

Use the project-case-study template. Always include:

- project positioning and experience goal;
- verified facts;
- end-to-end architecture;
- detailed TD logic by module;
- recommended project structure;
- core production judgment;
- risks and common failure modes;
- uncertainty and validation boundaries;
- source links and local evidence paths.

Use Mermaid only when relationships are materially clearer than a text pipeline. Keep Chinese prose direct; retain exact node, protocol and software names in English.

If the user asks to preview first, stop after presenting the complete draft. Do not write to Obsidian until they authorize it.

### 6. Place It in Obsidian

Use this default hierarchy unless the vault already has a stronger convention:

```text
TouchDesigner/
├─ Project Case Studies/
│  ├─ _Project Case Studies Index.md
│  └─ YYYY-MM-DD <Project or Speaker> 项目案例分析.md
├─ Tutorials/
├─ Skill Notes/
├─ Plugin Notes/
└─ Workflow Notes/
```

Classification boundary:

- `Project Case Studies`: complete artwork, commercial case, installation architecture or deployment review.
- `Tutorials`: a reproducible step-by-step lesson.
- `Skill Notes`: reusable technique independent of one project.
- `Workflow Notes`: environment and operational procedures.

Keep `Project Case Studies` flat while the collection is small. Add thematic subfolders only when the vault already uses them or the collection has enough notes to justify them. Prefer thematic sections in the index before deeper folders.

### 7. Index, Synchronize and Verify

Follow `obsidian-note-maintainer` exactly:

1. Inspect the target folder, index and a similar recent note.
2. Detect workspace mirror and actual vault.
3. Reconcile differences before editing.
4. Edit the workspace mirror with `apply_patch`.
5. Add the project entry to `_Project Case Studies Index.md`.
6. Ensure a higher-level TouchDesigner index links to the project-case-study index.
7. Request approval before writing outside allowed roots.
8. Copy only the new or changed notes and required indexes.
9. Re-read the destination and compare SHA-256 hashes.

Do not report completion until every paired file matches.

## Quality Gates

Before handing off, confirm:

- project count equals note count;
- every note has a source URL and backlink;
- every technical claim is verified, labeled reconstruction, or listed as unknown;
- TD logic covers input, control, visual/output and operations where relevant;
- exact operator names are not invented from transcript-only evidence;
- title, filename, frontmatter and index use the vault's established style;
- official-title conflicts are explained rather than silently normalized;
- mirror and vault copies have matching SHA-256 hashes after synchronization.

## Completion Report

Report:

- created or updated note and index paths;
- hierarchy decision;
- primary TD logic emphasized in each note;
- evidence limitations such as missing keyframes or source files;
- mirror/vault synchronization and hash status.
