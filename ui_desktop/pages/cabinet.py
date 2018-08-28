# -*- coding: utf-8 -*-
from ui_desktop.locators.cabinet import CabinetEstimatesControls
from ui_desktop.locators.cabinet import CabinetExpenseControls
from ui_desktop.locators.cabinet import CabinetOrderControls
from ui_desktop.locators.cabinet import CabinetOrderListControls
from ui_desktop.locators.cabinet import CabinetProfileControls
from ui_desktop.locators.cabinet import CabinetProjectsControls
from ui_desktop.pages.base import BasePage


class CartPage(BasePage):
    order_controls = CabinetOrderControls

    def status(self):
        self.click(*self.order_controls.s)