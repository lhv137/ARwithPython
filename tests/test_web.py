
import pytest
from pages.login_page import LoginPage
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from pages import *

@pytest.fixture

def browser():

    driver = Chrome(executable_path= r"C:\Users\PC\Desktop\Document\Driver\chromedriver.exe")

    driver.implicitly_wait(10)

    yield driver
    
    # driver.quit()

# def test_get_title(browser):

#     login_page = LoginPage(browser)

#     browser.set_window_size(1024, 768)

#     login_page.load()

#     sleep(10)

#     browser.get_screenshot_as_file(r"C:\Users\PC\Desktop\Document\ARwithPython\pictures\screenshot1.png")

#     assert 'Google' == browser.title


# def test_input_blank(browser):

#     name = ''

#     login_page = LoginPage(browser)

#     browser.set_window_size(1024, 768)

#     login_page.load()

#     login_page.set_store_name(name)

#     sleep(5)

#     get_msg = login_page.err_msg()

#     browser.get_screenshot_as_file(r"C:\Users\PC\Desktop\Document\ARwithPython\pictures\screenshot2.png")

#     sleep(5)

#     # print('Message Err:',get_msg)

#     assert 'Please enter your Store Name' == get_msg, "Message Failed"


# def test_input_fail(browser):

#     name = 'vile'

#     login_page = LoginPage(browser)

#     # browser.set_window_size(1024, 768)

#     browser.maximize_window()

#     login_page.load()

#     login_page.set_store_name(name)

#     get_msg = login_page.not_found_msg()

#     browser.get_screenshot_as_file(r"C:\Users\PC\Desktop\Document\ARwithPython\pictures\screenshot3.png")
   
#     sleep(5)

#     print('Message:', get_msg)

#     print("Title:", browser.title)

#     assert 'Create an Ecommerce Website and Sell Online! Ecommerce Software by Shopify' == browser.title, "Title Failed"
   
#     sleep(5)

#     assert 'Sorry, this shop is currently unavailable.' == get_msg, "Message Failed"

#     browser.close()

def test_input_pass(browser):

    name = 'vileh-store'
    email = 'hoangvidct1@gmail.com'
    password = 'vole132465798'

    login_page = LoginPage(browser)

    # browser.set_window_size(1024, 768)

    browser.maximize_window()

    login_page.load()

    login_page.set_store_name(name)

    # login_page.reload()

    sleep(5)

    email = browser.find_element_by_xpath('//*[@id="account_email"]')
    email.send_keys('aszxc')

    email.send_keys('123')

    email.send_keys('cvbn')


    # login_page.fill_email(email)

    # browser.get_screenshot_as_file(r"C:\Users\PC\Desktop\Document\ARwithPython\pictures\screenshot4.png")
   
    # sleep(5)

    # print("Title:", browser.title)

    # assert 'Create an Ecommerce Website and Sell Online! Ecommerce Software by Shopify' == browser.title, "Title Failed"
   
    # sleep(5)

    browser.close()
