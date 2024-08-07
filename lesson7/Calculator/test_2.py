import sys
import os
import pytest
from selenium import webdriver

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from lesson7.Calculator.Calmainpage import CalcMain

@pytest.fixture
def chrome_browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_calculator_assert(chrome_browser):
    calcmain = CalcMain(chrome_browser)
    calcmain.insert_time()
    calcmain.clicking_buttons()
    
    result = calcmain.wait_button_gettext()
    assert "15" in result, f"Expected '15' in the result, but got '{result}'"