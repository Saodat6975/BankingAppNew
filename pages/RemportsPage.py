from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from time import sleep
from logs.logger import logger

class ReportsPage(BasePage):

    def select_reports_menu(self):
        self.driver.find_element(By.XPATH, "//label[text()='Reports']").click()
        logger.info('Clicked on Reports menu')
        sleep(5)


    def select_accounts_in_reports_menu(self, account_number):
        
        self.driver.find_element(By.CSS_SELECTOR, "[formcontrolname='account']").click()
        logger.info('Clicked on Account numbers')
        sleep(5)

        self.driver.find_element(By.XPATH, f"//span[text()='{account_number}']").click()
        sleep(5)


    def verify_all_account_transaction(self):
        self.driver.find_element(By.LINK_TEXT, "All Accounts Transactions").click()
        logger.info('Clicked on All Account Transactions')
        sleep(5)