from selenium import webdriver
from ui_desktop.fixture.session import SessionHelper
from ui_desktop.fixture.regress import RegressHelper
from ui_desktop.fixture.register import RegisterHelper
from ui_desktop.fixture.city import CityHelper


class Application:

    def __init__(self):
        # self.wd.delete_all_cookies()
        # capabilities = {
        #     "browserName": "firefox",
        #     "version": "60.0",
        #     "enableVNC": True
        # }
        # self.wd = webdriver.Remote(
        #     command_executor="http://hw00.vm.a:4444/wd/hub",
        #     desired_capabilities=capabilities)
        # self.wd.set_window_size(1920, 1080)
        self.wd = webdriver.Chrome()
        self.wd.set_window_size(1920, 1080)
        # self.wd = webdriver.Ie()
        # self.wd = webdriver.Firefox()
        # self.wd.maximize_window()
        # self.wd = webdriver.Edge()
        self.session = SessionHelper(self)
        self.regress = RegressHelper(self)
        self.register = RegisterHelper(self)
        self.city = CityHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("https://pet.beta.kluatr.ru/")

    def destroy(self):
        self.wd.quit()