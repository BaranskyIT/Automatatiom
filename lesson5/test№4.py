from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

firefox_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

def close_modal(driver):
    try:
        driver.get("http://the-internet.herokuapp.com/entry_ad")
        time.sleep(2)
        close_button = driver.find_element(By.CSS_SELECTOR, "div.modal-footer > p")
        close_button.click()
        print("Модальное окно закрыто")
    except Exception as e:
        print("Ошибка:", e)

close_modal(chrome_driver)

close_modal(firefox_driver)

chrome_driver.quit()
firefox_driver.quit()
