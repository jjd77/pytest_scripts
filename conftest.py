import os
import sys
from selenium import webdriver
import time
import allure
import pytest
from allure_commons.types import AttachmentType


#this fixes the issue I had with Python bug (importing files from higher directories)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@allure.title("Test setup - get the page, maximize, set driver; teardown.")
@pytest.fixture(autouse=True)
def test_setup(request):
    driver = webdriver.Chrome("C:/bin/chromedriver.exe")
    driver.implicitly_wait(12)
    driver.get('http://www.kurs-selenium.pl/')
    driver.maximize_window()
    request.cls.driver = driver
    driver.get_screenshot_as_png()
    assert driver.title == 'PHPTRAVELS | Travel Technology Partner', 'Error - page title was changed'

    yield
    time.sleep(4)
    driver.close()

