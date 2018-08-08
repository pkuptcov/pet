# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class OrderCreateDeliveryControls:

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
    deliveryAddressInput = (By.CSS_SELECTOR, "{} input[name='addressInput'] [data-modify='ur,delivery']".format(orderElementBase))


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
    orderLifting = (By.XPATH, "//span[@class='label_name'][contains(text(),'Подъем на этаж')]")
    orderUnloading = (By.XPATH, "//span[@class='label_name'][contains(text(),'Разгрузка')]")
    orderManipulator = (By.XPATH, "//span[@class='label_name'][contains(text(),'Манипулятор')]")
    orderGarbageRemoval = (By.XPATH, "//span[@class='label_name'][contains(text(),'Вывоз мусора')]")
    orderReturn = (By.XPATH, "//span[@class='label_name'][contains(text(),'Возврат товара')]")
    orderRent = (By.XPATH, "//span[@class='label_name'][contains(text(),'Аренда оборудования)]")
    orderColoring = (By.XPATH, "//span[@class='label_name'][contains(text(),'Колеровка')]")
    orderSawed = (By.XPATH, "//span[@class='label_name'][contains(text(),'Распил')]")

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
    deliveryEmail = (By.CSS_SELECTOR, "[ng-model='orderDeliveryCtrl.contactsEmail']")
    deliveryPhone = (By.CSS_SELECTOR, "[ng-model='orderDeliveryCtrl.contactsPhone']")
    orderUsername = (By.NAME, "user_name")
    # orderDropdownMask = (By.CSS_SELECTOR, ".plugin__dropdown--masked")
    deliveryCallRequired = (By.CSS_SELECTOR, "input[ng-model='orderDeliveryCtrl.order.callRequired']")
    deliveryCallRequiredNow = (By.XPATH, "//span[@class='label_name'][contains(text(),'Сейчас')]")
    deliveryCallRequiredToday = (By.XPATH, "//span[@class='label_name'][contains(text(),'Сегодня')]")
    deliveryCallRequiredTomorrow = (By.XPATH, "//span[@class='label_name'][contains(text(),'Завтра')]")
    # Тут должно быть время звонка на сегодня
    # Тут должно быть время звонка на завтра
    deliveryUserComment = (By.CSS_SELECTOR, "textarea[ng-model='orderDeliveryCtrl.order.userComment']")

    # Подтверждение заказа
    deliverySubmitOrderButtonMain = (By.CSS_SELECTOR, "input[ng-click='orderDeliveryCtrl.make($event)']")
    SubmitOrderButtonRight = (By.XPATH, "//button[@type='submit'][contains(text(),'Подтвердить заказ')]")


class OrderCreateDeliveryUrControls(OrderCreateDeliveryControls):

    # Реквизиты компании
    companyName = (By.CSS_SELECTOR, "input[placeholder='Название']")
    companyInn = (By.CSS_SELECTOR, "input[placeholder='ИНН']")
    companyKpp = (By.CSS_SELECTOR, "input[placeholder='КПП']")

    # Способы оплаты заказа
    orderPayLegalNonCash = (By.CSS_SELECTOR, "input[value='legalNonCash']")
    orderPayLegalCard = (By.CSS_SELECTOR, "input[value='legalCard']")
    orderPayLegalCash = (By.CSS_SELECTOR, "input[value='legalCash']")


class OrderCreateDeliveryFizControls(OrderCreateDeliveryControls):

    # Способы оплаты заказа
    orderPayOnline = (By.CSS_SELECTOR, "input[value='online']")
    orderPayDriverCash = (By.CSS_SELECTOR, "input[value='driverCash']")
    orderPayDriverCard = (By.CSS_SELECTOR, "input[value='driverCard']")
    orderPayBase = (By.CSS_SELECTOR, "input[value='base']")
    orderPayPromo = (By.CSS_SELECTOR, "input[value='promo']")
    orderPayDelay = (By.CSS_SELECTOR, "input[value='delay']")