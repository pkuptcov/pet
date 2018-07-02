# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class CartHelperControls:
    cartHeadBasket = (By.CSS_SELECTOR, "div.head_basket_wrapper")
    cartSelectUr = (By.XPATH, "//a[contains(text(),'Юридическое лицо')]")
    cartSelectFiz = (By.XPATH, "//a[contains(text(),'Физиическое лицо')]")
    cartFastAddToCart = (By.ID, "add-product-from-cart")
    cartPrint = (By.CSS_SELECTOR, "cart_page_print_link")
    cartDelete = (By.CSS_SELECTOR, "cart_row_delete_link")
    cartDeleteAll = (By.CSS_SELECTOR, "cart_page_delete_all_link")
    cartDeleteAllConfirm = (By.XPATH, "//button[@class='confirm']")
    cartDeleteAllCancel = (By.XPATH, "//button[@class='cancel']")
    cartUpQty = (By.CSS_SELECTOR, "productItemCtrl.qtyStep('up', product, product.qty)")
    cartDownQty = (By.CSS_SELECTOR, "productItemCtrl.qtyStep('down', product, product.qty)")
    cartEnterQty = (By.CSS_SELECTOR, "product_id")

