import time
from selenium.webdriver.support.select import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_book_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="column-right"]/div/a[4]').click()
        wd.find_element_by_xpath('//*[@id="content"]/div/div[2]/a').click()

    def fill_required_fields(self, contact):
        wd = self.app.wd
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
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="content"]/form/div/div[2]/input').click()