# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class OrderControls:

    # Дополнительные услуги
    orderRent = (By.XPATH, "//span[@class='label_name'][contains(text(),'Аренда оборудования)]")
    orderColoring = (By.XPATH, "//span[@class='label_name'][contains(text(),'Колеровка')]")
    orderSawed = (By.XPATH, "//span[@class='label_name'][contains(text(),'Распил')]")
    orderLifting = (By.XPATH, "//span[@class='label_name'][contains(text(),'Подъем на этаж')]")
    orderUnloading = (By.XPATH, "//span[@class='label_name'][contains(text(),'Разгрузка')]")
    orderManipulator = (By.XPATH, "//span[@class='label_name'][contains(text(),'Манипулятор')]")
    orderGarbageRemoval = (By.XPATH, "//span[@class='label_name'][contains(text(),'Вывоз мусора')]")
    orderReturn = (By.XPATH, "//span[@class='label_name'][contains(text(),'Возврат товара')]")

    # Реквизиты компании
    companyName = (By.XPATH, "//input[@placeholder='Название']")
    companyInn = (By.XPATH, "//input[@placeholder='ИНН']")
    companyKpp = (By.XPATH, "//input[@placeholder='КПП']")

    # Способы оплаты заказа
    orderPayLegalNonCash = (By.XPATH, "//span[(text()='По безналичному расчету')]")
    orderPayLegalCard = (By.CSS_SELECTOR, "input[value='legalCard']")
    orderPayLegalCash = (By.CSS_SELECTOR, "input[value='legalCash']")

    # Подтверждение заказа
    submitOrderButtonMain = (By.XPATH, "//input[@value='Подтвердить заказ']")
    submitOrderButtonRight = (By.XPATH, "//button[@type='submit']")


