from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()   
options.add_argument("--start-maximized")  # Inicia el navegador en pantalla completa

service = webdriver.chrome.service.Service('chromedriver-mac-arm64/chromedriver')  # Path del `chromedriver`

driver = webdriver.Chrome(service=service, options=options)

moduloUsuario = int(input("¿En Que modulo estas actualmente?"))
paginasUsuario = int(input("Cuantas paginas quieres recorrer?\n 48 Paginas Aprox por modulo"))
velocidadUsuario = int(input("¿Cada cuantos segundos quieres que se cambie de pagina?\n"))

driver.get("https://problemasglobales.udg.mx/login/index.php")


driver.execute_script("alert('Por favor, inicia sesión manualmente. Tienes 2 minutos para hacerlo');")
time.sleep(30)  


WebDriverWait(driver, 180).until(
    EC.url_contains("https://problemasglobales.udg.mx/my/courses.php")  # URL de la página post-login
)

driver.get(f"https://problemasglobales.udg.mx/course/view.php?id=2&section={moduloUsuario}#tabs-tree-start")
bienvenida_link = driver.find_element(By.XPATH, ".//a[span[contains(text(), 'Bienvenida')]]")
bienvenida_link.click()
print(f"Clic en el botón de Bienvenida del módulo {moduloUsuario}")

for i in range(paginasUsuario):
    try:

        continuar_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "next-activity-link"))
        )
        
        continuar_button.click()
        print(f"Botón 'Continuar' presionado {i + 1} veces")

        time.sleep(velocidadUsuario)  

        WebDriverWait(driver, 10).until(EC.staleness_of(continuar_button))
        
    except Exception as e:
        print(f"No se pudo continuar a la siguiente página en la iteración {i + 1}: {e}")
        break  

perfil = driver.find_element(By.XPATH, "//div//a[@id='action-menu-toggle-0']")
perfil.click()

logout = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[text()='Salir']"))
)
logout.click()
driver.execute_script("alert('Concluido correctamente.');")

time.sleep(5)



# Cierra el navegador al finalizar
driver.quit()