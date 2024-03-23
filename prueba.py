from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuración del navegador Brave
brave_path = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'
options = webdriver.ChromeOptions()
options.binary_location = brave_path

# Inicializar el navegador Brave
driver = webdriver.Chrome(options=options)

# Navegar a la URL proporcionada
driver.get('https://timenet-wcp.gpisoftware.com/login/cd9f81e0-7137-4feb-9054-2a4a371fb2eb')

# Esperar a que el campo de entrada esté presente y sea interactuable
campo_input = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'form-control'))
)

# Ingresar el número 7991 en el campo de entrada
campo_input.send_keys('7991')

# Esperar a que el botón "Entrar" sea visible e interactuable
boton_entrar = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'gpi-button.btn-primary'))
)
boton_entrar.click()

# Pausa el script para que puedas ver el resultado
input("Presiona Enter para salir...")

# Cierra el navegador al finalizar
driver.quit()
