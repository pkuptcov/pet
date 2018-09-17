# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class HeaderControls:
    # Топбар (черный)
    headerBuildCenter = (By.XPATH, "(//a[contains(text(),'Строительные центры')])[1]")
    headerDeliveryAndLift = (By.XPATH, "//a[@href='/services/delivery/'][contains(text(),'Доставка и подъем')]]")
    headerReturn = (By.XPATH, "(//a[contains(text(),'Возврат')])[1]")
    headerAllServices = (By.XPATH, "(//a[@href='/services/']")

    # Выбор города
    headerRegionSelect = (By.CSS_SELECTOR, "//div.top_region")
    headerRegionSpb = (By.LINK_TEXT, 'Санкт-Петербург')
    headerRegionMsk = (By.LINK_TEXT, 'Москва')
    headerRegionNvr = (By.LINK_TEXT, 'Великий Новгород')
    headerRegionVbg = (By.LINK_TEXT, 'Выборг')
    headerRegionGtn = (By.LINK_TEXT, 'Гатчина')
    headerRegionLug = (By.LINK_TEXT, 'Луга')
    headerRegionKgs = (By.LINK_TEXT, 'Кингисепп')
    headerRegionPzv = (By.LINK_TEXT, 'Петрозаводск')
    headerRegionTvr = (By.LINK_TEXT, 'Тверь')
    headerRegionKlg = (By.LINK_TEXT, 'Калуга')
    headerRegionVld = (By.LINK_TEXT, 'Владимир')

    # Ссылки Авторзации и Регистрации в шапке
    registrationLink = (By.LINK_TEXT, "Регистрация")
    authLink = (By.LINK_TEXT, "Вход")

    # Разделы ЛК при клике на Имя Фамилию
    headerUsername = (By.CSS_SELECTOR, "a.auth_user_link")
    headerProfile = (By.LINK_TEXT, "Профиль")
    headerOrders = (By.LINK_TEXT, "Заказы")
    headerProjects = (By.LINK_TEXT, "Проекты")
    headerEstimates = (By.LINK_TEXT, "Сметы")
    headerExpense = (By.LINK_TEXT, "Расходы")
    headerLogout = (By.LINK_TEXT, "Выход")

    # Ссылки в желтой шапке
    logoPetrovich = (By.XPATH, "//div[@class='logo']")
    headerNovelty = (By.XPATH, "//a[contains(text(),'Новинки')]")
    headerActions = (By.XPATH, "//a[contains(text(),'акции')]")
    headerPetrovichClub = (By.XPATH, "//a[contains(text(),'клуб друзей')]")
    headerPhoneNumber = (By.CSS_SELECTOR, "a.head_phone_tel")

    # Корзина в шапке
    headerBasket = (By.XPATH, "//div[@class='head_basket_wrapper']")
    headerBasketCount = (By.XPATH, "//div[@class='head_basket_wrapper']")
    headerBasketPrice = (By.XPATH, "//span[@class='head_basket_price']")

    # Поиск в динамической шапке
    headerShortSearchInput = (By.NAME, "q")
    headerShortSearchSubmit = (By.XPATH, "//span[@class='request_small_form']")

    # Авторизация в динамической шапке / Переход в ЛК
    headerShortAuth = (By.XPATH, "//div[@class='head container clearfix']//a[@href='/login/']")
    headerShortIsAuth = (By.XPATH, "//div[@class='head container clearfix']//a[@href='/cabinet/orders/']")

    # Корзина в динамической шапке
    headerShortBasket = (By.XPATH, "//div[@class='common__icons basket_ico head_basket_img']")
    headerShortBasketCount = (By.XPATH, "//span[@class='short__fixed']")