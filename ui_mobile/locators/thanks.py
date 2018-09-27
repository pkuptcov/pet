from selenium.webdriver.common.by import By


class ThanksControls:

    # Кнопки справа (Оплатить заказ, Сообщить об ошибке, Задать вопрос)
    thanksOrderLink = (By.XPATH, "//div[@class='cart--success']//a[(text()='Личном кабинете')]")
    thanksContinueShopping = (By.XPATH, "//div[@class='cart--success']//a[(text()='Продолжить покупки')]")