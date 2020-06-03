from utilities.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class FindOwnersPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _find_owners_link = "//a[@title='find owners']"
    _last_name_field = "lastName"
    _find_owner_button = "//button[@type='submit']"

    def click_find_owners_link(self):
        self.element_click(self._find_owners_link, locator_type="xpath")

    def enter_last_name(self, last_name):
        self.send_keys(last_name, self._last_name_field)

    def click_owner_button(self):
        self.element_click(self._find_owner_button, locator_type="xpath")

    def find_by_last_name(self, last_name):
        self.click_find_owners_link()
        self.enter_last_name(last_name)
        self.click_owner_button()


