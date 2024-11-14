#!/bin/sh

# Verificar si Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "Python no está instalado. Iniciando la instalación..."

    # Detectar el sistema operativo
    if [ "$(uname)" = "Darwin" ]; then
        # Para macOS
        if ! command -v brew &> /dev/null; then
            echo "Homebrew no está instalado. Instalándolo primero..."
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        fi
        echo "Instalando Python con Homebrew..."
        brew install python3
    elif [ "$(uname)" = "Linux" ]; then
        # Para Linux
        echo "Instalando Python en Linux..."
        sudo apt update && sudo apt install -y python3 python3-venv
    else
        echo "Sistema operativo no compatible para instalación automática de Python. Instálalo manualmente."
        exit 1
    fi
else
    echo "Python ya está instalado."
fi

# Crear un entorno virtual en .venv si no existe
if [ ! -d ".venv" ]; then
    echo "Creando el entorno virtual en '.venv'..."
    python3 -m venv .venv
    echo "Entorno virtual creado en '.venv'."
else
    echo "El entorno virtual ya existe en '.venv'."
fi

# Instrucción para activar el entorno virtual
echo "Para activar el entorno virtual, usa el siguiente comando:"
echo "source .venv/bin/activate"  # Compatible con macOS y Linux