$project_dir = $args[0]
$file = $args[1]
$line = $args[2]
$option = $args[3]

conda activate manim

Set-Location $project_dir

$code = Get-Content $file | Select-Object -Index ($line - 1)
$code = $code.trim()

if (-Not $code.StartsWith("class")) {
    Write-Output "Wrong line: $code"
    exit
}

$classStart = $code.IndexOf(" ")
$code = $code.SubString($classStart + 1)
$classEnd = $code.IndexOf("(")
$code = $code.SubString(0, $classEnd)

Write-Output "You select class $code"

python -m manim $file $code $option