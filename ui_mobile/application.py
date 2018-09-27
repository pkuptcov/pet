from selenium import webdriver
from ui_mobile.pages.session import Session
from ui_mobile.fixture.smoke import SmokeHelper
from ui_mobile.fixture.register import RegisterHelper
from ui_mobile.fixture.city import CityHelper


CHROME_DEFAULT_VERSION = '68'


class Application:

    def __init__(self, browser, url, version=None):
        self.browser = browser
        self.version = version
        self.url = url

        self.wd = webdriver.Chrome()
        self.wd.set_window_size(1920, 1080)

        if browser not in ['chrome']:
            raise Exception('{} browser is not supported'.format(browser))

        # hub_url, capabilities = self.get_webdriver()
        # self.wd = webdriver.Remote(
        #     command_executor=hub_url,
        #     desired_capabilities=capabilities)
        # self.wd.set_window_size(1920, 1080)

        self.session = Session(self)
        self.smoke = SmokeHelper(self)
        self.register = RegisterHelper(self)
        self.city = CityHelper(self)

    def get_webdriver(self):
        if self.browser == 'chrome':
            hub_url = "http://hw00.vm.a:4444/wd/hub"
            capabilities = {
                "browserName": "chrome",
                "version": str(self.version) if self.version else CHROME_DEFAULT_VERSION,
                "enableVNC": True
            }
            return hub_url, capabilities

    def open_home_page(self):
        wd = self.wd
        wd.get(self.url)
        self.wd.delete_cookie("u__typeDevice")
        self.wd.add_cookie({"name": "u__typeDevice", "value": "mobile"})
        self.wd.refresh()

    def destroy(self):
        self.wd.quit()