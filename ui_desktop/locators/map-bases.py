# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class MapBasesHelperControls:

    # Вкладки выбора города и картя яндекса
    regionCfo = (By.CSS_SELECTOR, "div[data-region-code='r_cfo']")
    regionSpb = (By.CSS_SELECTOR, "div[data-region-code='r_spb']")
    region = (By.CSS_SELECTOR, "div[data-region-code='r_cfo']")
    ymaps = (By.XPATH, "//ymaps[@class='ymaps-glass-pane ymaps-events-pane']")