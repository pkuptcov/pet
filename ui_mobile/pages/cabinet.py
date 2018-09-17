# -*- coding: utf-8 -*-
from ui_desktop.locators.cabinet import CabinetEstimatesControls
from ui_desktop.locators.cabinet import CabinetExpenseControls
from ui_desktop.locators.cabinet import CabinetOrderControls
from ui_desktop.locators.cabinet import CabinetOrderListControls
from ui_desktop.locators.cabinet import CabinetProfileControls
from ui_desktop.locators.cabinet import CabinetProjectsControls
from ui_desktop.pages.base import BasePage


class CabinetOrderPage(BasePage):
    order_controls = CabinetOrderControls

    def check_information(self):
        self.click(*self.order_controls.orderInformation)

