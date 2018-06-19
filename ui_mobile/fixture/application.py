from selenium import webdriver
from ui_mobile.fixture.session import SessionHelper
from ui_mobile.fixture.regress import RegressHelper
from ui_mobile.fixture.register import RegisterHelper
from ui_mobile.fixture.city import CityHelper


class Application:

    def __init__(self):
        #self.wd.delete_all_cookies()
        self.wd = webdriver.Chrome()
        self.wd.set_window_size(1920, 1080)
        #self.wd.maximize_window()
        #self.wd = webdriver.Ie()
        #self.wd.set_window_size(1920, 1080)
        #self.wd = webdriver.Firefox()
        #self.wd.set_window_size(1920, 1080)
        #self.wd.add_cookie({"name": "u__typeDevice", "value": "mobile", "path": "/"})
        #self.wd.maximize_window()
        #self.wd = webdriver.Edge()
        #self.wd.set_window_size(1920, 1080)
        self.session = SessionHelper(self)
        self.regress = RegressHelper(self)
        self.register = RegisterHelper(self)
        self.city = CityHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("https://pet.beta.kluatr.ru/")
        self.wd.delete_cookie("u__typeDevice")
        self.wd.add_cookie({"name": "u__typeDevice", "value": "mobile", "domen": ".kluatr.ru", "path": "/"})
        self.wd.refresh()

    def destroy(self):
        self.wd.quit()