# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class OrderCreateHelperControls:

    # Адрес доставки
    deliveryAddress = (By.CSS_SELECTOR, "[ng-model='orderDeliveryCtrl.order.deliveryAddress']")
    # deliveryAddressHistory = (By.CSS_SELECTOR, "")
    deliveryAddressShowMore = (By.XPATH, "//a[@ng-hide='showMoreAdresses']']")
    deliveryArchParking = (By.CSS_SELECTOR, "input[ng-model='orderDeliveryCtrl.order.deliveryArchway']")
    deliveryVisibilityMap = (By.XPATH, "//a[@class='map_open_link']")
    deliveryDriverComment = (By.CSS_SELECTOR, "textarea[ng-model='orderDeliveryCtrl.order.driverComment']")
    deliveryForemanName = (By.CSS_SELECTOR, "input[ng-model='orderDeliveryCtrl.foremansName']")
    deliveryForemanPhone = (By.CSS_SELECTOR, ".master__phone __choose")

    # Выбор строительного центра
    # СПБ:
    baseTallinskoe = (By.CSS_SELECTOR, "[value='1ea6159b-594d-11e6-bef9-00259038e9f2']")
    baseEngelsa = (By.CSS_SELECTOR, "[value='42d0a3ba-2efc-11df-942d-0023543d7b52']")
    baseSofiyskaya = (By.CSS_SELECTOR, "[value='8e55188d-3e96-11e6-9830-00259038e9f2']")
    basePlanernaya = (By.CSS_SELECTOR, "[value='a15db6c3-305d-11e0-9d49-001f29c6db02']")
    baseIndustrialniy = (By.CSS_SELECTOR, "[value='a95a374c-2f82-11df-942d-0023543d7b52']")
    baseMurmanskoe = (By.CSS_SELECTOR, "[value='d41279b8-2f82-11df-942d-0023543d7b52']")
    baseMoskovskoe = (By.CSS_SELECTOR, "[value='d41279d5-2f82-11df-942d-0023543d7b52']")
    selfMoveToGatchina = (By.CSS_SELECTOR, "button[ng-click='orderingSelfCtrl.moveCartToGatchina()']")


    # Дни доставки
    deliveryDay1 = (By.XPATH, "(//input[@name='delivery_day'])[1]")
    deliveryDay2 = (By.XPATH, "(//input[@name='delivery_day'])[2]")
    deliveryDay3 = (By.XPATH, "(//input[@name='delivery_day'])[3]")
    deliveryDay4 = (By.XPATH, "(//input[@name='delivery_day'])[4]")
    deliveryDay5 = (By.XPATH, "(//input[@name='delivery_day'])[5]")
    deliveryDay6 = (By.XPATH, "(//input[@name='delivery_day'])[6]")

    # Типы доставки
    deliveryTypeToday = (By.CSS_SELECTOR, "[ng-change=\"orderDeliveryCtrl.deliveryTypeChange('today')\"]")
    deliveryTypeStandard = (By.CSS_SELECTOR, "[ng-change=\"orderDeliveryCtrl.deliveryTypeChange('standard')\"]")
    deliveryTypeExpress = (By.CSS_SELECTOR, "[ng-change=\"orderDeliveryCtrl.deliveryTypeChange('express')\"]")
    deliveryTypeExactly = (By.CSS_SELECTOR, "[ng-change=\"orderDeliveryCtrl.deliveryTypeChange('exactly')\"]")
    deliveryTypePacket = (By.CSS_SELECTOR, "[ng-change=\"orderDeliveryCtrl.deliveryTypeChange('packet')\"]")
    deliveryTypeCourier = (By.CSS_SELECTOR, "[ng-change=\"orderDeliveryCtrl.deliveryTypeChange('courier')\"]")

    # Время доставки
    deliveryIntervalStandard = (By.CSS_SELECTOR, "option[value='С2330До0330']")
    deliveryIntervalToday = (By.CSS_SELECTOR, "option[value='С13До22']")
    deliveryIntervalExactlyHour = (By.CSS_SELECTOR, "option[value='23']")
    deliveryIntervalExactlyMinute = (By.CSS_SELECTOR, "option[value='59']")
    deliveryIntervalPacket = (By.CSS_SELECTOR, "option[value='С09До22Д']")
    deliveryIntervalCourier = (By.CSS_SELECTOR, "option[value='С15До22М']")

    # Дополнительные услуги
    deliveryLifting = (By.XPATH, "//span[@class='label_name'][contains(text(),'Подъем на этаж')]")
    deliveryUnloading = (By.XPATH, "//span[@class='label_name'][contains(text(),'Разгрузка')]")
    deliveryManipulator = (By.XPATH, "//span[@class='label_name'][contains(text(),'Манипулятор')]")
    deliveryGarbageRemoval = (By.XPATH, "//span[@class='label_name'][contains(text(),'Вывоз мусора')]")
    deliveryReturn = (By.XPATH, "//span[@class='label_name'][contains(text(),'Возврат товара')]")
    deliveryRent = (By.XPATH, "//span[@class='label_name'][contains(text(),'Аренда оборудования)]")
    deliveryColoring = (By.XPATH, "//span[@class='label_name'][contains(text(),'Колеровка')]")
    deliverySawed = (By.XPATH, "//span[@class='label_name'][contains(text(),'Распил')]")

    # Реквизиты компании
    companyName = (By.CSS_SELECTOR, "input[placeholder='Название']")
    companyInn = (By.CSS_SELECTOR, "input[placeholder='ИНН']")
    companyKpp = (By.CSS_SELECTOR, "input[placeholder='КПП']")

    # Свойства подъёма
    liftingFloor = (By.CSS_SELECTOR, "input[ng-model='orderDeliveryCtrl.order.liftingFloor']")
    liftingPassengerLift = (By.CSS_SELECTOR, "input[ng-model='orderDeliveryCtrl.order.liftingPassengerLift']")
    liftingCargoLift = (By.CSS_SELECTOR, "input[ng-model='orderDeliveryCtrl.order.liftingCargoLift']")
    liftingBasement = (By.CSS_SELECTOR, "input[ng-model='orderDeliveryCtrl.order.liftingBasement']")
    liftingCarry = (By.CSS_SELECTOR, "input[ng-model='orderDeliveryCtrl.order.isLiftingCarry']")
    liftingCarryDistance = (By.CSS_SELECTOR, "input.only_digit.ng-valid-min")

    # Комментарии к доп. услугам
    sawedComment = (By.CSS_SELECTOR, "[ng-model='orderDeliveryCtrl.order.sawingComment']")
    coloringComment = (By.CSS_SELECTOR, "[ng-model='orderDeliveryCtrl.order.coloringComment']")
    garbageComment = (By.CSS_SELECTOR, "[ng-model='orderDeliveryCtrl.order.garbageComment']")
    returnComment = (By.CSS_SELECTOR, "[ng-model='orderDeliveryCtrl.order.returnComment']")
    rentComment = (By.CSS_SELECTOR, "[ng-model='orderDeliveryCtrl.order.rentComment']")

    # Способы оплаты заказа
    orderPayOnline = (By.CSS_SELECTOR, "input[value='online']")
    orderPayLegalNonCash = (By.CSS_SELECTOR, "input[value='legalNonCash']")
    orderPayLegalCard = (By.CSS_SELECTOR, "input[value='legalCard']")
    orderPayLegalCash = (By.CSS_SELECTOR, "input[value='legalCash']")
    orderPayDriverCash = (By.CSS_SELECTOR, "input[value='driverCash']")
    orderPayDriverCard = (By.CSS_SELECTOR, "input[value='driverCard']")
    orderPayBase = (By.CSS_SELECTOR, "input[value='base']")
    orderPayPromo = (By.CSS_SELECTOR, "input[value='promo']")
    orderPayDelay = (By.CSS_SELECTOR, "input[value='delay']")

    # Контактная информация
    deliveryEmail = (By.CSS_SELECTOR, "[ng-model='orderDeliveryCtrl.contactsEmail']")
    selfEmail = (By.CSS_SELECTOR, "[ng-model='orderingSelfCtrl.contactsEmail']")
    deliveryPhone = (By.CSS_SELECTOR, "[ng-model='orderDeliveryCtrl.contactsPhone']")
    selfPhone = (By.CSS_SELECTOR, "[ng-model='orderingSelfCtrl.contactsPhone']")
    deliveryUsername = (By.NAME, "user_name")
    deliveryUsernameMask = (By.CSS_SELECTOR, ".plugin__dropdown--masked")
    deliveryCallRequired = (By.CSS_SELECTOR, "input[ng-model='orderDeliveryCtrl.order.callRequired']")
    selfCallRequired = (By.CSS_SELECTOR, "input[ng-model='orderingSelfCtrl.order.callRequired']")
    deliveryCallRequiredNow = (By.XPATH, "//span[@class='label_name'][contains(text(),'Сейчас')]")
    deliveryCallRequiredToday = (By.XPATH, "//span[@class='label_name'][contains(text(),'Сегодня')]")
    deliveryCallRequiredTomorrow = (By.XPATH, "//span[@class='label_name'][contains(text(),'Завтра')]")
    # Тут должно быть время звонка на сегодня
    # Тут должно быть время звонка на завтра
    deliveryUserComment = (By.CSS_SELECTOR, "textarea[ng-model='orderDeliveryCtrl.order.userComment']")

    # Подтверждение заказа
    deliverySubmitOrderButtonMain = (By.CSS_SELECTOR, "input[ng-click='orderDeliveryCtrl.make($event)']")
    selfSubmitOrderButtonMain = (By.CSS_SELECTOR, "input[ng-click='orderingSelfCtrl.make($event)']")
    SubmitOrderButtonRight = (By.XPATH, "//button[@type='submit'][contains(text(),'Подтвердить заказ')]")
