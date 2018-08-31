# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class CartControls:

    # Форма добавить по-быстрому
    cartFastAddToCart = (By.ID, "add-product-from-cart")
    cartFastAddToCartSearch = (By.XPATH, "//input[@id='guid']")
    cartFastAddToCartSudjest101847 = (By.XPATH, "//div[@class='ui-menu-item-wrapper']")
    cartFastAddToCartQantityInput = (By.XPATH, "//input[@placeholder='1']")
    cartFastAddToCartQantityUp = (By.XPATH, "//div[@class='fast-add-up stepper-arrow up product__stepper unit--step']")
    cartFastAddToCartQantityDown = (By.XPATH, "//div[@class='fast-add-down stepper-arrow down product__stepper unit--step']")
    cartFastAddToCartSubmit = (By.XPATH, "//div[@class='fast-add-button']")

    # Работа с корзиной и товарами
    cartPrint = (By.CSS_SELECTOR, "a.cart_page_print_link")
    cartSaveEstimate = (By.CSS_SELECTOR, "cart_page_save_link")
    cartDelete = (By.CSS_SELECTOR, "a.cart_row_delete_link")
    cartDeleteAll = (By.CSS_SELECTOR, "a.cart_page_delete_all_link")
    cartSelectUr = (By.XPATH, "//a[contains(text(),'Юридическое лицо')]")
    cartSelectFiz = (By.XPATH, "//a[contains(text(),'Физиическое лицо')]")
    cartDeleteAllConfirm = (By.XPATH, "//button[@class='confirm']")
    cartDeleteAllCancel = (By.XPATH, "//button[@class='cancel']")
    cartUpQty = (By.CSS_SELECTOR, "span.stepper-arrow.up")
    cartDownQty = (By.CSS_SELECTOR, "span.stepper-arrow.down")
    cartEnterQty = (By.NAME, "product_id")

    # Форма сертификатов Высшей Лиги
    cartCouponWhere = (By.XPATH, "//a[contains(text(),'Куда ввести номер сертификата?')]")
    cartCouponInput = (By.CSS_SELECTOR, "input[ng-model='totalCtrl.couponValue']")
    cartCouponSubmit = (By.CSS_SELECTOR, "button[ng-click='totalCtrl.checkVerifyCoupon($event)']")

    # Блок с суммой заказа и выбором доставки / покупки
    cartOrderDelivery = (By.CSS_SELECTOR, "input[value=delivery]")
    cartOrderSelf = (By.XPATH, "//span[(text()='Самовывоз')]")
    cartOrderInit = (By.XPATH, "//button[(text()='Оформить')]")
    cartOrderPrice = (By.CSS_SELECTOR, ".cart_total_container_universal_sum_price")


class CartControlsFiz(CartControls):

    # Форма карты клуба друзей
    cartCardInput = (By.CSS_SELECTOR, "input[ng-model='totalCtrl.cardInput']")
    cartCardSubmit = (By.CSS_SELECTOR, "button[ng-click='totalCtrl.addCard()']")
    cartCardHowGet = (By.XPATH, "//a[(text()='Как получить карту?')]")
    cartCardChange = (By.XPATH, "//a[(text()='Изменить')]")
    cartCardDelete = (By.XPATH, "//a[(text()='Удалить')]")
    cartCardPin = (By.XPATH, "//a[contains(text(),'Ввести пин-код карты Клуба Друзей')]")


class CartControlsUr(CartControls):

    # Форма карты клуба друзей
    cartInnInput = (By.CSS_SELECTOR, "input[ng-model='totalCtrl.innValue']")
    cartInnSubmit = (By.CSS_SELECTOR, "button[ng-click='totalCtrl.checkVerifyInn($event)']")