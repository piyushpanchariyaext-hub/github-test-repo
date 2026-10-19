<#
Pushes this fixture repo to a GitHub repository for testing the governance
cockpit's GitHub repo-scan connector.

Prerequisites:
  1. Create an EMPTY repo on GitHub (no README/.gitignore), e.g. acp-test-agents.
  2. Have a Personal Access Token (classic: 'repo' scope, or fine-grained:
     Contents read/write) — the same kind of token the connector uses.

Usage (run from this directory):
  .\push-to-github.ps1 -Owner <your-user-or-org> -Repo acp-test-agents -Token ghp_xxx

The token is only used for this one push and is never written to disk.
#>
param(
    [Parameter(Mandatory = $true)][string]$Owner,
    [string]$Repo = "acp-test-agents",
    [Parameter(Mandatory = $true)][string]$Token,
    [string]$Branch = "main"
)

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

if (-not (Test-Path ".git")) {
    git init
    git branch -M $Branch
}

git add -A
git commit -m "Fixture: monorepo of six discoverable agents for connector testing"

$remoteUrl = "https://$Token@github.com/$Owner/$Repo.git"
if (git remote | Select-String -Quiet '^origin$') {
    git remote set-url origin $remoteUrl
} else {
    git remote add origin $remoteUrl
}

git push -u origin $Branch

# Scrub the token out of the stored remote URL.
git remote set-url origin "https://github.com/$Owner/$Repo.git"

Write-Host ""
Write-Host "Pushed to https://github.com/$Owner/$Repo" -ForegroundColor Green
Write-Host "Point the connector at org/user '$Owner' (or repo '$Owner/$Repo')." -ForegroundColor Green
