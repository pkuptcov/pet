# -*- coding: utf-8 -*-
from ui_mobile.locators.search_product import SearchControls
from ui_mobile.pages.base import BasePage


class SearchBlock(BasePage):
    controls = SearchControls

    def search_product(self, product_name):
        self.input(*self.controls.searchProductInput, value=product_name)
        self.click(*self.controls.searchProductSubmit)