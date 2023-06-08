from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from logs.logger import logger
from configs import config

# create a class for the page
class LoginPage(BasePage):

    # class attributes
    email_field = By.CSS_SELECTOR, "[type='email']"
    password_field = By.CSS_SELECTOR, "[type='password']"
    submit_button = By.CSS_SELECTOR, "[type='submit']"

    # create a method that performs login
    def login(self, username, password):
        self.driver.find_element(*self.email_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        logger.info(f'Entered username={username} and password={password}')
        self.driver.find_element(*self.submit_button).click()
        logger.info('Clicked on Sign In button')
    
    def user_login(self):
        self.login(config.USER, config.USER_PASSWORD)
    

    def admin_login(self):
        self.login(config.ADMIN, config.ADMIN_PASSWORD)