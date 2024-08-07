import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_slow_calculator(browser):
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    browser.get(url)
    wait = WebDriverWait(browser, 50)

    delay_field = wait.until(EC.presence_of_element_located((By.ID, "delay")))
    delay_field.clear()
    delay_field.send_keys("45")

    buttons = ["7", "+", "8", "="]
    for button in buttons:
        wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{button}']"))).click()

    result = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
    assert result, "The result is not 15"

if __name__ == "__main__":
    pytest.main()