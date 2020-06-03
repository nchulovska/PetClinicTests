from utilities.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class AddOwnersPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _find_owners_link = "//a[@title='find owners']"
    _add_owner_button = "//a[@href='/owners/new']"
    _first_name_field = "firstName"
    _last_name_field = "lastName"
    _address_field = "address"
    _city_field = "city"
    _telephone_field = "telephone"
    _submit_button = "//button[@type='submit']"

    def click_find_owners_link(self):
        self.element_click(self._find_owners_link, locator_type="xpath")

    def click_add_owner_button(self):
        self.element_click(self._add_owner_button, locator_type="xpath")

    def enter_first_name(self, first_name):
        self.send_keys(first_name, self._first_name_field)

    def enter_last_name(self, last_name):
        self.send_keys(last_name, self._last_name_field)

    def enter_address(self, address):
        self.send_keys(address, self._address_field)

    def enter_city(self, city):
        self.send_keys(city, self._city_field)

    def enter_telephone(self, telephone):
        self.send_keys(telephone, self._telephone_field)

    def click_submit_button(self):
        self.element_click(self._submit_button, locator_type="xpath")

    def add_new_owner(self, first_name, last_name, address, city, telephone):
        self.click_find_owners_link()
        self.click_add_owner_button()
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_address(address)
        self.enter_city(city)
        self.enter_telephone(telephone)
        self.click_submit_button()

