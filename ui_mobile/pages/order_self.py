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

    def input_email(self, email):
        self.input(*self.controls.selfEmail, value=email)

    def input_phone(self, phone):
        self.input(*self.controls.selfPhone, value=phone)

    def input_username(self, username, dropdown_mask=dropdown_mask):
        wd = self.app.wd
        self.input(*self.controls.orderUsername, value=username)
        wd.execute_script(dropdown_mask)

    def input_comment(self, comment):
        self.input(*self.controls.selfUserComment, value=comment)

    def submit_order(self):
        self.click(*self.controls.submitOrderButtonMain)


class OrderSelfFizPage(OrderSelfPage):
    controls = OrderSelfFizControls

    def select_pay_online(self):
        self.click(*self.controls.orderPayOnline)


class OrderSelfUrPage(OrderSelfPage):
    controls = OrderSelfUrControls

    def select_pay_noncash(self):
        self.click(*self.controls.orderPayLegalNonCash)

    def input_company_details(self, company_name, inn, kpp, dropdown_mask=OrderSelfPage.dropdown_mask):
        wd = self.app.wd
        self.input(*self.controls.companyName, value=company_name)
        wd.execute_script(dropdown_mask)
        self.input(*self.controls.companyInn, value=inn)
        self.input(*self.controls.companyKpp, value=kpp)