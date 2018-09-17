# -*- coding: utf-8 -*-
from ui_b2b.locators.catalog import CatalogControls
from ui_b2b.locators.header import HeaderControls
from ui_b2b.pages.base import BasePage


class CatalogPage(BasePage):
    controls = CatalogControls
    header_controls = HeaderControls

    def add_to_cart(self):
        self.click(*self.controls.catalogAddToCart)
        self.click(*self.header_controls.headerBasket)

    def quantity(self, qty):
        self.click(*self.controls.catalogProductQuantityUp)
        self.click(*self.controls.catalogProductQuantityDown)
        self.input(*self.controls.catalogProductQuantityInput, value=qty)

    def product_name(self):
        self.click(*self.controls.catalogProductName)

    def sort(self):
        self.click(*self.controls.catalogSortDefault)
        self.click(*self.controls.catalogSortPriceAsc)
        self.click(*self.controls.catalogSortPriceDesc)
        self.click(*self.controls.catalogSortTitleAsc)
        self.click(*self.controls.catalogSortTitleDesc)

    def view(self):
        self.click(*self.controls.catalogViewBlock)
        self.click(*self.controls.catalogViewListImage)
        self.click(*self.controls.catalogViewList)
