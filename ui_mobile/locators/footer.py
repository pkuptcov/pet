# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class FooterControls:

    # Подвал сайта
    footerDiscounts = (By.XPATH, "//div[@class='b--menu']//a[(text()='Скидки')]")
    footerReturn = (By.XPATH, "//div[@class='b--menu']//a[(text()='Возврат товара')]")
    footerComplaint = (By.XPATH, "//div[@class='b--menu']//a[(text()='Центр помощи')]")
    footerPolitic = (By.XPATH, "//div[@class='b--menu']//a[(text()='Политика в области обработки и защиты персональных данных')]")
    footerDelivery = (By.XPATH, "//div[@class='b--menu']//a[(text()='Доставка и подъем')]")
    footerSawing = (By.XPATH, "//div[@class='b--menu']//a[(text()='Распил')]")
    footerRent = (By.XPATH, "//div[@class='b--menu']//a[(text()='Прокат инструмента')]")
    footerCalculate = (By.XPATH, "//div[@class='b--menu']//a[(text()='Расчет материала')]")
    footerDesktopVersion = (By.XPATH, "//div[@class='b--menu']//p[(text()='Полная версия сайта')]")