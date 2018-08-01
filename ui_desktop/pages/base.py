# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, app):
        self.app = app
        self.wd = self.app.wd
        self.wait = WebDriverWait(10)

    def click(self, selector_type, selector):
        self.wd = self.app.wd
        wait.until(EC.presence_of_element_located(controls.submitOrderButtonMain))

