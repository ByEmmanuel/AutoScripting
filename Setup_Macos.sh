#!/bin/sh

# Verificar si Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "Python no está instalado. Procediendo con la instalación..."

    # Detectar el sistema operativo
    if [ "$(uname)" = "Darwin" ]; then
        # macOS
        if ! command -v brew &> /dev/null; then
            echo "Homebrew no está instalado. Instalándolo primero..."
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        fi
        brew install python3
    elif [ "$(uname)" = "Linux" ]; then
        # Linux
        sudo apt update
        sudo apt install -y python3 python3-venv
    else
        echo "Sistema operativo no compatible para la instalación automática de Python."
        exit 1
    fi
else
    echo "Python ya está instalado."
fi

# Crear un entorno virtual
if [ ! -d "venv" ]; then
    echo "Creando el entorno virtual en el directorio actual..."
    python3 -m venv venv
    echo "Entorno virtual creado en la carpeta 'venv'."
else
    echo "El entorno virtual ya existe."
fi

# Activar el entorno virtual
echo "Para activar el entorno virtual, usa el siguiente comando:"
echo "source venv/bin/activate"  # Para macOS y Linux