from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
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

#prueba
enlace_descarga_cv = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="pdf/CURRICULUM_JULIO_EMANUEL_ALBERTO_CARRILLO_NUÑEZ[1].pdf"]'))
)

# Hacer clic en el enlace de descarga del CV
enlace_descarga_cv.click()

# Cerrar el navegador al finalizar
driver.quit()

