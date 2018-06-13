import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegressHelper:

    def __init__(self, app):
        self.app = app

    def search(self):
        # Поиск товара по сайту
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        wd.find_element_by_id("query").send_keys("ондулин гвоздь")
        wd.find_element_by_css_selector("form#search [type=submit]").click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.head_basket_wrapper')))

    def go_to_cart(self):
        # Переход в корзину
        wd = self.app.wd
        wd.find_element_by_css_selector("div.head_basket_wrapper").click()

    def select_ur(self):
        # Выбор вкладки юридического лица
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Юридическое лицо')]")))
        wd.find_element_by_xpath("//a[contains(text(),'Юридическое лицо')]").click()

    def select_fiz(self):
        # Выбор вкладки юридического лица
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Физическое лицо')]")))
        wd.find_element_by_xpath("//a[contains(text(),'Физическое лицо')]").click()

    def edit_quantity_product(self):
        # Увеличение товара в листинге выдачи поиска и добавление в корзину
        wd = self.app.wd
        wd.find_element_by_css_selector("div.stepper-arrow.up.unit--step").click()
        wd.find_element_by_css_selector("div.btn_cart.listing__product-button.product__button.ng-scope").click()

    def edit_card(self):
        # Удаляем предыдущую карту и вводим новую
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        time.sleep(2)
        #wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[ng-model='totalCtrl.cardInput']")))
        if len(wd.find_elements_by_link_text("Удалить")) > 0:
            wd.find_element_by_link_text("Удалить").click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[ng-model='totalCtrl.cardInput']")))
        wd.find_element_by_css_selector("input[ng-model='totalCtrl.cardInput']").send_keys("111111")
        wd.find_element_by_css_selector("button[ng-click='totalCtrl.addCard()']").click()

    def init_order_creation_self(self):
        # Выбираем самовывоз и нажимаем оформить
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value=self]").click()
        wd.find_element_by_css_selector("button[ng-click='totalCtrl.goToOrdering()']").click()

    def init_order_creation_delivery(self):
        # Выбираем доставку и нажимаем оформить
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value=delivery]").click()
        wd.find_element_by_css_selector("button[ng-click='totalCtrl.goToOrdering()']").click()

    def create_order_fiz_self(self):
        # Страница оформления заказа для физ лиц самовывоз
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        wait.until(EC.presence_of_element_located((By.NAME, "base")))
        wd.find_element_by_css_selector("[value='1ea6159b-594d-11e6-bef9-00259038e9f2']").click()
        wd.find_element_by_css_selector("input[value='online']").click()
        wd.find_element_by_css_selector("[ng-model='orderingSelfCtrl.contactsEmail']").clear()
        wd.find_element_by_css_selector("[ng-model='orderingSelfCtrl.contactsEmail']").send_keys(
            "info@kluatr.ru")
        wd.find_element_by_css_selector("[ng-model='orderingSelfCtrl.contactsPhone']").clear()
        wd.find_element_by_css_selector("[ng-model='orderingSelfCtrl.contactsPhone']").send_keys(
            "(111) 111-11-11")
        wd.find_element_by_name("user_name").clear()
        wd.find_element_by_name("user_name").send_keys("Тест")
        if len(wd.find_elements_by_css_selector("div.plugin__dropdown--masked")) > 0:
            wd.find_element_by_css_selector("div.plugin__dropdown--masked").click()
        wd.find_element_by_css_selector("textarea[ng-model='orderingSelfCtrl.order.userComment']").send_keys(
            "тест")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[ng-click='orderingSelfCtrl.make($event)']")))
        wd.find_element_by_css_selector("input[ng-click='orderingSelfCtrl.make($event)']").click()

    def create_order_fiz_delivery(self):
        # Страница оформления заказа для физ лиц доставка
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[ng-model='orderDeliveryCtrl.order.deliveryAddress']")))
        wd.find_element_by_css_selector("[ng-model='orderDeliveryCtrl.order.deliveryAddress']").send_keys(
            "Россия, Санкт-Петербург, Благодатная улица, 6")
        wd.find_element_by_xpath("(//input[@name='delivery_day'])[3]").click()
        wd.find_element_by_css_selector("[ng-change=\"orderDeliveryCtrl.deliveryTypeChange('standard')\"]").click()
        time.sleep(2)
        wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "option[value='С2330До0330']")))
        wd.find_element_by_css_selector("option[value='С2330До0330']").click()
        wd.find_element_by_css_selector("input[value='online']").click()
        wd.find_element_by_css_selector("[ng-model='orderDeliveryCtrl.contactsEmail']").clear()
        wd.find_element_by_css_selector("[ng-model='orderDeliveryCtrl.contactsEmail']").send_keys(
            "info@kluatr.ru")
        wd.find_element_by_css_selector("[ng-model='orderDeliveryCtrl.contactsPhone']").clear()
        wd.find_element_by_css_selector("[ng-model='orderDeliveryCtrl.contactsPhone']").send_keys(
            "(111) 111-11-11")
        wd.find_element_by_name("user_name").clear()
        wd.find_element_by_name("user_name").send_keys("Тест")
        if len(wd.find_elements_by_css_selector("div.plugin__dropdown--masked")) > 0:
            wd.find_element_by_css_selector("div.plugin__dropdown--masked").click()
        wd.find_element_by_css_selector("textarea[ng-model='orderDeliveryCtrl.order.userComment']").send_keys(
            "тест")
        wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[ng-click='orderDeliveryCtrl.make($event)']")))
        wd.find_element_by_css_selector("input[ng-click='orderDeliveryCtrl.make($event)']").click()

    def create_order_ur_self(self):
        # Страница оформления заказа для юр лиц самовывоз
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        wait.until(EC.presence_of_element_located((By.NAME, "base")))
        wd.find_element_by_css_selector("[value='1ea6159b-594d-11e6-bef9-00259038e9f2']").click()
        wd.find_element_by_css_selector("input[value='legalNonCash']").click()
        wd.find_element_by_css_selector("input[placeholder='Название']").clear()
        wd.find_element_by_css_selector("input[placeholder='Название']").send_keys("Тест")
        time.sleep(1)
        if len(wd.find_elements_by_css_selector("div.plugin__dropdown--masked")) > 0:
            wd.find_element_by_css_selector("div.plugin__dropdown--masked").click()
        wd.find_element_by_css_selector("input[placeholder='ИНН']").clear()
        wd.find_element_by_css_selector("input[placeholder='ИНН']").send_keys("1231231231")
        wd.find_element_by_css_selector("input[placeholder='КПП']").clear()
        wd.find_element_by_css_selector("input[placeholder='КПП']").send_keys("123123123")
        wd.find_element_by_css_selector("[ng-model='orderingSelfCtrl.contactsEmail']").clear()
        wd.find_element_by_css_selector("[ng-model='orderingSelfCtrl.contactsEmail']").send_keys(
            "info@kluatr.ru")
        wd.find_element_by_css_selector("[ng-model='orderingSelfCtrl.contactsPhone']").clear()
        wd.find_element_by_css_selector("[ng-model='orderingSelfCtrl.contactsPhone']").send_keys(
            "(111) 111-11-11")
        wd.find_element_by_name("user_name").clear()
        wd.find_element_by_name("user_name").send_keys("Тест")
        time.sleep(2)
        if len(wd.find_elements_by_css_selector("div.plugin__dropdown--masked")) > 0:
            wd.find_element_by_css_selector("div.plugin__dropdown--masked").click()
        wd.find_element_by_css_selector("textarea[ng-model='orderingSelfCtrl.order.userComment']").send_keys(
            "тест")
        wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='Подтвердить заказ']")))
        wd.find_element_by_xpath("//input[@value='Подтвердить заказ']").click()

    def create_order_ur_delivery(self):
        # Страница оформления заказа для юр лиц доставка
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[ng-model='orderDeliveryCtrl.order.deliveryAddress']")))
        wd.find_element_by_css_selector("[ng-model='orderDeliveryCtrl.order.deliveryAddress']").send_keys(
            "Россия, Санкт-Петербург, Благодатная улица, 6")
        wd.find_element_by_xpath("(//input[@name='delivery_day'])[3]").click()
        wd.find_element_by_css_selector("[ng-change=\"orderDeliveryCtrl.deliveryTypeChange('standard')\"]").click()
        wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "option[value='С2330До0330']")))
        wd.find_element_by_css_selector("option[value='С2330До0330']").click()
        wd.find_element_by_css_selector("input[placeholder='Название']").clear()
        wd.find_element_by_css_selector("input[placeholder='Название']").send_keys("Тест")
        time.sleep(2)
        if len(wd.find_elements_by_css_selector("plugin__dropdown--masked")) > 0:
            wd.find_element_by_css_selector("plugin__dropdown--masked").click()
        wd.find_element_by_css_selector("input[placeholder='ИНН']").clear()
        wd.find_element_by_css_selector("input[placeholder='ИНН']").send_keys("1231231231")
        wd.find_element_by_css_selector("input[placeholder='КПП']").clear()
        wd.find_element_by_css_selector("input[placeholder='КПП']").send_keys("123123123")
        wd.find_element_by_css_selector("input[value='legalNonCash']").click()
        wd.find_element_by_css_selector("[ng-model='orderDeliveryCtrl.contactsEmail']").clear()
        wd.find_element_by_css_selector("[ng-model='orderDeliveryCtrl.contactsEmail']").send_keys(
            "info@kluatr.ru")
        wd.find_element_by_css_selector("[ng-model='orderDeliveryCtrl.contactsPhone']").clear()
        wd.find_element_by_css_selector("[ng-model='orderDeliveryCtrl.contactsPhone']").send_keys(
            "(111) 111-11-11")
        wd.find_element_by_name("user_name").clear()
        wd.find_element_by_name("user_name").send_keys("Тест")
        time.sleep(2)
        if len(wd.find_elements_by_css_selector("div.plugin__dropdown--masked")) > 0:
            wd.find_element_by_css_selector("div.plugin__dropdown--masked").click()
        wd.find_element_by_css_selector("textarea[ng-model='orderDeliveryCtrl.order.userComment']").send_keys(
            "тест")
        wd.find_element_by_xpath("//div[@id='delivery_final_scrolled']/div/button").click()

    def thanks(self):
        # Страница спасибо за покупку и переход в личный кабинет
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.thanks__lk-link')))
        wd.find_element_by_css_selector("a.thanks__lk-link").click()