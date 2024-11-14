# Definir la URL de descarga de Python
$python_url = "https://www.python.org/ftp/python/3.10.5/python-3.10.5.exe"

# Definir la ubicación para descargar el archivo
$download_path = "$env:TEMP\python-installer.exe"

# Descargar Python
Write-Host "Descargando Python desde $python_url..."
Invoke-WebRequest -Uri $python_url -OutFile $download_path

# Instalar Python de manera silenciosa
Write-Host "Instalando Python..."
Start-Process -FilePath $download_path -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -Wait

# Verificar la instalación de Python
Write-Host "Verificando la instalación de Python..."
$python_version = python --version
Write-Host "Python está instalado: $python_version"

# Definir la ruta del archivo Python a ejecutar
$python_file = "C:\ruta\a\tu\archivo\script.py"

# Verificar si el archivo existe
if (Test-Path $python_file) {
    Write-Host "Ejecutando el archivo Python..."
    python $python_file
} else {
    Write-Host "El archivo Python no se encuentra en la ruta especificada: $python_file"
}

# Limpiar archivo descargado
Remove-Item $download_path
Write-Host "Proceso completado."