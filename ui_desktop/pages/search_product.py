# -*- coding: utf-8 -*-
from ui_desktop.locators.search_product import SearchControls
from ui_desktop.pages.base import BasePage


class SearchBlock(BasePage):
    controls = SearchControls

    def login(self, username, password):
        self.click(*self.controls.)
        self.input(*self.controls.searchProductInput, value=username)