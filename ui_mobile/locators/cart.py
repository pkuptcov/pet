# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class CartControls:

    # Работа с корзиной и товарами
    cartSaveEstimate = (By.XPATH, "//p[(text()='Сохранить смету')]")
    cartSaveEstimateName = (By.XPATH, "//input[@placeholder='Название для сметы']")
    cartSaveEstimateSubmit = (By.XPATH, "//button[(text()='Сохранить')]")
    cartSaveEstimateCancel = (By.XPATH, "//button[(text()='Отменить')]")
    cartProductSelect = (By.XPATH, "(//div[@class='block--goods-preview'])[1]")
    cartDelete = (By.XPATH, "(//p[@class='delete--item'])[1]")
    cartDeleteAll = (By.XPATH, "//p[(text()='Удалить все товары')]")
    cartSelectUr = (By.XPATH, "//p[(text()='Юридическое лицо')]")
    cartSelectFiz = (By.XPATH, "//p[(text()='Физическое лицо')]")
    cartDeleteAllConfirm = (By.XPATH, "//div[@class='confirmation--button confirmation--button-true js--button']")
    cartDeleteAllCancel = (By.XPATH, "//div[@class='confirmation--button confirmation--button-false js--button']")
    cartUpQty = (By.XPATH, "(//div[@class='c--plus'])[1]")
    cartDownQty = (By.CSS_SELECTOR, "(//div[@class='c--minus'])[1]")
    cartEnterQty = (By.XPATH, "(//div[@class='c--input'])[1]")

    # Блок с суммой заказа и выбором доставки / покупки
    cartOrderDelivery = (By.XPATH, "//label[(text()='Доставка')]")
    cartOrderSelf = (By.XPATH, "//label[(text()='Самовывоз')]")
    cartOrderPrice = (By.XPATH, "//p[@class='total--price cart--total-price ng-binding']")
    cartOrderInit = (By.XPATH, "//button[(text()='Оформить')]")


class CartControlsFiz(CartControls):

    # Форма карты клуба друзей
    cartCardInput = (By.XPATH, "//input[@placeholder='№ карты']")
    cartCardSubmit = (By.XPATH, "//button[@class='card--send']")
    cartCardHowGet = (By.XPATH, "//a[(text()='Как получить карту?')]")
    cartCardChange = (By.XPATH, "//p[@class='enter--card']")
    cartCardDelete = (By.XPATH, "//p[@class='delete--card']")