# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class LeftSwipeMenuControls:

    # Меню ЛК
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

