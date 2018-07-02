# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class SearchHelperControls:
    searchProductInput = (By.ID, "query")
    searchProductSubmit = (By.CSS_SELECTOR, "form#search [type=submit]")