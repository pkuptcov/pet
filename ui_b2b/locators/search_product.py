# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class SearchControls:
    searchProductInput = (By.XPATH, "//input[@name='q']")
    searchProductSubmit = (By.XPATH, "//button[@class='find_catalog_search']")