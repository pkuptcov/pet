# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class OrderDeliveryControls:

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
    submitOrderButtonRight = (By.XPATH, "//button[@type='submit'][(text()='Подтвердить заказ')]")


class OrderDeliveryUrControls(OrderDeliveryControls):

    # Реквизиты компании
    companyName = (By.XPATH, "//input[@placeholder='Название']")
    companyInn = (By.XPATH, "//input[@placeholder='ИНН']")
    companyKpp = (By.XPATH, "//input[@placeholder='КПП']")

    # Способы оплаты заказа
    orderPayLegalNonCash = (By.XPATH, "//span[(text()='По безналичному расчету')]")
    orderPayLegalCard = (By.CSS_SELECTOR, "input[value='legalCard']")
    orderPayLegalCash = (By.CSS_SELECTOR, "input[value='legalCash']")


class OrderDeliveryFizControls(OrderDeliveryControls):

    # Способы оплаты заказа
    orderPayOnline = (By.XPATH, "//span[(text()='Картой онлайн')]")
    orderPayDriverCash = (By.XPATH, "//span[(text()='Водителю наличными')]")
    orderPayDriverCard = (By.XPATH, "//span[(text()='Водителю картой')]")
    orderPayBase = (By.XPATH, "//span[(text()='На базе или в офисе')]")
    orderPayPromo = (By.XPATH, "//span[(text()='Баллами Клуба Друзей')]")
    orderPayDelay = (By.XPATH, "//span[(text()='С отсрочкой на пять дней')]")