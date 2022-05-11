from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager

from vacations_with_po.pageobjects.LoggedInPage import LoggedInPage
from vacations_with_po.pageobjects.MainPage import MainPage
from vacations_with_po.pageobjects.ResultsPage import ResultsPage
from vacations_with_po.pageobjects.RegisterPage import RegisterPage
import time
import allure
import random


# pytest test_vacations_desktop.py
# pytest --alluredir=C:\development\pytest_scripts\vacations_with_po\report
# allure serve C:\development\pytest_scripts\vacations_with_po\report


class Setup:

    @allure.title("Test setup - get the page, maximize, set driver; teardown.")
    @pytest.fixture(autouse=True)
    def test_setup(self):
        self.driver = webdriver.Chrome("C:/bin/chromedriver.exe")
        self.driver.implicitly_wait(12)
        self.driver.get('http://www.kurs-selenium.pl/')
        self.driver.maximize_window()
        self.driver.get_screenshot_as_png()
        assert self.driver.title == 'PHPTRAVELS | Travel Technology Partner', 'Error - page title was changed'

        yield
        time.sleep(5)
        self.driver.close()


class TestCases(Setup):

    # @pytest.mark.skip
    @allure.title("test_search_results_are_correct")
    @allure.description("Verify searching, validates hotels and prices lists")
    def test_search_results_are_correct(self):
        """This test verifies proper hotel searching based on the city, validates expected hotel and check
        it the hotels list is as long as hotels prices list, aditionally it's validating if the first hotel
        price is correct"""
        search_for_hotel = MainPage(self.driver)
        search_for_hotel.search_for_hotels('Dubai')
        search_for_hotel.select_first_element_on_context_seach()
        search_for_hotel.set_checkin_date_the_first_of_next_month()
        search_for_hotel.set_checkout_date_input('14/08/2023')
        search_for_hotel.set_travellers('2', '3')
        search_for_hotel.search_button_click()
        verify_results = ResultsPage(self.driver)
        verify_results.verify_results_page_title()
        verify_results.check_if_expected_hotel_was_found("Jumeirah Beach Hotel")
        found_hotels_prices = verify_results.get_hotels_prices_list()
        # assert str(found_hotels_prices[0])[1:] == '14.30'

    @allure.title("test user creation")
    @allure.description("test user creation and metadata fields on the form")
    def test_create_new_user(self):
        main_page_navigation = MainPage(self.driver)
        main_page_navigation.select_my_account_menu()
        main_page_navigation.select_sign_up_option()
        sign_up_page = RegisterPage(self.driver)
        sign_up_page.verify_register_page_title()
        sign_up_page.click_sign_up_button()
        validation_errors = sign_up_page.validation_messages_checking()
        expected_validation_msgs = ["The Email field is required.",
                                    "The Password field is required.",
                                    "The Password field is required.",
                                    "The First name field is required.",
                                    "The Last Name field is required."]
        for i in validation_errors:
            assert i in expected_validation_msgs, "Error - validation messages not correct"
        username = "Mariano"
        user_surname = "Italiano"
        sign_up_page.input_name(username)
        sign_up_page.input_last_name(user_surname)
        sign_up_page.input_phone_number("123123123")
        sign_up_page.input_email_address("INVALID-EMAIL.COM")
        sign_up_page.click_sign_up_button()
        sign_up_page.validation_message_check("The Email field must contain a valid email address.")
        valid_email = ("valid" + str(random.randint(0,10000)) + "@mail.com")
        sign_up_page.input_email_address(valid_email)
        sign_up_page.set_password("123")
        sign_up_page.click_sign_up_button()
        sign_up_page.validation_message_check("The Password field must be at least 6 characters in length.")
        proper_password = "Abcd2020!"
        sign_up_page.set_password(proper_password)
        sign_up_page.set_password_confirmation("invalid confirmation of password")
        sign_up_page.click_sign_up_button()
        sign_up_page.validation_message_check("Password not matching with confirm password.")
        sign_up_page.set_password_confirmation(proper_password)
        sign_up_page.click_sign_up_button()
        my_account_page = LoggedInPage(self.driver)
        my_account_page.check_user_header(username, user_surname)
        my_account_page.verify_my_account_page_title()


