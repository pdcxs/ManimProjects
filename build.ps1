$project_dir = $args[0]
$file = $args[1]
$line = $args[2]
$option = $args[3]

Invoke-Expression "conda activate manim"

Set-Location $project_dir
$content = Get-Content $file

For ($l = $line; $l -GT 0; $l--) {
    $code = $content | Select-Object -Index ($l - 1)
    If ($Null -EQ $code) {
        Continue
    }
    If ($code.StartsWith("class")) {
        Break
    }
}

If (-Not $code.StartsWith("class")) {
    Write-Output "Cannot Find Class"
    exit
}

$classStart = $code.IndexOf(" ")
$code = $code.SubString($classStart + 1)
$classEnd = $code.IndexOf("(")
$code = $code.SubString(0, $classEnd)

Write-Output "You select class $code"

python -m manim $file $code $option
