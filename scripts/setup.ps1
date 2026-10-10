# One-time setup in the user's project for Windows.
# Installs Playwright + Chromium into .\motion\node_modules.
param (
    [string]$MotionDir = "./motion"
)

$ErrorActionPreference = "Stop"

New-Item -ItemType Directory -Force -Path "$MotionDir/clips", "$MotionDir/dist", "$MotionDir/out", "$MotionDir/work" | Out-Null

$missing = @()

if (-not (Get-Command node -ErrorAction SilentlyContinue)) {
    $missing += "Node.js (https://nodejs.org)"
}
if (-not (Get-Command ffmpeg -ErrorAction SilentlyContinue)) {
    $missing += "ffmpeg (winget install Gyan.FFmpeg or https://ffmpeg.org)"
}
if (-not (Get-Command python -ErrorAction SilentlyContinue) -and -not (Get-Command py -ErrorAction SilentlyContinue)) {
    $missing += "Python 3.10+ (https://python.org)"
}

if ($missing.Count -gt 0) {
    Write-Error "Missing dependencies: $($missing -join ', ')"
    exit 1
}

# Ensure numpy is installed
try {
    python -c "import numpy" 2>$null
} catch {
    python -m pip install numpy
}

# Install Playwright and Chromium
if (-not (Test-Path "$MotionDir/node_modules/playwright")) {
    Push-Location $MotionDir
    try {
        if (-not (Test-Path "package.json")) {
            Set-Content -Path "package.json" -Value '{"private": true}'
        }
        npm install --silent playwright
        npx playwright install chromium
    } finally {
        Pop-Location
    }
}

Write-Host "Ready! Clips go in $MotionDir/clips, renders in $MotionDir/out."
