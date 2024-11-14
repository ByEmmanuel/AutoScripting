from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configura el WebDriver
options = webdriver.ChromeOptions()   
options.add_argument("--start-maximized")  # Inicia el navegador en pantalla completa
service = webdriver.chrome.service.Service('chromedriver-mac-arm64/chromedriver')  # Path del `chromedriver`

# Inicializa el controlador Chrome con el servicio y las opciones
driver = webdriver.Chrome(service=service, options=options)

moduloUsuario = int(input("¿En Que modulo estas actualmente?"))

# Abre la página de inicio de sesión
driver.get("https://problemasglobales.udg.mx/login/index.php")

# Alerta para indicar al usuario que inicie sesión manualmente
driver.execute_script("alert('Por favor, inicia sesión manualmente. Tienes 2 minutos para hacerlo');")
time.sleep(30)  # Pausa para que el usuario vea la alerta

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

for i in range(10):
    try:
        # Espera a que el botón "Continuar" esté clickeable
        continuar_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "next-activity-link"))
        )
        
        # Hacer clic en el botón
        continuar_button.click()
        print(f"Botón 'Continuar' presionado {i + 1} veces")

        # Esperar que la página cargue después del clic
        time.sleep(2)  # Esto es opcional si no se necesita esperar para la siguiente iteración.

        # Opcional: Esperar que la página cambie antes de intentar hacer clic nuevamente
        WebDriverWait(driver, 10).until(EC.staleness_of(continuar_button))
        
    except Exception as e:
        print(f"No se pudo continuar a la siguiente página en la iteración {i + 1}: {e}")
        break  # Si ocurre un error, romper el bucle

# Cierra el navegador al finalizar
driver.quit()