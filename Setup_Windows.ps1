# Crear el entorno virtual en el directorio actual
$venvPath = ".\venv"
python -m venv $venvPath

Write-Host "Entorno virtual creado en $venvPath"
Write-Host "Para activarlo, ejecuta:"
Write-Host ".\$venvPath\Scripts\Activate"