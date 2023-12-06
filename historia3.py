from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# Opciones de navegación
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

# Utiliza 'options' directamente en lugar de 'chrome_options'
driver = webdriver.Chrome()
# Maximizar la ventana
driver.maximize_window()
# Inicializamos el navegador
driver.get('https://jeacn2810.github.io/Portafolio/#inicio')
time.sleep(5)

try:
    # Hacer clic en el enlace "SKILLS" utilizando el selector de CSS
    skills_link = driver.find_element(By.CSS_SELECTOR, 'a[href="#skills"]')
    skills_link.click()
    print("Clic en SKILLS exitoso")
except Exception as e:
    print(f"Error al hacer clic en SKILLS: {str(e)}")

# Cerrar el navegador al finalizar
driver.quit()