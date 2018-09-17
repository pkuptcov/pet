# -*- coding: utf-8 -*-
from ui_b2b.locators.thanks import ThanksControls
from ui_b2b.pages.base import BasePage


class ThanksPage(BasePage):
    controls = ThanksControls

    def order_link(self):
        self.click(*self.controls.thanksOrderLink)