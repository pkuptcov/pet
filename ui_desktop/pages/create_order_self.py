# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ui_desktop.locators.order_create_self import OrderCreateSelfControls
from ui_desktop.locators.order_create_self import OrderCreateSelfFizControls
from ui_desktop.locators.order_create_self import OrderCreateSelfUrControls
from ui_desktop.pages.base import BasePage


class OrderCreateSelfPage(BasePage):
    controls = OrderCreateSelfControls
    dropdown_mask = "document.querySelectorAll('.plugin__dropdown--masked').forEach((item) => item.style.display = 'none')"

    def select_base(self, controls):
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        wait.until(EC.presence_of_element_located(controls.baseList))
        wd.controls.baseTallinskoe.click()

    def input_phone(self):
        wd = self.app.wd
        wd.controls.selfPhone.clear()
        wd.controls.selfPhone.send_keys("(111) 111-11-11")

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


class OrderCreateSelfFizPage(OrderCreateSelfPage):
    controls = OrderCreateSelfFizControls

    def select_pay_online(self):
        wd = self.app.wd
        wd.controls.orderPayOnline.click()

    def input_username(self, dropdown_mask):
        wd = self.app.wd
        wd.controls.orderUsername.clear()
        wd.controls.orderUsername.send_keys("Тест")
        wd.execute_script(dropdown_mask)


class OrderCreateSelfUrPage(OrderCreateSelfPage):
    controls = OrderCreateSelfUrControls

    def input_company_details(self, dropdown_mask):
        wd = self.app.wd
        wd.companyName.clear()
        wd.companyName.send_keys("Тест")
        wd.execute_script(dropdown_mask)
        wd.companyInn.clear()
        wd.companyInn.send_keys("1231231231")
        wd.companyKpp.clear()
        wd.companyKpp.send_keys("123123123")

    def input_username(self, dropdown_mask):
        wd = self.app.wd
        wd.controls.orderUsername.clear()
        wd.controls.orderUsername.send_keys("Тест")
        wd.execute_script(dropdown_mask)