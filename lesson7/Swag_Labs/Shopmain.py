from selenium.webdriver.common.by import By
from lesson7.constants import Shop_URL
from selenium.webdriver.remote.webdriver import WebDriver

class ShopmainPage:
    def __init__(self, browser: WebDriver) -> None:
        """
        Инициализация ShopmainPage с экземпляром браузера и открытие URL магазина.

        Параметры:
            browser (WebDriver): Экземпляр WebDriver.
        """
        self.browser = browser
        self.browser.get(Shop_URL)

    def registration_fields(self) -> None:
        """
        Заполнение полей для авторизации пользователя в магазине.
        """
        self.browser.find_element(By.ID, "user-name").send_keys("standard_user")
        self.browser.find_element(By.ID, "password").send_keys("secret_sauce")
        self.browser.find_element(By.ID, "login-button").click()

    def buy_issue(self) -> None:
        """
        Определение локаторов для кнопок добавления товаров в корзину.
        """
        self.Sauce_Labs_Backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.Sauce_Labs_Bolt_Tshirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.Sauce_Labs_Onesie = (By.ID, "add-to-cart-sauce-labs-onesie")

    def click_issue(self) -> None:
        """
        Добавление товаров в корзину.
        """
        self.browser.find_element(*self.Sauce_Labs_Backpack).click()
        self.browser.find_element(*self.Sauce_Labs_Bolt_Tshirt).click()
        self.browser.find_element(*self.Sauce_Labs_Onesie).click()

    def into_container(self) -> None:
        """
        Переход в корзину.
        """
        self.browser.find_element(By.ID, "shopping_cart_container").click()
