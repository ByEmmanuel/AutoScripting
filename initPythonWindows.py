import os
import subprocess
import sys

def crearEntornoVirtual():
    # Paso 1: Crear el entorno virtual
    nombre_entorno = "env"
    subprocess.run([sys.executable, "-m", "venv", nombre_entorno])
    subprocess.run(".\env\Scripts\activate", shell=True)

    # Paso 2: Instalar las dependencias desde el archivo requirements.txt
    if os.path.exists("requirements.txt"):
        # Usamos el pip en el entorno virtual para instalar las dependencias
        if os.name == "nt":  # Para Windows
            subprocess.run([os.path.join(nombre_entorno, "Scripts", "pip"), "install", "-r", "requirements.txt"])
        else:  # Para macOS y Linux
            subprocess.run([os.path.join(nombre_entorno, "bin", "pip"), "install", "-r", "requirements.txt"])
    else:
        print("No se encontró el archivo requirements.txt. Por favor, asegúrate de que exista.")

    # Paso 3: Congelar las dependencias instaladas en requirements.txt
    # Usamos subprocess.run con captura de salida para evitar redirección incorrecta con '>'
    if os.name == "nt":  # Para Windows
        result = subprocess.run([os.path.join(nombre_entorno, "Scripts", "pip"), "freeze"], capture_output=True, text=True)
        
    else:  # Para macOS y Linux
        result = subprocess.run([os.path.join(nombre_entorno, "bin", "pip"), "freeze"], capture_output=True, text=True)
    
    # Escribir la salida en requirements.txt
    with open("requirements.txt", "w") as f:
        f.write(result.stdout)

if __name__ == "__main__":
    # Llamamos a la función
    crearEntornoVirtual()