# -*- coding: utf-8 -*-
from ui_mobile.locators.cart import CartControls
from ui_mobile.locators.cart import CartControlsFiz
from ui_mobile.pages.base import BasePage


class CartPage(BasePage):
    controls = CartControls

    def delete_all(self):
        self.click(*self.controls.cartProductSelect)
        self.click(*self.controls.cartDeleteAll)
        self.click(*self.controls.cartDeleteAllConfirm)

    def select_ur(self):
        self.click(*self.controls.cartSelectUr)

    def select_fiz(self):
        self.click(*self.controls.cartSelectFiz)

    def quantity(self, qty):
        self.click(*self.controls.cartProductSelect)
        self.click(*self.controls.cartUpQty)
        self.click(*self.controls.cartDownQty)
        self.input(*self.controls.cartEnterQty, value=qty)

    def delete(self):
        self.click(*self.controls.cartProductSelect)
        self.click(*self.controls.cartDelete)

    def init_order_delivery(self):
        self.click(*self.controls.cartOrderDelivery)
        self.click(*self.controls.cartOrderInit)

    def init_order_self(self):
        self.click(*self.controls.cartOrderSelf)
        self.click(*self.controls.cartOrderInit)


class CartPageFiz(CartPage):
    controls_fiz = CartControlsFiz

    def edit_card(self, card_number):
        # Удаляем предыдущую карту и вводим новую
        if len(self.wd.find_elements(*self.controls_fiz.cartCardDelete)) > 0:
            self.click(*self.controls_fiz.cartCardDelete)
        self.input(*self.controls_fiz.cartCardInput, value=card_number)
        self.click(*self.controls_fiz.cartCardSubmit)