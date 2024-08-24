from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver  

class ShopContainer:
    def __init__(self, browser: WebDriver) -> None:
        """
        Инициализация ShopContainer с экземпляром браузера.

        Параметры:
            browser (WebDriver): Экземпляр веб-драйвера.
        """
        self.browser = browser
        self.checkout_locator = (By.ID, "checkout")

    def checkout(self) -> None:
        """
        Переход к оформлению заказа.
        """
        self.browser.find_element(*self.checkout_locator).click()
    
    def info(self) -> None:
        """
        Ввод информации для оформления заказа.
        """
        self.first_name = (By.ID, "first-name")
        self.browser.find_element(*self.first_name).send_keys("Борис")
        self.last_name = (By.ID, "last-name")
        self.browser.find_element(*self.last_name).send_keys("Баранский")
        self.postcode = (By.ID, "postal-code")
        self.browser.find_element(*self.postcode).send_keys("300541")
        self.continue_button = (By.ID, "continue")
        self.browser.find_element(*self.continue_button).click()
    
    def price(self) -> str:
        """
        Получение итоговой цены из страницы оформления заказа.

        Возвращает:
            str: Итоговая цена.
        """
        WebDriverWait(self.browser, 10, 0.1).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".summary_total_label")))
        total_price = self.browser.find_element(By.CSS_SELECTOR, ".summary_total_label")
        total = total_price.text.strip().replace("Total: $", "")
        
        return total
