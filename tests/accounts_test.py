from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pytest

# importing the LoginPage class from LoginPage file
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from pages.AccountsPage import AccountsPage


account_numbers = ['EBQ11113487654', 'EBQ11223487456', 'EBQ11223387654', 'EBQ38495629375', '511264340']

# create test cases
@pytest.mark.parametrize("account_number", account_numbers)
def test_account_selection(driver, account_number):
    # create an instance/object of LoginPage class
    login_page = LoginPage(driver)
    # call user_login method of the object
    login_page.user_login()
    sleep(5)
    # create an instance of HomePage class
    accounts_page = AccountsPage(driver)
    accounts_page.select_account(account_number)
    
    displayed_account_number = driver.find_element(By.XPATH, "//span[text()='Account number']/following-sibling::span[1]").text
    assert displayed_account_number == account_number
