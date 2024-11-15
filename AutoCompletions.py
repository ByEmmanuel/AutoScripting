from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import platform


# Configura el WebDriver
options = webdriver.ChromeOptions()   
options.add_argument("--start-maximized")  # Inicia el navegador en pantalla completa
options.add_argument("--no-sandbox")  # Evita ciertas advertencias
options.add_argument("--disable-dev-shm-usage")  # Evita problemas con recursos
options.add_argument("--disable-infobars")  

sistema = platform.system()

if sistema == "Windows":
    service = webdriver.chrome.service.Service('Chromedriver/chromedriver.exe')      
elif sistema == "Darwin":
    service = webdriver.chrome.service.Service('Chromedriver/chromedriver')  # Path del `chromedriver`    
elif sistema == "Linux":
    service = webdriver.chrome.service.Service('Chromedriver/chromedriver')  # Path del `chromedriver`    
else:
    print("Sistema operativo no identificado.")




# Inicializa el controlador Chrome con el servicio y las opciones
driver = webdriver.Chrome(service=service, options=options)

moduloUsuario = int(input("¿En Que modulo estas actualmente?"))
paginasUsuario = int(input("Cuantas paginas quieres recorrer?\n 48 Paginas Aprox por modulo"))
velocidadUsuario = int(input("¿Cada cuantos segundos quieres que se cambie de pagina?\n"))

driver.get("https://problemasglobales.udg.mx/login/index.php")

driver.execute_script("alert('Por favor, inicia sesión manualmente. Tienes 2 minutos para hacerlo');")
time.sleep(30)  

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


perfil = driver.find_element(By.XPATH, "//div//a[@id='action-menu-toggle-0']")
perfil.click()



logout = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[text()='Salir']"))
)
logout.click()

time.sleep(2)
driver.execute_script("alert('Concluido correctamente.');")
time.sleep(5)



# Cierra el navegador al finalizar
driver.quit()