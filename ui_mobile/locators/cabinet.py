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
    orderName = (By.XPATH, "//a[(text()='Подробнее')]")

    # Пагинация
    ordersPagination1 = (By.XPATH, "//span[(text()='1')]")
    ordersPagination2 = (By.XPATH, "//span[(text()='2')]")
    ordersPagination3 = (By.XPATH, "//span[(text()='3')]")
    ordersPaginationNext = (By.XPATH, "//span[@class='step--next']")
    ordersPaginationPrev = (By.XPATH, "//span[@class='step--prev']")


class CabinetOrderControls:

    # Карточка заказа
    orderInformation = (By.XPATH, "//div[@class='status--info']")
    orderRepeat = (By.XPATH, "//div[contains(text(),'Повторить заказ')]")
    orderId = (By.XPATH, "//div[@class='title--item']//p")
    orderUpdate = (By.XPATH, "//div[@class='status--item']//p")
    orderPay = (By.CSS_SELECTOR, "button.__pay__to_pay")
    orderEdit = (By.XPATH, "//div[@class='order--button-change-wrapper']//div[1]")
    orderCancel = (By.XPATH, "//div[@class='order--button-change-wrapper']//div[2]")
    orderPopupNo = (By.XPATH, "//button[@class='cancel']")
    orderPopupYes = (By.XPATH, "//button[@class='confirm']")


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