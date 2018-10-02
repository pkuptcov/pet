# -*- coding: utf-8 -*-
from ui_mobile.locators.header import HeaderControls
from ui_mobile.pages.base import BasePage


class HeaderBlock(BasePage):
    controls = HeaderControls

    def left_swipe(self):
        self.click(*self.controls.leftMenu)

    def right_swipe(self):
        self.click(*self.controls.headerBasket)

    def select_msk(self):
        self.click(*self.controls.headerRegionSelect)
        self.click(*self.controls.headerRegionMsk)

    def logo_link(self):
        self.click(*self.controls.logoPetrovich)

    def cart_link(self):
        self.click(*self.controls.headerBasket)
        self.click(*self.controls.headerBasketGoToCart)

    def phone_link(self):
        self.click(*self.controls.headerPhoneNumber)
