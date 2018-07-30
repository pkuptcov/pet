# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class SideButtonsControls:

    # Кнопки справа (Оплатить заказ, Сообщить об ошибке, Задать вопрос)
    sideButtonOrder = (By.CSS_SELECTOR, ".side_button_order")
    sideButtonError = (By.CSS_SELECTOR, ".side_button_error")
    sideButtonQuestion = (By.CSS_SELECTOR, ".side_button_question")

    # Поп-ап Оплатить заказ
    payOrderPopupInput = (By.XPATH, "//input[@placeholder='ТУЭ00000001']")
    payOrderPopupSubmit = (By.XPATH, "//button[contains(text(),'Оплатить заказ')]")
    payOrderPopupVisa = (By.XPATH, "//ul[@class='card_variants']//div[@class='common__icons visaIcons']")
    payOrderPopupVisaEl = (By.XPATH, "//ul[@class='card_variants']//div[@class='common__icons visaEIcons']")
    payOrderPopupMasterCard = (By.XPATH, "//ul[@class='card_variants']//div[@class='common__icons mastercardIcons']")
    payOrderPopupMaestro = (By.XPATH, "//ul[@class='card_variants']//div[@class='common__icons maestroIcons']")
    payOrderPopupMir = (By.XPATH, "//ul[@class='card_variants']//div[@class='common__icons mirIcons']")
    payOrderPopupClose = (By.XPATH, "//a[@class='modal_close']//*[@class='ic ic_close']")

    # Поп-ап WebIM
    sideButtonQuestionWebim = (By.XPATH, "//a[@class='modal_close']//*[@class='ic ic_close']")