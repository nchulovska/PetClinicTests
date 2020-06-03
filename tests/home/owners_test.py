import unittest
import pytest
from pages.home.add_owners_page import AddOwnersPage
from pages.home.find_owners_page import FindOwnersPage


class TestsOwners(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, driver):
        self.driver = driver
        self.findOwners = FindOwnersPage(driver)
        self.addOwners = AddOwnersPage(driver)

    def test_find_owner_by_last_name(self):
        """
        Test Case 3: Find concrete owner through search field
        """
        self.findOwners.find_by_last_name("Davis")
        # Owner information window is displayed.
        assert self.findOwners.is_element_present("vets", locator_type="id")
        # Owner with given last name is found.
        assert "Davis" in self.driver.page_source

    def test_add_owner(self):
        """
        Test Case 2: Add new owner
        """
        self.addOwners.add_new_owner("Ola", "Clock", "street", "Krakow", "12345")
        # Owner information window is displayed.
        assert "Owner Information" in self.driver.page_source
        # Provided owner's data is present.
        assert "Ola" and "Clock" and "street" and "Krakow" and "12345" in self.driver.page_source





