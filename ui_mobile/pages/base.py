# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, app):
        self.app = app
        self.wd = self.app.wd
        self.wait = WebDriverWait(self.wd, 10)

    def click(self, selector_type, selector):
        self.find_element(selector_type, selector).click()

    def input(self, selector_type, selector, value):
        element = self.find_element(selector_type, selector)
        # self.wd.execute_script("arguments[0].scrollIntoView();", element)
        element.clear()
        element.send_keys(value)

    def find_element(self, selector_type, selector):
        self.wait.until(EC.presence_of_element_located((selector_type, selector)))
        self.wait.until(EC.visibility_of_element_located((selector_type, selector)))
        self.wait.until(EC.element_to_be_clickable((selector_type, selector)))
        return self.wd.find_element(selector_type, selector)

    def check(self, selector_type, selector):
        self.wait.until(EC.presence_of_element_located((selector_type, selector)))
        self.wait.until(EC.visibility_of_element_located((selector_type, selector)))
        self.wait.until(EC.element_to_be_clickable((selector_type, selector)))




    # def check(self, selector_type, selector, value):
    #     element = self.find_element(selector_type, selector)
    #     assert element.value
