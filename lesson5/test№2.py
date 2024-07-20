from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def perform_steps(driver):
    driver.get("http://uitestingplayground.com/dynamicid")
    
    blue_button = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary[type="button"]')
    blue_button.click()
    sleep(1) 

chrome_options = ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors')
for _ in range(3):
    driver_chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    try:
        perform_steps(driver_chrome)
    finally:
        driver_chrome.quit()

firefox_options = FirefoxOptions()
firefox_options.accept_insecure_certs = True
for _ in range(3):
    driver_firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
    try:
        perform_steps(driver_firefox)
    finally:
        driver_firefox.quit()

