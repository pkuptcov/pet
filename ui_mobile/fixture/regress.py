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
        wd.find_element_by_css_selector("input.s--button").click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.c--plus')))

    def edit_quantity_product(self):
        # Увеличение товара в листинге выдачи поиска и добавление в корзину
        wd = self.app.wd
        wd.find_element_by_css_selector("div.c--plus").click()
        wd.find_element_by_xpath("//button[contains(text(),'В корзину')]").click()

    def go_to_cart(self):
        # Переход в корзину
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        wd.find_element_by_css_selector("div.b--cart").click()
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Перейти в корзину")))
        wd.find_element_by_link_text("Перейти в корзину").click()

    def select_ur(self):
        # Выбор вкладки юридического лица
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Юридическое лицо')]")))
        wd.find_element_by_xpath("//p[contains(text(),'Юридическое лицо')]").click()

    def select_fiz(self):
        # Выбор вкладки юридического лица
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Физическое лицо')]")))
        wd.find_element_by_xpath("//p[contains(text(),'Физическое лицо')]").click()

    def edit_card(self):
        # Удаляем предыдущую карту и вводим новую
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.discount--card-event")))
        if len(wd.find_elements_by_css_selector('p.delete--card')) > 0:
            wd.find_element_by_css_selector('p.delete--card').click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='number']")))
        wd.find_element_by_xpath("//input[@type='number']").send_keys("111111")
        wd.find_element_by_css_selector('button.card--send').click()

    def init_order_creation_self(self):
        # Выбираем самовывоз и нажимаем оформить
        wd = self.app.wd
        wd.find_element_by_xpath("//label[@for='shipment--place']").click()
        wd.find_element_by_xpath("//button[@class='step--send']").click()

    def init_order_creation_delivery(self):
        # Выбираем доставку и нажимаем оформить
        wd = self.app.wd
        wd.find_element_by_xpath("//label[@for='delivery--place']").click()
        wd.find_element_by_xpath("//button[@class='step--send']").click()

    def create_order_fiz_self(self):
        # Страница оформления заказа для физ лиц самовывоз
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='base--1ea6159b-594d-11e6-bef9-00259038e9f2']")))
        wd.find_element_by_xpath("//label[@for='base--1ea6159b-594d-11e6-bef9-00259038e9f2']").click()
        wd.find_element_by_xpath("//label[@for='pay--online']").click()
        wd.find_element_by_xpath("//p[@class='st--text'][contains(text(),'Ваша электронная почта')]").click()
        wd.find_element_by_xpath("//input[@type='email']").clear()
        wd.find_element_by_xpath("//input[@type='email']").send_keys("info@kluatr.ru")
        wd.find_element_by_xpath("//input[@type='tel']").clear()
        wd.find_element_by_xpath("//input[@type='tel']").send_keys("(111) 111-11-11")
        wd.find_element_by_name("user_name").clear()
        wd.find_element_by_name("user_name").send_keys("Тест")
        wd.find_element_by_xpath("//p[@class='st--text'][contains(text(),'Комментарии к заказу')]").click()
        wd.find_element_by_css_selector("[ng-model='orderingSelfCtrl.order.userComment']").click()
        wd.find_element_by_css_selector("[ng-model='orderingSelfCtrl.order.userComment']").send_keys("тест")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='confirm--send']")))
        wd.find_element_by_xpath("//button[@class='confirm--send']").click()

    def create_order_fiz_delivery(self):
        # Страница оформления заказа для физ лиц доставка
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Показать карту')]")))
        wd.find_element_by_xpath("//p[contains(text(),'Показать карту')]").click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//ymaps[@class='ymaps-2-1-65-inner-panes']")))
        wd.find_element_by_css_selector("[ng-model='orderDeliveryCtrl.order.deliveryAddress']").send_keys(
            "Россия, Санкт-Петербург, Благодатная улица, 6")
        wd.find_element_by_xpath("//label[@for='date--1529657469000']").click()
        wd.find_element_by_xpath("//label[@for='pay--online']").click()
        wd.find_element_by_xpath("//label[@for='day--interval']").click()
        wd.find_element_by_css_selector("[ng-model='orderingSelfCtrl.order.userComment']").click()
        wd.find_element_by_xpath("//p[@class='st--text'][contains(text(),'Ваша электронная почта')]").click()
        wd.find_element_by_xpath("//input[@type='email']").clear()
        wd.find_element_by_xpath("//input[@type='email']").send_keys("info@kluatr.ru")
        wd.find_element_by_xpath("//input[@type='tel']").clear()
        wd.find_element_by_xpath("//input[@type='tel']").send_keys("(111) 111-11-11")
        wd.find_element_by_name("user_name").clear()
        wd.find_element_by_name("user_name").send_keys("Тест")
        wd.find_element_by_xpath("//p[@class='st--text'][contains(text(),'Комментарии к заказу')]").click()
        wd.find_element_by_css_selector("[ng-model='orderingSelfCtrl.order.userComment']").click()
        wd.find_element_by_css_selector("[ng-model='orderingSelfCtrl.order.userComment']").send_keys("тест")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='confirm--send']")))
        wd.find_element_by_xpath("//button[@class='confirm--send']").click()


    def create_order_ur_self(self):
        # Страница оформления заказа для юр лиц самовывоз
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='base--1ea6159b-594d-11e6-bef9-00259038e9f2']")))
        wd.find_element_by_xpath("//label[@for='base--1ea6159b-594d-11e6-bef9-00259038e9f2']").click()
        wd.find_element_by_css_selector("[ng-model='orderingSelfCtrl.companiesName']").clear()
        wd.find_element_by_css_selector("[ng-model='orderingSelfCtrl.companiesName']").send_keys("Тест")
        wd.find_element_by_css_selector("[ng-model='orderingSelfCtrl.companiesInn']").clear()
        wd.find_element_by_css_selector("[ng-model='orderingSelfCtrl.companiesInn']").send_keys("1231231231")
        wd.find_element_by_css_selector("[ng-model='orderingSelfCtrl.companiesKpp']").clear()
        wd.find_element_by_css_selector("[ng-model='orderingSelfCtrl.companiesKpp']").send_keys("123123123")
        wd.find_element_by_xpath("//label[@for='pay--legalNonCash']").click()
        wd.find_element_by_xpath("//input[@type='email']").clear()
        wd.find_element_by_xpath("//input[@type='email']").send_keys("info@kluatr.ru")
        wd.find_element_by_xpath("//input[@type='tel']").clear()
        wd.find_element_by_xpath("//input[@type='tel']").send_keys("(111) 111-11-11")
        wd.find_element_by_name("user_name").clear()
        wd.find_element_by_name("user_name").send_keys("Тест")
        wd.find_element_by_xpath("//p[@class='st--text'][contains(text(),'Комментарии к заказу')]").click()
        wd.find_element_by_css_selector("[ng-model='orderingSelfCtrl.order.userComment']").send_keys("тест")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='confirm--send']")))
        wd.find_element_by_xpath("//button[@class='confirm--send']").click()

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
        wd.execute_script(
            "document.querySelectorAll('.plugin__dropdown--masked').forEach((item) => item.style.display = 'none')")
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
        wd.execute_script(
            "document.querySelectorAll('.plugin__dropdown--masked').forEach((item) => item.style.display = 'none')")
        wd.find_element_by_css_selector("textarea[ng-model='orderDeliveryCtrl.order.userComment']").send_keys(
            "тест")
        wd.find_element_by_xpath("//div[@id='delivery_final_scrolled']/div/button").click()
        time.sleep(2)
        if wd.current_url.endswith("/delivery/"):
            wd.find_element_by_css_selector("option[value='С23До03']").click()
            time.sleep(3)
            wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[ng-click='orderDeliveryCtrl.make($event)']")))
            wd.find_element_by_xpath("//div[@id='delivery_final_scrolled']/div/button").click()

    def thanks(self):
        # Страница спасибо за покупку и переход в личный кабинет
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Личном кабинете')]")))
        wd.find_element_by_xpath("//a[contains(text(),'Личном кабинете')]").click()