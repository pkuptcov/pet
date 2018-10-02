# -*- coding: utf-8 -*-
from ui_mobile.locators.cabinet import CabinetOrderControls
from ui_mobile.locators.cabinet import CabinetOrderListControls
from ui_mobile.locators.cabinet import CabinetProfileControls
from ui_mobile.pages.base import BasePage


class CabinetOrderPage(BasePage):
    order_controls = CabinetOrderControls

    def check_information(self):
        self.click(*self.order_controls.orderInformation)

