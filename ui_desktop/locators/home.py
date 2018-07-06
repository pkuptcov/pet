# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class HomeHelperControls:

    # Баннеры
    bannerTop1 = (By.ID, "desktop_index_top1")
    bannerTop2 = (By.ID, "desktop_index_top2")
    bannerTop3 = (By.ID, "desktop_index_top3")
    bannerSide1 = (By.ID, "desktop_through_side1")
    bannerSide2 = (By.ID, "desktop_through_side2")
    bannerInner1 = (By.XPATH, "//img[@src='//s1.petrovich.ru/common/banners/client.png']")

    # Блок Петрович ЖЖОТ
    burnViewAll = (By.XPATH, "//a[@href='/action-type/burns/']")
    bannerAvailability = (By.CSS_SELECTOR, "div.tooltip_container.product_status_tooltip_container.tooltip_container_open")

    # Блок Вам может быть интересно
    interestingViewAll = (By.XPATH, "//div[@class='rocketRetail--more']")
    interestingPrevCat = (By.XPATH, "//button[@class='rr-tab-arrow rr-tab-arrow--next']")
    interestingNextCat = (By.XPATH, "//button[@class='rr-tab-arrow rr-tab-arrow--prev']")
    interestingAlLCat = (By.XPATH, "//li[@class='rr-tab-item swiper-slide-active']")

    # Блок Новинки
    noveltyViewAll = (By.XPATH, "//a[@href='/action-type/novelty/'][contains(text(),'Посмотреть все товары')]")

    # Видео
    video = (By.XPATH, "//source[@src='https://v.petrovich.ru/video/Kitchen_full_v3.mp4']")

    # Рассылка
    subscribeName = (By.NAME, "subscribeName")
    subscribeEmail = (By.NAME, "subscribeEmail")
    subscribeSubmit = (By.XPATH, "//button[@type='submit'][contains(text(),'Подписаться')]")