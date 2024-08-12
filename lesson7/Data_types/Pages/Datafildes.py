from selenium.webdriver.common.by import By

class DataFild:
    def __init__(self, browser):
        self.browser = browser

    def find_fields(self):
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
    
    def get_class(self, field_name):
        locator = self.fields[field_name]
        return self.browser.find_element(*locator).get_attribute("class")