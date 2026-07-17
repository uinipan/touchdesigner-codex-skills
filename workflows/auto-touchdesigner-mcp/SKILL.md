---
name: auto-touchdesigner-mcp
description: TouchDesigner MCP WebServer bootstrap, live-project inspection, connection workflow, route reference, and repair playbook. Use when Codex needs to open TouchDesigner 2023, import or verify mcp_webserver_base.tox, connect to port 9981, inspect or modify the current TD network, read CHOP/DAT state, compile and diagnose GLSL, call the TD MCP HTTP API, create/update TD nodes, diagnose NOT_FOUND routes, fix timeout/WebServer/JSON problems, or wire UDP/DAT Execute triggers.
---

# TouchDesigner MCP

Use this single skill for the whole local TD MCP lifecycle: launch/bootstrap, health check, Python exec, node API calls, troubleshooting, and small UDP trigger wiring.

## Local Defaults

- TouchDesigner shortcut: resolve it with `scripts/resolve_td23_shortcut.ps1` or use a user-provided path.
- MCP tox: locate `mcp_webserver_base.tox` from the user-provided MCP project or installation; keep its sibling `modules/` and `import_modules.py` together.
- MCP port: `9981`
- Server info endpoint: `http://127.0.0.1:9981/api/td/server/td`

Keep `mcp_webserver_base.tox` beside its original `modules/` and `import_modules.py`. Do not copy the tox alone.

## Bootstrap TD MCP

Use this when TD is not open, the MCP tox is not loaded, or the user asks to prepare a TD project for MCP.

1. Validate local resources.
   - Run `scripts/resolve_td23_shortcut.ps1` if the TD 2023 executable/version needs confirmation.
   - Confirm the MCP tox exists with its sibling `modules/` and `import_modules.py`.

2. Launch TouchDesigner 2023.
   - Run `scripts/launch_td23.ps1` for a new project.
   - If the user provides a `.toe`, run it with `-ProjectPath`.
   - Launching TD is a GUI action; request approval when required.

3. Import the MCP tox into `/project1`.
   - Prefer MCP/Python control if already available.
   - If no control channel exists yet, ask the user to manually import the tox into `/project1`.
   - Keep the imported component's external tox path pointing at the original tox path.
   - Set Web Server DAT port to `9981` and activate/restart/pulse the server if those controls exist.

4. Test the connection.
   - Run `scripts/test_mcp_connection.ps1`, or call the server info endpoint directly.
   - Success means JSON, `success: true`, and TD/server information in `data`.

## Canonical Routes

Do not guess old route names. These are the routes to use.

Execute Python in the currently open TD process:

```powershell
$body = @{ script = "result = 1 + 1" } | ConvertTo-Json -Compress
Invoke-RestMethod `
  -Uri "http://127.0.0.1:9981/api/td/server/exec" `
  -Method Post `
  -ContentType "application/json" `
  -Body $body
```

Create a node:

```powershell
$body = @{
  parentPath = "/project1"
  nodeType = "noiseTOP"
  nodeName = "noise1"
  parameters = @{ nodeX = 0; nodeY = -200 }
} | ConvertTo-Json -Depth 6 -Compress
Invoke-RestMethod `
  -Uri "http://127.0.0.1:9981/api/nodes" `
  -Method Post `
  -ContentType "application/json" `
  -Body $body
```

Check server info:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:9981/api/td/server/td" -Method Get
```

List nodes:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:9981/api/nodes?parentPath=/project1&includeProperties=false" -Method Get
```

