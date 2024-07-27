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

def test_form_submission(browser):
    url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    browser.get(url)
    wait = WebDriverWait(browser, 10)

    form_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "zip-code": "",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for name, value in form_data.items():
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f'input[name="{name}"]'))).send_keys(value)

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

    zip_code_alert = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#zip-code")))
    assert "alert-danger" in zip_code_alert.get_attribute("class"), "Zip code alert is not highlighted in red"

if __name__ == "__main__":
    pytest.main()