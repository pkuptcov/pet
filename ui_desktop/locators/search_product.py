# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class SearchControls:
    searchProductInput = (By.ID, "query")
    searchProductClose = (By.XPATH, "//form[@id='search']//div[@class='form__search-exit']")
    searchProductSubmit = (By.CSS_SELECTOR, "form#search [type=submit]")