class OrderDeliveryControls(OrderControls):

    # Адрес доставки
    deliveryAddress = (By.CSS_SELECTOR, "[ng-model='orderDeliveryCtrl.order.deliveryAddress']")
    # deliveryAddressHistory = (By.CSS_SELECTOR, "")
    deliveryAddressShowMore = (By.XPATH, "//a[@ng-hide='showMoreAdresses']']")
    deliveryArchParking = (By.CSS_SELECTOR, "input[ng-model='orderDeliveryCtrl.order.deliveryArchway']")
    deliveryVisibilityMap = (By.XPATH, "//a[@class='map_open_link']")
    deliveryDriverComment = (By.CSS_SELECTOR, "textarea[ng-model='orderDeliveryCtrl.order.driverComment']")
    deliveryForemanName = (By.CSS_SELECTOR, "input[ng-model='orderDeliveryCtrl.foremansName']")
    deliveryForemanPhone = (By.CSS_SELECTOR, ".master__phone __choose")

    orderElementBase = ".order"
    deliveryAddressInput = (By.CSS_SELECTOR, "{}[data-modify='ur,delivery'] input [name='deliveryAddress']".format(orderElementBase))

    # Дни доставки
    deliveryDay1 = (By.XPATH, "(//input[@name='delivery_day'])[1]")
    deliveryDay2 = (By.XPATH, "(//input[@name='delivery_day'])[2]")
    deliveryDay3 = (By.XPATH, "//ul[@class='delivery_form_step_list_variant delivery_time delivery_form_step_calendar_container']//li[3]")
    deliveryDay4 = (By.XPATH, "(//input[@name='delivery_day'])[4]")
    deliveryDay5 = (By.XPATH, "(//input[@name='delivery_day'])[5]")
    deliveryDay6 = (By.XPATH, "(//input[@name='delivery_day'])[6]")

    # Типы доставки
    deliveryTypeToday = (By.CSS_SELECTOR, "[ng-change=\"orderDeliveryCtrl.deliveryTypeChange('today')\"]")
    deliveryTypeStandard = (By.XPATH, "//span[(text()='Стандартная доставка')]")
    deliveryTypeExpress = (By.CSS_SELECTOR, "[ng-change=\"orderDeliveryCtrl.deliveryTypeChange('express')\"]")
    deliveryTypeExactly = (By.CSS_SELECTOR, "[ng-change=\"orderDeliveryCtrl.deliveryTypeChange('exactly')\"]")
    deliveryTypePacket = (By.CSS_SELECTOR, "[ng-change=\"orderDeliveryCtrl.deliveryTypeChange('packet')\"]")
    deliveryTypeCourier = (By.CSS_SELECTOR, "[ng-change=\"orderDeliveryCtrl.deliveryTypeChange('courier')\"]")

    # Время доставки
    deliveryIntervalStandard2330 = (By.XPATH, "//option[@value='С2330До0330']")
    deliveryIntervalStandard2230 = (By.XPATH, "//option[@value='С2230До0230']")
    deliveryIntervalToday = (By.CSS_SELECTOR, "option[value='С13До22']")
    deliveryIntervalExactlyHour = (By.CSS_SELECTOR, "option[value='23']")
    deliveryIntervalExactlyMinute = (By.CSS_SELECTOR, "option[value='59']")
    deliveryIntervalPacket = (By.CSS_SELECTOR, "option[value='С09До22Д']")
    deliveryIntervalCourier = (By.CSS_SELECTOR, "option[value='С15До22М']")

    # Свойства подъёма
    liftingFloor = (By.CSS_SELECTOR, "input[ng-model='orderDeliveryCtrl.order.liftingFloor']")
    liftingPassengerLift = (By.CSS_SELECTOR, "input[ng-model='orderDeliveryCtrl.order.liftingPassengerLift']")
    liftingCargoLift = (By.CSS_SELECTOR, "input[ng-model='orderDeliveryCtrl.order.liftingCargoLift']")
    liftingBasement = (By.CSS_SELECTOR, "input[ng-model='orderDeliveryCtrl.order.liftingBasement']")
    liftingCarry = (By.CSS_SELECTOR, "input[ng-model='orderDeliveryCtrl.order.isLiftingCarry']")
    liftingCarryDistance = (By.CSS_SELECTOR, "input.only_digit.ng-valid-min")

    # Комментарии к доп. услугам
    deliverySawedComment = (By.CSS_SELECTOR, "[ng-model='orderDeliveryCtrl.order.sawingComment']")
    deliveryColoringComment = (By.CSS_SELECTOR, "[ng-model='orderDeliveryCtrl.order.coloringComment']")
    deliveryGarbageComment = (By.CSS_SELECTOR, "[ng-model='orderDeliveryCtrl.order.garbageComment']")
    deliveryReturnComment = (By.CSS_SELECTOR, "[ng-model='orderDeliveryCtrl.order.returnComment']")
    deliveryRentComment = (By.CSS_SELECTOR, "[ng-model='orderDeliveryCtrl.order.rentComment']")

    # Контактная информация
    deliveryEmail = (By.XPATH, "//input[@placeholder='например, petrovich@mail.ru']")
    deliveryPhone = (By.XPATH, "//input[@placeholder='+7 (999) 999-99-99']")
    orderUsername = (By.NAME, "user_name")
    deliveryCallRequired = (By.CSS_SELECTOR, "input[ng-model='orderDeliveryCtrl.order.callRequired']")
    deliveryCallRequiredNow = (By.XPATH, "//span[@class='label_name'][contains(text(),'Сейчас')]")
    deliveryCallRequiredToday = (By.XPATH, "//span[@class='label_name'][contains(text(),'Сегодня')]")
    deliveryCallRequiredTomorrow = (By.XPATH, "//span[@class='label_name'][contains(text(),'Завтра')]")
    # Тут должно быть время звонка на сегодня
    # Тут должно быть время звонка на завтра
    deliveryUserComment = (By.CSS_SELECTOR, "textarea[ng-model='orderDeliveryCtrl.order.userComment']")


class OrderSelfControls(OrderControls):
    # Выбор строительного центра
    # Список баз:
    baseList = (By.CSS_SELECTOR, "ul.bases_list")
    # СПБ:
    baseTallinskoe = (By.XPATH, "//div[(text()=' Таллинское ш., 155, 1, стр. 1 ')]")
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

    # Комментарии к доп. услугам
    selfSawedComment = (By.CSS_SELECTOR, "[ng-model='orderingSelfCtrl.order.sawingComment']")
    selfColoringComment = (By.CSS_SELECTOR, "[ng-model='orderingSelfCtrl.order.coloringComment']")
    selfRentComment = (By.CSS_SELECTOR, "[ng-model='orderingSelfCtrl.order.rentComment']")

    # Контактная информация
    selfEmail = (By.CSS_SELECTOR, "[ng-model='orderingSelfCtrl.contactsEmail']")
    selfPhone = (By.CSS_SELECTOR, "[ng-model='orderingSelfCtrl.contactsPhone']")
    orderUsername = (By.NAME, "user_name")
    selfCallRequired = (By.CSS_SELECTOR, "input[ng-model='orderingSelfCtrl.order.callRequired']")
    selfUserComment = (By.CSS_SELECTOR, "textarea[ng-model='orderingSelfCtrl.order.userComment']")