import os
import sys
import platform
import subprocess


def ejecutar_comando(comando, descripcion):
    print(f"Iniciando: {descripcion}")
    resultado = subprocess.run(comando, shell=True)
    if resultado.returncode != 0:
        print(f"Error al ejecutar: {comando}")
    else:
        print(f"Completado: {descripcion}\n")


def crearEntornoVirtual():
    # Paso 1: Crear el entorno virtual
    nombre_entorno = "env"
    subprocess.run([sys.executable, "-m", "venv", nombre_entorno])

    # Paso 2: Activar el entorno virtual
    if os.name == "nt":  # Para Windows
        activar_entorno = os.path.join(nombre_entorno, "Scripts", "activate.bat")
    else:  # Para macOS y Linux
        activar_entorno = os.path.join(nombre_entorno, "bin", "activate")

    # Activar entorno virtual
    subprocess.run(f"{activar_entorno}", shell=True)

    # Paso 3: Instalar las dependencias desde el archivo requirements.txt
    if os.path.exists("requirements.txt"):
        subprocess.run([os.path.join(nombre_entorno, "bin", "pip"), "install", "-r", "requirements.txt"])
    else:
        print("No se encontró el archivo requirements.txt. Por favor, asegúrate de que exista.")

    # Paso 4: Congelar las dependencias instaladas en requirements.txt
    subprocess.run([os.path.join(nombre_entorno, "bin", "pip"), "freeze", ">", "requirements.txt"])

# Llamamos a la función
crearEntornoVirtual()
