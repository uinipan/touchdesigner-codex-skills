---
name: video-tutorial-to-build
description: Ingest tutorial videos from URLs or local files, collect transcript/keyframe evidence, classify the tutorial direction, and turn repeated tutorial patterns into reusable Codex skills. Use when the user provides a tutorial link/file and asks Codex to learn it, summarize it, compare tutorial directions, extract reusable patterns, create or update direction-specific skills, or produce a node/parameter/technique checklist. Supports subtitle retrieval, keyframe extraction, local transcription fallback, tutorial-type routing, and skill-generation guidance.
---

# Video Tutorial To Build

Use this skill as the tutorial intake and routing layer. Prefer automatic evidence gathering over asking the user to copy subtitles. Do not recreate the tutorial as the default outcome; first classify the direction, extract reusable patterns, and create or update a direction-specific skill when the learning is reusable.

## Workflow

1. Collect video context.
   - Run `scripts/fetch_video_context.py <url> --out <work-dir>` to fetch metadata, chapters, and subtitles with `yt-dlp`.
   - Treat `yt-dlp` as a generic video-site downloader, not a YouTube-only tool. If the site is unsupported, ask for a local video file, screenshots, copied transcript, or key timestamps.
   - Prefer author subtitles over auto subtitles. Prefer Chinese when present, then English, then auto English.
   - If `yt-dlp` is missing or fails, explain the exact missing dependency and continue with any available web metadata or user-provided transcript.

2. Extract visual evidence.
   - For visual tutorials, subtitles are not enough. Extract representative keyframes before drawing conclusions about the technique or direction.
   - Run `scripts/extract_keyframes.py <url-or-local-video> --timestamps <ts1> <ts2> ... --out <work-dir>/keyframes` when `ffmpeg` is available.
   - Choose keyframes at phase endpoints and visual inflection points, such as base geometry complete, deformation added, audio reaction visible, and final post-processing.
   - If direct URL keyframe extraction fails, try downloading a low-resolution local source with `yt-dlp` after user approval, then extract keyframes from the local file.
   - If keyframe extraction fails because `ffmpeg` or the site is unavailable, state that the current plan is transcript-only and ask for screenshots or permission to install/configure video tooling.

3. Transcribe only when needed.
   - If no usable subtitles are found, ask before downloading audio if the user has not already approved local transcription.
   - Run `scripts/transcribe_audio.py <url> --out <work-dir> --model small` for local transcription.
   - Keep downloaded audio and transcripts in the chosen work directory, preferably on D drive.

4. Clean and structure the tutorial.
   - Run `scripts/clean_transcript.py <subtitle-or-transcript-file> --out <timeline.md>`.
   - Produce a time-coded outline: goal, prerequisites, major steps, parameters, assets, and unclear moments.
   - For TouchDesigner tutorials, also produce a "TD tips learned from this video" section with reusable node, parameter, workflow, and debugging tips.
   - For TouchDesigner tutorials, produce a "visual-critical parameters" section that explains which parameters most affect the look, grouped by geometry, motion/deformation, audio, post-processing, and color when applicable.
   - Preserve timestamps for any operation or technique that may need visual confirmation.

5. Classify and route the tutorial type.
   - Decide the primary reusable tutorial direction before writing the final note.
   - For TouchDesigner tutorials, use these local skills when the tutorial matches:
     - `td-geometry-sop-tutorial`: SOP networks, procedural meshes, curves, surfaces, deformations, normals, UVs, and visible 3D form.
     - `td-audio-reactive-tutorial`: audio analysis, CHOP control chains, beat/spectrum/envelope detection, smoothing, lag, and audio-to-parameter mapping.
     - `td-particle-instancing-tutorial`: particles, point clouds, instancing, emitters, feedback motion, GPU particles, TOP-to-instance data, and many-object systems.
     - `td-glsl-shader-tutorial`: GLSL TOP/MAT, raymarching, SDFs, shader uniforms, UV math, feedback shaders, and GPU effects.
     - `td-compositing-render-tutorial`: Render TOP, cameras, lights, materials, TOP post-processing, feedback, bloom, blur, color correction, and final polish.
     - `td-ui-panel-interface-tutorial`: Container COMP, Panel COMP, Button/Slider/Table/List UI, custom control panels, perform mode interfaces, preset/cue panels, and VJ/operator surfaces.
     - `td-interaction-tracking-tutorial`: MediaPipe, Kinect, LiDAR, sensors, tracking, gestures, calibration, and interaction mapping.
     - `td-data-python-protocol-tutorial`: DATs, Python, callbacks, extensions, OSC, MIDI, WebSocket, HTTP/API, serial, and external app communication.
   - If a tutorial spans multiple types, choose one primary skill and one or two secondary skills. Keep the primary skill responsible for the final reusable recipe.
   - If no existing type skill fits, propose a new skill name, trigger description, and minimal workflow before creating it.
   - Output `tutorial type`, `primary skill`, `secondary skills`, and `why this routing was chosen`.

