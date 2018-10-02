# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class OrderSelfControls:

    # Выбор строительного центра
    # Список баз:
    baseList = (By.CSS_SELECTOR, "ul.bases_list")
    # СПБ:
    baseTallinskoe = (By.XPATH, "//label[text()=' Таллинское ш., 155, 1, стр. 1 ']")
    baseEngelsa = (By.XPATH, "//label[text()=' пр. Энгельса, 157, лит. А ']")
    baseSofiyskaya = (By.XPATH, "//label[text()=' ул. Софийская, д.59, корп.2, стр.1 ']")
    basePlanernaya = (By.XPATH, "//label[text()=' ул. Планерная, 15в ']")
    baseIndustrialniy = (By.XPATH, "//label[text()=' Индустриальный пр., 73 ']")
    baseMurmanskoe = (By.XPATH, "//label[text()=' Мурманское шоссе 12-13 км ']")
    baseMoskovskoe = (By.XPATH, "//label[text()=' Московское шоссе, д.304 ']")
    baseKadSever = (By.XPATH, "//label[text()=' КАД, 21 км, между Выборгским ш. и пр. Энгельса ']")

    # МСК:
    baseBalashiha = (By.CSS_SELECTOR, "[value='10c5ed9d-7185-11e4-89d5-00259038e9f2']")
    baseNovorizhskoe = (By.CSS_SELECTOR, "[value='172b9cec-7185-11e4-89d5-00259038e9f2']")
    baseNovoryazanskoe = (By.CSS_SELECTOR, "[value='6a60a7fc-53bf-11e6-bef9-00259038e9f2']")
    baseAltufevo = (By.CSS_SELECTOR, "[value='8d019325-709f-11e4-89d5-00259038e9f2']")
    # Великий Новгород:
    baseNovgorod = (By.CSS_SELECTOR, "[value='d41279bd-2f82-11df-942d-0023543d7b52']")
    # Выборг:
    baseVyborg = (By.CSS_SELECTOR, "[value='a95a3747-2f82-11df-942d-0023543d7b52']")
    # Гатчина:
    baseGatchina = (By.CSS_SELECTOR, "[value='7d3f6711-f0fb-11e1-aa5b-00259038e9f2']")
    # Луга:
    baseLuga = (By.CSS_SELECTOR, "[value='309ed970-2951-11e0-9d49-001f29c6db02']")
    # Кингисепп:
    baseKingisepp = (By.CSS_SELECTOR, "[value='51c3d796-7fa7-11e0-b5e3-001f29c6db02']")
    # Петрозаводск:
    basePetrozavodsk = (By.CSS_SELECTOR, "[value='893c542a-8538-11e1-bb26-00259038e9f2']")
    # Тверь:
    baseTver = (By.CSS_SELECTOR, "[value='469f28be-ea07-11e2-8ae0-00259038e9f2']")

    # Дополнительные услуги
    orderGarbageRemoval = (By.XPATH, "//label[@for='garbage--i'][(text()=' Вывоз мусора ')]")
    orderRent = (By.XPATH, "//label[@for='rent--i'][(text()=' Аренда оборудования ')]")
    orderColoring = (By.XPATH, "//label[@for='coloring--i'][(text()=' Колеровка ')]")
    orderSawed = (By.XPATH, "//label[@for='cut--i'][(text()=' Распил ')]")

    # Комментарии к доп. услугам
    selfSawedComment = (By.XPATH, "//label[@for='cut--i']//textarea[@placeholder='Комментарий']")
    selfColoringComment = (By.XPATH, "//label[@for='coloring--i']//textarea[@placeholder='Комментарий']")
    selfGarbageComment = (By.XPATH, "//label[@for='garbage--i']//textarea[@placeholder='Комментарий']")
    selfRentComment = (By.XPATH, "//label[@for='rent--i']//textarea[@placeholder='Комментарий']")

    # Контактная информация
    selfEmail = (By.XPATH, "//input[@type='email'][@placeholder='например, petrovich@mail.ru']")
    selfPhone = (By.XPATH, "//input[@type='tel'][@placeholder='+7 (999) 999-99-99']")
    orderUsername = (By.NAME, "user_name")
    selfCallRequired = (By.XPATH, "//label[@for='call--i']//span[(text()='Обязательно нужен звонок оператора')]")
    selfUserComment = (By.XPATH, "//textarea[@placeholder='В арку налево. До железной двери и стучать. Раньше 6:00 не звонить. На объекте прораб Кузьмич.']")

    # Подтверждение заказа
    submitOrderButton = (By.XPATH, "//button[@class='confirm--send'][(text()='Подтвердить заказ')]")

    # Раскрыть пункты
    orderBase = (By.XPATH, "//p[(text()='Выберите строительный центр')]")
    orderAdditionalSevices = (By.XPATH, "//p[(text()='Дополнительные услуги')]")
    orderPaymentType = (By.XPATH, "//p[(text()='Способ оплаты')]")
    orderEmail = (By.XPATH, "//p[(text()='Ваша электронная почта')]")
    orderPhone = (By.XPATH, "//p[(text()='Телефон для звонков и СМС')]")
    orderComment = (By.XPATH, "//p[(text()='Комментарии к заказу')]")
    orderAboutCompany = (By.XPATH, "//p[(text()='Информация о компании')]")


class OrderSelfUrControls(OrderSelfControls):

    # Реквизиты компании
    companyName = (By.XPATH, "//input[@placeholder='Название']")
    companyInn = (By.XPATH, "//input[@placeholder='ИНН']")
    companyKpp = (By.XPATH, "//input[@placeholder='КПП']")

    # Способы оплаты заказа
    orderPayLegalNonCash = (By.XPATH, "//label[@for='pay--legalNonCash'][(text()='По безналичному расчету')]")
    orderPayLegalCard = (By.XPATH, "//label[@for='pay--legalCard'][(text()='Банковской картой')]")
    orderPayLegalCash = (By.XPATH, "//label[@for='pay--legalCash'][(text()='За наличный расчет')]")


class OrderSelfFizControls(OrderSelfControls):

    # Способы оплаты заказа
    orderPayOnline = (By.XPATH, "//label[@for='pay--online'][(text()='Картой онлайн')]")
    orderPayBase = (By.XPATH, "//label[@for='pay--base'][(text()='На базе или в офисе')]")
    orderPayPromo = (By.XPATH, "//label[@for='pay--promo'][(text()='Баллами Клуба Друзей')]")
    orderPayDelay = (By.XPATH, "//label[@for='pay--delay'][(text()='С отсрочкой на пять дней')]")