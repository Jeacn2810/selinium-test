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
enlace_facebook = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="https://www.facebook.com/"]'))
)

# Hacer clic en el enlace de Facebook
enlace_facebook.click()
time.sleep(120)


