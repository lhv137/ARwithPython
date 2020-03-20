from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from pages.locators import *


class LoginPage:

    URL = 'https://alireviews.fireapps.io/'
    URL1 = 'https://accounts.shopify.com/lookup?rid=31134437-d967-446e-a981-1b89e8f5c965'

    store_name = (By.XPATH, STORE_NAME_XPATH)
    login_btn = (By.XPATH,LOG_IN_BTN_XPATH)
    msg_fail = (By.XPATH,LOGIN_BLANK_MESSAGE_XPATH)
    msg_not_found = (By.XPATH, LOGIN_FAILED_MESSAGE_XPATH)
    email = (By.XPATH, FILL_EMAIL)
    password = (By.XPATH, FILL_PASS)
    btn_next = (By.XPATH, BTN_NEXT)
    btn_login = (By.XPATH,BTN_LOGIN) 
    
    def __init__(self,browser):
        self.browser = browser
    
    def load(self):
        self.browser.get(self.URL)

    def reload(self):
        self.browser.get(self.URL1)

    def set_store_name(self, name):
        store_name = self.browser.find_element(*self.store_name)
        store_name.send_keys(name)
        store_name = self.browser.find_element(*self.login_btn)
        store_name.click()

    def err_msg(self):
        # get_msg = browser.find_element_by_xpath('//*[@id="shop-error"]').text
        err_msg = self.browser.find_element(*self.msg_fail).text
        return(err_msg)

    def not_found_msg(self):
        # get_msg = browser.find_element_by_xpath('//*[@id="shop-error"]').text
        not_found_msg = self.browser.find_element(*self.msg_not_found).text
        return(not_found_msg)

    def fill_email(self, email):
        email = self.browser.find_element(*self.email)
        email.send_keys(email)
        email = self.browser.find_element(*self.btn_next)
        email.click()

        # password =self.browser.find_elements(*self.password)
        # password.send_keys(password)
        # password = self.browser.find_elements(*self.btn_login)
        # password.click()

    




    
