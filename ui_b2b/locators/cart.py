# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class CartControls:

    # Работа с корзиной и товарами
    cartRefresh = (By.XPATH, "//a[@class='order_container_refresh_link']")
    cartPrint = (By.CSS_SELECTOR, "a.cart_page_print_link")
    cartDelete = (By.CSS_SELECTOR, "a.cart_row_delete_link")
    cartDeleteAll = (By.CSS_SELECTOR, "a.cart_page_delete_all_link")
    cartDeleteAllConfirm = (By.XPATH, "//button[@class='confirm']")
    cartDeleteAllCancel = (By.XPATH, "//button[@class='cancel']")
    cartUpQty = (By.CSS_SELECTOR, "span.stepper-arrow.up")
    cartDownQty = (By.CSS_SELECTOR, "span.stepper-arrow.down")
    cartEnterQty = (By.NAME, "product_id")

    # Блок с суммой заказа и выбором доставки / покупки
    cartOrderDelivery = (By.XPATH, "//span[(text()='Доставка')]")
    cartOrderSelf = (By.XPATH, "//span[(text()='Самовывоз')]")
    cartOrderInit = (By.XPATH, "//button[(text()='Оформить')]")
    cartOrderPrice = (By.XPATH, "//div[@class='cart_total_container_final_prices']")
    cartOrderCollect = (By.XPATH, "//span[(text()='При самовывозе доступна услуга «Соберет Петрович»')]")
    cartOrderCollectClose = (By.XPATH, "//div[@class='modal--close']")