# TD System Analysis Checklist

Use this checklist to avoid reducing a project case study to visual-style description.

## 1. Intent and Constraints

- What should the audience feel or do?
- Is the system live, interactive, generative, linear or hybrid?
- What are the space, duration, throughput and operator constraints?
- Is the project an artwork, event, retail experience, stage show or permanent installation?

## 2. Inputs

- Camera, mocap, MediaPipe, Kinect, LiDAR, encoder, Hall sensor, microphone, MIDI, Stream Deck.
- OSC, UDP, TCP, WebSocket, HTTP, serial, NDI, Spout/Syphon, Dante.
- Frame rate, sample rate, coordinate system, packet schema, timestamp and heartbeat.
- Calibration, smoothing, dead zones, dropout and simulator fallback.

## 3. Data and Control

- CHOP channel schema and normalization.
- DAT parsing, tables, Python Extensions and callbacks.
- Database ownership and asynchronous access.
- Global state, session state and module-local state.
- Event bus or publish/subscribe boundaries.
- Handshake, timeout, retry and idempotency.

## 4. Visual and Render

- SOP geometry, instancing, particles and point clouds.
- GLSL TOP/MAT, SDF, uniforms and multi-pass effects.
- Render TOP, camera, lighting, material and post-processing.
- Unreal or other engines: decide which application owns 3D, UI, media and state.
- Separate source endpoint from helper preview and operator UI.

## 5. Output

- Resolution, orientation, pixel map, multi-screen layout and projection mapping.
- NDI channel strategy and texture-atlas opportunities.
- DMX / Art-Net universes, channel ordering and fixture configuration.
- Audio device routing, latency and synchronization.
- Recording, QR delivery and online/offline media handoff.

## 6. Deployment and Operations

- Shared core build versus per-machine configuration.
- Auto-start, full screen, process order and shutdown.
- Hardware health, FPS, cook time, network and external-process heartbeat.
- Logging, operator controls, reset, panic and staged recovery.
- Offline simulator and failure injection.
- Backup version and recovery procedure.

## 7. Evidence Discipline

Ask for each claim:

1. Was it stated in a source?
2. Was it visible in a keyframe or source file?
3. Is it only a plausible TD implementation?
4. What evidence would confirm it?

Use precise labels:

- “演讲明确提到……” for verified statements.
- “画面可见……” only after visual inspection.
- “一种可执行的 TD 复刻方式是……” for reconstruction.
- “需要原始 `.toe` / schema / device spec 确认……” for unknowns.
