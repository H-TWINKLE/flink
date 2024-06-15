$ReleaseVersion=Get-Date -Format 'yyyy-MM-dd_HH-mm-ss'
$ReleaseVersion
Add-Content -Path $env:GITHUB_ENV -Value "ReleaseVersion=${ReleaseVersion}"