6. Decide whether to create or update a direction skill.
   - Read `references/touchdesigner_workflow.md` when the tutorial involves TouchDesigner, TD nodes, materials, GLSL, CHOP/TOP/SOP, particles, cameras, or audio-reactive visuals.
   - Create a new skill only when the tutorial introduces a direction not covered by existing skills.
   - Update an existing direction skill when the tutorial adds a reusable pattern, parameter heuristic, debugging rule, or classification signal.
   - Keep each direction skill focused on learning and reuse: triggers, classification signals, extraction workflow, reusable patterns, validation cues, and output format.
   - When TouchDesigner experimentation is useful, scope it by block/module rather than a whole project: one SOP structure, one CHOP mapping, one GLSL pass, one particle data path, one TOP post chain, one UI/panel control, one protocol/data block, one tracking input, or one render/material setup.
   - Treat MCP work as an experiment loop: hypothesis -> small TD block edit -> observe -> compare -> summarize -> update the direction skill.
   - Do not include whole-project execution steps in direction skills.

7. Maintain notes when useful.
   - Read `references/note_workflow.md` when the user asks to write, update, save, or sync notes, or when the tutorial work reaches a natural milestone.
   - When `obsidian-note-maintainer` is available, use it for dated change records, cleanup, workspace/vault synchronization, and integrity checks. Keep this skill responsible for tutorial evidence, timestamps, keyframes, routing, and tutorial-specific note content.
   - Notes may be generated at any time: after video understanding, after direction classification, after skill updates, or at the user's request.
   - Do not assume every project has audio reactivity, particles, GLSL, or post-processing. Derive note sections from the actual tutorial and current project.

## Local Transcription Policy

- Default to subtitles and metadata; do not download audio if subtitles are enough.
- Use local transcription for privacy. Do not upload audio to a cloud service unless the user explicitly asks.
- Start with `small` for speed. Use `base` for quick drafts or `medium` for better accuracy when the user accepts slower runs.
- If GPU support is unavailable, CPU transcription is acceptable but may be slow.

## Fallbacks

- If automatic subtitles and local transcription both fail, the user may provide copied subtitles, SRT/VTT files, screenshots, or key timestamps.
- Browser translation extensions can help the user obtain text, but do not assume Codex can read extension-rendered subtitles directly.

## Outputs

For each tutorial, produce:

- A short understanding of what the tutorial teaches.
- Tutorial type routing: primary type skill, optional secondary skills, and reasoning.
- A time-coded step list.
- Visual keyframes used for comparison, with timestamp links or local image paths when available.
- A technique checklist with assets, nodes/tools, parameters, and concepts.
- A reusable pattern note: what should be preserved as cross-tutorial knowledge.
- For TD tutorials: important TouchDesigner tips learned from the video, grouped as node workflow tips, parameter tips, visual-design tips, and common pitfalls.
- For TD tutorials: visual-critical parameters, explaining what each important parameter changes in the image and how to tune it when the result looks wrong.
- For TD tutorials: keyframe-linked parameter notes when screenshots are available, so important tuning advice points to the visual moment it affects.
- If notes are requested or a milestone is reached: update the user's note destination, such as an Obsidian vault, or save a regular Markdown file when no note app is configured.
- For each phase: record the real tutorial endpoint node/type separately from helper preview nodes. A Render TOP used only for visibility should not replace a SOP/CHOP/TOP endpoint from the tutorial.
- A visual comparison note for each visually important phase: `matches`, `close`, `different`, or `unknown because no keyframe/screenshot`.
- If TD experimentation was done: block scope, hypothesis, changes, observations, failed attempts, and what should be added to the direction skill.
- A list of uncertainties that require watching a timestamp, screenshot, or user confirmation.
