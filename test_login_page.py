import pytest
from selenium import webdriver
from login_page import LoginPage

@pytest.fixture()
def initialize_driver():

        opts=webdriver.ChromeOptions()
        opts.add_experimental_option("detach",True)
        driver=webdriver.Chrome(options=opts)
        url="https://demo.actitime.com/login.do"
        driver.get(url)

        yield driver

        driver.close()

def test_login(initialize_driver):
        driver=initialize_driver

        lp=LoginPage(driver)
        lp.enter_username("admin")
        lp.enter_password("manager")
        lp.click_login_btn()