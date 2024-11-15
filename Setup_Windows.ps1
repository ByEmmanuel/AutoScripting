# Ruta de instalación de Python
$pythonInstallerUrl = "https://www.python.org/ftp/python/3.10.9/python-3.10.9-amd64.exe" # Cambia a la versión que prefieras
$installerPath = "$env:TEMP\python_installer.exe"

# Descargar el instalador de Python
Invoke-WebRequest -Uri $pythonInstallerUrl -OutFile $installerPath

# Instalar Python en modo silencioso
Start-Process -FilePath $installerPath -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -Wait

# Verificar si Python se instaló correctamente
if (!(Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Python no se instaló correctamente."
    exit 1
} else {
    Write-Host "Python instalado correctamente."
}

# Crear el entorno virtual en el directorio actual
$venvPath = ".\venv"
python -m venv $venvPath

Write-Host "Entorno virtual creado en $venvPath"
Write-Host "Para activarlo, ejecuta:"
Write-Host ".\$venvPath\Scripts\Activate"