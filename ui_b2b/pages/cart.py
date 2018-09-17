# -*- coding: utf-8 -*-
from ui_b2b.locators.cart import CartControls
from ui_b2b.pages.base import BasePage


class CartPage(BasePage):
    controls = CartControls

    def print(self):
        self.click(*self.controls.cartPrint)

    def delete_all(self):
        self.click(*self.controls.cartDeleteAll)
        self.click(*self.controls.cartDeleteAllConfirm)

    def quantity(self, qty):
        self.click(*self.controls.cartUpQty)
        self.click(*self.controls.cartDownQty)
        self.input(*self.controls.cartEnterQty, value=qty)

    def delete(self):
        self.click(*self.controls.cartDelete)

    def init_order_delivery(self):
        self.click(*self.controls.cartOrderDelivery)
        self.click(*self.controls.cartOrderInit)

    def init_order_self(self):
        self.click(*self.controls.cartOrderSelf)
        self.click(*self.controls.cartOrderInit)