# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class HeaderControls:
    # Топбар (черный)
    # Выбор города
    headerRegionSelect = (By.XPATH, "//div[@class='l--top-menu']//div[@class='city--active']")
    headerRegionSpb = (By.XPATH, "//div[@class='city--choose dark--theme']//a[(text()='Санкт-Петербург')]")
    headerRegionMsk = (By.LINK_TEXT, "//div[@class='city--choose dark--theme']//a[(text()='Москва')]"'')
    headerRegionNvr = (By.LINK_TEXT, "//div[@class='city--choose dark--theme']//a[(text()='Великий Новгород')]")
    headerRegionVbg = (By.LINK_TEXT, "//div[@class='city--choose dark--theme']//a[(text()='Выборг')]")
    headerRegionGtn = (By.LINK_TEXT, "//div[@class='city--choose dark--theme']//a[(text()='Гатчина')]")
    headerRegionLug = (By.LINK_TEXT, "//div[@class='city--choose dark--theme']//a[(text()='Луга')]"'')
    headerRegionKgs = (By.LINK_TEXT, "//div[@class='city--choose dark--theme']//a[(text()='Кингисепп')]")
    headerRegionPzv = (By.LINK_TEXT, "//div[@class='city--choose dark--theme']//a[(text()='Петрозаводск')]")
    headerRegionTvr = (By.LINK_TEXT, "//div[@class='city--choose dark--theme']//a[(text()='Тверь')]")
    headerRegionKlg = (By.LINK_TEXT, "//div[@class='city--choose dark--theme']//a[(text()='Калуга')]")
    headerRegionVld = (By.LINK_TEXT, "//div[@class='city--choose dark--theme']//a[(text()='Владимир')]")

    # Номер телефона
    headerPhoneNumber = (By.XPATH, "//div[@class='l--top-menu']//div[@class='i--phone']")

    # Желтая шапка
    LeftMenu = (By.XPATH, "//div[@class='l--top-header']//div[@class='b--menu']")
    logoPetrovich = (By.XPATH, "//div[@class='l--top-header']//span[@class='logo--s']")
    headerBasket = (By.XPATH, "//div[@class='l--top-header']//div[@class='b--cart']")