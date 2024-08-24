from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver  
from lesson7.constants import Calculator_URL

class CalcMain:
    def __init__(self, browser: WebDriver) -> None:
        """
        Инициализация CalcMain с экземпляром браузера и открытие URL калькулятора.

        Параметры:
            browser (WebDriver): Экземпляр веб-драйвера.
        """
        self.browser = browser
        self.browser.get(Calculator_URL)

    def insert_time(self) -> None:
        """
        Ввод времени задержки в калькулятор.
        """
        delay_input = self.browser.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(45)

    def clicking_buttons(self) -> None:
        """
        Нажатие на кнопки калькулятора для выполнения арифметической операции.
        """
        self.browser.find_element(By.XPATH, "//span[text() = '7']").click()
        self.browser.find_element(By.XPATH, "//span[text() = '+']").click()
        self.browser.find_element(By.XPATH, "//span[text() = '8']").click()
        self.browser.find_element(By.XPATH, "//span[text() = '=']").click()

    def wait_button_gettext(self) -> str:
        """
        Ожидание появления текста результата на экране калькулятора.

        Возвращает:
            str: Текст результата на экране калькулятора.
        """
        expected_text = "15"
        WebDriverWait(self.browser, 46).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), expected_text))
        return self.browser.find_element(By.CLASS_NAME, "screen").text
