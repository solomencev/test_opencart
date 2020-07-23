class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, user_name, password):
        wd = self.app.wd
        self.app.open_page()
        wd.find_element_by_xpath('//*[@id="input-email"]').send_keys(user_name)
        wd.find_element_by_xpath('//*[@id="input-password"]').send_keys(password)
        wd.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/form/input').click()


    def exit_from_profile(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/a/span[1]').click()
        wd.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/ul/li[5]/a').click()
