from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 40)

try:
    driver.get("http://uitestingplayground.com/ajax")

    blue_button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()
    text_from_content = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".bg-success"))).text
    
    blue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#ajaxButton")))
    blue_button.click()
    
    text_from_content = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success"))).text
    
    print(text_from_content)

except Exception as ex:
    print(ex)
finally:
    driver.quit()
