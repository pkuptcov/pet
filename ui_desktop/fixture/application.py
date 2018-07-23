from selenium import webdriver
from ui_desktop.fixture.session import SessionHelper
from ui_desktop.fixture.smoke import SmokeHelper
from ui_desktop.fixture.register import RegisterHelper
from ui_desktop.fixture.city import CityHelper

CHROME_DEFAULT_VERSION = '66'
FIREFOX_DEFAULT_VERSION = '60'


class Application:

    def __init__(self, browser, version=None):
        self.browser = browser
        self.version = version

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
        wd.get("https://pet.beta.kluatr.ru/")

    def destroy(self):
        self.wd.quit()