# -*- coding: utf-8 -*-
from ui_desktop.locators.search_product import SearchControls
from ui_desktop.pages.base import BasePage


class SearchBlock(BasePage):
    controls = SearchControls

    def search_product(self, product_name):
        self.input(*self.controls.searchProductInput, value=product_name)
        self.click(*self.controls.searchProductSubmit)