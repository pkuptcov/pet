# -*- coding: utf-8 -*-
from ui_mobile.locators.order_self import OrderSelfControls
from ui_mobile.locators.order_self import OrderSelfFizControls
from ui_mobile.locators.order_self import OrderSelfUrControls
from ui_mobile.pages.base import BasePage


class OrderSelfPage(BasePage):

    controls = OrderSelfControls

    def select_base(self):
        self.click(*self.controls.baseTallinskoe)

    def input_email_fiz(self, email):
        self.click(*self.controls.orderEmail)
        self.input(*self.controls.selfEmail, value=email)

    def input_email_ur(self, email):
        self.input(*self.controls.selfEmail, value=email)

    def input_phone(self, phone):
        self.input(*self.controls.selfPhone, value=phone)

    def input_username(self, username):
        self.input(*self.controls.orderUsername, value=username)

    def input_comment(self, comment):
        self.click(*self.controls.orderComment)
        self.input(*self.controls.selfUserComment, value=comment)

    def submit_order(self):
        self.click(*self.controls.submitOrderButton)


class OrderSelfFizPage(OrderSelfPage):
    controls = OrderSelfFizControls

    def select_pay_online(self):
        self.click(*self.controls.orderPayOnline)


class OrderSelfUrPage(OrderSelfPage):
    controls = OrderSelfUrControls

    def select_pay_noncash(self):
        self.click(*self.controls.orderPayLegalNonCash)

    def input_company_details(self, company_name, inn, kpp):
        self.input(*self.controls.companyName, value=company_name)
        self.input(*self.controls.companyInn, value=inn)
        self.input(*self.controls.companyKpp, value=kpp)