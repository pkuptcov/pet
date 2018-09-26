# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class HomeControls:

    # Баннер
    bannerTop1 = (By.XPATH, "//div[@id='mobile_index_top1']")

    # Блок с ссылками
    urlAction = (By.XPATH, "//a[@href='/actions/']//p[(text()='Акции и новинки')]")
    urlBases = (By.XPATH, "//a[@href='/map-bases/']//p[(text()='Строительные центры')]")
    urlPropetrovich = (By.XPATH, "//a[@href='https://propetrovich.ru/']//p[(text()='Биржа профессионалов')]")
    urlPetrovichClub = (By.XPATH, "//a[@href='http://petrovichclub.ru/']//p[(text()='Клуб Друзей')]")

    # Кнопка форма оплаты заказа
    payOrderButton = (By.XPATH, "//div[@class='p--order']//p[(text()='Оплатить заказ')]")
    payOrderFormInput = (By.XPATH, "//input[@class='pay--number'][@placeholder='ТУЭ00000001']")
    payOrderFormSubmit = (By.XPATH, "//button[@class='pay--send'][text()='оплатить заказ']")
    payOrderFormClose = (By.XPATH, "//div[@class='modal--close']")

    # Блок рассылки
    subscribeEmail = (By.XPATH, "//input[@class='s--email'][@placeholder='Введите ваш e-mail']")
    subscribeSubmit = (By.XPATH, "//button[@class='s--send'][text()='Подписаться']")