# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class CartHelperControls:

    # Кнопки для перемещения в корзину
    cartButtonAlready = (By.CSS_SELECTOR, "span.btn btn_cart.product__button.btn_cart_already")
    cartHeadBasket = (By.CSS_SELECTOR, "div.head_basket_wrapper")

    # Работа с корзиной и товарами
    cartFastAddToCart = (By.ID, "add-product-from-cart")
    cartPrint = (By.CSS_SELECTOR, "a.cart_page_print_link")
    cartSaveEstimate = (By.CSS_SELECTOR, "cart_page_save_link")
    cartDelete = (By.CSS_SELECTOR, "a.cart_row_delete_link")
    cartDeleteAll = (By.CSS_SELECTOR, "a.cart_page_delete_all_link")
    cartSelectUr = (By.XPATH, "//a[contains(text(),'Юридическое лицо')]")
    cartSelectFiz = (By.XPATH, "//a[contains(text(),'Физиическое лицо')]")
    cartDeleteAllConfirm = (By.XPATH, "//button[@class='confirm']")
    cartDeleteAllCancel = (By.XPATH, "//button[@class='cancel']")
    cartUpQty = (By.CSS_SELECTOR, ".productItemCtrl.qtyStep('up', product, product.qty)")
    cartDownQty = (By.CSS_SELECTOR, ".productItemCtrl.qtyStep('down', product, product.qty)")
    cartEnterQty = (By.CSS_SELECTOR, ".product_id")

    # Форма карты клуба друзей
    cartCardInput = (By.CSS_SELECTOR, "input[ng-model='totalCtrl.cardInput']")
    cartCardSubmit = (By.CSS_SELECTOR, "button[ng-click='totalCtrl.addCard()']")
    cartCardHowGet = (By.XPATH, "//a[contains(text(),'Как получить карту?')]")
    cartCardChange = (By.XPATH, "//a[contains(text(),'Изменить')]")
    cartCardDelete = (By.XPATH, "//a[contains(text(),'Удалить')]")
    cartCardPin = (By.XPATH, "//a[contains(text(),'Ввести пин-код карты Клуба Друзей')]")

    # Форма сертификатов Высшей Лиги
    cartCouponWhere = (By.XPATH, "//a[contains(text(),'Куда ввести номер сертификата?')]")
    cartCouponInput = (By.CSS_SELECTOR, "input[ng-model='totalCtrl.couponValue']")
    cartOrderDelivery = (By.CSS_SELECTOR, "input[value=delivery]")
    cartOrderSelf = (By.CSS_SELECTOR, "input[value=self]")
    cartOrderInit = (By.CSS_SELECTOR, "button[ng-click='totalCtrl.goToOrdering()']")