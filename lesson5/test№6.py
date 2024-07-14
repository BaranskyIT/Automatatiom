from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time


chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

firefox_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

def login(driver):
    try:
        driver.get("http://the-internet.herokuapp.com/login")
        time.sleep(3)
        username_field = driver.find_element(By.ID, 'username')
        password_field = driver.find_element(By.ID, 'password')
        login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        
        username_field.send_keys("tomsmith")
        print("Введен username: tomsmith")
        time.sleep(2)
        
        password_field.send_keys("SuperSecretPassword!")
        print("Введен password: SuperSecretPassword!")
        time.sleep(2)
        
        login_button.click()
        print("Нажата кнопка Login")
        time.sleep(3)
    except Exception as e:
        print("Ошибка:", e)

login(chrome_driver)

login(firefox_driver)

chrome_driver.quit()
firefox_driver.quit()
