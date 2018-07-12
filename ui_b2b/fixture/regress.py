from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class RegressHelper:

    def __init__(self, app):
        self.app = app

    def select_city(self):
        # Выбор города и организации
        wd = self.app.wd
        wd.find_element_by_css_selector("div.organiztions_and-city-chosen-box").click()
        wd.find_element_by_xpath("//div[contains(text(),'Санкт-Петербург')]").click()
        time.sleep(1)

    def search(self):
        # Поиск товара по сайту
        wd = self.app.wd
        wd.find_element_by_name("q").click()
        wd.find_element_by_name("q").send_keys("ондулин гвоздь")
        wd.find_element_by_css_selector("button.find_catalog_search").click()

    def edit_quantity_product(self):
        # Увеличение товара в листинге выдачи поиска и добавление в корзину
        wd = self.app.wd
        wd.find_element_by_css_selector("span.plus").click()
        wd.find_element_by_id("to_basket_button").click()

    def go_to_cart(self):
        # Переход в корзину
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        wd.find_element_by_css_selector("button.basket_catalog_search").click()

    def init_order_creation_self(self):
        # Выбираем самовывоз и нажимаем оформить
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[value='self']")))
        wd.find_element_by_css_selector("input[value='self']").click()
        wd.find_element_by_css_selector("button[ng-click='totalFinalCtrl.goToOrdering()']").click()

    def init_order_creation_delivery(self):
        # Выбираем доставку и нажимаем оформить
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[value='delivery']")))
        wd.find_element_by_css_selector("input[value='delivery']").click()
        wd.find_element_by_css_selector("button[ng-click='totalFinalCtrl.goToOrdering()']").click()

    def create_order_ur_self(self):
        # Страница оформления заказа для юр лиц самовывоз
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        wait.until(EC.element_to_be_clickable((By.NAME, "base")))
        wd.find_element_by_name("base").click()
        wd.find_element_by_css_selector("input[value='legalNonCash']").click()
        wd.find_element_by_css_selector("input[placeholder='Название']").clear()
        wd.find_element_by_css_selector("input[placeholder='Название']").send_keys("Тест")
        if len(wd.find_elements_by_css_selector("div.plugin__dropdown--masked")) > 0:
            wd.find_element_by_css_selector("div.plugin__dropdown--masked").click()
        wd.find_element_by_css_selector("input[placeholder='ИНН']").clear()
        wd.find_element_by_css_selector("input[placeholder='ИНН']").send_keys("1231231231")
        wd.find_element_by_css_selector("input[placeholder='КПП']").clear()
        wd.find_element_by_css_selector("input[placeholder='КПП']").send_keys("123123123")
        wd.find_element_by_css_selector("[ng-model='orderingSelfCtrl.contactsEmail']").clear()
        wd.find_element_by_css_selector("[ng-model='orderingSelfCtrl.contactsEmail']").send_keys("info@kluatr.ru")
        wd.find_element_by_css_selector("[ng-model='orderingSelfCtrl.contactsPhone']").clear()
        wd.find_element_by_css_selector("[ng-model='orderingSelfCtrl.contactsPhone']").send_keys("(111) 111-11-11")
        wd.find_element_by_name("user_name").clear()
        wd.find_element_by_name("user_name").send_keys("Тест")
        if len(wd.find_elements_by_css_selector("div.plugin__dropdown--masked")) > 0:
            wd.find_element_by_css_selector("div.plugin__dropdown--masked").click()
        wd.find_element_by_css_selector("textarea[ng-model='orderingSelfCtrl.order.userComment']").send_keys("тест")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Подтвердить заказ']")))
        wd.find_element_by_xpath("//input[@value='Подтвердить заказ']").click()

    def create_order_ur_delivery(self):
        # Страница оформления заказа для юр лиц доставка
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[ng-model='orderDeliveryCtrl.order.deliveryAddress']")))
        wd.find_element_by_css_selector("[ng-model='orderDeliveryCtrl.order.deliveryAddress']").send_keys(
            "Россия, Санкт-Петербург, Благодатная улица, 6")
        wd.find_element_by_xpath("(//input[@name='delivery_day'])[3]").click()
        wd.find_element_by_css_selector("[ng-change=\"orderDeliveryCtrl.deliveryTypeChange('standard')\"]").click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "option[value='С2330До0330']")))
        wd.find_element_by_css_selector("option[value='С2330До0330']").click()
        wd.find_element_by_css_selector("input[placeholder='Название']").clear()
        wd.find_element_by_css_selector("input[placeholder='Название']").send_keys("Тест")
        if len(wd.find_elements_by_css_selector("div.plugin__dropdown--masked")) > 0:
            wd.find_element_by_css_selector("div.plugin__dropdown--masked").click()
        wd.find_element_by_css_selector("input[placeholder='ИНН']").clear()
        wd.find_element_by_css_selector("input[placeholder='ИНН']").send_keys("1231231231")
        wd.find_element_by_css_selector("input[placeholder='КПП']").clear()
        wd.find_element_by_css_selector("input[placeholder='КПП']").send_keys("123123123")
        wd.find_element_by_css_selector("input[value='legalNonCash']").click()
        wd.find_element_by_css_selector("[ng-model='orderDeliveryCtrl.contactsEmail']").clear()
        wd.find_element_by_css_selector("[ng-model='orderDeliveryCtrl.contactsEmail']").send_keys("info@kluatr.ru")
        wd.find_element_by_css_selector("[ng-model='orderDeliveryCtrl.contactsPhone']").clear()
        wd.find_element_by_css_selector("[ng-model='orderDeliveryCtrl.contactsPhone']").send_keys("(111) 111-11-11")
        wd.find_element_by_name("user_name").clear()
        wd.find_element_by_name("user_name").send_keys("Тест")
        if len(wd.find_elements_by_css_selector("div.plugin__dropdown--masked")) > 0:
            wd.find_element_by_css_selector("div.plugin__dropdown--masked").click()
        wd.find_element_by_css_selector("textarea[ng-model='orderDeliveryCtrl.order.userComment']").send_keys("тест")
        wd.find_element_by_xpath("//div[@id='delivery_final_scrolled']/div/button").click()
        if wd.current_url.endswith("/delivery/"):
            wd.find_element_by_css_selector("option[value='С23До03']").click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[ng-click='orderDeliveryCtrl.make($event)']")))
            wd.find_element_by_xpath("//div[@id='delivery_final_scrolled']/div/button").click()

    def thanks(self):
        # Страница спасибо за покупку и переход в личный кабинет
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        time.sleep(1)
        wait.until(EC.presence_of_element_located((By.XPATH, "//p[@class='thanks__big-text']")))
        wd.find_element_by_xpath("//a[contains(text(),'заказ')]").click()