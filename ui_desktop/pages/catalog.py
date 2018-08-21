# -*- coding: utf-8 -*-
from ui_desktop.locators.catalog import CatalogControls
from ui_desktop.pages.base import BasePage


class CatalogPage(BasePage):
    controls = CatalogControls

    def add_to_cart(self):
        self.click(*self.controls.catalogAddToCart)
        self.click(*self.controls.catalogAlreadyInCart)

    def quantity(self):
        self.click(*self.controls.catalogProductQuantityUp)
        self.click(*self.controls.catalogProductQuantityDown)
        self.input(*self.controls.catalogProductQuantityInput, value="2")

    def product_name(self):
        self.click(*self.controls.catalogProductName)

    def sort(self):
        self.click(*self.controls.catalogSortPrice)
        self.click(*self.controls.catalogSortTitle)
        self.click(*self.controls.catalogSortAccordance)
        self.click(*self.controls.catalogSortUsefulness)

    def view(self):
        self.click(*self.controls.catalogViewTile)
        self.click(*self.controls.catalogViewList)

    def compare(self):
        self.click(*self.controls.catalogProductCompare)

    def select_base(self):
        self.click(*self.controls.catalogSubdivision)
        self.click(*self.controls.catalogSubdivisionAll)
