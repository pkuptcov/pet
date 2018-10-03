from selenium import webdriver
from ui_mobile.pages.session import Session
from ui_mobile.pages.cart import CartPageFiz
from ui_mobile.pages.cart import CartPage
from ui_mobile.pages.catalog import CatalogPage
from ui_mobile.pages.cabinet import CabinetOrderPage
from ui_mobile.pages.header import HeaderBlock
from ui_mobile.pages.authorization import AuthorizationPage
from ui_mobile.pages.authorization import ForgotPasswordPage
from ui_mobile.pages.authorization import RegisterPage
from ui_mobile.pages.order_delivery import OrderDeliveryFizPage
from ui_mobile.pages.order_delivery import OrderDeliveryUrPage
from ui_mobile.pages.order_self import OrderSelfFizPage
from ui_mobile.pages.order_self import OrderSelfUrPage
from ui_mobile.pages.search_product import SearchBlock
from ui_mobile.pages.thanks import ThanksPage


CHROME_DEFAULT_VERSION = '68'


class Application:

    def __init__(self, browser, url, version=None):
        self.browser = browser
        self.version = version
        self.url = url

        # self.wd = webdriver.Chrome()
        # self.wd.set_window_size(1920, 1080)

        if browser not in ['chrome']:
            raise Exception('{} browser is not supported'.format(browser))

        hub_url, capabilities = self.get_webdriver()
        self.wd = webdriver.Remote(
            command_executor=hub_url,
            desired_capabilities=capabilities)
        self.wd.set_window_size(1920, 1080)

        self.session = Session(self)
        self.cart = CartPage(self)
        self.cart_fiz = CartPageFiz(self)
        self.catalog = CatalogPage(self)
        self.cabinet = CabinetOrderPage(self)
        self.header = HeaderBlock(self)
        self.authorization = AuthorizationPage(self)
        self.authorization = ForgotPasswordPage(self)
        self.authorization = RegisterPage(self)
        self.order_delivery_fiz = OrderDeliveryFizPage(self)
        self.order_delivery_ur = OrderDeliveryUrPage(self)
        self.order_self_fiz = OrderSelfFizPage(self)
        self.order_self_ur = OrderSelfUrPage(self)
        self.search_product = SearchBlock(self)
        self.thanks = ThanksPage(self)

    def get_webdriver(self):
        if self.browser == 'chrome':
            hub_url = "http://hw00.vm.a:4444/wd/hub"
            capabilities = {
                "browserName": "chrome",
                "version": str(self.version) if self.version else CHROME_DEFAULT_VERSION,
                "enableVNC": True
            }
            return hub_url, capabilities

    def open_home_page(self):
        wd = self.wd
        wd.get(self.url)
        self.wd.delete_cookie("u__typeDevice")
        self.wd.add_cookie({"name": "u__typeDevice", "value": "mobile"})
        self.wd.refresh()

    def destroy(self):
        self.wd.quit()