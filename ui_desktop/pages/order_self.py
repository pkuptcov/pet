# -*- coding: utf-8 -*-
from ui_desktop.locators.order_self import OrderCreateSelfControls
from ui_desktop.locators.order_self import OrderCreateSelfFizControls
from ui_desktop.locators.order_self import OrderCreateSelfUrControls
from ui_desktop.pages.base import BasePage


class OrderCreateSelfPage(BasePage):

    controls = OrderCreateSelfControls
    dropdown_mask = "document.querySelectorAll('.plugin__dropdown--masked').forEach((item) => item.style.display = 'none')"

    def select_base(self):
        self.click(*self.controls.baseTallinskoe)

    def input_phone(self):
        self.input(*self.controls.selfPhone, value="(111) 111-11-11")

    def input_email(self):
        self.input(*self.controls.selfEmail, value="info@kluatr.ru")

    def input_comment(self):
        self.input(*self.controls.selfUserComment, value="тест")

    def submit_order(self):
        self.click(*self.controls.submitOrderButtonMain)


class OrderCreateSelfFizPage(OrderCreateSelfPage):
    controls = OrderCreateSelfFizControls

    def select_pay_online(self):
        self.click(*self.controls.orderPayOnline)

    def input_username(self, dropdown_mask):
        wd = self.app.wd
        self.input(*self.controls.orderUsername, value="Тест")
        wd.execute_script(dropdown_mask)


class OrderCreateSelfUrPage(OrderCreateSelfPage):
    controls = OrderCreateSelfUrControls

    def input_company_details(self, dropdown_mask):
        wd = self.app.wd
        self.input(*self.controls.companyName, value="Тест")
        wd.execute_script(dropdown_mask)
        self.input(*self.controls.companyInn, value="1231231231")
        self.input(*self.controls.companyKpp, value="123123123")

    def input_username(self, dropdown_mask):
        wd = self.app.wd
        self.input(*self.controls.orderUsername, value="Тест")
        wd.execute_script(dropdown_mask)