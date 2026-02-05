# Push TCO Simulator to GitHub and optionally open Pages settings
# Run from project folder. Requires: Git installed, GitHub repo "TCO_Simulator" created under your account.

$ErrorActionPreference = "Stop"
$git = "C:\Program Files\Git\cmd\git.exe"
$repoRoot = "d:\03. Projects\TCO_Simulator"

Set-Location $repoRoot

# Ensure global git user is set (required for push)
$name = & $git config --global user.name 2>$null
$email = & $git config --global user.email 2>$null
if (-not $name -or -not $email) {
    Write-Host "Git needs your name and email for commits." -ForegroundColor Yellow
    $name = Read-Host "Enter your name (e.g. Your Name)"
    $email = Read-Host "Enter your GitHub email"
    & $git config --global user.name $name
    & $git config --global user.email $email
    Write-Host "Saved. Continuing push." -ForegroundColor Green
}

# Remote should already be: https://github.com/yskim/TCO_Simulator.git
$remote = & $git remote get-url origin 2>$null
if (-not $remote) {
    & $git remote add origin "https://github.com/yskim/TCO_Simulator.git"
    Write-Host "Added remote origin." -ForegroundColor Green
}

Write-Host "Pushing to GitHub (browser or login may open for auth)..." -ForegroundColor Cyan
& $git push -u origin main
if ($LASTEXITCODE -eq 0) {
    Write-Host "Done. Enable Pages: Repo -> Settings -> Pages -> Source: main, / (root) -> Save" -ForegroundColor Green
    Write-Host "App URL: https://yskim.github.io/TCO_Simulator/" -ForegroundColor Green
}
