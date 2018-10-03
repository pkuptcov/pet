from selenium import webdriver
from ui_b2b.pages.session import Session
from ui_b2b.pages.header import HeaderPage
from ui_b2b.pages.search_product import SearchBlock
from ui_b2b.pages.cart import CartPage
from ui_b2b.pages.catalog import CatalogPage
from ui_b2b.pages.order_delivery import OrderDeliveryPage
from ui_b2b.pages.order_self import OrderSelfPage
from ui_b2b.pages.thanks import ThanksPage


CHROME_DEFAULT_VERSION = '68'
FIREFOX_DEFAULT_VERSION = '61'
EDGE_DEFAULT_VERSION = '42'
IE_DEFAULT_VERSION = '11'
DEFAULT_LOGIN = 'pavel.kuptcov@gmail.com'
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
        self.header = HeaderPage(self)
        self.search_product = SearchBlock(self)
        self.cart = CartPage(self)
        self.catalog = CatalogPage(self)
        self.order_delivery = OrderDeliveryPage(self)
        self.order_self = OrderSelfPage(self)
        self.thanks = ThanksPage(self)

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