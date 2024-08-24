# import sys
# import os
# import pytest
# from selenium import webdriver

# # Добавление корневой директории проекта в sys.path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# from lesson7.Swag_Labs.Shopmain import ShopmainPage
# from lesson7.Swag_Labs.Shopcontainer import ShopContainer

# # @pytest.fixture
# # def chrome_browser():
# #     driver = webdriver.Chrome()
# #     yield driver
# #     driver.quit()
# def test_shop(chrome_browser):
#     expected_total = "58.29"

#     shopmain = ShopmainPage(chrome_browser)
#     shopmain.registration_fields()
#     shopmain.buy_issue()
#     shopmain.click_issue()
#     shopmain.into_container()

#     container = ShopContainer(chrome_browser)
#     container.checkout()
#     container.info()
#     container.price()
        
#     assert expected_total in container.price()
#     print(f"Итоговая сумма равна ${container.price()}")

import pytest
from selenium import webdriver
from lesson7.Swag_Labs.Shopmain import ShopmainPage
from lesson7.Swag_Labs.Shopcontainer import ShopContainer
import allure

@allure.title("Тест проверки итоговой цены после покупки")
@allure.description("Тест для проверки правильности итоговой цены после покупки товаров в магазине")
@allure.feature("Магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(chrome_browser: webdriver.Chrome) -> None:
    """
    Тест на проверку итоговой цены после покупки товаров в магазине.

    Параметры:
        chrome_browser (webdriver.Chrome): Экземпляр WebDriver Chrome.
    """
    expected_total = "58.29"

    with allure.step("Авторизация и добавление товаров в корзину"):
        shopmain = ShopmainPage(chrome_browser)
        shopmain.registration_fields()
        shopmain.buy_issue()
        shopmain.click_issue()
        shopmain.into_container()

    with allure.step("Оформление заказа и получение итоговой цены"):
        container = ShopContainer(chrome_browser)
        container.checkout()
        container.info()
        actual_price = container.price()

    with allure.step("Проверка итоговой цены"):
        assert expected_total in actual_price, f"Ожидаемая сумма '{expected_total}' не совпадает с фактической '{actual_price}'"
        print(f"Итоговая сумма равна ${actual_price}")
