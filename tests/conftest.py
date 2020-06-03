import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def driver():
    url = "https://spring-petclinic-community.herokuapp.com"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(url)
    yield driver
    driver.quit()

