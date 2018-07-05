from selenium import webdriver
from ui_mobile.fixture.session import SessionHelper
from ui_mobile.fixture.regress import RegressHelper
from ui_mobile.fixture.register import RegisterHelper
from ui_mobile.fixture.city import CityHelper


class Application:

    def __init__(self):
        # capabilities = {
        #     "browserName": "firefox",
        #     "version": "60.0",
        #     "enableVNC": True
        # }
        # self.wd = webdriver.Remote(
        #     command_executor="http://hw00.vm.a:4444/wd/hub",
        #     desired_capabilities=capabilities)
        # self.wd.set_window_size(1920, 1080)
        # self.wd = webdriver.Firefox()
        self.wd = webdriver.Chrome()
        self.wd.set_window_size(1920, 1080)
        self.session = SessionHelper(self)
        self.regress = RegressHelper(self)
        self.register = RegisterHelper(self)
        self.city = CityHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("https://petrovich.ru/")
        self.wd.delete_cookie("u__typeDevice")
        self.wd.add_cookie({"name": "u__typeDevice", "value": "mobile", "domen": ".kluatr.ru", "path": "/"})
        self.wd.refresh()

    def destroy(self):
        self.wd.quit()