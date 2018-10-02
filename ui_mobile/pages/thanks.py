# -*- coding: utf-8 -*-
from ui_mobile.locators.thanks import ThanksControls
from ui_mobile.pages.base import BasePage


class ThanksPage(BasePage):
    controls = ThanksControls

    def continue_shopping(self):
        self.click(*self.controls.thanksContinueShopping)

    def order_link(self):
        self.click(*self.controls.thanksOrderLink)