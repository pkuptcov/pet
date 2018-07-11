# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class CatalogHelperControls:

    # Каталог - Напольные покрытия
    catalogFirstLevelLinoleum = (By.XPATH, "//ul[@class='categories_list']//li[3]//a[1]")
    catalogSecondLevelLinoleum = (By.XPATH, "//ul[@class='categories_list small_preview']//li[2]//a[2]")
    catalogSubdivision = (By.XPATH, "//select[@id='subdivision-select']")
    catalogSubdivisionIndus = (By.XPATH, "//option[contains(text(),'Индустриальный')]")
    catalogSortPrice = (By.XPATH, "//span[@class='product_table_sorting_link sorting__link price']")
    catalogSortTitle = (By.XPATH, "//span[@class='product_table_sorting_link sorting__link title']")
    catalogViewList = (By.XPATH, "//*[@class='ic ic_table']")
    catalogViewTile = (By.XPATH, "//*[@class='ic ic_tile']")