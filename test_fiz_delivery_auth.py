# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import time, unittest


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class fiz_delivery_auth(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(10)

    def fiz_delivery_auth(self):
        success = True
        self.login(username="xigekuba@p33.org", password="111111")
        self.search()
        self.edit_quantity_product()
        self.go_to_cart()
        self.edit_card()
        self.init_order_creation()
        self.create_order()
        self.thanks()
        self.logout()

    def tearDown(self):
        self.wd.quit()

    def logout(self):
        # Выход из ЛК
        wd = self.wd
        wd.find_element_by_css_selector("a.auth_user_link").click()
        wd.find_element_by_link_text("Выход").click()

    def thanks(self, wd):
        wd = self.wd
        # Страница спасибо за покупку и переход в личный кабинет
        wd.find_element_by_css_selector("a.thanks__lk-link").click()

    def create_order(self):
        # Страница оформления заказа
        wd = self.wd
        wd.find_element_by_css_selector("[ng-model=\"orderDeliveryCtrl.order.deliveryAddress\"]").send_keys(
            "Россия, Санкт-Петербург, Благодатная улица, 6")
        wd.find_element_by_xpath("(//input[@name='delivery_day'])[3]").click()
        wd.find_element_by_css_selector("[ng-change=\"orderDeliveryCtrl.deliveryTypeChange('standard')\"]").click()
        time.sleep(1)
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

    def init_order_creation(self):
        # Нажимаем оформить
        wd = self.wd
        wd.find_element_by_css_selector("button[ng-click='totalCtrl.goToOrdering()']").click()

    def edit_card(self):
        # Удаляем предыдущую карту и вводим новую
        wd = self.wd
        wd.find_element_by_link_text("Удалить").click()
        wd.find_element_by_css_selector("input[placeholder=\"•••••••\"]").send_keys("111111")
        wd.find_element_by_css_selector("button[ng-click='totalCtrl.addCard()']").click()

    def go_to_cart(self):
        # Переход в корзину
        wd = self.wd
        wd.find_element_by_css_selector("div.head_basket_wrapper").click()

    def edit_quantity_product(self):
        # Увеличение товара в листинге выдачи поиска
        wd = self.wd
        wd.find_element_by_css_selector("div.stepper-arrow.up.unit--step").click()
        wd.find_element_by_css_selector("[data-product-code='101846']").click()

    def search(self):
        # Поиск товара по сайту
        wd = self.wd
        wd.find_element_by_id("query").send_keys("ондулин гвоздь")
        wd.find_element_by_css_selector("form#search [type=submit]").click()

    def login(self, username, password):
        # Авторизация
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_link_text("Вход").click()
        wd.find_element_by_id("mainPetrovichLogin_login").send_keys(username)
        wd.find_element_by_id("mainPetrovichLogin_password").send_keys(password)
        wd.find_element_by_css_selector("div.form_row [type=submit]").click()
        #time.sleep(1)

    def open_home_page(self):
        # Переход на сайт
        wd = self.wd
        wd.get("https://petrovich.ru/")

    if __name__ == '__main__':
        unittest.main()