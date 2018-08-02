# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, app):
        self.app = app
        self.wd = self.app.wd
        self.wait = WebDriverWait(self.wd, 10)

    def click(self, selector_type, selector):

        element = self.wd.find_element(selector_type, selector)

        self.wait.until(EC.presence_of_element_located((selector_type, selector)))
        self.wd.execute_script("arguments[0].scrollIntoView();", element)
        self.wait.until(EC.visibility_of_element_located((selector_type, selector)))
        self.wait.until(EC.element_to_be_clickable((selector_type, selector)))
        self.wd.find_element(selector_type, selector).click()