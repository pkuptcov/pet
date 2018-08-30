# -*- coding: utf-8 -*-
from ui_desktop.locators.order_delivery import OrderDeliveryControls
from ui_desktop.locators.order_delivery import OrderDeliveryFizControls
from ui_desktop.locators.order_delivery import OrderDeliveryUrControls
from ui_desktop.pages.base import BasePage


class OrderDeliveryPage(BasePage):
    controls = OrderDeliveryControls
    dropdown_mask = "document.querySelectorAll('.plugin__dropdown--masked').forEach((item) => item.style.display = 'none')"

    def input_address(self):
        self.input(*self.controls.deliveryAddress, value="Россия, Санкт-Петербург, Благодатная улица, 6")

    def select_delivery_standart3(self):
        self.click(*self.controls.deliveryDay3)
        self.click(*self.controls.deliveryTypeStandard)
        self.click(*self.controls.deliveryIntervalStandard)

    def input_email(self):
        self.input(*self.controls.deliveryEmail, value="info@kluatr.ru")

    def input_comment(self):
        self.input(*self.controls.deliveryUserComment, value="тест")

    def submit_order(self):
        self.click(*self.controls.deliverySubmitOrderButtonMain)


class OrderDeliveryFizPage(OrderDeliveryPage):
    controls = OrderDeliveryFizControls

    def select_pay_online(self):
        self.click(*self.controls.orderPayOnline)

    def input_username(self, dropdown_mask):
        wd = self.app.wd
        self.input(*self.controls.orderUsername, value="Тест")
        wd.execute_script(dropdown_mask)


class OrderDeliveryUrPage(OrderDeliveryPage):
    controls = OrderDeliveryUrControls

    def select_pay_online(self):
        self.click(*self.controls.orderPayLegalNonCash)

    def input_company_details(self):
        wd = self.app.wd
        self.input(*self.controls.companyName, value="Тест")
        wd.execute_script(OrderDeliveryPage.dropdown_mask)
        self.input(*self.controls.companyInn, value="1231231231")
        self.input(*self.controls.companyKpp, value="123123123")

    def input_username(self):
        wd = self.app.wd
        wd.controls.orderUsername.clear()
        self.input(*self.controls.orderUsername, value="Тест")
        wd.execute_script(OrderDeliveryPage.dropdown_mask)