Check errors:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:9981/api/nodes/errors?nodePath=/project1" -Method Get
```

## Avoid Wrong Routes

These commonly return `NOT_FOUND: No route matched`:

- `/execute_python_script`
- `/exec_python_script`
- `/api/execute_python_script`
- `/api/exec_python_script`

If the port is open but a route returns `NOT_FOUND`, switch to `POST /api/td/server/exec` with body `{"script":"..."}`.

## Repair Playbook

1. Port not listening or timeout:
   - Confirm TD is open.
   - Inspect the TD WebServer DAT: it should be Active, on port `9981`, and may need Restart.
   - Check for another process using the port:

```powershell
Get-NetTCPConnection -LocalPort 9981 -ErrorAction SilentlyContinue | Select-Object LocalAddress,LocalPort,State,OwningProcess
```

2. Server info fails:
   - Confirm `mcp_webserver_base.tox` is imported into `/project1`.
   - Confirm the tox still points to its original directory with `modules/` and `import_modules.py`.
   - If the response is HTML/plain text, the request is hitting the wrong service or route.

3. Python exec fails:
   - First test `result = 1 + 1`.
   - If `NOT_FOUND`, do not try old route names; use `/api/td/server/exec`.
   - If JSON parsing fails, avoid hand-written curl quoting. Prefer `Invoke-RestMethod` with `ConvertTo-Json -Compress`; for nested bodies use `-Depth 6` or higher.

4. Node creation fails:
   - Verify the parent path exists, usually `/project1`.
   - Verify the `nodeType` spelling against TD operator names such as `noiseTOP`, `mathCHOP`, or `containerCOMP`.
   - Query `/api/nodes/errors?nodePath=/project1` after creating or updating nodes.

5. Project path confusion:
   - MCP controls the currently open TD process, not necessarily the repo workspace.
   - Ask for the current `.toe` path when file paths matter.
   - Use absolute Windows paths for scripts/shaders passed into TD, especially:

```python
exec(open(r"D:\path\to\script.py", encoding="utf-8").read())
```

## Live Project Inspection

Inspect before editing. Return JSON-safe primitive values rather than OP, Par, or Channel objects.

```python
import json

target = op('/project1/example')
out = {
    'path': str(target.path),
    'type': str(target.OPType),
}

if target.isCHOP:
    out['channels'] = {str(c.name): float(c.eval()) for c in target.chans()}

if target.isDAT:
    out['text'] = str(target.text)

result = json.dumps(out, ensure_ascii=False)
```

- If a nested result is serialized as an unrelated `parameter1` OP, return `json.dumps(...)` as a string and parse it outside TD.
- In TD builds where `children`, `errors`, or `warnings` are properties, do not call them as functions. If uncertain, inspect the attribute before use.
- Read actual paths, channel names, sample counts, values, custom parameters, DAT text, and errors before changing a network.
- MCP controls the currently open TD process. Confirm the target component and project before mutation.

### GLSL Inspection

After editing a shader DAT:

1. Force cook the GLSL operator.
2. Read its errors and warnings.
3. Confirm the intended uniform expressions still resolve.
4. Verify output state, not only compile success.
5. For ordering algorithms, run a CPU-side check for unique, missing, and duplicate indices using the same formula.

Do not claim a random mapping is non-repeating until it has been counted. Compile success does not prove complete visual coverage.

### Text Encoding

- Use UTF-8 request bodies: `application/json; charset=utf-8` and `UTF8.GetBytes($body)`.
- When Chinese comments display as mojibake in GLSL or callback DATs, keep executable-source comments in ASCII and place detailed Chinese notes in a nearby UTF-8 Text DAT or Obsidian note.
- Do not repeatedly rewrite source comments to test encoding while the visual system is live.

## Import Tox With Existing Exec Channel

When Python exec already works, this is the safe starting shape:

```python
tox_path = r"D:\path\to\touchdesigner-mcp-td\mcp_webserver_base.tox"
parent_comp = op("/project1")

existing = op("/project1/mcp_webserver_base")
if existing:
    existing.destroy()

mcp_comp = parent_comp.loadTox(tox_path)
mcp_comp.name = "mcp_webserver_base"

if hasattr(mcp_comp.par, "externaltox"):
    mcp_comp.par.externaltox = tox_path

for candidate in [mcp_comp] + list(mcp_comp.findChildren(depth=10)):
    if "webserver" in candidate.OPType.lower() or "webserver" in candidate.name.lower():
        if hasattr(candidate.par, "port"):
            candidate.par.port = 9981
        if hasattr(candidate.par, "active"):
            candidate.par.active = 1
```

Treat this as a starting point. If a parameter is missing, enumerate `pars()` on the imported component or Web Server DAT before changing it.

## UDP Trigger Pattern

For small project triggers from a UDP toolkit:

```text
udp_toolkit output -> Null DAT -> DAT Execute DAT
```

Enable `Table Change` on the DAT Execute DAT. Start with:

```python
def onTableChange(dat):
    message = dat[1, 'message'].val.strip()

    if message == '111':
        # Execute current project action.
        pass

    return
```

Add project-specific `if/elif` branches only after confirming the incoming DAT table shape.
