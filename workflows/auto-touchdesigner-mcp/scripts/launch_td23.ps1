param(
    [string]$ShortcutPath = "C:\Users\Public\Desktop\TouchDesigner.lnk",
    [string]$ProjectPath = "",
    [switch]$PassThru
)

$ErrorActionPreference = "Stop"

$resolver = Join-Path $PSScriptRoot "resolve_td23_shortcut.ps1"
$resolved = & $resolver -ShortcutPath $ShortcutPath | ConvertFrom-Json
$targetPath = [string]$resolved.TargetPath
$workingDirectory = [string]$resolved.WorkingDirectory

$startArgs = @()
if ($ProjectPath) {
    if (-not (Test-Path -LiteralPath $ProjectPath)) {
        Write-Error "TouchDesigner project not found: $ProjectPath"
        exit 1
    }
    if ([System.IO.Path]::GetExtension($ProjectPath).ToLowerInvariant() -ne ".toe") {
        Write-Error "ProjectPath must be a .toe file: $ProjectPath"
        exit 1
    }
    $startArgs += $ProjectPath
}

$process = Start-Process -FilePath $targetPath -ArgumentList $startArgs -WorkingDirectory $workingDirectory -PassThru

$result = [pscustomobject]@{
    TargetPath = $targetPath
    ProductVersion = $resolved.ProductVersion
    ProjectPath = $ProjectPath
    ProcessId = $process.Id
}

if ($PassThru) {
    $result | ConvertTo-Json -Depth 4
} else {
    Write-Output "Started TouchDesigner $($resolved.ProductVersion) with PID $($process.Id)."
}
