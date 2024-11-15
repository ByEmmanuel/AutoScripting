# Verificar si Python está instalado
if (!(Get-Command python3 -ErrorAction SilentlyContinue)) {
    Write-Host "Python no está instalado. Iniciando la instalación..."

    # Detectar el sistema operativo
    $os = $PSVersionTable.OS
    if ($os -match "Darwin") {
        # Para macOS
        if (!(Get-Command brew -ErrorAction SilentlyContinue)) {
            Write-Host "Homebrew no está instalado. Instalándolo primero..."
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        }
        Write-Host "Instalando Python con Homebrew..."
        brew install python3
    }
    elseif ($os -match "Linux") {
        # Para Linux
        Write-Host "Instalando Python en Linux..."
        sudo apt update
        sudo apt install -y python3 python3-venv
    }
    elseif ($os -match "Windows") {
        # Para Windows
        $pythonInstallerUrl = "https://www.python.org/ftp/python/3.10.9/python-3.10.9-amd64.exe"
        $installerPath = "$env:TEMP\python_installer.exe"
        
        Write-Host "Descargando el instalador de Python..."
        Invoke-WebRequest -Uri $pythonInstallerUrl -OutFile $installerPath
        Write-Host "Instalando Python..."
        Start-Process -FilePath $installerPath -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -Wait
    }
    else {
        Write-Host "Sistema operativo no compatible para instalación automática de Python. Instálalo manualmente."
        exit 1
    }
}
else {
    Write-Host "Python ya está instalado."
}

# Crear un entorno virtual en .venv si no existe
$venvPath = ".\.venv"
if (!(Test-Path $venvPath)) {
    Write-Host "Creando el entorno virtual en '.venv'..."
    python3 -m venv $venvPath
    Write-Host "Entorno virtual creado en '.venv'."
} else {
    Write-Host "El entorno virtual ya existe en '.venv'."
}

# Instrucción para activar el entorno virtual
if ($os -match "Windows") {
    Write-Host "Para activar el entorno virtual, usa el siguiente comando:"
    Write-Host ".\.venv\Scripts\Activate"
} else {
    Write-Host "Para activar el entorno virtual, usa el siguiente comando:"
    Write-Host "source .venv/bin/activate"
}