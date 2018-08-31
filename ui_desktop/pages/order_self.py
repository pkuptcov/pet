# -*- coding: utf-8 -*-
from ui_desktop.locators.order_self import OrderSelfControls
from ui_desktop.locators.order_self import OrderSelfFizControls
from ui_desktop.locators.order_self import OrderSelfUrControls
from ui_desktop.pages.base import BasePage


class OrderSelfPage(BasePage):

    controls = OrderSelfControls
    dropdown_mask = "document.querySelectorAll('.plugin__dropdown--masked').forEach((item) => item.style.display = 'none')"

    def select_base(self):
        self.click(*self.controls.baseTallinskoe)

    def input_email(self):
        self.input(*self.controls.selfEmail, value="info@kluatr.ru")

    def input_phone(self):
        self.input(*self.controls.selfPhone, value="(111) 111-11-11")

    def input_comment(self):
        self.input(*self.controls.selfUserComment, value="тест")

    def submit_order(self):
        self.click(*self.controls.submitOrderButtonMain)


class OrderSelfFizPage(OrderSelfPage):
    controls_fiz = OrderSelfFizControls

    def select_pay_online(self):
        self.click(*self.controls_fiz.orderPayOnline)

    def input_username(self, dropdown_mask):
        wd = self.app.wd
        self.input(*self.controls.orderUsername, value="Тест")
        wd.execute_script(dropdown_mask)


class OrderSelfUrPage(OrderSelfPage):
    controls_ur = OrderSelfUrControls

    def input_company_details(self, dropdown_mask):
        wd = self.app.wd
        self.input(*self.controls_ur.companyName, value="Тест")
        wd.execute_script(dropdown_mask)
        self.input(*self.controls_ur.companyInn, value="1231231231")
        self.input(*self.controls_ur.companyKpp, value="123123123")

    def input_username(self, dropdown_mask):
        wd = self.app.wd
        self.input(*self.controls.orderUsername, value="Тест")
        wd.execute_script(dropdown_mask)