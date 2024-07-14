from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

def perform_steps(driver):
    driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
    
    add_button = driver.find_element(By.CSS_SELECTOR, 'button[onclick="addElement()"]')
    for _ in range(5):
        add_button.click()
        sleep(1)
    
    delete_buttons = driver.find_elements(By.CSS_SELECTOR, 'button.added-manually[onclick="deleteElement()"]')
    
    print(f"Количество кнопок 'Delete': {len(delete_buttons)}")

driver_chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
try:
    perform_steps(driver_chrome)
finally:
    driver_chrome.quit()

driver_firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
try:
    perform_steps(driver_firefox)
finally:
    driver_firefox.quit()
