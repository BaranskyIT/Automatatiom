from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time


chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

firefox_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

def input_text(driver):
    try:
        driver.get("http://the-internet.herokuapp.com/inputs")
        time.sleep(2)
        input_field = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')
        input_field.send_keys("1000")
        print("Введен текст: 1000")
        time.sleep(1)
        input_field.clear()
        print("Поле очищено")
        time.sleep(1)
        input_field.send_keys("999")
        print("Введен текст: 999")
        time.sleep(1)
    except Exception as e:
        print("Ошибка:", e)

input_text(chrome_driver)

input_text(firefox_driver)

chrome_driver.quit()
firefox_driver.quit()
