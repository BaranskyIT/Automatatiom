import pytest
from selenium import webdriver
from lesson7.Calculator.Calmainpage import CalcMain
import allure

@allure.title("Тест результата калькулятора")
@allure.description("Тест для проверки правильности результата калькулятора после операций")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator_assert(chrome_browser: webdriver.Chrome) -> None:
    """
    Тест на проверку правильности результата калькулятора после выполнения операций.

    Параметры:
        chrome_browser (webdriver.Chrome): Экземпляр WebDriver Chrome.
    """
    with allure.step("Инициализация страницы калькулятора"):
        calcmain = CalcMain(chrome_browser)
    
    with allure.step("Установка времени задержки"):
        calcmain.insert_time()
    
    with allure.step("Выполнение арифметической операции"):
        calcmain.clicking_buttons()
    
    with allure.step("Ожидание и получение результата"):
        result = calcmain.wait_button_gettext()
    
    with allure.step("Проверка результата"):
        assert "15" in result, f"Ожидалось '15', но получено '{result}'"
