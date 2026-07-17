param(
    [string]$ShortcutPath = "C:\Users\Public\Desktop\TouchDesigner.lnk",
    [string]$ExpectedProductYear = "2023"
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path -LiteralPath $ShortcutPath)) {
    Write-Error "TouchDesigner shortcut not found: $ShortcutPath"
    exit 1
}

$shell = New-Object -ComObject WScript.Shell
$shortcut = $shell.CreateShortcut($ShortcutPath)
$targetPath = $shortcut.TargetPath

if (-not $targetPath -or -not (Test-Path -LiteralPath $targetPath)) {
    Write-Error "Shortcut target does not exist: $targetPath"
    exit 1
}

$versionInfo = (Get-Item -LiteralPath $targetPath).VersionInfo
$productVersion = [string]$versionInfo.ProductVersion

if ($productVersion -notmatch "\.$ExpectedProductYear\.") {
    Write-Error "Expected TouchDesigner $ExpectedProductYear, but shortcut target ProductVersion is '$productVersion': $targetPath"
    exit 1
}

[pscustomobject]@{
    ShortcutPath = $ShortcutPath
    TargetPath = $targetPath
    Arguments = $shortcut.Arguments
    WorkingDirectory = $shortcut.WorkingDirectory
    ProductVersion = $productVersion
} | ConvertTo-Json -Depth 4
