# -*- coding: utf-8 -*-
from ui_desktop.locators.footer import FooterControls
from ui_desktop.pages.base import BasePage


class FooterBlock(BasePage):
    controls = FooterControls

    def add_fast(self):
        self.click(*self.controls.cartFastAddToCart)
        self.input(*self.controls.cartFastAddToCartSearch, value="101847")