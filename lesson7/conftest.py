import pytest
from selenium import webdriver

@pytest.fixture()
def chrome_browser():
    driver = webdriver.Chrome()
    """
    Фикстура для создания и возврата экземпляра веб-драйвера Chrome.

    Эта фикстура запускает браузер Chrome, разворачивает его на полный экран и
    возвращает его для использования в тестах. По завершению тестов браузер закрывается.

    Возвращает:
        webdriver.Chrome: Экземпляр веб-драйвера Chrome.
    """
    driver.maximize_window()
    yield driver
    driver.quit()