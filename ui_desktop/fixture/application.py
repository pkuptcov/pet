from selenium import webdriver
from ui_desktop.fixture.session import SessionHelper
from ui_desktop.fixture.regress import RegressHelper
from ui_desktop.fixture.register import RegisterHelper
from ui_desktop.fixture.city import CityHelper


class Application:

    def __init__(self):
        #self.wd = webdriver.Chrome()
        #self.wd.set_window_size(1920, 1080)
        #self.wd.maximize_window()
        #self.wd = webdriver.Ie()
        #self.wd.set_window_size(1920, 1080)
        self.wd = webdriver.Firefox()
        self.wd.set_window_size(1920, 1080)
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

    def destroy(self):
        self.wd.quit()