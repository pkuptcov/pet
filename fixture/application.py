from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.regress import RegressHelper
import time


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.regress = RegressHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("https://pet.beta.kluatr.ru/")

    def destroy(self):
        self.wd.quit()