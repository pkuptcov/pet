import time


class RegressHelper:

    def __init__(self, app):
        self.app = app

    def thanks(self):
        wd = self.app.wd
        # Страница спасибо за покупку и переход в личный кабинет
        time.sleep(1)
        wd.find_element_by_css_selector("a.thanks__lk-link").click()

    def create_order_fiz_delivery(self):
        # Страница оформления заказа для физ лиц доставка
        wd = self.app.wd
        wd.find_element_by_css_selector("[ng-model=\"orderDeliveryCtrl.order.deliveryAddress\"]").send_keys(
            "Россия, Санкт-Петербург, Благодатная улица, 6")
        wd.find_element_by_xpath("(//input[@name='delivery_day'])[3]").click()
        wd.find_element_by_css_selector("[ng-change=\"orderDeliveryCtrl.deliveryTypeChange('standard')\"]").click()
        time.sleep(2)
        wd.find_element_by_css_selector("option[value='С2330До0330']").click()
        wd.find_element_by_css_selector("input[value=\"online\"]").click()
        wd.find_element_by_css_selector("[ng-model=\"orderDeliveryCtrl.order.userEmail\"]").clear()
        wd.find_element_by_css_selector("[ng-model=\"orderDeliveryCtrl.order.userEmail\"]").send_keys(
            "propetrovich@mail.ru")
        wd.find_element_by_css_selector("[ng-model=\"orderDeliveryCtrl.contactsPhone\"]").clear()
        wd.find_element_by_css_selector("[ng-model=\"orderDeliveryCtrl.contactsPhone\"]").send_keys(
            "(111) 111-11-11")
        #wd.find_element_by_name("user_name").clear()
        #wd.find_element_by_name("user_name").send_keys("Тест")
        #wd.find_element_by_css_selector("div.__js__contacts--element").click()
        wd.find_element_by_css_selector("textarea[ng-model='orderDeliveryCtrl.order.userComment']").send_keys("тест")
        time.sleep(2)
        wd.find_element_by_css_selector("input[ng-click='orderDeliveryCtrl.make($event)']").click()
        time.sleep(2)

    def create_order_fiz_self(self):
        wd = self.app.wd
        time.sleep(1)
        wd.find_element_by_name("base").click()
        wd.find_element_by_css_selector("input[value=\"online\"]").click()
        wd.find_element_by_css_selector("[ng-model=\"orderingSelfCtrl.order.userEmail\"]").clear()
        wd.find_element_by_css_selector("[ng-model=\"orderingSelfCtrl.order.userEmail\"]").send_keys(
            "propetrovich@mail.ru")
        wd.find_element_by_css_selector("[ng-model=\"orderingSelfCtrl.contactsPhone\"]").clear()
        wd.find_element_by_css_selector("[ng-model=\"orderingSelfCtrl.contactsPhone\"]").send_keys(
            "(111) 111-11-11")
        #wd.find_element_by_name("user_name").clear()
        #wd.find_element_by_name("user_name").send_keys("Тест")
        # wd.find_element_by_css_selector("div.__js__contacts--element").click()
        wd.find_element_by_css_selector("textarea[ng-model='orderingSelfCtrl.order.userComment']").send_keys(
            "тест")
        time.sleep(1)
        wd.find_element_by_css_selector("input[ng-click=\"orderingSelfCtrl.make($event)\"]").click()

    def create_order_ur_delivery(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("[ng-model=\"orderDeliveryCtrl.order.deliveryAddress\"]").send_keys(
            "Россия, Санкт-Петербург, Благодатная улица, 6")
        wd.find_element_by_xpath("(//input[@name='delivery_day'])[3]").click()
        wd.find_element_by_css_selector("[ng-change=\"orderDeliveryCtrl.deliveryTypeChange('standard')\"]").click()
        time.sleep(2)
        wd.find_element_by_css_selector("option[value='С2330До0330']").click()
        wd.find_element_by_css_selector("input[placeholder=\"Название\"]").clear()
        wd.find_element_by_css_selector("input[placeholder=\"Название\"]").send_keys("Тест")
        wd.find_element_by_css_selector("input[placeholder=\"ИНН\"]").clear()
        wd.find_element_by_css_selector("input[placeholder=\"ИНН\"]").send_keys("1231231231")
        wd.find_element_by_css_selector("input[placeholder=\"КПП\"]").clear()
        wd.find_element_by_css_selector("input[placeholder=\"КПП\"]").send_keys("123123123")
        wd.find_element_by_css_selector("input[value=\"legalNonCash\"]").click()
        wd.find_element_by_css_selector("[ng-model=\"orderDeliveryCtrl.order.userEmail\"]").clear()
        wd.find_element_by_css_selector("[ng-model=\"orderDeliveryCtrl.order.userEmail\"]").send_keys(
            "propetrovich@mail.ru")
        wd.find_element_by_css_selector("[ng-model=\"orderDeliveryCtrl.contactsPhone\"]").clear()
        wd.find_element_by_css_selector("[ng-model=\"orderDeliveryCtrl.contactsPhone\"]").send_keys(
            "(111) 111-11-11")
        #wd.find_element_by_name("user_name").clear()
        #wd.find_element_by_name("user_name").send_keys("Тест")
        #wd.find_element_by_css_selector("div.__js__contacts--element").click()
        wd.find_element_by_css_selector("textarea[ng-model='orderDeliveryCtrl.order.userComment']").send_keys(
            "тест")
        time.sleep(2)
        wd.find_element_by_css_selector("input[ng-click='orderDeliveryCtrl.make($event)']").click()
        time.sleep(2)

    def create_order_ur_self(self):
        wd = self.app.wd
        time.sleep(1)
        wd.find_element_by_name("base").click()
        wd.find_element_by_css_selector("input[placeholder=\"Название\"]").send_keys("Тест")
        wd.find_element_by_css_selector("input[placeholder=\"ИНН\"]").clear()
        wd.find_element_by_css_selector("input[placeholder=\"ИНН\"]").send_keys("1231231231")
        wd.find_element_by_css_selector("input[placeholder=\"КПП\"]").clear()
        wd.find_element_by_css_selector("input[placeholder=\"КПП\"]").send_keys("123123123")
        wd.find_element_by_css_selector("input[value=\"legalNonCash\"]").click()
        wd.find_element_by_css_selector("[ng-model=\"orderingSelfCtrl.order.userEmail\"]").clear()
        wd.find_element_by_css_selector("[ng-model=\"orderingSelfCtrl.order.userEmail\"]").send_keys(
            "propetrovich@mail.ru")
        wd.find_element_by_css_selector("[ng-model=\"orderingSelfCtrl.contactsPhone\"]").clear()
        wd.find_element_by_css_selector("[ng-model=\"orderingSelfCtrl.contactsPhone\"]").send_keys(
            "(111) 111-11-11")
        #wd.find_element_by_name("user_name").clear()
        #wd.find_element_by_name("user_name").send_keys("Тест")
        #wd.find_element_by_css_selector("div.__js__contacts--element").click()
        wd.find_element_by_css_selector("textarea[ng-model='orderingSelfCtrl.order.userComment']").send_keys(
            "тест")
        time.sleep(1)
        wd.find_element_by_css_selector("input[ng-click=\"orderingSelfCtrl.make($event)\"]").click()

    def init_order_creation_delivery(self):
        # Нажимаем оформить
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value=delivery]").click()
        wd.find_element_by_css_selector("button[ng-click='totalCtrl.goToOrdering()']").click()

    def edit_card(self):
        # Удаляем предыдущую карту и вводим новую
        wd = self.app.wd
        time.sleep(1)
        if len(wd.find_elements_by_link_text("Удалить")) > 0:
            wd.find_element_by_link_text("Удалить").click()
        time.sleep(1)
        wd.find_element_by_css_selector("input[ng-model='totalCtrl.cardInput']").send_keys("111111")
        wd.find_element_by_css_selector("button[ng-click='totalCtrl.addCard()']").click()

    def go_to_cart(self):
        # Переход в корзину
        wd = self.app.wd
        wd.find_element_by_css_selector("div.head_basket_wrapper").click()

    def edit_quantity_product(self):
        # Увеличение товара в листинге выдачи поиска и добавление в корзину
        wd = self.app.wd
        wd.find_element_by_css_selector("div.stepper-arrow.up.unit--step").click()
        wd.find_element_by_css_selector("div.btn_cart.listing__product-button.product__button.ng-scope").click()
        # wd.find_element_by_css_selector("[data-product-code='101846']").click()

    def search(self):
        # Поиск товара по сайту
        wd = self.app.wd
        wd.find_element_by_id("query").send_keys("ондулин гвоздь")
        wd.find_element_by_css_selector("form#search [type=submit]").click()
        time.sleep(1)

    def init_order_creation_self(self):
        # Выбираем самовывоз и нажимаем оформить
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value=self]").click()
        wd.find_element_by_css_selector("button[ng-click='totalCtrl.goToOrdering()']").click()
        #time.sleep(1)

    def select_ur(self):
        wd = self.app.wd
        # Выбор вкладки юридического лица
        time.sleep(1)
        wd.find_element_by_xpath("//a[contains(text(),'Юридическое лицо')]").click()