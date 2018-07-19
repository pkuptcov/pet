from selenium import webdriver
from ui_b2b.fixture.session import SessionHelper
from ui_b2b.fixture.smoke import SmokeHelper
from ui_b2b.fixture.register import RegisterHelper
from ui_b2b.fixture.city import CityHelper


class Application:

    def __init__(self, browser):

        if browser not in ['firefox', 'chrome']:
            raise Exception('{} browser is not supported'.format(browser))

        capabilities = self.get_capabilities(browser)
        self.wd = webdriver.Remote(
            command_executor="http://hw00.vm.a:4444/wd/hub",
            desired_capabilities=capabilities)
        self.wd.set_window_size(1920, 1080)

        # self.wd = webdriver.Chrome()
        # self.wd.set_window_size(1920, 1080)
        self.session = SessionHelper(self)
        self.smoke = SmokeHelper(self)
        self.register = RegisterHelper(self)
        self.city = CityHelper(self)

    @staticmethod
    def get_capabilities(browser_name):
        if browser_name == 'firefox':
            return {
                "browserName": "firefox",
                "version": "60.0",
                "enableVNC": True
            }
        if browser_name == 'chrome':
            return {
                "browserName": "chrome",
                "version": "66.0",
                "enableVNC": True
            }

    def open_home_page(self):
        wd = self.wd
        wd.get("https://b2b.beta.kluatr.ru/")

    def destroy(self):
        self.wd.quit()