import os
import subprocess
import platform

def crearEntornoVirtual():
    
    sistema = platform.system()
    nombre_carpeta = "chromedriver"

    # Ruta de la carpeta (directorio actual)
    ruta_carpeta = os.path.join(os.getcwd(), nombre_carpeta)

    # Crear la carpeta si no existe
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)
        print(f"Carpeta '{nombre_carpeta}' creada en {ruta_carpeta} para {sistema}.")
    else:
        print(f"La carpeta '{nombre_carpeta}' ya existe en {ruta_carpeta} para {sistema}.")

    

    # Paso 2: Instalar las dependencias desde el archivo requirements.txt
    if os.path.exists("requirements.txt"):
        # Usamos el pip en el entorno virtual para instalar las dependencias
        if os.name == "nt":  # Para Windows
            subprocess.run([os.path.join("venv", "Scripts", "pip"), "install", "-r", "requirements.txt"])
            subprocess.run(".\env\Scripts\activate", shell=True)
        else:  # Para macOS y Linux
            subprocess.run([os.path.join(".venv", "bin", "pip"), "install", "-r", "requirements.txt"])

    else:
        print("No se encontró el archivo requirements.txt. Por favor, asegúrate de que exista.")

    # Paso 3: Congelar las dependencias instaladas en requirements.txt
    # Usamos subprocess.run con captura de salida para evitar redirección incorrecta con '>'
    if os.name == "nt":  # Para Windows
        result = subprocess.run([os.path.join("venv", "Scripts", "pip"), "freeze"], capture_output=True, text=True)
    else:  # Para macOS y Linux
        result = subprocess.run([os.path.join(".venv", "bin", "pip"), "freeze"], capture_output=True, text=True)
    
    # Escribir la salida en requirements.txt
    with open("requirements.txt", "w") as f:
        f.write(result.stdout)

if __name__ == "__main__":
    # Llamamos a la función
    crearEntornoVirtual()