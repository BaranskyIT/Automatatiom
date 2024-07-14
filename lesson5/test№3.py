from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

firefox_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

def click_button(driver):
    try:
        driver.get("http://uitestingplayground.com/classattr")
        button = driver.find_element(By.CLASS_NAME, "btn-primary")
        button.click()
        print("Клик по кнопке выполнен")
        alert = Alert(driver)
        alert.accept()
        print("Всплывающее окно закрыто")
    except Exception as e:
        print("Ошибка:", e)

for _ in range(3):
    click_button(chrome_driver)
    time.sleep(1)

for _ in range(3):
    click_button(firefox_driver)
    time.sleep(1)

chrome_driver.quit()
firefox_driver.quit()
