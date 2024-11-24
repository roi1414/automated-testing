from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get("http://127.0.0.1:5500/web/index.html")  


nombre_input = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "nombre"))
)


time.sleep(3)


correo_input = driver.find_element(By.ID, "correo")
enviar_btn = driver.find_element(By.ID, "enviar")


nombre_input.send_keys("Roi")
correo_input.send_keys("roi@example.com")


enviar_btn.click()


time.sleep(5)


driver.quit()

