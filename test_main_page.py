import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select


class test_open_cart(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)


    def open_page(self, wd):
        wd.get('https://demo.opencart.com/index.php?route=account/login')
        # wd.webdriver.Chrome()
        wd.maximize_window()

    def login(self, wd):
        wd.find_element_by_xpath('//*[@id="input-email"]').send_keys('exjfizhh@firste.ml')
        wd.find_element_by_xpath('//*[@id="input-password"]').send_keys('admin')
        wd.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/form/input').click()

    def open_book_contact(self,wd):
        wd.find_element_by_xpath('//*[@id="column-right"]/div/a[4]').click()
        wd.find_element_by_xpath('//*[@id="content"]/div/div[2]/a').click()

    def fill_required_fields(self, wd):
        wd.find_element_by_xpath('//*[@id="input-firstname"]').send_keys('Alexsandr')
        wd.find_element_by_xpath('//*[@id="input-lastname"]').send_keys('Ivanov')
        wd.find_element_by_xpath('//*[@id="input-address-1"]').send_keys('Moscow, Lenina streer, house 8')
        wd.find_element_by_xpath('//*[@id="input-city"]').send_keys('Moscow')
        wd.find_element_by_xpath('//*[@id="input-postcode"]').send_keys(152121)
        select = Select(wd.find_element_by_xpath('//*[@id="input-country"]'))
        select.select_by_value('176')
        time.sleep(1)
        select = Select(wd.find_element_by_xpath('//*[@id="input-zone"]'))
        select.select_by_value('2761')


    def create_contact(self, wd):
        wd.find_element_by_xpath('//*[@id="content"]/form/div/div[2]/input').click()


    def exit_from_profile(self, wd):
        wd.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/a/span[1]').click()
        wd.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/ul/li[5]/a').click()

    def test_add_contacts(self):
        wd = self.wd
        self.open_page(wd)
        self.login(wd)
        self.open_book_contact(wd)
        self.fill_required_fields(wd)
        self.create_contact(wd)
        self.exit_from_profile(wd)

    def tearDown(self):
        self.wd.quit()

