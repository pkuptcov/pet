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
    leftMenu = (By.XPATH, "//div[@class='l--top-header']//div[@class='b--menu']")
    logoPetrovich = (By.XPATH, "//div[@class='l--top-header']//span[@class='logo--s']")
    headerBasket = (By.XPATH, "//div[@class='l--top-header']//div[@class='b--cart']")
    headerBasketGoToCart = (By.XPATH, "//div[@id='small-cart-list']//a[(text()='Перейти в корзину')]")

    # Меню ЛК
    # У незарегистрированного пользователя
    menuCabinetAuth = (By.XPATH, "//div[@class='user--forms']//a[(text()='Вход')]")
    menuCabinetRegistration = (By.XPATH, "//div[@class='user--forms']//a[(text()='Регистрация')]")

    # У зарегистрированного пользователя
    menuCabinetUsername = (By.XPATH, "//div[@class='user--name']")
    menuCabinetProfile = (By.XPATH, "//div[@class='menu--user']//a[(text()='Регистрационная информация')]")
    menuCabinetOrderList = (By.XPATH, "//div[@class='menu--user']//a[contains(text(),'Мои заказы')]")
    menuCabinetEstimates = (By.XPATH, "//div[@class='menu--user']//a[contains(text(),'Мои сметы')]")
    menuCabinetLogout = (By.XPATH, "//div[@class='menu--user']//p[(text()='Выход')]")

    # Остальное меню
    menuAbout = (By.XPATH, "//div[@class='menu--area menu--show-left animate--duration']//a[(text()='О компании')]")
    menuDiscounts = (By.XPATH, "//div[@class='menu--area menu--show-left animate--duration']//a[(text()='Скидки')]")
    menuReturn = (By.XPATH, "//div[@class='menu--area menu--show-left animate--duration']//a[(text()='Возврат товара')]")
    menuPayment = (By.XPATH, "//div[@class='menu--area menu--show-left animate--duration']//a[(text()='Способы оплаты')]")
    menuLegal = (By.XPATH, "//div[@class='menu--area menu--show-left animate--duration']//a[(text()='Для юридических лиц')]")
    menuKdp = (By.XPATH, "//div[@class='menu--area menu--show-left animate--duration']//a[(text()='Анкета Клуба Друзей')]")
    menuCertificates = (By.XPATH, "//div[@class='menu--area menu--show-left animate--duration']//a[(text()='Подарочные сертификаты')]")
    menuServices = (By.XPATH, "//div[@class='menu--area menu--show-left animate--duration']//a[(text()='Услуги')]")
    menuContacts = (By.XPATH, "//div[@class='menu--area menu--show-left animate--duration']//a[(text()='Контакты')]")