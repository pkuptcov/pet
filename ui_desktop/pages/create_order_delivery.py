# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ui_desktop.locators.order_create_delivery import OrderCreateDeliveryControls
from ui_desktop.locators.order_create_delivery import OrderCreateDeliveryFizControls
from ui_desktop.locators.order_create_delivery import OrderCreateDeliveryUrControls
from ui_desktop.pages.base import BasePage


class OrderCreateDeliveryPage(BasePage):
    controls = OrderCreateDeliveryControls
    dropdown_mask = "document.querySelectorAll('.plugin__dropdown--masked').forEach((item) => item.style.display = 'none')"

    def input_address(self, controls):
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        wait.until(EC.element_to_be_clickable(controls.deliveryAddress))
        wd.controls.deliveryAddress.send_keys("Россия, Санкт-Петербург, Благодатная улица, 6")

    def select_delivery_standart3(self, controls):
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        wd.controls.deliveryDay3.click()
        wd.controls.deliveryTypeStandard.click()
        wait.until(EC.element_to_be_clickable(controls.deliveryIntervalStandard))
        wd.deliveryIntervalStandard.click()

    def input_email(self):
        wd = self.app.wd
        wd.controls.selfEmail.clear()
        wd.controls.selfEmail.send_keys("info@kluatr.ru")

    def input_comment(self):
        wd = self.app.wd
        wd.controls.orderUsername.clear()
        wd.controls.selfUserComment.send_keys("тест")

    def submit_order(self, controls):
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        wait.until(EC.element_to_be_clickable(controls.submitOrderButtonMain))
        wd.find_element_by_css_selector(controls.submitOrderButtonRight).click()


class OrderCreateDeliveryFizPage(OrderCreateDeliveryPage):
    controls = OrderCreateDeliveryFizControls

    def select_pay_online(self):
        wd = self.app.wd
        wd.controls.orderPayOnline.click()

    def input_username(self, dropdown_mask):
        wd = self.app.wd
        wd.controls.orderUsername.clear()
        wd.controls.orderUsername.send_keys("Тест")
        wd.execute_script(dropdown_mask)


class OrderCreateSelfUrPage(OrderCreateDeliveryPage):
    controls = OrderCreateDeliveryUrControls

    def input_company_details(self, controls):
        wd = self.app.wd
        wd.companyName.clear()
        wd.companyName.send_keys("Тест")
        wd.execute_script("document.querySelectorAll('.plugin__dropdown--masked').forEach((item) => item.style.display = 'none')")
        wd.companyInn.clear()
        wd.companyInn.send_keys("1231231231")
        wd.companyKpp.clear()
        wd.companyKpp.send_keys("123123123")

    def input_username(self, controls):
        wd = self.app.wd
        wd.controls.orderUsername.clear()
        wd.controls.orderUsername.send_keys("Тест")
        wd.execute_script("document.querySelectorAll('.plugin__dropdown--masked').forEach((item) => item.style.display = 'none')")