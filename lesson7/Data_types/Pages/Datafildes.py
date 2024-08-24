from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class DataFild:
    def __init__(self, browser: WebDriver) -> None:
        """
        Инициализация DataFild с экземпляром браузера и определение локаторов полей.

        Параметры:
            browser (WebDriver): Экземпляр WebDriver.
        """
        self.browser = browser
        self.find_fields()

    def find_fields(self) -> None:
        """
        Определение локаторов для полей формы.
        """
        self.fields = {
            "first_name": (By.ID, "first-name"),
            "last_name": (By.ID, "last-name"),
            "address": (By.ID, "address"),
            "email": (By.ID, "e-mail"),
            "phone": (By.ID, "phone"),
            "zip_code": (By.ID, "zip-code"),
            "city": (By.ID, "city"),
            "country": (By.ID, "country"),
            "job_position": (By.ID, "job-position"),
            "company": (By.ID, "company")
        }

    def get_class(self, field_name: str) -> str:
        """
        Получение значения атрибута класса поля.

        Параметры:
            field_name (str): Имя поля для получения атрибута класса.

        Возвращает:
            str: Значение атрибута класса поля.
        """
        locator = self.fields[field_name]
        return self.browser.find_element(*locator).get_attribute("class")
