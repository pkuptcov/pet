# -*- coding: utf-8 -*-
from ui_desktop.locators.cart import CartControls
from ui_desktop.locators.cart import CartControlsFiz
from ui_desktop.locators.cart import CartControlsUr
from ui_desktop.pages.base import BasePage


class CartPage(BasePage):
    controls = CartControls

    def add_fast(self):
        self.click(*self.controls.cartFastAddToCart)
        self.input(*self.controls.cartFastAddToCartSearch, value="101847")
        self.click(*self.controls.cartFastAddToCartSudjest101847)
        self.input(*self.controls.cartFastAddToCartQantityInput, value="2")
        self.click(*self.controls.cartFastAddToCartQantityUp)
        self.click(*self.controls.cartFastAddToCartQantityDown)
        self.click(*self.controls.cartFastAddToCartSubmit)

    def print(self):
        self.click(*self.controls.cartPrint)

    def save_estimate(self):
        self.click(*self.controls.cartSaveEstimate)

    def delete_all(self):
        self.click(*self.controls.cartDeleteAll)
        self.click(*self.controls.cartDeleteAllConfirm)

    def select_ur(self):
        self.click(*self.controls.cartSelectUr)

    def select_fiz(self):
        self.click(*self.controls.cartSelectFiz)

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


class CartPageFiz(CartPage):
    controls_fiz = CartControlsFiz

    def edit_card(self, card_number):
        # Удаляем предыдущую карту и вводим новую
        if len(self.wd.find_elements(*self.controls_fiz.cartCardDelete)) > 0:
            self.click(*self.controls_fiz.cartCardDelete)
        self.input(*self.controls_fiz.cartCardInput, value=card_number)
        self.click(*self.controls_fiz.cartCardSubmit)


class CartPageUr(CartPage):
    controls_ur = CartControlsUr
