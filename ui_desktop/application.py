from selenium import webdriver
from ui_desktop.pages.session import Session
from ui_desktop.fixture.smoke import SmokeHelper
from ui_desktop.fixture.register import RegisterHelper
from ui_desktop.fixture.city import CityHelper
from ui_desktop.pages.search_product import SearchBlock
from ui_desktop.pages.authorization import AuthorizationPage
from ui_desktop.pages.authorization import RegisterPage
from ui_desktop.pages.authorization import ForgotPasswordPage
from ui_desktop.pages.cart import CartPageFiz
from ui_desktop.pages.cart import CartPageUr
from ui_desktop.pages.catalog import CatalogPage
from ui_desktop.pages.order_delivery import OrderCreateDeliveryFizPage
from ui_desktop.pages.order_delivery import OrderCreateDeliveryUrPage
from ui_desktop.pages.order_self import OrderCreateSelfFizPage
from ui_desktop.pages.order_self import OrderCreateSelfUrPage
from ui_desktop.pages.thanks import ThanksPage
from ui_desktop.pages.cabinet import CabinetOrderPage


CHROME_DEFAULT_VERSION = '66'
FIREFOX_DEFAULT_VERSION = '60'
EDGE_DEFAULT_VERSION = '42'
IE_DEFAULT_VERSION = '11'
DEFAULT_LOGIN = 'test@kluatr.ru'
DEFAULT_PASSWORD = '111111'


class Application:

    def __init__(self, browser, url, version=None):
        self.browser = browser
        self.version = version
        self.url = url

        # self.wd = webdriver.Chrome()
        # self.wd.set_window_size(1920, 1080)

        if browser not in ['firefox', 'chrome', 'edge', 'ie']:
            raise Exception('{} browser is not supported'.format(browser))

        hub_url, capabilities = self.get_webdriver()
        self.wd = webdriver.Remote(
            command_executor=hub_url,
            desired_capabilities=capabilities)
        self.wd.set_window_size(1920, 1080)

        self.session = Session(self)
        self.smoke = SmokeHelper(self)
        self.register = RegisterHelper(self)
        self.city = CityHelper(self)
        self.search_product = SearchBlock(self)
        self.cart_fiz = CartPageFiz(self)
        self.cart_ur = CartPageUr(self)
        self.catalog = CatalogPage(self)
        self.create_order_delivery_fiz = OrderCreateDeliveryFizPage(self)
        self.create_order_delivery_ur = OrderCreateDeliveryUrPage(self)
        self.create_order_self_fiz = OrderCreateSelfFizPage(self)
        self.create_order_self_fiz = OrderCreateSelfUrPage(self)
        self.thanks = ThanksPage(self)
        self.cabinet_order = CabinetOrderPage(self)

    def get_webdriver(self):
        if self.browser == 'firefox':
            hub_url = "http://hw00.vm.a:4444/wd/hub"
            capabilities = {
                "browserName": "firefox",
                "version": str(self.version) if self.version else FIREFOX_DEFAULT_VERSION,
                "enableVNC": True
            }
            return hub_url, capabilities

        elif self.browser == 'chrome':
            hub_url = "http://hw00.vm.a:4444/wd/hub"
            capabilities = {
                "browserName": "chrome",
                "version": str(self.version) if self.version else CHROME_DEFAULT_VERSION,
                "enableVNC": True
            }
            return hub_url, capabilities

        elif self.browser == 'edge':
            hub_url = "http://sel01.hw00.vm.a:4444/wd/hub"
            capabilities = {
                "browserName": "MicrosoftEdge",
                "version": str(self.version) if self.version else EDGE_DEFAULT_VERSION,
                "enableVNC": True,
            }
            return hub_url, capabilities

        elif self.browser == 'ie':
            hub_url = "http://sel01.hw00.vm.a:4444/wd/hub"
            capabilities = {
                "browserName": "internet explorer",
                "version": str(self.version) if self.version else IE_DEFAULT_VERSION,
                "enableVNC": True,
            }
            return hub_url, capabilities

    def open_home_page(self):
        wd = self.wd
        wd.get(self.url)

    def destroy(self):
        self.wd.quit()