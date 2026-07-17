param(
    [string]$HostName = "127.0.0.1",
    [int]$Port = 9981,
    [int]$TimeoutSeconds = 30,
    [int]$IntervalSeconds = 1
)

$ErrorActionPreference = "Stop"

$endpoint = "http://${HostName}:${Port}/api/td/server/td"
$deadline = (Get-Date).AddSeconds($TimeoutSeconds)
$lastError = $null
$lastResponse = $null

while ((Get-Date) -le $deadline) {
    try {
        $response = Invoke-RestMethod -Uri $endpoint -Method Get -TimeoutSec 5
        $lastResponse = $response

        if ($response.success -eq $true -and $null -ne $response.data) {
            [pscustomobject]@{
                Success = $true
                Endpoint = $endpoint
                Server = $response.data.server
                Version = $response.data.version
                McpApiVersion = $response.data.mcpApiVersion
                OsName = $response.data.osName
                OsVersion = $response.data.osVersion
            } | ConvertTo-Json -Depth 5
            exit 0
        }

        $lastError = "Endpoint responded, but success was not true. Response: $($response | ConvertTo-Json -Depth 5 -Compress)"
    } catch {
        $lastError = $_.Exception.Message
    }

    Start-Sleep -Seconds $IntervalSeconds
}

$diagnostic = [ordered]@{
    Success = $false
    Endpoint = $endpoint
    TimeoutSeconds = $TimeoutSeconds
    LastError = $lastError
}

if ($lastResponse) {
    $diagnostic.LastResponse = $lastResponse
}

$diagnostic | ConvertTo-Json -Depth 6
exit 1
