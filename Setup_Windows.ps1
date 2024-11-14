# Verificar si Python está instalado
if (!(Get-Command python3 -ErrorAction SilentlyContinue)) {
    Write-Output "Python no está instalado. Procediendo con la instalación..."

    # Instalar Chocolatey si no está disponible
    if (!(Get-Command choco -ErrorAction SilentlyContinue)) {
        Set-ExecutionPolicy Bypass -Scope Process -Force
        [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
        Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
    }

    # Instalar Python usando Chocolatey
    choco install python -y
} else {
    Write-Output "Python ya está instalado."
}

# Crear el entorno virtual en el directorio actual
if (!(Test-Path "venv")) {
    Write-Output "Creando el entorno virtual en el directorio actual..."
    python -m venv venv
    Write-Output "Entorno virtual creado en la carpeta 'venv'."
} else {
    Write-Output "El entorno virtual ya existe."
}

# Instrucción para activar el entorno virtual
Write-Output "Para activar el entorno virtual, usa el siguiente comando:"
Write-Output ".\venv\Scripts\Activate"  # Activar en Windows