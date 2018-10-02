# -*- coding: utf-8 -*-
from ui_mobile.locators.order_delivery import OrderDeliveryControls
from ui_mobile.locators.order_delivery import OrderDeliveryFizControls
from ui_mobile.locators.order_delivery import OrderDeliveryUrControls
from ui_mobile.pages.base import BasePage
import time


class OrderDeliveryPage(BasePage):
    controls = OrderDeliveryControls
    dropdown_mask = "document.querySelectorAll('.plugin__dropdown--masked').forEach((item) => item.style.display = 'none')"

    def input_address(self, address):
        self.input(*self.controls.deliveryAddress, value=address)

    def select_day2(self):
        self.click(*self.controls.deliveryDay2)

    def select_standart(self):
        self.click(*self.controls.deliveryTypeStandard)

    def select_interval(self):
        self.click(*self.controls.deliveryIntervalStandard2330)

    def input_email_fiz(self, email):
        self.click(*self.controls.orderEmail)
        self.input(*self.controls.deliveryEmail, value=email)

    def input_email_ur(self, email):
        self.input(*self.controls.deliveryEmail, value=email)

    def input_phone(self, phone):
        self.input(*self.controls.deliveryPhone, value=phone)

    def input_username(self, username):
        self.input(*self.controls.orderUsername, value=username)

    def input_comment(self, comment):
        self.click(*self.controls.orderComment)
        self.input(*self.controls.deliveryUserComment, value=comment)

    def submit_order(self):
        wd = self.app.wd
        self.click(*self.controls.submitOrderButton)
        time.sleep(1)
        if wd.current_url.endswith("/delivery/"):
            self.click(*self.controls.deliveryIntervalStandard2230)
            time.sleep(2)
            self.click(*self.controls.submitOrderButton)


class OrderDeliveryFizPage(OrderDeliveryPage):
    controls = OrderDeliveryFizControls

    def select_pay_online(self):
        self.click(*self.controls.orderPayOnline)


class OrderDeliveryUrPage(OrderDeliveryPage):
    controls = OrderDeliveryUrControls

    def select_pay_noncash(self):
        self.click(*self.controls.orderPayLegalNonCash)

    def input_company_details(self, company_name, inn, kpp):
        self.input(*self.controls.companyName, value=company_name)
        self.input(*self.controls.companyInn, value=inn)
        self.input(*self.controls.companyKpp, value=kpp)
