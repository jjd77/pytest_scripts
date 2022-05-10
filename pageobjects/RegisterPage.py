import logging
import allure
import time
from allure_commons.types import AttachmentType


class RegisterPage:
    """Represents Register new user form page."""

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.results_page_title = 'Register'
        self.name_input_field_name = "firstname"
        self.last_name_input_field_name = "lastname"
        self.phone_input_field_name = "phone"
        self.mail_input_field_name = "email"
        self.sign_up_button_css = "button.signupbtn "
        self.alert_validations_section_css = "div.alert p"
        self.password_input_field_name = "password"
        self.password_confirm_input_field_name = "confirmpassword"
        self.top_nav_my_account_button_

    @allure.step("veryfy page title")
    def verify_register_page_title(self):
        self.logger.info("Verifying page title")
        assert self.driver.title == self.results_page_title

    @allure.step("Input name on sign up page")
    def input_name(self, name):
        self.driver.find_element_by_name(self.name_input_field_name).send_keys(name)
        self.logger.info(f"Name input on the sign up page: {name}")

    @allure.step("Input last name on sign up page")
    def input_last_name(self, surname):
        self.driver.find_element_by_name(self.last_name_input_field_name).send_keys(surname)
        self.logger.info(f"Surname input on the sign up page: {surname}")

    @allure.step("Input phone number on sign up page")
    def input_phone_number(self, number):
        self.driver.find_element_by_name(self.phone_input_field_name).send_keys(number)
        self.logger.info(f"Phone number input on the sign up page: {number}")

    @allure.step("Input email on sign up page")
    def input_email_address(self, mail):
        self.driver.find_element_by_name(self.mail_input_field_name).clear()
        self.driver.find_element_by_name(self.mail_input_field_name).send_keys(mail)
        self.logger.info(f"Mail input on the sign up page: {mail}")

    @allure.step("Set password on sign up page")
    def set_password(self, password):
        self.driver.find_element_by_name(self.password_input_field_name).clear()
        self.driver.find_element_by_name(self.password_input_field_name).send_keys(password)
        self.logger.info(f"Set user passord to: {password}")

    @allure.step("Set password confirmation on sign up page")
    def set_password_confirmation(self, password_conf):
        self.driver.find_element_by_name(self.password_confirm_input_field_name).clear()
        self.driver.find_element_by_name(self.password_confirm_input_field_name).send_keys(password_conf)
        self.logger.info(f"Set passord confirmation to: {password_conf}")

    @allure.step("Click Sign Up button")
    def click_sign_up_button(self):
        self.driver.find_element_by_css_selector(self.sign_up_button_css).click()
        self.logger.info("Click Sign up button")

    @allure.step("Checking specific validation message based on the argument")
    def validation_message_check(self, message):
        time.sleep(1)  # sleep is added because: if element is already present it needs it for a refresh of DOM
        alerts_list2 = self.driver.find_elements_by_css_selector(self.alert_validations_section_css)
        alerts_list_string2 = []
        for i in alerts_list2:
            alerts_list_string2.append(i.text)
            assert message in alerts_list_string2, "Error - validation message not present"

    @allure.step("Checking validation messages")
    def validation_messages_checking(self):
        alerts_list = self.driver.find_elements_by_css_selector(self.alert_validations_section_css)
        alerts_list_string = []
        for i in alerts_list:
            alerts_list_string.append(i.text)
        return alerts_list_string

