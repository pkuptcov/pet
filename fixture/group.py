class GroupHelper:
    def __init__(self, app):
        self.app = app

    def thanks(self, group):
        wd = self.app.wd
        wd.find_element_by_css_selector("a.thanks__lk-link").click()

    def create_order(self, group):
        wd = self.app.wd
        wd.find_element_by_css_selector("[ng-model=\"orderDeliveryCtrl.order.deliveryAddress\"]").send_keys(
            "Россия, Санкт-Петербург, Благодатная улица, 6")
        wd.find_element_by_xpath("(//input[@name='delivery_day'])[3]").click()
        wd.find_element_by_css_selector("[ng-change=\"orderDeliveryCtrl.deliveryTypeChange('standard')\"]").click()
        wd.find_element_by_css_selector("option[value='С2330До0330']").click()
        wd.find_element_by_css_selector("input[value=\"online\"]").click()
        wd.find_element_by_css_selector("[ng-model=\"orderDeliveryCtrl.order.userEmail\"]").clear()
        wd.find_element_by_css_selector("[ng-model=\"orderDeliveryCtrl.order.userEmail\"]").send_keys(
            "propetrovich@mail.ru")
        wd.find_element_by_css_selector("[ng-model=\"orderDeliveryCtrl.order.userPhone\"]").clear()
        wd.find_element_by_css_selector("[ng-model=\"orderDeliveryCtrl.order.userPhone\"]").send_keys(
            "(111) 111-11-11")
        wd.find_element_by_name("user_name").clear()
        wd.find_element_by_name("user_name").send_keys("Тест")
        wd.find_element_by_css_selector("textarea[ng-model='orderDeliveryCtrl.order.userComment']").send_keys(
            "тест")
        wd.find_element_by_css_selector("input[ng-click=\"orderDeliveryCtrl.make($event)\"]").click()

    def init_order(self, group):
        wd = self.app.wd
        wd.find_element_by_css_selector("button[ng-click='totalCtrl.goToOrdering()']").click()

    def card(self, group):
        wd = self.app.wd
        wd.find_element_by_link_text("Удалить").click()
        wd.find_element_by_css_selector("input[placeholder=\"•••••••\"]").send_keys("111111")
        wd.find_element_by_css_selector("button[ng-click='totalCtrl.addCard()']").click()

    def go_to_cart(self, group):
        wd = self.app.wd
        wd.find_element_by_css_selector("div.head_basket_wrapper").click()

    def listing(self, group):
        wd = self.app.wd
        wd.find_element_by_css_selector("div.stepper-arrow.up.unit--step").click()
        wd.find_element_by_css_selector("[data-product-code='101846']").click()

    def search(self, group):
        wd = self.app.wd
        wd.find_element_by_id("query").send_keys("ондулин гвоздь")
        wd.find_element_by_css_selector("form#search [type=submit]").click()