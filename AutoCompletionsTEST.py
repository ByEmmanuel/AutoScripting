from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import sys
import platform
import subprocess
import time


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


# Configura el WebDriver
options = webdriver.ChromeOptions()   
options.add_argument("--start-maximized")  # Inicia el navegador en pantalla completa

service = webdriver.chrome.service.Service('chromedriver-mac-arm64/chromedriver')  # Path del `chromedriver`

# Inicializa el controlador Chrome con el servicio y las opciones
driver = webdriver.Chrome(service=service, options=options)

moduloUsuario = int(input("¿En Que modulo estas actualmente?"))
paginasUsuario = int(input("Cuantas paginas quieres recorrer?\n 48 Paginas Aprox por modulo"))
velocidadUsuario = int(input("¿Cada cuantos segundos quieres que se cambie de pagina?\n"))

# Abre la página de inicio de sesión
driver.get("https://problemasglobales.udg.mx/login/index.php")

# Alerta para indicar al usuario que inicie sesión manualmente
driver.execute_script("alert('Por favor, inicia sesión manualmente. Tienes 2 minutos para hacerlo');")
time.sleep(30)  # Pausa para que el usuario vea la alerta

# Alerta para indicar al usuario que ingrese el módulo donde quiere ir

# modulo = driver.execute_script("""
#     var modulo = prompt('Ingresa el módulo (número de página) donde deseas ir:', '');
#     console.log(modulo);  // Agregar un log para depuración
#     return modulo;
# """)
# time.sleep(3)  # Pausa para esperar que el usuario ingrese el valor

# Verifica si el valor es válido
# if modulo is not None and modulo.strip():  # Verifica que no esté vacío
#     if modulo.isdigit():  # Verifica si el valor es un número
#         modulo = int(modulo)
#         print(f"Redirigiendo a la página {modulo}")
#     else:
#         print("Entrada no válida. El valor ingresado no es un número.")
# else:
#     print("Entrada vacía o cancelada por el usuario.")

# Espera a que la página cargue después de la redirección
#time.sleep(5)


# Espera a que la página principal cargue tras el login exitoso
WebDriverWait(driver, 180).until(
    EC.url_contains("https://problemasglobales.udg.mx/my/courses.php")  # URL de la página post-login
)

driver.get(f"https://problemasglobales.udg.mx/course/view.php?id=2&section={moduloUsuario}#tabs-tree-start")
# Encuentra todos los botones "Bienvenida" en la página
bienvenida_link = driver.find_element(By.XPATH, ".//a[span[contains(text(), 'Bienvenida')]]")
bienvenida_link.click()
print(f"Clic en el botón de Bienvenida del módulo {moduloUsuario}")

 

# Bucle para hacer clic en los botones "Continuar" en la página de lectura
# Intentar hacer clic en el botón durante 10 veces
for i in range(paginasUsuario):
    try:
        # Espera a que el botón "Continuar" esté clickeable
        continuar_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "next-activity-link"))
        )
        
        # Hacer clic en el botón
        continuar_button.click()
        print(f"Botón 'Continuar' presionado {i + 1} veces")

        # Esperar que la página cargue después del clic
        time.sleep(velocidadUsuario)  # Esto es opcional si no se necesita esperar para la siguiente iteración.

        # Opcional: Esperar que la página cambie antes de intentar hacer clic nuevamente
        WebDriverWait(driver, 10).until(EC.staleness_of(continuar_button))
        
    except Exception as e:
        print(f"No se pudo continuar a la siguiente página en la iteración {i + 1}: {e}")
        break  # Si ocurre un error, romper el bucle

# Busca el botón con ID dentro de su estructura
perfil = driver.find_element(By.XPATH, "//div//a[@id='action-menu-toggle-0']")
perfil.click()

# Espera a que el menú desplegable aparezca

logout = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[text()='Salir']"))
)
logout.click()

time.sleep(5)  # Pausa para que el menú se despliegue correctamente

#driver.execute_script("alert('Concluido correctamente. Por favor, cierra sesión manualmente. Tienes 2 minutos para hacerlo');")


# Cierra el navegador al finalizar
driver.quit()