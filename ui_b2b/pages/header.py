# -*- coding: utf-8 -*-
from ui_desktop.locators.header import HeaderControls
from ui_desktop.pages.base import BasePage


class HeaderBlock(BasePage):
    controls = HeaderControls

    def auth_link(self):
        self.click(*self.controls.authLink)

    def reg_link(self):
        self.click(*self.controls.registrationLink)

    def map_bases_link(self):
        self.click(*self.controls.headerBuildCenter)

    def delivery_lift_link(self):
        self.click(*self.controls.headerDeliveryAndLift)

    def return_link(self):
        self.click(*self.controls.headerReturn)

    def services_link(self):
        self.click(*self.controls.headerAllServices)

    def select_region(self):
        self.click(*self.controls.headerRegionSelect)

    def select_msk(self):
        self.click(*self.controls.headerRegionMsk)

    def logo_link(self):
        self.click(*self.controls.logoPetrovich)

    def cart_link(self):
        self.click(*self.controls.headerBasket)

    def novelty_link(self):
        self.click(*self.controls.headerNovelty)

    def actions_link(self):
        self.click(*self.controls.headerActions)
