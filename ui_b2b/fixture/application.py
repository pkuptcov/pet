from selenium import webdriver
from ui_b2b.fixture.session import SessionHelper
from ui_b2b.fixture.smoke import SmokeHelper
from ui_b2b.fixture.register import RegisterHelper
from ui_b2b.fixture.city import CityHelper

CHROME_DEFAULT_VERSION = '68'
FIREFOX_DEFAULT_VERSION = '60'


class Application:

    def __init__(self, browser, url, version=None):
        self.browser = browser
        self.version = version
        self.url = url

        # self.wd = webdriver.Chrome()
        # self.wd.set_window_size(1920, 1080)

        if browser not in ['firefox', 'chrome']:
            raise Exception('{} browser is not supported'.format(browser))

        capabilities = self.get_capabilities()
        self.wd = webdriver.Remote(
            command_executor="http://hw00.vm.a:4444/wd/hub",
            desired_capabilities=capabilities)
        self.wd.set_window_size(1920, 1080)

        self.session = SessionHelper(self)
        self.smoke = SmokeHelper(self)
        self.register = RegisterHelper(self)
        self.city = CityHelper(self)

    def get_capabilities(self):
        if self.browser == 'firefox':
            return {
                "browserName": "firefox",
                "version": str(self.version) if self.version else FIREFOX_DEFAULT_VERSION,
                "enableVNC": True
            }
        elif self.browser == 'chrome':
            return {
                "browserName": "chrome",
                "version": str(self.version) if self.version else CHROME_DEFAULT_VERSION,
                "enableVNC": True
            }

    def open_home_page(self):
        wd = self.wd
        wd.get(self.url)

    def destroy(self):
        self.wd.quit()