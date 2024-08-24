import pytest
import allure
from selenium import webdriver
from lesson7.Data_types.Pages.Datafildes import DataFild
from lesson7.Data_types.Pages.Mainpage import MainPage

@allure.title("Тест полей формы")
@allure.description("Тест для проверки класса DataFild и правильности заполнения полей формы")
@allure.feature("Форма")
@allure.severity(allure.severity_level.NORMAL)
def test_data_fild(chrome_browser: webdriver.Chrome) -> None:
    """
    Тест на проверку класса DataFild.

    Параметры:
        chrome_browser (webdriver.Chrome): Экземпляр веб-драйвера Chrome.
    """
    with allure.step("Проверка класса DataFild"):
        assert isinstance(DataFild, object)

@allure.title("Тест проверки полей формы и отправки")
@allure.description("Тест для заполнения полей формы и проверки их состояния после отправки")
@allure.feature("Форма")
@allure.severity(allure.severity_level.CRITICAL)
def test_assertion(chrome_browser: webdriver.Chrome) -> None:
    """
    Тест на заполнение полей формы и проверку их состояния после отправки.

    Параметры:
        chrome_browser (webdriver.Chrome): Экземпляр веб-драйвера Chrome.
    """
    with allure.step("Инициализация страницы формы и заполнение полей"):
        main_page = MainPage(chrome_browser)
        main_page.find_fields()
        main_page.filling_in_the_fields()
        main_page.click_submit_button()
    
    with allure.step("Проверка состояния полей формы"):
        data_fild = DataFild(chrome_browser)
        data_fild.find_fields()
        
        assert "success" in data_fild.get_class("first_name")
        assert "success" in data_fild.get_class("last_name")
        assert "success" in data_fild.get_class("address")
        assert "success" in data_fild.get_class("email")
        assert "success" in data_fild.get_class("phone")
        assert "success" in data_fild.get_class("city")
        assert "success" in data_fild.get_class("country")
        assert "success" in data_fild.get_class("job_position")
        assert "success" in data_fild.get_class("company")
        assert "danger" in data_fild.get_class("zip_code")
