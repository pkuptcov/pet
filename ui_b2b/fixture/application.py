from selenium import webdriver
from ui_b2b.fixture.session import SessionHelper
from ui_b2b.fixture.smoke import SmokeHelper
from ui_b2b.fixture.register import RegisterHelper
from ui_b2b.fixture.city import CityHelper


class Application:

    def __init__(self):
        # self.wd = webdriver.Chrome()
        # self.wd.set_window_size(1920, 1080)

        capabilities = {
            "browserName": "firefox",
            "version": "60.0",
            "enableVNC": True
        }
        self.wd = webdriver.Remote(
            command_executor="http://hw00.vm.a:4444/wd/hub",
            desired_capabilities=capabilities)
        self.wd.set_window_size(1920, 1080)

        # self.wd.maximize_window()
        # self.wd = webdriver.Ie()
        # self.wd = webdriver.Firefox()
        # self.wd.set_window_size(1920, 1080)
        # self.wd.maximize_window()
        # self.wd = webdriver.Edge()
        self.session = SessionHelper(self)
        self.smoke = SmokeHelper(self)
        self.register = RegisterHelper(self)
        self.city = CityHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("https://b2b.beta.kluatr.ru/")

    def destroy(self):
        self.wd.quit()