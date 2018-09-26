# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class OrderDeliveryControls:

    # Адрес доставки
    deliveryAddress = (By.XPATH, "//textarea[@placeholder='Адрес доставки:']")
    deliveryVisibilityMap = (By.XPATH, "//p[(text()=' Показать карту ')]")
    deliveryArchParking = (By.XPATH, "//span[(text()='Есть ограничение по высоте (арка, подземный паркинг)?')]")
    deliveryDriverComment = (By.XPATH, "//textarea[@class='textarea--order adress--in ng-pristine ng-valid ng-valid-maxlength ng-touched']")

    # orderElementBase = ".order"
    # deliveryAddressInput = (By.CSS_SELECTOR, "{}[data-modify='ur,delivery'] input [name='deliveryAddress']".format(orderElementBase))

    # Дни доставки
    deliveryDay1 = (By.XPATH, "(//input[@name='delivery_day'])[1]")
    deliveryDay2 = (By.XPATH, "//label[contains(text(),'ЗАВТРА')]")
    deliveryDay3 = (By.XPATH, "(//input[@name='delivery_day'])[4]")
    deliveryDay4 = (By.XPATH, "(//input[@name='delivery_day'])[4]")
    deliveryDay5 = (By.XPATH, "(//input[@name='delivery_day'])[5]")
    deliveryDay6 = (By.XPATH, "(//input[@name='delivery_day'])[6]")

    # Типы доставки
    deliveryTypeToday = (By.XPATH, "//label[(text()=' В течение дня ')]")
    deliveryTypeStandard = (By.XPATH, "//label[(text()=' Стандартная доставка ')]")
    deliveryTypeExpress = (By.XPATH, "//label[(text()='Экспресс доставка')]")
    deliveryTypeExactly = (By.XPATH, "//label[(text()=' Точно ко времени ')]")
    deliveryTypePacket = (By.XPATH, "//label[(text()='Пакетная доставка длинномерных грузов')]")
    deliveryTypeCourier = (By.XPATH, "//label[(text()=' Курьерская доставка ')]")

    # Время доставки
    deliveryIntervalStandard2330 = (By.XPATH, "//option[@value='С2330До0330']")
    deliveryIntervalStandard2230 = (By.XPATH, "//option[@value='С2230До0230']")
    deliveryIntervalToday = (By.XPATH, "//option[@value='С13До22']")
    deliveryIntervalExactlyHour = (By.XPATH, "(//label[@for='day--exact']//option[@value='23'])[1]")
    deliveryIntervalExactlyMinute = (By.XPATH, "(//label[@for='day--exact']//option[@value='23'])[2]")
    deliveryIntervalPacket = (By.XPATH, "//option[@value='С09До22Д']")
    deliveryIntervalCourier = (By.XPATH, "//option[@value='С15До22М']")

    # Дополнительные услуги
    orderLifting = (By.XPATH, "//label[@for='rise--i'][(text()=' Подъем на этаж ')]")
    orderUnloading = (By.XPATH, "//label[@for='unloading--i'][(text()='Разгрузка')]")
    orderManipulator = (By.XPATH, "//label[@for='manipulator--i'][(text()='Разгрузка манипулятором')]")
    orderGarbageRemoval = (By.XPATH, "//label[@for='garbage--i'][(text()=' Вывоз мусора ')]")
    orderReturn = (By.XPATH, "//label[@for='return--i'][(text()=' Возврат товара ')]")
    orderRent = (By.XPATH, "//label[@for='rent--i'][(text()=' Аренда оборудования ')]")
    orderColoring = (By.XPATH, "//label[@for='coloring--i'][(text()=' Колеровка ')]")
    orderSawed = (By.XPATH, "//label[@for='cut--i'][(text()=' Распил ')]")

    # Свойства подъёма
    liftingFloor = (By.XPATH, "//label[@for='rise--i']//div[@class='c--input']//input[@placeholder='11']")
    liftingPassengerLift = (By.XPATH, "//label[(text()='Лифт')]")
    liftingCargoLift = (By.XPATH, "//label[(text()='Грузовой лифт')]")
    liftingBasement = (By.XPATH, "//label[(text()='Технический этаж')]")
    liftingCarry = (By.XPATH, "//label[(text()='Грузчикам нужно нести заказ от машины до вас дальше 50 метров?')]")
    liftingCarryDistance = (By.XPATH, "(//label[@for='rise--i']//div[@class='c--input'])[2]")

    # Комментарии к доп. услугам
    deliverySawedComment = (By.XPATH, "//label[@for='cut--i']//textarea[@placeholder='Комментарий']")
    deliveryColoringComment = (By.XPATH, "//label[@for='coloring--i']//textarea[@placeholder='Комментарий']")
    deliveryGarbageComment = (By.XPATH, "//label[@for='garbage--i']//textarea[@placeholder='Комментарий']")
    deliveryReturnComment = (By.XPATH, "//label[@for='return--i']//textarea[@placeholder='Комментарий']")
    deliveryRentComment = (By.XPATH, "//label[@for='rent--i']//textarea[@placeholder='Комментарий']")

    # Контактная информация
    deliveryEmail = (By.XPATH, "//input[@type='email'][@placeholder='например, petrovich@mail.ru']")
    deliveryPhone = (By.XPATH, "//input[@type='tel'][@placeholder='+7 (999) 999-99-99']")
    orderUsername = (By.NAME, "user_name")
    deliveryCallRequired = (By.XPATH, "//label[@for='call--i']//span[(text()='Обязательно нужен звонок оператора')]")
    deliveryCallRequiredNow = (By.XPATH, "//label[@for='call--now'][(text()='Сейчас')]")
    deliveryCallRequiredToday = (By.XPATH, "//label[@for='call--today'][contains(text(),'Сегодня')]")
    deliveryCallRequiredTomorrow = (By.XPATH, "//label[@for='call--tomorrow'][contains(text(),'Завтра')]")
    # Тут должно быть время звонка на сегодня
    # Тут должно быть время звонка на завтра
    deliveryUserComment = (By.XPATH, "//textarea[@placeholder='В арку налево. До железной двери и стучать. Раньше 6:00 не звонить. На объекте прораб Кузьмич.']")

    # Подтверждение заказа
    submitOrderButton = (By.XPATH, "//button[@class='confirm--send'][(text()='Подтвердить заказ')]")

    # Раскрыть пункты
    orderDeliveryAddress = (By.XPATH, "//p[(text()='Введите адрес доставки')]")
    orderDeliveryDay = (By.XPATH, "//p[(text()='День доставки')]")
    orderDeliveryTime = (By.XPATH, "//p[(text()='Время доставки')]")
    orderAdditionalSevices = (By.XPATH, "//p[(text()='Дополнительные услуги')]")
    orderPaymentType = (By.XPATH, "//p[(text()='Способ оплаты')]")
    orderEmail = (By.XPATH, "//p[(text()='Ваша электронная почта')]")
    orderPhone = (By.XPATH, "//p[(text()='Телефон для звонков и СМС')]")
    orderComment = (By.XPATH, "//p[(text()='Комментарии к заказу')]")
    orderAboutCompany = (By.XPATH, "//p[(text()='Информация о компании')]")


