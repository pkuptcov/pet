from selenium import webdriver
from ui_b2b.fixture.session import SessionHelper
from ui_b2b.fixture.regress import RegressHelper
from ui_b2b.fixture.register import RegisterHelper
from ui_b2b.fixture.city import CityHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd = webdriver.Ie()
        self.wd = webdriver.Firefox()
        self.wd = webdriver.Edge()
        self.session = SessionHelper(self)
        self.regress = RegressHelper(self)
        self.register = RegisterHelper(self)
        self.city = CityHelper(self)

    def open_home_page_b2b(self):
        wd = self.wd
        wd.get("https://b2b.beta.kluatr.ru/")

    def destroy(self):
        self.wd.quit()