import logging
import allure
import time
from allure_commons.types import AttachmentType


class LoggedInPage:
    """Represents the page/profile for logged in user in the system."""

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.my_account_page_title = "My Account"
        self.user_name_header_css = "h3.RTL"
        self.user_menu_field_xpath = "//nav//div[2]/ul[2]/ul/li[1]/a"
        self.user_menu_logout_field_xpath = "//nav//a[text()='  Logout']"


    @allure.step("veryfy page title")
    def verify_my_account_page_title(self):
        self.logger.info("Verifying page title")
        assert self.driver.title == self.my_account_page_title

    @allure.step("verify user header/invitation")
    def check_user_header(self, name, surname):
        header_text = self.driver.find_element_by_css_selector(self.user_name_header_css)
        header_text_string = header_text.text
        self.logger.info(header_text_string)
        expected_header = ("Hi, " + name + ' ' + surname)
        self.logger.info(expected_header)
        assert header_text_string == expected_header
        self.logger.info("User header on the user profile got the name: " + header_text.text)

    @allure.step("user logout")
    def logout_user(self):
        self.driver.find_element_by_xpath(self.user_menu_field_xpath).click()
        self.driver.find_element_by_xpath(self.user_menu_logout_field_xpath).click()
        assert self.driver.title != self.my_account_page_title



