# -*- coding: utf-8 -*-
from ui_mobile.locators.catalog import CatalogControls
from ui_mobile.pages.base import BasePage


class CatalogPage(BasePage):
    controls = CatalogControls

    def add_to_cart(self):
        self.click(*self.controls.catalogAddToCart)
        self.click(*self.controls.catalogAlreadyInCart)

    def quantity(self, qty):
        self.click(*self.controls.catalogProductQuantityUp)
        self.click(*self.controls.catalogProductQuantityDown)
        self.input(*self.controls.catalogProductQuantityInput, value=qty)

    def product_name(self):
        self.click(*self.controls.catalogProductName)

    def sort(self):
        self.click(*self.controls.catalogSort)
        self.click(*self.controls.catalogSortPriceAsc)
        self.click(*self.controls.catalogSortPriceDesc)
        self.click(*self.controls.catalogSortTitleAsc)
        self.click(*self.controls.catalogSortTitleDesc)
