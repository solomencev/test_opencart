from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.contact import ContactHelper
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)


    def open_page(self):
        wd = self.wd
        wd.get('https://demo.opencart.com/index.php?route=account/login')
        wd.maximize_window()


    def destroy(self):
        self.wd.quit()