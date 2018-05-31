from selenium.webdriver.firefox.webdriver import WebDriver
#from selenium import webdriver
from ui_b2b.fixture.session import SessionHelper
from ui_b2b.fixture.regress import RegressHelper
from ui_b2b.fixture.register import RegisterHelper
from ui_b2b.fixture.city import CityHelper


class Application:

    def __init__(self):
        #self.wd = WebDriver()
        #options = webdriver.ChromeOptions()
        #options.add_argument("--start-maximized")
        #self.wd = webdriver.Chrome(chrome_options=options)
        self.wd = WebDriver(capabilities={"marionette": True, "pageLoadStrategy": "eager"})
        self.wd.set_window_size(1920, 1080)
        #self.wd.implicitly_wait(3)
        self.session = SessionHelper(self)
        self.regress = RegressHelper(self)
        self.register = RegisterHelper(self)
        self.city = CityHelper(self)

    def open_home_page_b2b(self):
        wd = self.wd
        wd.get("https://b2b.beta.kluatr.ru/")

    def destroy(self):
        self.wd.quit()