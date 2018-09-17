# -*- coding: utf-8 -*-
from ui_b2b.locators.order import OrderControls
from ui_b2b.locators.order import OrderDeliveryControls
from ui_b2b.pages.base import BasePage
import time


class OrderDeliveryPage(BasePage):
    controls = OrderDeliveryControls
    dropdown_mask = "document.querySelectorAll('.plugin__dropdown--masked').forEach((item) => item.style.display = 'none')"

    def input_address(self, address):
        self.input(*self.controls.deliveryAddress, value=address)

    def select_day3(self):
        self.click(*self.controls.deliveryDay3)

    def select_standart(self):
        self.click(*self.controls.deliveryTypeStandard)

    def select_interval(self):
        self.click(*self.controls.deliveryIntervalStandard2330)

    def input_email(self, email):
        self.input(*self.controls.deliveryEmail, value=email)

    def input_phone(self, phone):
        self.input(*self.controls.deliveryPhone, value=phone)

    def input_username(self, username, dropdown_mask=dropdown_mask):
        wd = self.app.wd
        self.input(*self.controls.orderUsername, value=username)
        wd.execute_script(dropdown_mask)

    def input_comment(self, comment):
        self.input(*self.controls.deliveryUserComment, value=comment)

    def submit_order(self):
        wd = self.app.wd
        self.click(*self.controls.submitOrderButtonMain)
        time.sleep(1)
        if wd.current_url.endswith("/delivery/"):
            self.click(*self.controls.deliveryIntervalStandard2230)
            time.sleep(2)
            self.click(*self.controls.submitOrderButtonMain)

    def select_pay_noncash(self):
        self.click(*self.controls.orderPayLegalNonCash)

    def input_company_details(self, company_name, inn, kpp, dropdown_mask=dropdown_mask):
        wd = self.app.wd
        self.input(*self.controls.companyName, value=company_name)
        wd.execute_script(dropdown_mask)
        self.input(*self.controls.companyInn, value=inn)
        self.input(*self.controls.companyKpp, value=kpp)
