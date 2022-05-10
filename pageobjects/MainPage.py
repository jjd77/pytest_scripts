import logging
import allure
from allure_commons.types import AttachmentType


class MainPage:
    """Represents base page."""

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.hotel_or_city_clickable_xpath = "//span[text()='Search by Hotel or City Name']"
        self.hotel_or_city_input_field_css = "div#select2-drop input"
        self.first_city_value_on_a_hover_css = "li.select2-result-selectable"
        self.check_in_date_input_css = "input[name='checkin']"
        self.next_month_button_css = 'th.next'
        self.fist_day_locator_xpath = "//td[@class='day ' and text()='1']"
        self.travellers_locator_name = 'travellers'
        self.travellers_adults_locator_name = 'adults'
        self.travellers_child_locator_name = 'child'
        self.search_button_css = 'div#hotels button.btn-primary'
        self.my_account_menu_css = 'nav.navbar-default li#li_myaccount a.dropdown-toggle'
        self.my_account_manu_sign_up_xpath = "//li[@id='li_myaccount' and @class='open']//a[contains(.,'  Sign Up')]"

    @allure.step("search for hotels by city: '{1}'")
    def search_for_hotels(self, city):
        """Inputs the City or Hotel to the search bar, use it with select_first_element_on_context_search where
        applicable """
        self.driver.find_element_by_xpath(self.hotel_or_city_clickable_xpath).click()
        self.driver.find_element_by_css_selector(self.hotel_or_city_input_field_css).send_keys(city)
        self.logger.info(f"Search for hotel or city value provided: {city}")
        allure.attach(self.driver.get_screenshot_as_png(), name='city search', attachment_type=AttachmentType.PNG)

    @allure.step("select first value from city/hotel search context menu")
    def select_first_element_on_context_seach(self):
        """Clicks the first hotel/city name from the Search bar context menu"""
        self.driver.find_element_by_css_selector(self.first_city_value_on_a_hover_css).click()
        self.logger.info("Selct the first value from the context results")
        allure.attach(self.driver.get_screenshot_as_png(), name='first value selected', attachment_type=AttachmentType.PNG)

    @allure.step("set_checkin_date_the_first_of_next_month")
    def set_checkin_date_the_first_of_next_month(self):
        """Selects the check in date via callendar 1st of next month on the base page search bar"""
        self.driver.find_element_by_css_selector(self.check_in_date_input_css).click()
        list_of_next_elements = self.driver.find_elements_by_css_selector(self.next_month_button_css)
        for i in list_of_next_elements:
            if i.is_displayed():
                i.click()
                break
        self.driver.find_element_by_xpath(self.fist_day_locator_xpath).click()
        allure.attach(self.driver.get_screenshot_as_png(), name='date in 1st of next month', attachment_type=AttachmentType.PNG)
        self.logger.info("Set checkin date to the first day of next month")

    @allure.step("Set checkout date: '{1}'")
    def set_checkout_date_input(self, checkoutdate):
        """Selects the check out date via DD/MM/YYYY on the base page search bar"""
        self.driver.find_element_by_name('checkout').send_keys(checkoutdate)
        allure.attach(self.driver.get_screenshot_as_png(), name='set checkout', attachment_type=AttachmentType.PNG)
        self.logger.info(f"Select check out date: {checkoutdate}")

    @allure.step("Set passengers adults:'{1}' and kids:'{2}'")
    def set_travellers(self, adults, kids):
        """Sets the numeber of adults and kids on the base page search bar"""
        self.driver.find_element_by_name(self.travellers_locator_name).click()
        self.driver.find_element_by_name(self.travellers_adults_locator_name).clear()
        self.driver.find_element_by_name(self.travellers_adults_locator_name).send_keys(adults)
        self.driver.find_element_by_name(self.travellers_child_locator_name).clear()
        self.driver.find_element_by_name(self.travellers_child_locator_name).send_keys(kids)
        allure.attach(self.driver.get_screenshot_as_png(), name='travellers', attachment_type=AttachmentType.PNG)
        self.logger.info(f"Select {adults} adults and {kids} kids")

    @allure.step("Click search button")
    def search_button_click(self):
        """Clicks the search button on the base page search bar"""
        self.driver.find_element_by_css_selector(self.search_button_css).click()
        self.logger.info("Click search button")
        allure.attach(self.driver.get_screenshot_as_png(), name='click search', attachment_type=AttachmentType.PNG)

    @allure.step("select my account menu")
    def select_my_account_menu(self):
        """Clicks the MY ACCOUNT menu on the base page nav bar"""
        self.driver.find_element_by_css_selector(self.my_account_menu_css).click()

    @allure.step("select sign up menu")
    def select_sign_up_option(self):
        """Clicks the Sing Up option from My Account  menu on the base page nav bar"""
        self.driver.find_element_by_xpath(self.my_account_manu_sign_up_xpath).click()

