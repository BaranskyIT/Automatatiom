from time import sleep 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://ya.ru")

sleep(5)

driver.get("https://vk.com")

driver.save_screenshot('./image.png')

driver.get("https://google.com")

# driver.back()
# driver.forward
# driver.refresh

driver.set_window_size(1440, 1024)

sleep(15)