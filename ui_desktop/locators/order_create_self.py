# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class OrderCreateSelfControls:

    # Выбор строительного центра
    # Список баз:
    baseList = (By.CSS_SELECTOR, "ul.bases_list")
    # СПБ:
    baseTallinskoe = (By.CSS_SELECTOR, "[value='1ea6159b-594d-11e6-bef9-00259038e9f2']")
    baseEngelsa = (By.CSS_SELECTOR, "[value='42d0a3ba-2efc-11df-942d-0023543d7b52']")
    baseSofiyskaya = (By.CSS_SELECTOR, "[value='8e55188d-3e96-11e6-9830-00259038e9f2']")
    basePlanernaya = (By.CSS_SELECTOR, "[value='a15db6c3-305d-11e0-9d49-001f29c6db02']")
    baseIndustrialniy = (By.CSS_SELECTOR, "[value='a95a374c-2f82-11df-942d-0023543d7b52']")
    baseMurmanskoe = (By.CSS_SELECTOR, "[value='d41279b8-2f82-11df-942d-0023543d7b52']")
    baseMoskovskoe = (By.CSS_SELECTOR, "[value='d41279d5-2f82-11df-942d-0023543d7b52']")
    selfMoveToGatchina = (By.CSS_SELECTOR, "button[ng-click='orderingSelfCtrl.moveCartToGatchina()']")
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

    # Перейти в корзину и изменить заказ
    baseReturnToCart = (By.XPATH, "//input[contains(text(),'Перейти в корзину и изменить заказ')]")

    # Дополнительные услуги
    orderRent = (By.XPATH, "//span[@class='label_name'][contains(text(),'Аренда оборудования)]")
    orderColoring = (By.XPATH, "//span[@class='label_name'][contains(text(),'Колеровка')]")
    orderSawed = (By.XPATH, "//span[@class='label_name'][contains(text(),'Распил')]")

    # Комментарии к доп. услугам
    selfSawedComment = (By.CSS_SELECTOR, "[ng-model='orderingSelfCtrl.order.sawingComment']")
    selfColoringComment = (By.CSS_SELECTOR, "[ng-model='orderingSelfCtrl.order.coloringComment']")
    selfRentComment = (By.CSS_SELECTOR, "[ng-model='orderingSelfCtrl.order.rentComment']")

    # Контактная информация
    selfEmail = (By.CSS_SELECTOR, "[ng-model='orderingSelfCtrl.contactsEmail']")
    selfPhone = (By.CSS_SELECTOR, "[ng-model='orderingSelfCtrl.contactsPhone']")
    orderUsername = (By.NAME, "user_name")
    # orderDropdownMask = (By.CSS_SELECTOR, ".plugin__dropdown--masked")
    selfCallRequired = (By.CSS_SELECTOR, "input[ng-model='orderingSelfCtrl.order.callRequired']")
    selfUserComment = (By.CSS_SELECTOR, "textarea[ng-model='orderingSelfCtrl.order.userComment']")

    # Подтверждение заказа
    submitOrderButtonMain = (By.CSS_SELECTOR, "input[ng-click='orderingSelfCtrl.make($event)']")
    submitOrderButtonRight = (By.XPATH, "//button[@type='submit'][contains(text(),'Подтвердить заказ')]")


class OrderCreateSelfUrControls(OrderCreateSelfControls):

    # Реквизиты компании
    companyName = (By.CSS_SELECTOR, "input[placeholder='Название']")
    companyInn = (By.CSS_SELECTOR, "input[placeholder='ИНН']")
    companyKpp = (By.CSS_SELECTOR, "input[placeholder='КПП']")

    # Способы оплаты заказа
    orderPayLegalNonCash = (By.CSS_SELECTOR, "input[value='legalNonCash']")
    orderPayLegalCard = (By.CSS_SELECTOR, "input[value='legalCard']")
    orderPayLegalCash = (By.CSS_SELECTOR, "input[value='legalCash']")


class OrderCreateSelfFizControls(OrderCreateSelfControls):

    # Способы оплаты заказа
    orderPayOnline = (By.CSS_SELECTOR, "input[value='online']")
    orderPayBase = (By.CSS_SELECTOR, "input[value='base']")
    orderPayPromo = (By.CSS_SELECTOR, "input[value='promo']")
    orderPayDelay = (By.CSS_SELECTOR, "input[value='delay']")
