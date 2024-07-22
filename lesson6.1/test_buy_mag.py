import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_purchase(browser):
    wait = WebDriverWait(browser, 10)

    browser.get("https://www.saucedemo.com/")
    time.sleep(2)

    user_name = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    user_name.send_keys("standard_user")

    password = wait.until(EC.presence_of_element_located((By.ID, "password")))
    password.send_keys("secret_sauce")

    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    login_button.click()
    time.sleep(2)

    backpack_button = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
    backpack_button.click()
    time.sleep(1)

    bolt_tshirt_button = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")))
    bolt_tshirt_button.click()
    time.sleep(1)

    onesie_button = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-onesie")))
    onesie_button.click()
    time.sleep(1)

    cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".shopping_cart_link")))
    cart_button.click()
    time.sleep(2)

    checkout_button = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
    checkout_button.click()
    time.sleep(2) 

    first_name = wait.until(EC.presence_of_element_located((By.ID, "first-name")))
    first_name.send_keys("Борис")

    last_name = wait.until(EC.presence_of_element_located((By.ID, "last-name")))
    last_name.send_keys("Барансикй")

    postal_code = wait.until(EC.presence_of_element_located((By.ID, "postal-code")))
    postal_code.send_keys("300541")

    continue_button = wait.until(EC.element_to_be_clickable((By.ID, "continue")))
    continue_button.click()
    time.sleep(2)

    finish_button = wait.until(EC.element_to_be_clickable((By.ID, "finish")))
    finish_button.click()
    time.sleep(2)

    total_label = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".summary_info_label.summary_total_label")))
    total_text = total_label.text

    assert "Total: $58.29" in total_text, f"Expected total to be '$58.29', but got '{total_text}'"

    back_button = wait.until(EC.element_to_be_clickable((By.ID, "back-to-products"))).click

if __name__ == "__main__":
    pytest.main()
