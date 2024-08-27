import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
import allure

cookie = {"name": "cookie_policy", "value": "1"}

@allure.title("Тест счетчика книг на сайте Лабиринт")
@allure.description("Тест на добавление книг в корзину и проверку счетчика")
@allure.feature("Лабиринт")
@allure.severity(allure.severity_level.CRITICAL)
def test_card_counter(chrome_browser: webdriver.Chrome) -> None:
    """
    Тест на добавление книг в корзину на сайте Лабиринт и проверку счетчика.

    Параметры:
        chrome_browser (webdriver.Chrome): Экземпляр WebDriver Chrome.
    """
    with allure.step("Открытие сайта Лабиринт"):
        browser = chrome_browser
        browser.get("https://www.labirint.ru/")
        browser.implicitly_wait(4)
        browser.add_cookie(cookie)
    
    with allure.step("Поиск книг по ключевому слову 'python'"):
        browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys('python')
        browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
    
    with allure.step("Добавление всех книг на первой странице в корзину"):
        buy_buttons = browser.find_elements(By.CSS_SELECTOR, "a._btn.btn-tocart.buy-link")
        counter = 0
        for btn in buy_buttons:
            btn.click()
            counter += 1
    
    with allure.step("Переход в корзину и проверка количества товаров"):
        browser.get("https://www.labirint.ru/cart/")
        txt = browser.find_element(By.CSS_SELECTOR, "a[data-event-label='myCart']").find_element(By.CSS_SELECTOR, 'b').text
        assert counter == int(txt)
