# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class CabinetProfileControls:

    # Профиль
    profileFormFirstName = (By.XPATH, "//input[@id='mainPetrovichProfile_firstName']")
    profileFormLastName = (By.XPATH, "//input[@id='mainPetrovichProfile_lastName']")
    profileFormLogin = (By.XPATH, "//input[@id='mainPetrovichProfile_login']")
    profileFormEmail = (By.XPATH, "//input[@id='mainPetrovichProfile_email']")
    profileFormPassword = (By.XPATH, "//input[@id='mainPetrovichProfile_password']")
    profileFormPasswordConfirm = (By.XPATH, "//input[@id='mainPetrovichProfile_passwordconfirm']")
    profileFormCard = (By.XPATH, "//input[@id='mainPetrovichProfile_card']")
    profileFormSave = (By.XPATH, "//button[@class='f--send btn_save']")


class CabinetOrderListControls:

    # Список заказов
    orderName = (By.XPATH, "//span[contains(text(),'ТВЭ00325631 от 09.07.2018 10:16:35')]")

    # Пагинация
    ordersPagination1 = (By.XPATH, "//li[contains(@class,'pagination_item')]//a[contains(text(),'1')]")
    ordersPagination2 = (By.XPATH, "//li[contains(@class,'pagination_item')]//a[contains(text(),'2')]")
    ordersPagination3 = (By.XPATH, "//li[contains(@class,'pagination_item')]//a[contains(text(),'3')]")
    ordersPaginationNext = (By.XPATH, "//i[@class='ic ic_arrow_next']")
    ordersPaginationFinish = (By.XPATH, "//i[@class='ic ic_arrow_finish']")


class CabinetOrderControls:

    # Карточка заказа
    orderInformation = (By.XPATH, "//div[@class='block__line order__information']")
    orderPrint = (By.XPATH, "//div[contains(@class,'order__event __print')]")
    orderRepeat = (By.XPATH, "//div[contains(@class,'order__event __repeat')]")
    orderCopy = (By.XPATH, "//span[contains(@class,'order__copy')]")
    orderId = (By.XPATH, "//span[contains(@class,'order__id')]")
    orderUpdate = (By.XPATH, "//span[contains(@class,'order__update')]")
    orderAddToProject = (By.XPATH, "//div[contains(@class,'order__folder add_folder')]")
    orderPay = (By.CSS_SELECTOR, "button.__pay__to_pay")
    orderEdit = (By.XPATH, "//button[contains(@class,'order__edit __js__order_edit')]")
    orderCancel = (By.XPATH, "//button[contains(@class,'order__cancel')]")
    orderPopupNo = (By.XPATH, "//button[contains(@class,'choose__button __orange __js__popup--close')]")
    orderPopupYes = (By.XPATH, "//button[contains(@class,'choose__button __opacity __js__edit__order')]")
    orderPopupClose = (By.XPATH, "//div[contains(@class,'close__popup __js__popup--close')]")


class CabinetProjectsControls(SearchOrdersControls):

    # Название проекта
    projectName = (By.XPATH, "//span[contains(text(),'test')]")


class CabinetEstimatesControls:

    # Список смет
    estimateListName = (By.XPATH, "//a[contains(text(),'Смета 17.05.2018 17.05.21')]")
    estimateListEdit = (By.XPATH, "//*[@class='ic ic_pen']")
    estimateListDelete = (By.XPATH, "//*[@class='ic ic_delete_grey']")
    estimateListDownload = (By.XPATH, "//span[contains(text(),'скачать')]")

    # Карточка сметы
    estimateNameEdit = (By.XPATH, "//*[@class='ic ic_pen']")
    estimateFormCart = (By.XPATH, "//a[@class='estimateToCart']")

    # Поп-ап изменения названия сметы
    estimateNameEditInput = (By.CSS_SELECTOR, "input[placeholder='новое название']")
    estimateNameEditConfirm = (By.XPATH, "//button[@class='confirm']")
    estimateNameEditCancel = (By.XPATH, "//button[@class='cancel']")


class CabinetExpenseControls:

    # Расходы
    expenseProjectList = (By.XPATH, "//div[@class='field__search __tags']")
    expenseProjectSelect = (By.XPATH, "//p[contains(text(),'test')]")
    expenseIntervalYear = (By.XPATH, "//div[contains(text(),'За год')]")
    expenseIntervalMonth = (By.XPATH, "//div[contains(text(),'За месяц')]")
    expenseIntervalWeek = (By.XPATH, "//div[contains(text(),'За неделю')]")
    expenseIntervalCalendar = (By.XPATH, "//input[@class='__order__search_enter']")
    # expenseViewBlock = (By.XPATH, "")
    # expenseViewList =(By.XPATH, "")