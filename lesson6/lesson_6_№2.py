from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 40)

try:
    driver.get("http://uitestingplayground.com/textinput")
    
    input_field = wait.until(EC.presence_of_element_located((By.ID, "newButtonName")))
    input_field.send_keys("SkyPro")
    
    button = wait.until(EC.element_to_be_clickable((By.ID, "updatingButton")))
    button.click()
    
    new_button_name = wait.until(EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro"))
    print(button.text)

except Exception as ex:
    print(ex)
finally:
    driver.quit()
