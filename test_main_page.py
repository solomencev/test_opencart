import time

from selenium import webdriver

def test_login():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get('https://demo.opencart.com/index.php?route=account/login')
    email = browser.find_element_by_xpath('//*[@id="input-email"]').send_keys('exjfizhh@firste.ml')
    password = browser.find_element_by_xpath('//*[@id="input-password"]').send_keys('admin')
    submit = browser.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/form/input').click()

    print(None)
