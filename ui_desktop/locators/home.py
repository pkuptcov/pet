# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class HomeHelperControls:

    # Баннеры
    bannerTop1 = (By.ID, "desktop_index_top1")
    bannerTop2 = (By.ID, "desktop_index_top2")
    bannerTop3 = (By.ID, "desktop_index_top3")
    bannerSide1 = (By.ID, "desktop_through_side1")
    bannerSide2 = (By.ID, "desktop_through_side2")

    # Блок Петрович ЖЖОТ
    burnViewAll = (By.XPATH, "//a[@href='/action-type/burns/']")
    bannerAvailability = (By.CSS_SELECTOR, "div.tooltip_container.product_status_tooltip_container.tooltip_container_open")

    # Видео
    video = (By.XPATH, "//source[@src='https://v.petrovich.ru/video/Kitchen_full_v3.mp4']")


