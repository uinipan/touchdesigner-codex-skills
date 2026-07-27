---
name: td-data-python-protocol-tutorial
description: Learn TouchDesigner tutorials focused on DATs, Python scripting, data models, tables, callbacks, Execute DATs, extensions, OSC, MIDI, WebSocket, HTTP/API, serial, NDI/control protocols, and external app communication. Use when a tutorial's main reusable value is data flow, scripting, automation, or communication.
---

# TD Data Python Protocol Tutorial

Use this skill to turn data, scripting, and protocol tutorials into reusable system knowledge. Treat TouchDesigner MCP as a block experiment workspace: test one DAT table, callback, protocol endpoint, or data transform at a time.

## Workflow

1. Identify the data role.
   - Classify as DAT/table workflow, Python callback, component extension, external API, OSC, MIDI, WebSocket, serial, NDI/control, file I/O, or automation.
   - Record where data enters, how it is transformed, and what node family consumes it.
   - Separate transport/protocol, parsing, state, callbacks, mapping, and visual/control target.

2. Map the schema.
   - Preserve column names, row semantics, channel names, message addresses, JSON fields, callback signatures, and parameter references.
   - Record update frequency, event timing, cook behavior, and whether state is pull-based, push-based, or callback-driven.
   - Note error handling, reconnect behavior, initialization order, and dependency setup.

3. Extract reusable data patterns.
   - Group the tutorial into input, parse/normalize, store state, trigger callbacks, map to TD operators, and debug/monitor.
   - Explain why each DAT/Python/protocol piece exists.
   - Preserve minimal examples only when exact syntax matters.

4. Run block experiments when useful.
   - Limit each TD experiment to one data/protocol block.
   - Define the hypothesis: what message/table/callback should appear, where it should be observed, and which tutorial timestamp supports it.
   - Record observations, failed attempts, useful snippets, and what should update this skill.

## Knowledge To Preserve

- Data schema and ownership.
- Callback signatures, parameter references, and operator paths.
- Protocol addresses, ports, payload examples, and reconnect rules.
- Initialization order and dependency assumptions.
- Debugging cues for empty DATs, stale values, callback loops, bad paths, encoding issues, or blocked ports.

## Output Shape

Produce a compact tutorial type note with:

- `Type`: data/python/protocol.
- `Data map`: source -> schema -> transform -> target.
- `Callback/protocol map`: handlers, addresses, payloads, timing.
- `Block experiments`: scope, hypothesis, observations, failed attempts.
- `Reusable patterns`: scripts, schemas, callback rules, and debugging heuristics.
- `Uncertainties`: missing dependencies, credentials, hardware, ports, or API details.
