from selenium.webdriver.common.by import By
import utilities.custom_logger as cl
import logging


class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        if locator_type == "name":
            return By.NAME
        if locator_type == "xpath":
            return By.XPATH
        if locator_type == "css":
            return By.CSS_SELECTOR
        if locator_type == "class":
            return By.CLASS_NAME
        if locator_type == "link":
            return By.LINK_TEXT
        if locator_type == "partial_link":
            return By.PARTIAL_LINK_TEXT
        else:
            self.log.info("Locator type ", locator_type,
                          "is not supported")
        return False

    def get_element(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info("Element Found with locator: " + locator + " and locatorType: " + locator_type)
        except:
            self.log.info("Element not found with locator: " + locator + " and locatorType: " + locator_type)
        return element

    def element_click(self, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locator_type)
        except:
            self.log.info("Cannot click on the element with locator: " + locator + " locatorType: " + locator_type)

    def send_keys(self, data, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator + " locatorType: " + locator_type)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator + " locatorType: " + locator_type)

    def is_element_present(self, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            if element is not None:
                self.log.info("Element found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def element_presence_check(self, locator, locator_type="id"):
        try:
            element_list = self.driver.find_elements(locator)
            if len(element_list) > 0:
                self.log.info("Element is found")
                return True
            else:
                self.log.info("Element is not found")
                return False
        except:
            self.log.info("element not found")
            return False

    def get_elements(self, locator, locator_type="id"):
        elements_list = []
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            elements_list = self.driver.find_elements(by_type, locator)
            self.log.info("Elements Found with locator: " + locator + " and locatorType: " + locator_type)
        except:
            self.log.info("Elements not found with locator: " + locator + " and locatorType: " + locator_type)
        return elements_list



