import time
import logging
import allure
from allure_commons.types import AttachmentType


class ResultsPage:
    """Represents search results page."""

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.results_page_title = 'Search Results'
        self.hotels_names_css = 'h4.list_title b'
        self.hotels_prices_css = 'table.table-striped div.price_tab b'

    @allure.step("veryfy search page title")
    def verify_results_page_title(self):
        self.logger.info("Verifying page title")
        assert self.driver.title == self.results_page_title

    @allure.step("assert if hotel was found: '{1}'")
    def check_if_expected_hotel_was_found(self, expected_hotel):
        self.logger.info(f"Verifying if expected hotel was found: {expected_hotel}")
        hotels_names_list_objects = self.driver.find_elements_by_css_selector(self.hotels_names_css)
        time.sleep(2)  # there is sleep here because of random refresh on page that can happen for results
        hotel_names_list_string = [i.text for i in hotels_names_list_objects]
        allure.attach(self.driver.get_screenshot_as_png(), name='hotels found', attachment_type=AttachmentType.PNG)
        self.logger.info(f"Hotels found {hotel_names_list_string}")
        assert expected_hotel in hotel_names_list_string, 'Error - expected hotel was not found in results'

    @allure.step("get hotels prives list")
    def get_hotels_prices_list(self):
        hotels_prices_list_objects = self.driver.find_elements_by_css_selector(self.hotels_prices_css)
        hotels_prices_list_string = [i.text for i in hotels_prices_list_objects]
        self.logger.info(f"Prices of hotels: {hotels_prices_list_string}")
        return hotels_prices_list_string
