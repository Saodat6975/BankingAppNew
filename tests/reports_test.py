from selenium import webdriver
from selenium.webdriver.common.by import By
from logs.logger import logger
from time import sleep
import pytest

from pages.LoginPage import LoginPage
from pages.RemportsPage import ReportsPage
from pages.BasePage import BasePage

account_numbers = ['EBQ11113487654', 'EBQ11223487456', 'EBQ11223387654', 'EBQ38495629375', '511264340']

# create test cases
@pytest.mark.parametrize("account_number", account_numbers)
def test_account_selection_in_reports_menu(driver, account_number):
    login_page = LoginPage(driver)
    login_page.user_login()
    sleep(5)
    reports_page = ReportsPage(driver)
    reports_page.select_reports_menu()
    sleep(5)
    account_selection = ReportsPage(driver)
    account_selection.select_accounts_in_reports_menu(account_number)


    displayed_account_number = driver.find_element(By.CSS_SELECTOR, "div .ng-value-container > .select-value").text
    assert displayed_account_number == account_number


def test_all_account_transactions(driver):
    login_page = LoginPage(driver)
    login_page.user_login()
    sleep(5)
    reports_page = ReportsPage(driver)
    reports_page.select_reports_menu()
    all_accounts_transactions_page = ReportsPage(driver)
    all_accounts_transactions_page.verify_all_account_transaction()
    login_page = LoginPage(driver)
    assert login_page.text_exists('Log Out')
