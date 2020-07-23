import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)

    def open_page(self):
        wd = self.wd
        wd.get('https://demo.opencart.com/index.php?route=account/login')
        wd.maximize_window()


    def open_book_contact(self):
        wd = self.wd
        wd.find_element_by_xpath('//*[@id="column-right"]/div/a[4]').click()
        wd.find_element_by_xpath('//*[@id="content"]/div/div[2]/a').click()

    def fill_required_fields(self, contact):
        wd = self.wd
        self.open_book_contact()
        wd.find_element_by_xpath('//*[@id="input-firstname"]').send_keys(contact.first_name)
        wd.find_element_by_xpath('//*[@id="input-lastname"]').send_keys(contact.last_name)
        wd.find_element_by_xpath('//*[@id="input-address-1"]').send_keys(contact.adress)
        wd.find_element_by_xpath('//*[@id="input-city"]').send_keys(contact.city)
        wd.find_element_by_xpath('//*[@id="input-postcode"]').send_keys(contact.post_code)
        select = Select(wd.find_element_by_xpath('//*[@id="input-country"]'))
        select.select_by_value(contact.value_of_country)
        time.sleep(1)
        select = Select(wd.find_element_by_xpath('//*[@id="input-zone"]'))
        select.select_by_value(contact.zone_in_country)
        self.create_contact()

    def create_contact(self):
        wd = self.wd
        wd.find_element_by_xpath('//*[@id="content"]/form/div/div[2]/input').click()


    def destroy(self):
        self.wd.quit()