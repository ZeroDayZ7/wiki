# tcp-monitor.ps1
# Skrypt monitorujący połączenia TCP na porcie 443 i wyświetl
# Uruchom skrypt:
#   .\tcp-monitor.ps1

while ($true) {
    Clear-Host
    Write-Host "=== Połączenia TCP (port 443) z procesami - $(Get-Date) ===`n"
    netstat -ano | findstr ":443" | ForEach-Object {
        $line = $_
        $procId = ($line -split "\s+")[-1]
        try {
            $proc = (Get-Process -Id $procId -ErrorAction SilentlyContinue).ProcessName
        } catch { $proc = "?" }
        "$line  [$proc]"
    }
    Start-Sleep -Seconds 5
}