class OrderDeliveryUrControls(OrderDeliveryControls):

    # Реквизиты компании
    companyName = (By.XPATH, "//input[@placeholder='Название']")
    companyInn = (By.XPATH, "//input[@placeholder='ИНН']")
    companyKpp = (By.XPATH, "//input[@placeholder='КПП']")

    # Способы оплаты заказа
    orderPayLegalNonCash = (By.XPATH, "//label[@for='pay--legalNonCash'][(text()='По безналичному расчету')]")
    orderPayLegalCard = (By.XPATH, "//label[@for='pay--legalCard'][(text()='Банковской картой')]")
    orderPayLegalCash = (By.XPATH, "//label[@for='pay--legalCash'][(text()='За наличный расчет')]")


class OrderDeliveryFizControls(OrderDeliveryControls):

    # Способы оплаты заказа
    orderPayOnline = (By.XPATH, "//label[@for='pay--online'][(text()='Картой онлайн')]")
    orderPayDriverCash = (By.XPATH, "//label[@for='pay--driverCash'][(text()='Водителю наличными')]")
    orderPayDriverCard = (By.XPATH, "//label[@for='pay--driverCard'][(text()='Водителю картой')]")
    orderPayBase = (By.XPATH, "//label[@for='pay--base'][(text()='На базе или в офисе')]")
    orderPayPromo = (By.XPATH, "//label[@for='pay--promo'][(text()='Баллами Клуба Друзей')]")
    orderPayDelay = (By.XPATH, "//label[@for='pay--delay'][(text()='С отсрочкой на пять дней')]")