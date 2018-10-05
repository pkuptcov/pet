from ui_b2b.locators.header import HeaderControls
from ui_b2b.pages.base import BasePage
import time


class HeaderPage(BasePage):
    controls = HeaderControls

    def select_spb(self):
        self.click(*self.controls.headerCompanyList)
        self.click(*self.controls.headerCompanyListSpb)
        time.sleep(2)